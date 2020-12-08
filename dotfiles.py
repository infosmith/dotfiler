#!/usr/bin/env python
"""CLI for managing dotfiles."""
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path

import click

DOTFILES_TARGET_DIRECTORY_NAME = ".dotfiles"


class Command:
    def __init__(self, cmd: str) -> None:
        self.command = cmd

    @staticmethod
    def get_result(cmd, captures=True, encodes="UTF-8", **kwargs):
        return subprocess.run(
            cmd, shell=True, capture_output=captures, encoding=encodes, **kwargs
        )

    @staticmethod
    def wrap_result(cmd_process):
        return CommandResult(
            command=cmd_process.args,
            output=cmd_process.stdout,
            error=cmd_process.stderr,
            exit_code=cmd_process.returncode,
        )

    def execute(self, **kwargs):
        return self.wrap_result(self.get_result(self.command, **kwargs))


@dataclass
class CommandResult:
    command: str
    output: str
    error: str
    exit_code: int


class DotfilesPackage:
    def __init__(self, path):
        self.path = path
        self.name = path.resolve().name

    def add_symlinks(self):
        return Command(f"stow {self.name}").execute()

    def remove_symlinks(self):
        return Command(f"stow -D {self.name}").execute()

    def repair_symlinks(self):
        return Command(f"stow -R {self.name}").execute()


class DotfilesRepository:
    EXCLUDES = ["tests", "__pycache__", ".pytest_cache"]

    def __init__(self, directory="."):
        self.path = Path(directory)

    @property
    def package_paths(self):
        for child in self.path.iterdir():
            if self.is_package(child):
                yield child

    def add_packages(self, package_paths=()):
        paths = package_paths if package_paths else self.package_paths
        for path in paths:
            yield path.name, DotfilesPackage(path).add_symlinks()

    def is_package(self, suspect_path):
        return suspect_path.is_dir() and not any(
            [
                suspect_path.name.startswith("."),
                suspect_path.name.startswith("__"),
                suspect_path.name in self.EXCLUDES,
            ]
        )

    def remove_packages(self, package_paths=()):
        paths = package_paths if package_paths else self.package_paths
        for path in paths:
            yield path.name, DotfilesPackage(path).remove_symlinks()

    def repair_packages(self, package_paths=()):
        paths = package_paths if package_paths else self.package_paths
        for path in paths:
            yield path.name, DotfilesPackage(path).repair_symlinks()


class FeedbackPrinter:
    @staticmethod
    def __print_result_passed_or_failed(result, success_msg, failure_msg):
        if result.exit_code == 0:
            click.echo(success_msg)
        else:
            click.echo(failure_msg)

    @classmethod
    def added_package(cls, package_name, result):
        cls.__print_result_passed_or_failed(
            result,
            f"Symlinked {package_name}",
            f"Unable to symlink {package_name}: {result.error.strip()}",
        )

    @classmethod
    def removed_package(cls, package_name, result):
        cls.__print_result_passed_or_failed(
            result,
            f"Removed symlink of {package_name}",
            f"Unable to remove symlink of {package_name}: {result.error.strip()}",
        )

    @classmethod
    def repaired_package(cls, package_name, result):
        cls.__print_result_passed_or_failed(
            result,
            f"Repaired symlink of {package_name}",
            f"Unable to repair symlink of {package_name}: {result.error.strip()}",
        )

    @staticmethod
    def list_package_symlinks(path):
        if path.exists():
            s = str(path).replace(str(Path.home()) + "/", "")
            success_msg = f"{s} symlinked to {path.resolve()}"
            click.echo(success_msg)
        else:
            failure_msg = f"{path.name} is not symlinked"
            click.echo(failure_msg)


class UserProfile:
    def __init__(self, path=Path.home()):
        self.path = path
        self.dotfiles_target = Path(self.path, DOTFILES_TARGET_DIRECTORY_NAME)

    def __list_profile_directory_symlinks(self):
        for path in sorted(self.path.iterdir()):
            if path.is_symlink():
                yield path

    def __walk_dotfiles_directory_symlinks(self):
        for root, dirs, files in os.walk(self.dotfiles_target):
            for name in sorted(dirs + files):
                path = Path(root, name)
                if path.is_symlink():
                    yield path

    def list_symlinks(self):
        for path in self.__walk_dotfiles_directory_symlinks():
            yield path
        for path in self.__list_profile_directory_symlinks():
            yield path


def build_cli():
    @click.group()
    @click.pass_context
    def cli(ctx):
        ctx.ensure_object(dict)
        ctx.obj["repo"] = DotfilesRepository()
        ctx.obj["prints"] = FeedbackPrinter()
        ctx.obj["user_profile"] = UserProfile()

    @click.command(help="Symlink packages following this option.")
    @click.option("--all", is_flag=True, help="Symlink all packages.")
    @click.argument("named_packages", nargs=-1)
    @click.pass_context
    def add(ctx, all, named_packages):
        if all:
            for package_name, result in ctx.obj["repo"].add_packages():
                ctx.obj["prints"].added_package(package_name, result)
        elif named_packages:
            paths = [Path(name) for name in named_packages]
            for package_name, result in ctx.obj["repo"].add_packages(paths):
                ctx.obj["prints"].added_package(package_name, result)
        else:
            click.echo("One or package names is required.")

    @click.command(help="Remove symlinks of packages following this option.")
    @click.option("--all", is_flag=True, help="Remove all symlinked packages.")
    @click.argument("named_packages", nargs=-1)
    @click.pass_context
    def remove(ctx, all, named_packages):
        if all:
            for pkg_name, result in ctx.obj["repo"].remove_packages():
                ctx.obj["prints"].removed_package(pkg_name, result)
        elif named_packages:
            paths = [Path(name) for name in named_packages]
            for pkg_name, result in ctx.obj["repo"].remove_packages(paths):
                ctx.obj["prints"].removed_package(pkg_name, result)
        else:
            click.echo("One or package names is required.")

    @click.command(help="Repair symlinks of packages following this option.")
    @click.option("--all", is_flag=True, help="Repair all symlinked packages.")
    @click.argument("named_packages", nargs=-1)
    @click.pass_context
    def repair(ctx, all, named_packages):
        if all:
            for pkg_name, result in ctx.obj["repo"].repair_packages():
                ctx.obj["prints"].repaired_package(pkg_name, result)
        elif named_packages:
            paths = [Path(name) for name in named_packages]
            for pkg_name, result in ctx.obj["repo"].remove_packages(paths):
                ctx.obj["prints"].repaired_package(pkg_name, result)
        else:
            click.echo("One or package names is required.")

    @click.command(help="List files of symlinked packages.")
    @click.pass_context
    def symlinks(ctx):
        for path in ctx.obj["user_profile"].list_symlinks():
            ctx.obj["prints"].list_package_symlinks(path)

    cli.add_command(add)
    cli.add_command(remove)
    cli.add_command(repair)
    cli.add_command(symlinks)

    return cli


def main():
    cli = build_cli()
    cli()


if __name__ == "__main__":
    main()
