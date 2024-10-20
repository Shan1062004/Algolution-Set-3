def is_palindrome(s):
    return s == s[::-1]

def min_shifts_to_palindrome(s):
    n = len(s)
    for i in range(n):
        if is_palindrome(s):
            return i
        s = s[1:] + s[0]  
    return -1

def process_test_cases(test_cases):
    results = []
    for s in test_cases:
        results.append(min_shifts_to_palindrome(s))
    return results


T = 4
test_cases = ["abb", "aaabb", "aabb", "abc"]
results = process_test_cases(test_cases)
for result in results:
    print(result)
