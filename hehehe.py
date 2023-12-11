
def get_longest_increasing_subsequence(seq: list[int]) -> int:
    """
    Finds the length of the longest strictly increasing subsequence in the input
    :param seq: A list of integers
    :return: the length of the longest strictly increasing subsequence in the input
    """
    max_length = 0
    cur_length = 1
    previous_value = seq[0]
    for i in range(len(seq)):
        value = seq[i]
        if value > previous_value:
            # This number is part of a strictly increasing subsequence
            cur_length += 1
        else:
            # We start a new subsequence, but also register
            # the length of the current sequence
            if cur_length > max_length:
                max_length = cur_length
            cur_length = 1
        previous_value = value
    # Don't forget that the sequence may end at the list's end
    if cur_length > max_length:
        max_length = cur_length
    return max_length


sequence: list[int] = [int(i) for i in input().split(" ")]
max_length = get_longest_increasing_subsequence(sequence)
if len(sequence) > 1:
    for i in range(len(sequence)):
        cur_length = get_longest_increasing_subsequence(sequence[:i] + sequence[i+1:])
        if cur_length > max_length:
            max_length = cur_length
print(max_length)


