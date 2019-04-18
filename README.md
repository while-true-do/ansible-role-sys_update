<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-sys_update.svg)](https://github.com/while-true-do/ansible-role-sys_update/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-sys_update.svg)](https://github.com/while-true-do/ansible-role-sys_update/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-sys_update.svg)](https://github.com/while-true-do/ansible-role-sys_update/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-sys_update.svg)](https://github.com/while-true-do/ansible-role-sys_update/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-sys_update.svg)](https://travis-ci.com/while-true-do/ansible-role-sys_update)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_update%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_update)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_update%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_update)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_update%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_update)

# Ansible Role: sys_update

An Ansible Role to update a system and reboot it.

## Motivation

Updating a system is a very common use case during every lifecycle.

## Description

This Role applies updates and reboots the system, if needed.

## Requirements

Used Modules:

-   [Ansible Module Package](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Module Reboot](https://docs.ansible.com/ansible/latest/modules/reboot_module.html)
-   [Ansible Module dnf](https://docs.ansible.com/ansible/latest/modules/dnf_module.html)
-   [Ansible Module yum](https://docs.ansible.com/ansible/latest/modules/yum_module.html)
-   [Ansible Module command](https://docs.ansible.com/ansible/latest/modules/command_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/sys_update)
```
ansible-galaxy install while_true_do.sys_update
```

Install from [Github](https://github.com/while-true-do/ansible-role-sys_update)
```
git clone https://github.com/while-true-do/ansible-role-sys_update.git while_true_do.sys_update
```

## Usage

### Role Variables

defaults/main.yml
```
---
# defaults file for while_true_do.sys_update

# Dependencies to check for reboots (defined in vars/*.yml)
wtd_sys_update_dep_packages: ""
wtd_sys_update_dep_packages_state: "present"

# Reboot automatically, when needed
wtd_sys_update_reboot_enabled: True
# Force reboot after every update
wtd_sys_update_reboot_forced: False
wtd_sys_update_reboot_msg: "System is going down to apply updates."
wtd_sys_update_reboot_timeout: "3600"
```

vars/CentOS.yml
```
---
# vars file for while_true_do.sys_update

wtd_sys_update_dep_packages: "yum-utils"

```

vars/Fedora.yml
```
---
# vars file for while_true_do.sys_update

wtd_sys_update_dep_packages: "tracer"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.sys_update
```

#### Advanced

```
- hosts: all
  roles:
    - role: while_true_do.sys_update
      wtd_sys_update_reboot_forced: True
      wtd_sys_update_reboot_msg: "Go down down down..."
      wtd_sys_update_reboot_timeout: "600"

```

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-sys_update/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-sys_update/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
