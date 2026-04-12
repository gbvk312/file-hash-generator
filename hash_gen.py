import argparse
import hashlib
import sys
import os

def hash_file(filepath):
    """
    Reads a file in chunks and computes MD5, SHA-1, and SHA-256 hashes.
    """
    if not os.path.isfile(filepath):
        print(f"Error: The file '{filepath}' does not exist or is a directory.", file=sys.stderr)
        sys.exit(1)

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
         print(f"Error: Permission denied when reading '{filepath}'.", file=sys.stderr)
         sys.exit(1)
    except Exception as e:
         print(f"An error occurred while reading the file: {e}", file=sys.stderr)
         sys.exit(1)

    return {
        'MD5': md5_hash.hexdigest(),
        'SHA1': sha1_hash.hexdigest(),
        'SHA256': sha256_hash.hexdigest()
    }

def main():
    parser = argparse.ArgumentParser(description="Generate MD5, SHA-1, and SHA-256 hashes for a file.")
    parser.add_argument("file", help="Path to the file to hash")
    args = parser.parse_args()

    hashes = hash_file(args.file)

    print(f"\nHashes for {args.file}:\n")
    print(f"\033[96mMD5\033[0m    : {hashes['MD5']}")
    print(f"\033[96mSHA-1\033[0m  : {hashes['SHA1']}")
    print(f"\033[96mSHA-256\033[0m: {hashes['SHA256']}")
    print("\n")

if __name__ == "__main__":
    main()
