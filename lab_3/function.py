import json

from constants import PATHS


class IOFunctions:
    """Class that contains additional functions
    for reading and writing files.
    """

    def write_bytes(path: str, data: bytes) -> None:
        """
        Writes bytes into txt file.
        
        Args:
            path: path to txt file.
            data: bytes object that is needed to write.
        """
        try:
            with open(path, "wb") as file:
                file.write(data)
        except Exception as e:
            print("Error:", e)

    def read_bytes(path: str) -> bytes:
        """
        Reads bytes from txt file.
        
        Args:
            path: path to txt file.
            
        Returns:
            bytes.
        """
        try:
            with open(path, "rb") as file:
                data = file.read()
            return data
        except Exception as e:
            print("Error:", e)

    def write_txt(path: str, data: str) -> None:
        """
        Writes string into txt file.
        
        Args:
            path: path to txt file.
            data: string object that is needed to write.
        """
        try:
            with open(path, "w") as file:
                data = file.write(data)
        except Exception as e:
            print("Error:", e)

    def read_txt(path: str) -> str:
        """
        Reads from txt file.
        
        Args:
            path: path to txt file.
            
        Returns:
            string
        """
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = file.read()
            return data
        except Exception as e:
            print("Error:", e)

    def json_reader(path: str) -> dict:
        """
        Reads json file.
        
        Args:
            path: path to json file.
            
        Returns:
            dict which contains keys and values from file.
        """
        try:
            with open(path, "r", encoding="utf-8") as file:
                paths = json.load(file)
            return paths
        except Exception as e:
            print("Error:", e)
