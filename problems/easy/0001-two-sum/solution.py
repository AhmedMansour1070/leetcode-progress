"""
LeetCode 1: Two Sum
Difficulty: Easy
Topics: arrays,hash-table
Date: 2025-11-20
"""

class Solution:
    def twoSum(self, nums, target: int):    
        num_map = {}  # Dictionary to store numbers and their indices
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], i]  # Found the pair
            
            num_map[num] = i  # Store index of the current number
        
        return []  # Return empty list if no pair is found



# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test_input = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    result = solution.twoSum(test_input, target)  # ← Changed this line
    print(f"Test 1: {result} - Expected: {expected} - {'✅ PASSED' if result == expected else '❌ FAILED'}")
    
    # Test case 2
    test_input = [3, 2, 4]
    target = 6
    expected = [1, 2]
    result = solution.twoSum(test_input, target)
    print(f"Test 2: {result} - Expected: {expected} - {'✅ PASSED' if result == expected else '❌ FAILED'}")
    
    # Test case 3
    test_input = [3, 3]
    target = 6
    expected = [0, 1]
    result = solution.twoSum(test_input, target)
    print(f"Test 3: {result} - Expected: {expected} - {'✅ PASSED' if result == expected else '❌ FAILED'}")
    
    print("\n✅ All tests completed!")