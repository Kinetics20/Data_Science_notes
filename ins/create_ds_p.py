from pathlib import Path
import subprocess
import sys


def get_project_name():
    project_name = input("Enter project name: ").strip()
    while not project_name:
        project_name = input("Project name cannot be empty. Enter project name: ").strip()
    return project_name


def create_project_structure(base_path: Path):
    structure = {
        "data/raw": None,
        "data/processed": None,
        "data/external": None,
        "data/interim": None,
        "notebooks/exploration": None,
        "notebooks/modeling": None,
        "notebooks/reporting": None,
        "src/data": None,
        "src/features": None,
        "src/models": None,
        "src/visualization": None,
        "reports/figures": None,
        "tests": None,
    }

    # creating folders
    for path in structure.keys():
        (base_path / path).mkdir(parents=True, exist_ok=True)

    # creating files
    (base_path / "reports/final_report.md").touch()
    (base_path / "requirements.txt").touch()

    print(f"Project '{base_path.name}' created successfully!")


def create_pyproject_toml(base_path: Path, project_name: str):
    pyproject_content = f"""[project]
name = "{project_name}"
version = "0.1.0"
description = "The repository is dedicated to exercises in data science and python programming."
authors = ["Piotr Lipinski <kinetics20@gmail.com>"]
license = "Beerware"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "jupyterlab>=4.3.5",
    "matplotlib>=3.10.1",
    "openpyxl>=3.1.5",
    "pandas==2.2.3",
    "pyarrow>=19.0.1",
    "tabulate>=0.9.0",
    "xlsxwriter>=3.2.2"
]
"""

    with open(base_path / "pyproject.toml", "w") as f:
        f.write(pyproject_content)

    print("pyproject.toml created successfully!")


def add_dependencies(base_path: Path):
    dependencies = [
        "jupyterlab>=4.3.5",
        "matplotlib>=3.10.1",
        "openpyxl>=3.1.5",
        "pandas==2.2.3",
        "pyarrow>=19.0.1",
        "tabulate>=0.9.0",
        "xlsxwriter>=3.2.2"
    ]

    for dep in dependencies:
        print(f"Adding dependency: {dep}")
        subprocess.run(["uv", "add", dep], cwd=base_path, check=True)

    print("Dependencies added successfully!")


def main():
    base_dir = Path.cwd()  # current folder
    project_name = get_project_name()
    project_path = base_dir / project_name

    if project_path.exists():
        print(f"Error: Directory '{project_name}' already exists.")
        sys.exit(1)

    create_project_structure(project_path)
    create_pyproject_toml(project_path, project_name)
    add_dependencies(project_path)


if __name__ == "__main__":
    main()
