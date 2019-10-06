def twoSum(nums,target):
    complement = {}
    pairs = set()
    for num in nums:
        if num in complement:
            pair = (complement[num], num) if num>complement[num] else (num,complement[num])
            if pair not in pairs:
                pairs.add(pair)
        else:
            complement[target - num] = target - num
    return len(pairs)

print(twoSum([1, 1, 2, 45, 46, 46],47))

                    