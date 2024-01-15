class Solution():
    def twoSum(self, nums, target):
        storage= {}
        for index, value in enumerate(nums):
            looking_for = target - value
            if looking_for in storage:
                
                first_index = storage[looking_for]
                second_index = index
                return [first_index, second_index]
            else:
                storage[value] = index

        return []
