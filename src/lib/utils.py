# external imports
import json
from pathlib import Path
from subprocess import run

import tomlkit

# internal imports
from src.lib.templates import templates


def clone_template(template_name: str, output: str) -> None:
    """Clone the template.

    Args:
    ----
        template_name (str): template to clone
        output (str): output directory


    """
    template = templates[template_name]
    run(["git", "clone", template.url, output], check=True)  # noqa: S603, S607
    print(f"Cloned {template.name} template to {output}")  # noqa: T201
    run(["rm", "-rf", f"{output}/.git"], check=True)  # noqa: S603, S607
    print("Removed .git directory")  # noqa: T201


def update_pyproject_name(project_dir: str, name: str) -> None:
    """Update pyproject.toml name.

    Args:
    ----
        project_dir (str): project directory
        name (str): name to update

    """
    pyproject_toml = f"{project_dir}/pyproject.toml"
    with Path(pyproject_toml).open("r") as f:
        pyproject = tomlkit.parse(f.read())

    pyproject["project"]["name"] = name

    with Path(pyproject_toml).open("w") as f:
        f.write(tomlkit.dumps(pyproject))

    print(f"Updated {pyproject_toml} name to {name}")  # noqa: T201


def update_readme_name(project_dir: str, name: str) -> None:
    """Update README.md name.

    Args:
    ----
        project_dir (str): project directory
        name (str): name to update

    """
    readme = f"{project_dir}/README.md"
    with Path(readme).open("r") as f:
        content = f.read()

    # 1行目を`# {name}`に更新
    content = content.split("\n")
    content[0] = f"# {name.upper()}"

    with Path(readme).open("w") as f:
        f.write("\n".join(content))

    print(f"Updated {readme} name to {name}")  # noqa: T201


def update_devcontainer_name(project_dir: str, name: str) -> None:
    """Update .devcontainer/devcontainer.json name.

    Args:
    ----
        project_dir (str): project directory
        name (str): name to update

    """
    devcontainer_json = f"{project_dir}/.devcontainer/devcontainer.json"

    if not Path(project_dir / ".devcontainer").exists():
        print("No .devcontainer directory")  # noqa: T201
        return

    with Path(devcontainer_json).open("r") as f:
        devcontainer = json.load(f)

    if "name" in devcontainer:
        devcontainer["name"] = name

    with Path(devcontainer_json).open("w") as f:
        json.dump(devcontainer, f, indent=4, ensure_ascii=False)

    print(f"Updated {devcontainer_json} name to {name}")  # noqa: T201
