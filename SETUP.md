# Setup Guide

## Initial Setup

### 1. Clone or Create Repository

```bash
# If creating new repository on GitHub
git init
git add .
git commit -m "Initial commit: LeetCode progress tracker"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/leetcode-progress.git
git push -u origin main
```

### 2. Make Scripts Executable

```bash
chmod +x scripts/create_problem.py
chmod +x scripts/update_progress.py
```

### 3. Create Directory Structure

The scripts will automatically create directories as needed, but you can create them manually:

```bash
mkdir -p problems/{easy,medium,hard}
mkdir -p stats
```

## Daily Workflow

### Starting a New Problem

1. **Create problem structure:**
   ```bash
   python scripts/create_problem.py \
     --number 1 \
     --name "Two Sum" \
     --difficulty easy \
     --topics "arrays,hash-table"
   ```

2. **Navigate to the problem directory:**
   ```bash
   cd problems/easy/0001-two-sum/
   ```

3. **Work on your solution:**
   - Edit `solution.py` to write your code
   - Update `README.md` with problem details and your approach
   - Use `notes.md` for personal insights

### After Solving a Problem

1. **Update progress:**
   ```bash
   python scripts/update_progress.py
   ```

2. **Commit your work:**
   ```bash
   git add .
   git commit -m "Solved: #1 Two Sum (Easy)"
   git push
   ```

## Tips for Success

### 1. Consistent Naming
Always use the format: `{number}-{problem-name-slug}`
The script handles this automatically.

### 2. Detailed Documentation
Fill in all sections of the README:
- Problem description
- Your approach and intuition
- Complexity analysis
- Alternative solutions
- Key learnings

### 3. Connect to CV Engineering
For each problem, think about:
- How it relates to computer vision algorithms
- Where you might use this in real projects
- Similar patterns in image processing

### 4. Test Your Solutions
Always include test cases in `solution.py`:
```python
if __name__ == "__main__":
    solution = Solution()
    # Add multiple test cases
    assert solution.method(input1) == expected1
    assert solution.method(input2) == expected2
```

### 5. Track Patterns
Keep notes on recurring patterns:
- Sliding window
- Two pointers
- Dynamic programming states
- Graph traversal techniques

## GitHub Integration

### Enable GitHub Actions (Optional)

Create `.github/workflows/update-stats.yml` for automatic updates:

```yaml
name: Update Stats
on:
  push:
    branches: [ main ]
    paths:
      - 'problems/**'

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Update progress
      run: python scripts/update_progress.py
    - name: Commit changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add README.md stats/progress.json
        git diff --quiet && git diff --staged --quiet || git commit -m "Auto-update progress"
        git push
```

### Protect Your Main Branch
1. Go to repository Settings → Branches
2. Add branch protection rule for `main`
3. Require pull request reviews (optional)

### Use GitHub Projects
Create a project board with columns:
- To Solve
- In Progress
- Solved
- Review Later

## Customization

### Add More Topics
Edit `stats/progress.json` to add new topic categories.

### Modify Template
Edit `PROBLEM_TEMPLATE.md` to customize the problem documentation format.

### Add Visualizations
Consider adding:
- Heatmap of solving activity
- Topic distribution charts
- Difficulty progression graph

## Troubleshooting

### Scripts not executable
```bash
chmod +x scripts/*.py
```

### Progress not updating
Make sure your problem files follow the correct format in the README.

### Git push fails
```bash
git pull --rebase origin main
git push
```

## Resources

- [LeetCode](https://leetcode.com/)
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [Algorithm Visualizations](https://visualgo.net/)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

---

Happy coding! 🚀
