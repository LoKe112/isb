import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricCryptography:
    """
    Class that contains methods for generating key,
    encryption and decryption by symmetrical method.
    """

    def __init__(self, key_path: str) -> None:
        """
        Initializes AsymmetricCryptography class object.

        Args:
            key_path: path to key

        Returns:
            None.
        """
        self.key_path = key_path

    def generate_key(self, size: int) -> bytes:
        """
        Performs generation key for symmetrical method.

        Args:
            size: size of key in bits.

        Returns:
            key as bytes object.
        """
        try:
            key = os.urandom(size)
            return key
        except Exception as e:
            print("Error:", e)

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        """
        Performs symmetrical encryption of data using key.

        Args:
            data: bytes object that is needed to encrypt.
            key: bytes object key for encryption.

        Returns:
            bytes of encrypted data.
        """
        try:
            iv = os.urandom(16)
            cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(256).padder()
            padded_text = padder.update(data) + padder.finalize()
            c_text = iv + encryptor.update(padded_text) + encryptor.finalize()
            return c_text
        except Exception as e:
            print("Error:", e)

    def decrypt(self, data: bytes, key: bytes) -> bytes:
        """
        Performs symmetrical decryption of encrypted data using key.

        Args:
            data: bytes object that is needed to decrypt.
            key: bytes object key for decryption.

        Returns:
            bytes of decrypted data.
        """
        try:
            iv = data[:16]
            data = data[16:]
            cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            dc_data = decryptor.update(data) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            unpadded_dc_data = unpadder.update(dc_data) + unpadder.finalize()
            return unpadded_dc_data
        except Exception as e:
            print("Error:", e)
