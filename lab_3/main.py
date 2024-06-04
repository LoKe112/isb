import argparse

from hybrid import HybridCryptography
from function import IOFunctions
from constants import PATHS


if __name__ == "__main__":
    paths = IOFunctions.json_reader(PATHS)
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-gen",
        "--generation",
        help="Запускает режим генерации ключей",
        action="store_true",
    )
    group.add_argument(
        "-enc", "--encryption", help="Запускает режим шифрования", action="store_true"
    )
    group.add_argument(
        "-dec", "--decryption", help="Запускает режим дешифрования", action="store_true"
    )

    args = parser.parse_args()
    match (args.generation, args.encryption, args.decryption):
        case (True, False, False):
            h = HybridCryptography(
                paths["sym_path"], paths["private_path"], paths["public_path"]
            )
            h.generate_keys(32)
        case (False, True, False):
            h = HybridCryptography(
                paths["sym_path"], paths["private_path"], paths["public_path"]
            )
            h.encrypt(paths["text"], paths["encrypted_text"])
        case (False, False, True):
            h = HybridCryptography(
                paths["sym_path"], paths["private_path"], paths["public_path"]
            )
            h.decrypt(paths["encrypted_text"], paths["decrypted_text"])
