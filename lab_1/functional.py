import operator
import json
import argparse
import os
import sys


def get_frequency(text: str) -> dict:
    frequency = {}
    for i in text :
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return dict(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True))

def text_process(text: str, key : dict) ->str:
    result = ""
    for i in text:
        if (i in key) and (len(key[i])):
            result += key[i]
        else:
            result += i
    return result

def txt_write (file_path: str, data:str) -> None:
    try:
        with open(file_path, 'w', encoding="UTF-8") as file:
            file.write(data)
    except Exception :
        print(Exception)
        
def txt_read (file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            return file.read().replace("\n", " \n")
    except Exception as e:
        print("Произошла ошибка:", e)

def json_read(file_path: str) -> dict[str:str]:
    try:
        with open(file_path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except Exception as e:
        print("Произошла ошибка:", e)


def json_write(file_path: str, key: dict) -> None:
    try:
        with open(file_path, 'w', encoding="UTF-8") as file:
            json.dump(key, file)
    except Exception as e:
        print("Произошла ошибка:", e)
        
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str)
    parser.add_argument('key', type=str)
    parser.add_argument('original_file', type=str)
    parser.add_argument('result_file', type=str)
    args = parser.parse_args()
    type_key = text_process(
        txt_read(os.path.join(args.dir, args.original_file)), json_read(os.path.join(args.dir, args.key)))
    txt_write(os.path.join(args.dir, args.result_file), type_key)
    

if __name__ == '__main__':
    main()
    