a = [1,4,3,2,5]
k=4

def find_largest(a,k):
    first_idx = 0
    print(a[first_idx:len(a) - k + 1])
    for x in range(1, len(a) - k + 1):
        # compare values at each index for the would be sub arrays
        print(a[first_idx:first_idx+k])

        for i in range(k):
            # replace the largest index and break out of the inner loop is larger value is found
            if a[first_idx + i] < a[x + i]:
                print("idx : ",a[first_idx])
                print("x : ",a[x])
                first_idx = x
                print("Then idx : ",a[first_idx])
                break
            # if the current stored largest subarray is larger than the current subarray, move on
            else:
                break

    return a[first_idx:first_idx+k]
print(find_largest([5,3,2,76,75,73,23,77,79,74,86],3))
print(find_largest(a,k))
print("---------------------------")
print(find_largest([1,4,4,3,2,5],3))
