# external imports
import sys
from pathlib import Path

# internal imports
sys.path.append(str(Path(__file__).parent.parent))
from src.lib.arguments import Arguments
from src.lib.utils import (
    clone_template,
    update_devcontainer_name,
    update_pyproject_name,
    update_readme_name,
)


def generate_template(args: Arguments) -> None:
    target_dir = Path(args.output) / args.name
    target_dir.mkdir(parents=True, exist_ok=True)

    try:
        clone_template(args.template, target_dir)
        update_pyproject_name(target_dir, args.name)
        update_readme_name(target_dir, args.name)
        update_devcontainer_name(target_dir, args.name)
        print(f"Created {args.name} project in {target_dir}")  # noqa: T201

    except Exception as e:  # noqa: BLE001
        print(f"Failed to create {args.name} project in {target_dir}")  # noqa: T201
        print(e)  # noqa: T201
        return 1

    return 0


def main() -> None:
    args: Arguments = Arguments.parse_args()
    generate_template(args)


if __name__ == "__main__":
    main()
