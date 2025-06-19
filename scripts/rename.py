# This script will be used to enforce kebab-case filenames.
# It will be integrated as a pre-commit hook.

import os
import sys

def to_kebab_case(name):
    # A simple conversion to kebab-case:
    # 1. Replace underscores and spaces with hyphens.
    # 2. Convert to lowercase.
    # This is a basic implementation and might need to be more robust.
    return name.replace("_", "-").replace(" ", "-").lower()

def rename_files_in_directory(directory):
    renamed_count = 0
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            original_path = os.path.join(root, name)
            kebab_name = to_kebab_case(name)

            if name == kebab_name:
                continue

            new_path = os.path.join(root, kebab_name)

            if os.path.exists(new_path):
                print(f"Warning: Target path {new_path} already exists. Skipping rename for {original_path}")
                continue

            try:
                os.rename(original_path, new_path)
                print(f"Renamed: {original_path} -> {new_path}")
                renamed_count += 1
            except OSError as e:
                print(f"Error renaming {original_path} to {new_path}: {e}")
    return renamed_count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directories_to_scan = sys.argv[1:]
    else:
        # Default to docs directory if no arguments are provided
        # As per fixes-1.md, files are in docs/
        directories_to_scan = ["docs"]

    total_renamed = 0
    for directory in directories_to_scan:
        if os.path.exists(directory):
            print(f"\nScanning directory: {directory}")
            total_renamed += rename_files_in_directory(directory)
        else:
            print(f"Error: Directory '{directory}' not found.")

    if total_renamed > 0:
        print(f"\nSuccessfully renamed {total_renamed} files/directories to kebab-case.")
        # For pre-commit hook, exit with non-zero if changes were made.
        # This helps pre-commit identify that the hook modified files.
        # However, a rename script is usually run manually or with care.
        # For now, let's exit 0, assuming manual run or further integration logic.
        # To make it fail for pre-commit if not compliant:
        # sys.exit(1)
    else:
        print("\nNo files/directories needed renaming or an error occurred.")

    # For actual pre-commit hook usage, this script would typically check for
    # non-kebab-case files and exit 1 if any are found,
    # or automatically rename them and potentially exit 1 to indicate changes.
    # The renaming logic itself would be the core part.
    # This script is a starting point for such a utility.
    print("\nScript execution finished.")
