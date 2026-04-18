import argparse
import hashlib
import sys
import os

def hash_file(filepath):
    """
    Reads a file in chunks and computes MD5, SHA-1, and SHA-256 hashes.
    """
    if not os.path.isfile(filepath):
        return None

    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()
    sha256_hash = hashlib.sha256()

    # Read the file in chunks to handle arbitrarily large files without high memory usage
    chunk_size = 65536  # 64 KB
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                md5_hash.update(chunk)
                sha1_hash.update(chunk)
                sha256_hash.update(chunk)
    except PermissionError:
         return "Error: Permission denied."
    except Exception as e:
         return f"An error occurred: {e}"

    return {
        'MD5': md5_hash.hexdigest(),
        'SHA1': sha1_hash.hexdigest(),
        'SHA256': sha256_hash.hexdigest()
    }

def main():
    parser = argparse.ArgumentParser(description="Generate MD5, SHA-1, and SHA-256 hashes for a file or directory.")
    parser.add_argument("path", help="Path to the file or directory to hash")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively walk through directories")
    args = parser.parse_args()

    target_path = args.path
    files_to_hash = []

    if os.path.isfile(target_path):
        files_to_hash.append(target_path)
    elif os.path.isdir(target_path):
        if args.recursive:
            for root, _, files in os.walk(target_path):
                for name in files:
                    files_to_hash.append(os.path.join(root, name))
        else:
            for name in os.listdir(target_path):
                full_path = os.path.join(target_path, name)
                if os.path.isfile(full_path):
                    files_to_hash.append(full_path)
    else:
        print(f"Error: The path '{target_path}' does not exist or is not a valid file/directory.", file=sys.stderr)
        sys.exit(1)

    if not files_to_hash:
        print(f"No files found at '{target_path}'.")
        return

    # Sort files for consistent output
    files_to_hash.sort()

    for filepath in files_to_hash:
        hashes = hash_file(filepath)
        
        if isinstance(hashes, str):
            print(f"\n[{filepath}] -> {hashes}")
            continue

        print(f"\nHashes for {filepath}:\n")
        print(f"\033[96mMD5\033[0m    : {hashes['MD5']}")
        print(f"\033[96mSHA-1\033[0m  : {hashes['SHA1']}")
        print(f"\033[96mSHA-256\033[0m: {hashes['SHA256']}")
    
    print("\n")

if __name__ == "__main__":
    main()
