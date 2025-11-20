# Contributing to Your LeetCode Progress

This repository is primarily for personal use, but here are guidelines to maintain consistency.

## Workflow

### 1. Starting a New Problem

```bash
# Create problem structure
python scripts/create_problem.py \
    -n <problem_number> \
    -N "<Problem Name>" \
    -d <easy|medium|hard> \
    -t "<topic1,topic2,...>"

# Example
python scripts/create_problem.py \
    -n 42 \
    -N "Trapping Rain Water" \
    -d hard \
    -t "arrays,two-pointers,dynamic-programming"
```

### 2. Working on the Solution

Navigate to the created directory:
```bash
cd problems/<difficulty>/<problem-folder>/
```

Files to edit:
- **README.md**: Document problem description, approach, complexity
- **solution.py**: Write your solution code
- **notes.md**: Personal insights and learnings

### 3. Solution Template

```python
"""
LeetCode {number}: {name}
Difficulty: {difficulty}
Topics: {topics}
Date: {date}

Problem Link: https://leetcode.com/problems/{slug}/
"""

class Solution:
    def solutionMethod(self, param):
        """
        Approach: [Brief description]
        
        Time: O(?)
        Space: O(?)
        """
        # Your solution here
        pass


def test_solution():
    """Test cases for verification"""
    solution = Solution()
    
    # Test case 1
    assert solution.solutionMethod(input1) == expected1
    
    # Test case 2
    assert solution.solutionMethod(input2) == expected2
    
    print("All tests passed! ✅")


if __name__ == "__main__":
    test_solution()
```

### 4. Documentation Guidelines

#### Problem Description
- Copy the exact problem statement
- Include constraints
- Add examples with explanations

#### Approach Section
- Start with intuition
- Explain the algorithm step-by-step
- Include visualizations or diagrams (ASCII art is fine)
- Discuss edge cases

#### Complexity Analysis
- Always include both time and space complexity
- Explain the reasoning
- Compare with alternative approaches if applicable

#### Key Learnings
- What pattern did you recognize?
- How does it relate to CV engineering?
- What similar problems use this approach?

### 5. Updating Progress

```bash
# Run the update script
python scripts/update_progress.py

# Review changes
git diff README.md stats/progress.json

# Commit your work
git add .
git commit -m "Solved: #42 Trapping Rain Water (Hard)"
git push origin main
```

## Commit Message Format

Use semantic commit messages:

```
Solved: #<number> <Problem Name> (<Difficulty>)

- Key insight: [brief description]
- Time: O(?)
- Space: O(?)
- Topics: [tags]
```

Examples:
```
Solved: #1 Two Sum (Easy)

- Key insight: Hash table for O(1) lookup
- Time: O(n)
- Space: O(n)
- Topics: arrays, hash-table

---

Solved: #42 Trapping Rain Water (Hard)

- Key insight: Two-pointer technique with max heights
- Time: O(n)
- Space: O(1)
- Topics: arrays, two-pointers, dynamic-programming
```

## File Organization

### Directory Structure
```
problems/
├── easy/
│   ├── 0001-two-sum/
│   │   ├── README.md
│   │   ├── solution.py
│   │   └── notes.md
│   └── 0020-valid-parentheses/
│       ├── README.md
│       ├── solution.py
│       └── notes.md
├── medium/
│   └── 0042-trapping-rain-water/
│       ├── README.md
│       ├── solution.py
│       └── notes.md
└── hard/
    └── 0123-best-time-to-buy-sell-stock-iii/
        ├── README.md
        ├── solution.py
        └── notes.md
```

### Naming Conventions
- Folders: `{4-digit-number}-{kebab-case-name}`
- Example: `0001-two-sum`, `0042-trapping-rain-water`
- Always use 4 digits for problem numbers (pad with zeros)

## Code Quality

### Python Style
- Follow PEP 8
- Use type hints when helpful
- Include docstrings for complex functions
- Add comments for tricky logic

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            Indices of the two numbers
        """
        seen = {}  # value -> index mapping
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        return []  # No solution found
```

### Testing
- Include at least 3 test cases
- Cover edge cases
- Test with LeetCode examples
- Add your own challenging cases

## Tags and Topics

### Standard Topics
- arrays
- strings
- hash-tables
- linked-list
- trees
- graphs
- sorting
- searching
- dynamic-programming
- greedy
- backtracking
- bit-manipulation
- math
- two-pointers
- sliding-window
- stack
- queue
- heap
- trie
- union-find

### CV-Specific Tags (add in notes.md)
- `#image-processing`
- `#object-detection`
- `#segmentation`
- `#tracking`
- `#optimization`
- `#real-time`
- `#3d-vision`
- `#feature-extraction`

## Best Practices

1. **Solve First, Optimize Later**
   - Get a working solution first
   - Then optimize for time/space
   - Document both approaches

2. **Learn from Solutions**
   - After solving, review top solutions
   - Understand different approaches
   - Note trade-offs

3. **Connect to Real Work**
   - Always note CV applications
   - Link to relevant papers/libraries
   - Consider real-world constraints

4. **Maintain Consistency**
   - Solve regularly (daily is ideal)
   - Update progress after each solution
   - Review old solutions periodically

5. **Review and Refactor**
   - Revisit hard problems after a week
   - Improve documentation
   - Add alternative solutions

## Troubleshooting

### Script Issues
```bash
# Make scripts executable
chmod +x scripts/*.py

# Test script
python scripts/create_problem.py --help
```

### Progress Not Updating
```bash
# Manually run update
python scripts/update_progress.py

# Check for errors
python -m py_compile scripts/update_progress.py
```

### Git Issues
```bash
# Reset local changes
git checkout -- README.md stats/progress.json

# Re-run update
python scripts/update_progress.py
```

## Questions?

If you're sharing this template with others or using it publicly:
- Open an issue for bugs
- Submit PRs for improvements
- Share your progress tracking strategies

Happy solving! 🚀
