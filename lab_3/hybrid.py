from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.asymmetric import padding

from function import IOFunctions
from symmetrical import SymmetricCryptography
from asymmetrical import AsymmetricCryptography
from serialize import Serialization


class HybridCryptography:
    """Class that contains methods for generating key,
    encryption and decryption by hybrid method(symmetrical and asymmetrical).
    """

    def __init__(
        self, symmetric_key_path: str, private_key_path: str, public_key_path: str
    ) -> None:
        """
        Initializes HybridCryprography class object.

        Args:
            symmetric_key_path: path for saving symmetrical key.
            private_key_path: path for saving private key.
            public_key_path: path for saving public key.
        """
        self.symmetric = SymmetricCryptography(symmetric_key_path)
        self.asymmetric = AsymmetricCryptography(private_key_path, public_key_path)

    def generate_keys(self, size: int) -> None:
        """
        Generates key for hybrid method.

        Args:
            size: size of keys in bits.

        Returns:
            tuple of private and public keys.
        """
        try:
            if size != 16 and size != 24 and size != 32:
                raise ValueError("Size of keys must be 128, 192 or 256")
            symmetric_key = self.symmetric.generate_key(size)
            asymmetric_key = self.asymmetric.generate_key(size)
            private_key, public_key = asymmetric_key
            Serialization.serialize_private_key(
                self.asymmetric.private_key_path, private_key
            )
            Serialization.serialize_public_key(
                self.asymmetric.public_key_path, public_key
            )
            IOFunctions.write_bytes(
                self.symmetric.key_path,
                public_key.encrypt(
                    symmetric_key,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None,
                    ),
                ),
            )
        except Exception as e:
            print("Error:", e)

    def encrypt(self, text_path: str, encrypted_text_path: str) -> None:
        """
        Does hybrid encryption of data.

        Args:
            text_path: path to file with data that is needed to encrypt.
            encrypted_text_path: path to file for saving encrypted data.
        """
        try:
            text = bytes(IOFunctions.read_txt(text_path), "UTF-8")
            key = Serialization.deserialize_private_key(
                self.asymmetric.private_key_path
            )
            symmetric_key = self.asymmetric.decrypt(
                IOFunctions.read_bytes(self.symmetric.key_path), key
            )
            c_text = self.symmetric.encrypt(text, symmetric_key)
            IOFunctions.write_bytes(encrypted_text_path, c_text)
        except Exception as e:
            print("Error:", e)

    def decrypt(self, text_path: str, decrypted_text_path: str) -> None:
        """
        Does hybrid dencryption of data.

        Args:
            text_path: path to file with data that is needed to decrypt.
            decrypted_text_path: path to file for saving decrypted data.
        """
        try:
            c_data = IOFunctions.read_bytes(text_path)
            key = Serialization.deserialize_private_key(
                self.asymmetric.private_key_path
            )
            symmetric_key = self.asymmetric.decrypt(
                IOFunctions.read_bytes(self.symmetric.key_path), key
            )
            dc_data = self.symmetric.decrypt(c_data, symmetric_key)
            IOFunctions.write_bytes(decrypted_text_path, dc_data)
        except Exception as e:
            print("Error:", e)
