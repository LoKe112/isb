from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


class AsymmetricCryptography:
    """
    Class that contains methods for generating key,
    encryption and decryption by asymmetrical method.
    """

    def __init__(self, private_key_path: str, public_key_path: str) -> None:
        """
        Initializes AsymmetricCryptography class object.

        Args:
            private_key_path: path for saving private key.
            public_key_path: path for saving public key.

        Returns:
            None.
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path

    def generate_key(self, size: int) -> tuple:
        """
        Generates key for asymmetrical method.

        Args:
            size: size of keys in bits.

        Returns:
            tuple of private and public keys.
        """
        try:
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            public_key = private_key.public_key()
            return private_key, public_key
        except Exception as e:
            print("Error:", e)

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        """
        Performs asymmetrical encryption of data using key.

        Args:
            data: bytes object that is needed to encrypt.
            key: bytes object key for encryption.

        Returns:
            bytes of encrypted data.
        """
        try:
            c_data = key.encrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            return c_data
        except Exception as e:
            print("Error:", e)

    def decrypt(self, data: bytes, key: bytes) -> bytes:
        """
        Performs asymmetrical decryption of encrypted data using key.

        Args:
            data: bytes object that is needed to decrypt.
            key: bytes object key for decryption.

        Returns:
            bytes of decrypted data.
        """
        try:
            c_data = key.decrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            return c_data
        except Exception as e:
            print("Error:", e)
