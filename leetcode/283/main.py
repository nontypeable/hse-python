class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        next_nonzero = 0

        for current in range(len(nums)):
            if nums[current] != 0:
                if current != next_nonzero:
                    nums[next_nonzero], nums[current] = (
                        nums[current],
                        nums[next_nonzero],
                    )
                next_nonzero += 1
