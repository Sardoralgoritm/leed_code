class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        if len(nums1) % 2:
            return float(nums1[len(nums1)//2])
        else:
            ind1 = nums1[len(nums1)//2]
            ind2 = nums1[len(nums1)//2-1]
            return (ind1 + ind2) / 2
