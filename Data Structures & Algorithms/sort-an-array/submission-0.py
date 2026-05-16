class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):

            n = len(nums)
            if n <= 1:
                return nums
            mid = n//2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left,right)



        def merge(left,right):

            l = len(left)
            r = len(right)
            result = []
            i,j = 0,0

            while i < l and j < r:
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < l:
                result.append(left[i])
                i += 1

            while j < r:
                result.append(right[j])
                j +=1

            return result

        return merge_sort(nums)
                
        