# external imports
from pydantic import BaseModel

# internal imports


class Templates(BaseModel):
    """Templates class for the main script."""

    # templates
    name: str

    # url
    url: str

    # description
    description: str


templates: dict[str, Templates] = {
    "torch": Templates(
        name="torch",
        url="https://github.com/nishide-dev/pytorch-template",
        description="PyTorch template",
    ),
    "py": Templates(
        name="py",
        url="https://github.com/nishide-dev/python-template",
        description="Python template",
    ),
}
