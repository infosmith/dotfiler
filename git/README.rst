git configuration
=================

My Git configuration and reference.


Dependencies
------------
Dependencies are installed automatically with Ansible during deployment.

* `commitizen  <https://github.com/commitizen/cz-cli>`_
* `commitlint  <https://github.com/conventional-changelog/commitlint>`_
* `Git Large File Storage (LFS) <https://git-lfs.github.com/>`_
* `micro text editor <https://github.com/zyedidia/micro>`_
* `pre-commit <https://pre-commit.com/>`_
* `pytest <https://docs.pytest.org/en/latest/>`_
* `yamllint  <https://github.com/adrienverge/yamllint>`_


File Descriptions
-----------------
`.gitattributes <https://www.git-scm.com/docs/gitattributes/>`_
`.gitconfig <https://git-scm.com/docs/gitconfig>`_
`.gitignore <https://git-scm.com/docs/gitignore>`_
`.gitmessage <https://git-scm.com/docs/gitmessage>`_
`.gitmodules <https://git-scm.com/docs/gitmodules>`_

.dotfiles/storage/git/precommit/install.sh
    Script used by git precommit alias to copy
    $DOTFILES/storage/git/precommit/<template_name>.yaml files into
    initialized repositories as pre-commit-config.yaml files such as:

.. code-block:: bash

    git precommit python


.dotfiles/terminal/development/git.sh
    Git BASH functions automatically sourced by terminal package

.ssh/config
    ssh host configuration file including git hosts

    Adding this file saves a negligible amount of time but some may argue the
    time saved isn't worth potential security vulnerabilities adding this file
    to a public repository may entail. However, there really isn't any
    compromising information here. Knowing what hosts I use isn't anymore
    compromising than knowing there are a limited number of widely adopted git
    hosts. It's also not compromising to know the names of the identity files
    used -- at least not significantly. If someone is able to access these files
    knowing their complete path then more significant vulnerabilities exist on
    the host where this file resides.


Integrations of Interest
------------------------
* `conventional-changelog  <https://github.com/conventional-changelog/conventional-changelog>`_
* `diff-so-fancy  <https://github.com/so-fancy/diff-so-fancy>`_
* `git-crypt  <https://github.com/AGWA/git-crypt>`_
* `git-extras  <https://github.com/tj/git-extras>`_
* `git-open  <https://github.com/paulirish/git-open#oh-my-zsh>`_
* `git-recent  <https://github.com/paulirish/git-recent>`_
* `GitHub Résumé <https://github.com/resume/resume.github.com>`_
* `linty-fresh <https://github.com/lyft/linty_fresh>`_
* `overcommit <https://github.com/sds/overcommit>`_
* `reviewdog <https://github.com/reviewdog/reviewdog>`_
* `semantic-release  <https://github.com/semantic-release/semantic-release>`_
* `standard-version <https://github.com/conventional-changelog/standard-version>`_


References
----------

Documentation
+++++++++++++
* `Conventional Commits <https://www.conventionalcommits.org>`_
* `Git book <https://git-scm.com/book/en/v2>`_
* `Git commands <https://git-scm.com/docs/git#_git_commands>`_
* `Git hooks <https://git-scm.com/docs/githooks>`_
* `Git manpages <http://web.mit.edu/git/www/>`_
* `GitHub Docs <https://docs.github.com/en>`_
* `GitHub Pro <https://docs.github.com/en/free-pro-team@latest/github>`_
* `TOML <https://github.com/toml-lang/toml>`_

