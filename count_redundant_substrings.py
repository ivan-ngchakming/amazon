def count_redundant_substrings__brute_force(word, a, b):
    """
    O(n^3) time complexity
    """
    vowels = set("aeiou")
    redundant_count = 0

    # Generate all substrings
    for i in range(len(word)):
        for j in range(i, len(word)):
            substring = word[i : j + 1]
            V = sum(1 for char in substring if char in vowels)
            C = len(substring) - V
            if len(substring) == a * V + b * C:
                print(substring)
                redundant_count += 1

    return redundant_count

def count_redundant_substrings(word, a, b):
    vowels = set("aeiou")
    
    # Convert the word into a list of values based on vowels and consonants
    values = [(1 - a) if char in vowels else (1 - b) for char in word]
    
    # Use a dictionary to store prefix sums and their counts
    prefix_sum_counts = {0: 1}  # Start with 0 sum having one count
    prefix_sum = 0
    redundant_count = 0
    
    for value in values:
        prefix_sum += value
        if prefix_sum in prefix_sum_counts:
            redundant_count += prefix_sum_counts[prefix_sum]
            prefix_sum_counts[prefix_sum] += 1
        else:
            prefix_sum_counts[prefix_sum] = 1
    
    return redundant_count


word = "abbaccabb"
a = -1
b = 2

print(count_redundant_substrings__brute_force(word, a, b))
print(count_redundant_substrings(word, a, b))
