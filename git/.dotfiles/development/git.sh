#!/usr/bin/env bash


alias gitssh="git_config_ssh"
git_config_ssh() {

  DEFAULT_HOST="github"
  DEFAULT_USERNAME="infosmith"
  PROMPT_HOSTNAME="Enter a unique git host name: bitbucket, github, gitlab, etc... [$DEFAULT_HOST]: "
  PROMPT_USERNAME="Enter your username for this host: [$DEFAULT_USERNAME]"
  PROMPT_EMAIL="Enter your private email address for this host: "
  PROMPT_PASSPHRASE="Enter a passphrase to secure your ssh private key: "

  # Prompt for git host name
  echo -n $PROMPT_HOSTNAME
  read git_host
  git_host=${git_host:-${DEFAULT_HOST}}

  # Prompt for git private email address
  echo -n $PROMPT_EMAIL
  read git_email

  # Prompt for git ssh private key passphrase
  echo -n $PROMPT_PASSPHRASE
  read passphrase

  # Prompt for git ssh private key filename
  default_filename="$HOME/.ssh/$git_host"
  echo -n "Save your ssh private key to: [$default_filename]"
  read filename
  filename=${filename:-${default_filename}}

  # Generate ssh private key
  ssh-keygen -t rsa -b 4096 -C "$git_email" -f "$filename" -N "$passphrase"
  pkill -f ssh-agent
  eval "$(ssh-agent -s)"
  ssh-add $filename

  # Copy ssh public key to clipboard
  case "$OSTYPE" in
  darwin*)
    pbcopy <$filename.pub ;;
  linux*)
    xclip -sel clip <$filename.pub ;;
  esac

  # Open browser and create SSH key
  echo "Login to $git_host and create a new key."
  case "$git_host" in
  github)
    firefox "https://github.com/login" ;;
  bitbucket)
    firefox "https://bitbucket.org/account/signin/" ;;
  gitlab)
    firefox "https://gitlab.com/users/sign_in" ;;
  *)
    firefox ;;
  esac
}

alias gitgui=git_open_gui
git_open_gui() {
  case "$OSTYPE" in
  linux*) nohup cola $1 &>/dev/null &;;
  esac
}
