import nist

from constants import PATH


def main() -> None:
    sequences = nist.read_data(PATH)
    for key in sequences.keys():
        print(f"{key} results:")
        print(f"frequency_bit test --> {nist.frequency_test(sequences[key])}")
        print(
            f"identical_consecutive_bits test --> {nist.identical_consecutive_test(sequences[key])}"
        )
        print(
            f"longest_sequence_of_ones_in_block test --> {nist.longest_sequence_test(sequences[key])}"
        )


if __name__ == "__main__":
    main()
