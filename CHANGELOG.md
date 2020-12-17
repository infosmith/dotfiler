# Changelog

All notable changes to infosmith/dotfiles will be documented here.

The file format is based on [Keep a Changelog][changelog],
and this project adheres to [Semantic Versioning][semver].

## [Unreleased]

## [0.1.0] - 2020-12-7

### Added

- README describing project.
- CHANGELOG tracking project evolution.
- pre-commit framework integration.
- example.md for repo copy of example provided by [Keep a Changelog][changelog].
- requirements.in to pin project dependencies.
- requirements.txt to pin transitive dependencies and their sources.
- CLI with add, remove, and repair commands for n+ stow packages
- symlinks command to CLI for showing all symlinks in $HOME directory
- tests covering add and remove CLI commands
- explicit GNU Stow target directory in .stowrc configuration file
- explicit GNU Stow ignored paths in .stow-local-ignore

[changelog]: https://keepachangelog.com/en/1.0.0/
[semver]: https://semver.org/spec/v2.0.0.html
