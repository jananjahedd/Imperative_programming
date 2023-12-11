def get_longest_increasing_subsequence(seq: list[int]) -> int:
    max_length = 0
    cur_length = 1
    previous_value = seq[0]

    for i in range(len(seq)):
        value = seq[i]
        if value > previous_value:
            cur_length += 1
        else:
            if cur_length > max_length:
                max_length = cur_length
            cur_length = 1
        previous_value = value

    if cur_length > max_length:
        max_length = cur_length

    return max_length

def longest_sequence_with_k(user_input, k):
    length = len(user_input)

    if length <= 1:
        return length
    
    max_length = 0
    
    for i in range(k+1):
        cur_length = get_longest_increasing_subsequence(user_input[:i] + user_input[i+1:])
        if cur_length > max_length:
            max_length = cur_length
    
    return max_length


#additional code
user_input = list(map(int, input().split()))
#additional code for extension
k = int(input())
for i in range(k):
    max_length = 0
    for j in range(len(user_input)):
        cur_length = get_longest_increasing_subsequence(user_input[:j] + user_input[j+1:])
        if cur_length > max_length:
            max_length = cur_length
    user_input.pop(max_length)

print(max_length)