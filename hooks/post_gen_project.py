from pathlib import Path

molecule = "{{ cookiecutter.molecule }}"

if molecule != "docker":
    Path(".github/workflows/molecule.yml").unlink(missing_ok=True)
