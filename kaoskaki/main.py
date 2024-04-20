def count_pairs_of_socks(socks_list):
    sock_counter = {}
    pairs_count = 0
    
    # Count how many times each number appears in the list
    for sock in socks_list:
        if sock in sock_counter:
            sock_counter[sock] += 1
        else:
            sock_counter[sock] = 1
    
    # Check how many pairs of socks appear more than once
    for count in sock_counter.values():
        pairs_count += count // 2
    
    return pairs_count

# Take input from the user
input_user = input()

# Convert the input string into a list of integers
socks_list = list(map(int, input_user.split()))

# Call the count_pairs_of_socks function with user input
result = count_pairs_of_socks(socks_list)
print(result)
