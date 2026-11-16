class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)


            if target == nums[mid]:
                return mid

            if target < nums[mid] and target <= nums[right] and nums[right] < nums[mid]:
                left = mid + 1
            elif target > nums[mid] and target > nums[right] and nums[mid] < nums[left]:
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1            

        return -1