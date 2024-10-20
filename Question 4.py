def check_valid_string(s):
    low = 0  
    high = 0  

    for char in s:
        if char == '(':
            low += 1
            high += 1
        elif char == ')':
            low -= 1
            high -= 1
        else:  
            low -= 1
            high += 1

        
        if high < 0:
            return False

        
        low = max(low, 0)
    
    return low == 0

print(check_valid_string("()"))  
print(check_valid_string("(())"))  
print(check_valid_string(")("))   
print(check_valid_string("()("))   
