def is_square_free(n):
    if n % 2 == 0:
        n = n // 2
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            n = n // i
        if n % i == 0:
            return False
            
    return True

def count_square_free_divisors(N):
    count = 0
    
    for i in range(2, N + 1):
        if N % i == 0 and is_square_free(i):
            count += 1
    
    return count

# Example usage
N1 = 20
N2 = 72
print("Square free divisors count for", N1, "is:", count_square_free_divisors(N1))  
print("Square free divisors count for", N2, "is:", count_square_free_divisors(N2)) 