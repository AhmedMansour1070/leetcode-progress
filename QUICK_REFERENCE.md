# LeetCode Progress Tracker - Quick Reference

## 🚀 Quick Start Commands

### Create New Problem
```bash
python scripts/create_problem.py -n <NUM> -N "<NAME>" -d <DIFF> -t "<TOPICS>"

# Example:
python scripts/create_problem.py -n 1 -N "Two Sum" -d easy -t "arrays,hash-table"
```

### Update Progress
```bash
python scripts/update_progress.py
```

### Complete Workflow
```bash
# 1. Create problem
python scripts/create_problem.py -n 42 -N "Trapping Rain Water" -d hard -t "arrays,dp"

# 2. Solve it (edit files in problems/hard/0042-trapping-rain-water/)

# 3. Update and commit
python scripts/update_progress.py
git add .
git commit -m "Solved: #42 Trapping Rain Water (Hard)"
git push
```

## 📋 Script Parameters

### create_problem.py
| Flag | Parameter | Required | Description |
|------|-----------|----------|-------------|
| `-n` | `--number` | Yes | Problem number (e.g., 1, 42) |
| `-N` | `--name` | Yes | Problem name (e.g., "Two Sum") |
| `-d` | `--difficulty` | Yes | easy, medium, or hard |
| `-t` | `--topics` | Yes | Comma-separated topics |

### update_progress.py
No parameters - scans all problems automatically.

## 📁 File Structure

```
leetcode-progress/
├── README.md                     # Dashboard (auto-updated)
├── GETTING_STARTED.md           # Start here!
├── QUICK_REFERENCE.md           # This file
├── problems/
│   ├── easy/0001-two-sum/
│   │   ├── README.md
│   │   ├── solution.py
│   │   └── notes.md
│   ├── medium/
│   └── hard/
├── scripts/
│   ├── create_problem.py
│   └── update_progress.py
└── stats/
    └── progress.json
```

## 🎯 Common Topics

Arrays, Strings, Hash Tables, Dynamic Programming, Graphs, Trees, Linked Lists, Sorting, Searching, Two Pointers, Sliding Window, Backtracking, Greedy, Bit Manipulation, Math, Stack, Queue, Heap, Trie, Union Find

## 💡 Tips

1. **Make scripts executable:**
   ```bash
   chmod +x scripts/*.py quickstart.sh
   ```

2. **Create aliases:**
   ```bash
   alias lc='python ~/leetcode-progress/scripts/create_problem.py'
   alias lcu='python ~/leetcode-progress/scripts/update_progress.py'
   ```

3. **Search problems:**
   ```bash
   grep -r "dynamic-programming" problems/
   ```

## 📊 What Gets Updated

- Badge counts (total/easy/medium/hard)
- Progress percentages
- Recent 5 solutions
- Topic distribution
- Streak tracking
- Achievements

## 🏆 Achievements

- First Problem (1 solved)
- Ten Problems (10 solved)
- Fifty Problems (50 solved)  
- Hundred Problems (100 solved)
- First Hard (1 hard solved)
- Week Streak (7 days)
- Month Streak (30 days)

## 🐛 Troubleshooting

```bash
# Permission denied
chmod +x scripts/*.py

# Progress not updating
python -u scripts/update_progress.py

# Git issues
git pull --rebase origin main
```

---

**Need more help?** Check `GETTING_STARTED.md` or `SETUP.md`
