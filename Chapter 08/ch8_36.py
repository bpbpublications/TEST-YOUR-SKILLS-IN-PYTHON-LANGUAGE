nums1 = [1, 2, 3]
nums2 = [4, 5]
nums=[(x,y) for x in nums1 for y in nums2]
print(nums)

#[(1,4), (1,5), (2,4), (2,5), (3,4), (3,5)]