def twoSum(self, nums: List[int], target: int) -> List[int]:
    indexes=[]
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in nums:
            indexes.append(i)
    return indexes
