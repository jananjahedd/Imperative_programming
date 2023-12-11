def get_longest_increasing_subsequence(seq: list[int]) -> int:
    max_length = 1
    cur_length = 1
    previous_value = seq[0]

    for i in range(1, len(seq)):
        value = seq[i]
        if value > previous_value:
            cur_length += 1
            if cur_length > max_length:
                max_length = cur_length
        else:
            cur_length = 1
        previous_value = value

    return max_length

def longest_sequence_with_k(user_input, k):
    length = len(user_input)

    # Create a list to store the length of the longest increasing subsequence ending at each index
    dp = [1] * length

    for i in range(1, length):
        for j in range(i):
            if user_input[i] > user_input[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)

    # Create a dictionary to count the frequency of each value in the sequence
    value_count = {}
    for value in user_input:
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    # Calculate the minimum number of elements to remove to maximize the length of the increasing subsequence
    min_removals = length - max_length

    # Adjust min_removals to account for duplicate values
    for value, count in value_count.items():
        if count > 1:
            min_removals -= count - 1

    # Adjust for k removals
    min_removals = max(0, min_removals - k)

    return max_length - min_removals

# Additional code
user_input = list(map(int, input().split()))
k = int(input())
result = longest_sequence_with_k(user_input, k)
print(result)

