# Changelog

All notable changes to infosmith/dotfiles will be documented here.

The file format is based on [Keep a Changelog][changelog],
and this project adheres to [Semantic Versioning][semver].

# [0.2.0](/compare/v0.1.0...v) (2020-12-17)

### Features

* **git:** add alias for amending previous commit
* **git:** add alias for listing branches
* **git:** add alias for removing pulled changes
* **git:** add aliases for stash commands
* **git:** add commit message template
* **git:** background git cola
* **git:** configure git ssh keys
* **git:** configure git user
* **git:** enforce end of line normalization
* **git:** ignore GitBook files
* **git:** ignore Node.js files
* **git:** ignore Packer files
* **git:** ignore Python files
* **git:** ignore SASS files
* **git:** ignore Terraform files
* **git:** integrate pre-commit framework
* **git:** integrate preferred diff tools
* **git:** integrate preferred merge tool
* **git:** prevent .gitattributes encryption
* **git:** revert MacOS decomposed unicode filenames
* **git:** simplify ssh key generation and uploading
* **git:** specify editor used for messages



## [0.1.0]() - 2020-12-7

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
