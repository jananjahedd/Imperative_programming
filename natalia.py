def sort_sequences():
    sequences = []

    while True:
        input_sequence = input().rstrip()
        if not input_sequence:
            break
        else:
            sequence = list(map(int, input_sequence.split()))
            sequences.extend(sequence)

    sorted_sequences = sorted(sequences)
    sorted_sequence_str = map(str, sorted_sequences)
    return sorted_sequence_str

result = sort_sequences()
result_str = ' '.join(result)
print(result_str)

