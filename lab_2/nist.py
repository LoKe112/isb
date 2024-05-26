import json
import math
import mpmath

from constants import PI


def frequency_test(sequence: str) -> float:
    """
    Function that perform frequency bit test

    Args:
        sequence (str): The binary sequence to test.

    Returns:
        float: p-value resulting from the test.
    """
    try:
        ones_count = sequence.count("1")
        zeros_count = sequence.count("0")
        S = math.fabs((ones_count - zeros_count) / math.sqrt(len(sequence)))
        p_value = math.erfc(S / math.sqrt(2))
        return p_value
    except Exception as e:
        print("Error:", e)


def identical_consecutive_test(sequence: str) -> float:
    """
    Function that perform identical consecutive bits test

    Args:
        sequence (str): The binary sequence to test.

    Returns:
        float: The p-value resulting from the test.
    """
    try:
        one_proportion = sequence.count("1") / len(sequence)
        if math.fabs(one_proportion - 0.5) < (2 / math.sqrt(len(sequence))):            
            v_n = 0
            for i in range(0, len(sequence) - 1):
                if sequence[i] != sequence[i+1]:
                    v_n += 1                
            p_value = math.erfc(
                math.fabs(v_n - 2 * len(sequence) * one_proportion * (1 - one_proportion))
                / (2 * math.sqrt(2 * len(sequence)) * one_proportion * (1 - one_proportion)))
            return p_value       
        else:
            return 0
    except Exception as e:
        print("Error:", e)


def longest_sequence_test(sequence: str) -> float:
    """
    Function that perform longest sequence test
    
    Args:
        sequence (str): The binary sequence to test.
        
    Returns:
        float: The p-value resulting from the test.
    """
    try:
        i_seq = list(map(int, sequence))
        block_size = 8
        blocks = []
        for i in range (0, len(i_seq), block_size):
            blocks.append(i_seq[i:i + block_size])
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for block in blocks:
            max_seq = 0
            temp_max = 0
            for bit in block:
                temp_max = (temp_max + 1) if bit == 1 else 0
                max_seq = max(max_seq, temp_max)
            match max_seq:
                case 0 | 1:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case 4 | 5 | 6 | 7 | 8:
                    v[4] += 1
                case _:
                    pass

        x_square = 0
        for i in range(4):
            x_square += math.pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i])
        p_value = mpmath.gammainc(3/2, x_square/2)
        
        return p_value
    except Exception as e:
        print("Error:", e)


def read_data(file_path: str) -> dict[str, str]:
    """Function that read data from json

    Args:
        file_path (str): path to .json file

    Returns:
        dict[str, str]: data from file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print("Error:", e)
