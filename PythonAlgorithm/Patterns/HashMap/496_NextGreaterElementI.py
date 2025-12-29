class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        stack = []
        for n2 in range(len(nums2)-1, -1, -1):
            ng = -1
            for i in range(0, len(stack)):
                if stack[i] > nums2[n2]:
                    ng = stack[i]
                    break
            stack.insert(0, nums2[n2])
            dict[nums2[n2]] = ng
        #
        r = [0] * len(nums1)
        for i in range(len(nums1)):
            r[i] = dict[nums1[i]]
        return r
        