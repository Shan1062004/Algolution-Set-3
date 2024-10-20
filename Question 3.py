from collections import deque

def max_of_subarrays(arr, n, k):
    dq = deque()
    result = []

    for i in range(k):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)

    for i in range(k, n):
        result.append(arr[dq[0]])

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        dq.append(i)

    result.append(arr[dq[0]])

    return result

# Example usage
arr1 = [1, 2, 3, 1, 4, 5]
k1 = 3
arr2 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k2 = 4
arr3 = [20, 10, 30]
k3 = 1

print("Output for arr1:", max_of_subarrays(arr1, len(arr1), k1))  
print("Output for arr2:", max_of_subarrays(arr2, len(arr2), k2))  
print("Output for arr3:", max_of_subarrays(arr3, len(arr3), k3))  
