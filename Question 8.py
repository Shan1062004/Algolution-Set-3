def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


text1_1 = "abcde"
text2_1 = "ace"
text1_2 = "abc"
text2_2 = "abc"
text1_3 = "abc"
text2_3 = "def"

print("Length of LCS for text1_1 and text2_1:", longest_common_subsequence(text1_1, text2_1)) 
print("Length of LCS for text1_2 and text2_2:", longest_common_subsequence(text1_2, text2_2))  
print("Length of LCS for text1_3 and text2_3:", longest_common_subsequence(text1_3, text2_3)) 
