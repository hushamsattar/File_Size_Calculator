# 3 – Checking File Size

import os


def get_file_size(file_path):

    # Returns the size of a file in bytes, KB, MB, and GB.
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    size_bytes = os.path.getsize(file_path)

    return {
        "bytes": size_bytes,
        "KB": size_bytes / 1024,
        "MB": size_bytes / (1024 ** 2),
        "GB": size_bytes / (1024 ** 3)
    }


# Example usage
file_path = "file.txt"

try:
    size = get_file_size(file_path)

    print(f"File: {file_path}")
    print(f"Size in bytes: {size['bytes']}")
    print(f"Size in KB: {size['KB']:.2f}")
    print(f"Size in MB: {size['MB']:.4f}")
    print(f"Size in GB: {size['GB']:.6f}")

except FileNotFoundError as e:
    print(e)

