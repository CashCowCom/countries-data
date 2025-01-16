#!/usr/bin/env python3

import argparse

import toml


def update_version(version_type: str) -> None:
    """Updates the version in the pyproject.toml file.

    Args:
        version_type (str): The type of version increment (patch, minor, major).
    """

    file_path = "./pyproject.toml"

    with open(file_path, "r+") as f:  # noqa: PTH123
        data = toml.load(f)

        # Extract current version
        current_version = data["tool"]["poetry"]["version"]
        major, minor, patch = map(int, current_version.split("."))

        # Increment version based on type
        if version_type == "patch":
            patch += 1
        elif version_type == "minor":
            minor += 1
            patch = 0
        elif version_type == "major":
            major += 1
            minor = patch = 0
        else:
            raise ValueError("Invalid version type. Please specify patch, minor, or major.")

        # Update the version in the TOML data
        data["tool"]["poetry"]["version"] = f"{major}.{minor}.{patch}"

        # Write the updated data back to the file
        f.seek(0)
        toml.dump(data, f)  # type: ignore
        f.truncate()

        print(f"{data['tool']['poetry']['version']}")  # noqa T201


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update package version")
    parser.add_argument(
        "version_type",
        choices=["patch", "minor", "major"],
        help="The type of version increment",
    )

    args = parser.parse_args()

    update_version(args.version_type)
