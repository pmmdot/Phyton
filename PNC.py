import itertools

def is_valid(word):
    # Check that no two U's or L's are adjacent
    for i in range(len(word) - 1):
        if word[i] == word[i+1] and word[i] in ['S', 'C']:
            return False
    return True

word = "SUCCESS"
valid_set = set()  # use a set to avoid duplicates

# Generate all permutations (accounting for repeated letters)
for perm in itertools.permutations(word):
    candidate = ''.join(perm)
    if is_valid(candidate):
        valid_set.add(candidate)

valid_list = sorted(valid_set)
print("Total valid arrangements:", len(valid_list))
for arrangement in valid_list:
    print(arrangement)
