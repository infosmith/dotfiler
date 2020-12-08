dotfiles
========

These are my dotfiles. There are many like them but these are mine...


Prerequisites
*********************
Use homebrew on Linux and MacOS to install stow.

.. code-block:: bash

    brew update
    brew install stow


Install dotfiles
****************
Clone this repository.

.. code-block:: bash

    git clone https://www.github.com/infosmith/dotfiles $HOME/my.dotfiles

Change into the cloned repository.

.. code-block:: bash

    cd $HOME/my.dotfiles

Install Python dependencies

.. code-block:: bash

    pip install requirements.txt


Manage dotfiles
***************
Symlink a package to your $HOME directory.

.. code-block:: bash

    ./dotfiles.py add pkg

Symlink specific packages to your $HOME directory.

.. code-block:: bash

    ./dotfiles.py add pkg1_name pkg2_name pkg3_name

Symlink all packages to your $HOME directory. This excludes the tests folder
used to test the dotfiles.py module.

.. code-block:: bash

    ./dotfiles.py add --all

Remove symlinks of a package from your $HOME directory.

.. code-block:: bash

    ./dotfiles.py remove pkg1_name

Remove symlinks of specific packages from your $HOME directory.

.. code-block:: bash

    ./dotfiles.py remove pkg1_name pkg2_name pkg3_name

Remove symlinks of all packages from you $HOME directory.

.. code-block:: bash

    ./dotfiles.py remove --all

Show symlinked files.

.. code-block:: bash

    (virtualsys) (master) ➜  ./dotfiles symlinks                                                                                                                                               ~/my.projects/dotfiles
    .aws symlinked to $HOME/my.dotfiles/aws/.aws
    .bash_profile symlinked to $HOME/my.dotfiles/shell/.bash_profile
    .condarc symlinked to $HOME/my.dotfiles/python/.condarc
    .curlrc symlinked to $HOME/my.dotfiles/shell/.curlrc
    .gitconfig symlinked to $HOME/my.dotfiles/git/.gitconfig
    .gitignore_global symlinked to $HOME/my.dotfiles/git/.gitignore_global
    .gitmessage symlinked to $HOME/my.dotfiles/git/.gitmessage
    .hidden symlinked to $HOME/my.dotfiles/shell/.hidden
    .nvmrc symlinked to $HOME/my.dotfiles/javascript/.nvmrc
    .pylintrc symlinked to $HOME/my.dotfiles/python/.pylintrc
    .pypirc symlinked to $HOME/my.dotfiles/python/.pypirc
    .zshrc symlinked to $HOME/my.dotfiles/shell/.zshrc
    .dotfiles/shell/aliases symlinked to $HOME/my.dotfiles/shell/.dotfiles/shell/aliases
    .dotfiles/shell/bash_profile.sh symlinked to $HOME/my.dotfiles/shell/.dotfiles/shell/bash_profile.sh
    .dotfiles/shell/functions symlinked to $HOME/my.dotfiles/shell/.dotfiles/shell/functions
    .dotfiles/shell/interpreters symlinked to $HOME/my.dotfiles/shell/.dotfiles/shell/interpreters
    .dotfiles/shell/scripts symlinked to $HOME/my.dotfiles/python/.dotfiles/shell/scripts
    .dotfiles/shell/secrets symlinked to $HOME/my.dotfiles/shell/.dotfiles/shell/secrets
    .dotfiles/shell/temp symlinked to $HOME/my.dotfiles/shell/.dotfiles/shell/temp
    .dotfiles/shell/zshrc.sh symlinked to $HOME/my.dotfiles/shell/.dotfiles/shell/zshrc.sh
    .dotfiles/shell/apps/apps.sh symlinked to $HOME/my.dotfiles/shell/.dotfiles/shell/apps/apps.sh
    .dotfiles/shell/apps/rclone.sh symlinked to $HOME/my.dotfiles/rclone/.dotfiles/shell/apps/rclone.sh
    .dotfiles/shell/development/aws.sh symlinked to $HOME/my.dotfiles/aws/.dotfiles/shell/development/aws.sh
    .dotfiles/shell/development/development.sh symlinked to $HOME/my.dotfiles/shell/.dotfiles/shell/development/development.sh
    .dotfiles/shell/development/django.sh symlinked to $HOME/my.dotfiles/python/.dotfiles/shell/development/django.sh
    .dotfiles/shell/development/docker.sh symlinked to $HOME/my.dotfiles/docker/.dotfiles/shell/development/docker.sh
    .dotfiles/shell/development/git.sh symlinked to $HOME/my.dotfiles/git/.dotfiles/shell/development/git.sh
    .dotfiles/shell/development/jupyter.sh symlinked to $HOME/my.dotfiles/python/.dotfiles/shell/development/jupyter.sh
    .dotfiles/shell/development/react.sh symlinked to $HOME/my.dotfiles/javascript/.dotfiles/shell/development/react.sh
    .dotfiles/shell/development/serverless.sh symlinked to $HOME/my.dotfiles/javascript/.dotfiles/shell/development/serverless.sh



.. _.stow-global-ignore: http://www.gnu.org/software/stow/manual/html_node/Types-And-Syntax-Of-Ignore-Lists.html
.. _.stowrc: http://www.gnu.org/software/stow/manual/stow.html#Resource-Files
.. _Stow: https://www.gnu.org/software/stow/
.. _Stow documents: https://www.gnu.org/software/stow/manual/stow.html
.. _nix: https://en.wikipedia.org/wiki/Unix-like
