from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import (
    load_pem_public_key,
    load_pem_private_key,
)


class Serialization:
    """
    Class that contains Serialization functions.
    """
    def __init__(self):
        pass

    def symmetric_key_serialization(file_path: str, key: bytes) -> None:
        """
        Serialization of the symmetric encryption key
        
        Args:
            file_path: file_path for serialization
            key: symmetric key
        """
        try:
            with open(file_path, "wb") as key_file:
                key_file.write(key)
        except Exception as error:
            print(error)

    def symmetric_key_deserialization(file_path: str) -> bytes:
        """
        Deserialization of the symmetric encryption key
        
        Args:
            file_path: file_path for deserialization
            
        Returns:
            symmetric key
        """
        try:
            with open(file_path, "rb") as key_file:
                return key_file.read()
        except Exception as error:
            print(error)

    def serialize_private_key(path: str, private_key: rsa.RSAPrivateKey) -> None:
        """
        Serializes private key for asymmetrical method.
        
        Args:
            path: path to key to serialize.
            private_key: private key object.
        """
        try:
            with open(path, "wb") as private_out:
                private_out.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
        except Exception as e:
            print("Error:", e)

    def serialize_public_key(path: str, public_key: rsa.RSAPublicKey) -> None:
        """
        Serializes public key for asymmetrical method.
        
        Args:
            path: path to key to serialize.
            public_key: public key object.
        """
        try:
            with open(path, "wb") as public_out:
                public_out.write(
                    public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
                    )
                )
        except Exception as e:
            print("Error:", e)

    def deserialize_private_key(path) -> rsa.RSAPrivateKey:
        """
        Deserializes private key for asymmetrical method.
        
        Args:
            path: path to key to deserialize.
            
        Returns:
            private key.
        """
        try:
            with open(path, "rb") as pem_in:
                private_bytes = pem_in.read()
                d_private_key = load_pem_private_key(
                    private_bytes,
                    password=None,
                )
            return d_private_key
        except Exception as e:
            print("Error:", e)

    def deserialize_public_key(path) -> rsa.RSAPublicKey:
        """
        Deserializes public key for asymmetrical method.
        
        Args:
            path: path to key to deserialize.
            
        Returns:
            public key.
        """
        try:
            with open(path, "rb") as pem_in:
                public_bytes = pem_in.read()
                d_public_key = load_pem_public_key(public_bytes)
            return d_public_key
        except Exception as e:
            print("Error:", e)
