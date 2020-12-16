#!/usr/bin/env sh

cp $DOTFILES/storage/git/precommits/python.yaml $PWD/.pre-commit-config.yaml
pre-commit autoupdate
pre-commit install
pre-commit install -t commit-msg
