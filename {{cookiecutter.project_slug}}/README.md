# Ansible Role: {{ cookiecutter.role_name.capitalize() }}

[![Ansible Molecule](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/molecule.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/molecule.yml)

{{ cookiecutter.description }}

## Prerequisites

- Ensure you have Ansible installed (e.g. `pip3 install ansible`)
- **Development**: Install the pip packages listed in [requirements.txt](requirements.txt)

## Role Variables

The default values for the variables are set in [defaults/main.yml](defaults/main.yml)

```yaml
- hosts: all
  roles:
    - role: {{ cookiecutter.github_username }}.{{ cookiecutter.role_name }}
```

## License

Copyright (c) {% now 'local', '%Y' %} {{ cookiecutter.full_name }}