Files
+++++
* `.gitconfig of garybernhardt/dotfiles <https://github.com/garybernhardt/dotfiles/blob/35e0d65f5a13d4bf5f6e303ded8bdd1b7af7cb69/.gitconfig>`_
* `.gitconfig of gitconfig/gitconfig <https://github.com/gitconfig/gitconfig/blob/0b27adf2e61772db58ccf96e954cc8e1922f44ad/.gitconfig>`_
* `.gitconfig of lewagon/dotfiles <https://github.com/lewagon/dotfiles/blob/2da817a00711a392325ee4515bde5cc4dc0770ec/gitconfig>`_
* `.gitconfig of mathiasbynens/dotfiles <https://github.com/mathiasbynens/dotfiles/blob/0cd43d175a25c0e13e1e06ab31ccfd9f0169cf73/.gitconfig>`_
* `.gitconfig of nicknisi/dotfiles <https://github.com/nicknisi/dotfiles/blob/27e7a87338153c704de3416bedef977c30d50bd0/git/gitconfig.symlink>`_
* `.gitconfig of paulirish/dotfiles <https://github.com/paulirish/dotfiles/blob/c4e1e846a11877670de8576a5f8fe74b306b3f9d/.gitconfig>`_
* `.gitconfig of skwp/dotfiles <https://github.com/skwp/dotfiles/blob/b28008745bade9206e1ed281eebc9d563d62fccc/git/gitconfig>`_
* `.gitconfig of thoughtbot/dotfiles <https://github.com/thoughtbot/dotfiles/blob/e5c5ff3ebda365b70346c3034ab846fde106d735/gitconfig>`_
* `.gitignore of github/gitignore <https://github.com/github/gitignore>`_
* `.gitmessage of thoughtbot/dotfiles <https://github.com/thoughtbot/dotfiles/blob/ef58e42a248863c4010dd9977adeffe1b5e6755e/gitmessage>`_
* `.gitmodule of paulirish/dotfiles <https://github.com/paulirish/dotfiles/blob/a5f8f1272ff15958514e0ba2cfcf27015f17e237/.gitmodules>`_


Tutorials
+++++++++
* `.gitattributes Best Practices <https://rehansaeed.com/gitattributes-best-practices/>`_
* `Adding a new SSH key to your GitHub account  <https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/>`_
* `Atlassians's Git Tutorials <https://www.atlassian.com/git/tutorials>`_
* `Configuring mergetool To Delete Temporary Files <https://git-scm.com/docs/git-mergetool#_temporary_files>`_
* `Conventional Commit Messages <https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13>`_
* `Conventional Commit messages in git <https://medium.com/@github.gkarthiks/conventional-commit-messages-in-git-47b04129fffa>`_
* `Create A Custom Git Commit Template <https://alex-wasik.medium.com/create-a-custom-git-commit-template-84468232a459>`_
* `Customizing Git Attributes <https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes>`_
* `Customizing Git Configuration <https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration>`_
* `Diff tools for the command line <https://blog.42mate.com/diff-tools-for-the-command-line/>`_
* `Generating a new SSH key and adding it to the ssh-agent  <https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/>`_
* `Git Hooks Tutorials <https://githooks.com/>`_
* `Git in Other Environments - Git in Zsh <https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Zsh>`_
* `Git tip: Fix a mistake in a previous commit <https://croisant.net/blog/2008-06-22-git-tip-fix-a-mistake-in-a-previous-commit/>`_
* `Git: Prevent commits in master branch  <https://stackoverflow.com/questions/40462111/git-prevent-commits-in-master-branch>`_
* `How to Spoof Any User on Github…and What to Do to Prevent It <https://blog.gruntwork.io/how-to-spoof-any-user-on-github-and-what-to-do-to-prevent-it-e237e95b8deb>`_
* `Private emails, now more private <https://github.blog/2017-04-11-private-emails-now-more-private/>`_
* `Rewriting Git Commit History <https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History>`_
* `Setting up a seperate Github and Bitbucket account <https://gist.github.com/rosswd/e1afd2b0b0d515517eac>`_
* `Setting up and using Meld as your git difftool and mergetool <https://stackoverflow.com/questions/34119866/setting-up-and-using-meld-as-your-git-difftool-and-mergetool>`_
* `Setting Up Git for the First Time <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>`_
* `Stashing Changes and Cleaning Untracked Files <https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning>`_
* `Understanding Semantic Commit Messages Using Git and Angular <https://nitayneeman.com/posts/understanding-semantic-commit-messages-using-git-and-angular/>`_
* `Using Git Commit Message Templates to Write Better Commit Messages <https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733>`_
* `W3 Docs' Tutorials  <https://www.w3docs.com/learn-git.html>`_
