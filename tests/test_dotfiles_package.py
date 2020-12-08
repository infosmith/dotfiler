from ..dotfiles import DotfilesPackage


def get_paths(profile_path, package_path):
    symlinks = [p for p in profile_path.iterdir() if p.is_symlink()]
    followed_links = [str(p.readlink().resolve().name) for p in symlinks]
    package_file_paths = sorted([str(p.name) for p in package_path.iterdir()])
    return symlinks, followed_links, package_file_paths


def test_add_symlink(user_profile, package_path):
    package = DotfilesPackage(package_path)
    package.add_symlinks()
    symlinks, actual, expected = get_paths(user_profile, package.path)
    for path in expected:
        assert path in actual
    package.remove_symlinks()


def test_remove_symlink(user_profile, package_path):
    package = DotfilesPackage(package_path)
    package.add_symlinks()
    symlinks, actual, expected = get_paths(user_profile, package.path)
    for path in expected:
        assert path in actual
    package.remove_symlinks()
    symlinks, actual, expected = get_paths(user_profile, package.path)
    for path in expected:
        assert path not in actual
