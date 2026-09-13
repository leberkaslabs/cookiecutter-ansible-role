# Cookiecutter: Ansible Role

[![Cookiecutter Test](https://github.com/leberkaslabs/cookiecutter-ansible-role/actions/workflows/cookiecutter.yml/badge.svg)](https://github.com/leberkaslabs/cookiecutter-ansible-role/actions/workflows/cookiecutter.yml)

This repository offers a ready-to-use template for building Ansible roles with Cookiecutter. It helps you quickly set up a consistent, well-structured project layout, making your roles easier to reuse and maintain over time.

## Prerequisites

- Ensure you have Cookiecutter installed (e.g. `pip3 install cookiecutter`)

## Usage

Run the following command and answer the prompted questions:

```bash
cookiecutter https://github.com/leberkaslabs/cookiecutter-ansible-role
```

> [!NOTE]
> *The values in parentheses show the default options*

```bash
[1/9] full_name (Niclas Spreng):
[2/9] github_username (leberkaslabs):
[3/9] role_name (Ansible Role Boilerplate): nginx
[4/9] project_slug (ansible-role-nginx):
[5/9] namespace (leberkaslabs):
[6/9] description (Enter Ansible role description): This is my nginx role
[7/9] Select molecule
  1 - docker
  2 - vagrant
  Choose from [1/2] (1): 1
[8/9] Select license
  1 - MIT
  2 - Proprietary
  Choose from [1/2] (1): 1
[9/9] min_ansible_version (2.15):
```

## License

Copyright (c) 2026 Niclas Spreng
