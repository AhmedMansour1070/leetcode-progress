# 🚀 Getting Started with LeetCode Progress Tracker

Welcome! This repository will help you track your LeetCode progress with automatic statistics and GitHub integration.

## ⚡ Quick Setup (3 minutes)

### Step 1: Initialize Git Repository

```bash
cd leetcode-progress
git init
git add .
git commit -m "Initial commit: LeetCode progress tracker"
```

### Step 2: Connect to GitHub

1. Create a new repository on GitHub (call it `leetcode-progress`)
2. Connect and push:

```bash
git remote add origin https://github.com/YOUR_USERNAME/leetcode-progress.git
git branch -M main
git push -u origin main
```

### Step 3: Test It Out

```bash
# Make scripts executable
chmod +x scripts/*.py quickstart.sh

# Run demo
./quickstart.sh
```

Done! Your progress tracker is ready. 🎉

## 📝 How to Use Daily

### 1. Create Problem Structure

```bash
python scripts/create_problem.py \
    --number 1 \
    --name "Two Sum" \
    --difficulty easy \
    --topics "arrays,hash-table"
```

This creates:
- `problems/easy/0001-two-sum/README.md` - Problem documentation
- `problems/easy/0001-two-sum/solution.py` - Your code
- `problems/easy/0001-two-sum/notes.md` - Personal notes

### 2. Solve the Problem

1. Write your solution in `solution.py`
2. Document your approach in `README.md`
3. Add insights to `notes.md`

### 3. Update Progress

```bash
python scripts/update_progress.py
```

This automatically updates:
- README badges and stats
- Progress percentages
- Topic distribution
- Streak tracking
- Achievement flags

### 4. Commit Your Work

```bash
git add .
git commit -m "Solved: #1 Two Sum (Easy)"
git push
```

## 🎯 For Computer Vision Engineers

This tracker is designed with CV engineers in mind!

### Why LeetCode for CV?
- **Arrays** → Image processing
- **Dynamic Programming** → Video analysis, tracking
- **Graphs** → Scene understanding
- **Trees** → Hierarchical features
- **Sliding Windows** → Object detection

### CV Engineering Guide
Check `CV_ENGINEERING_GUIDE.md` for:
- Problem-to-CV mapping
- Study plan for CV engineers
- Real-world applications
- Code templates with CV context

## 📚 Documentation

| File | Purpose |
|------|---------|
| `GETTING_STARTED.md` | You are here! |
| `QUICK_REFERENCE.md` | Command cheat sheet |
| `SETUP.md` | Detailed setup guide |
| `CONTRIBUTING.md` | Best practices & workflow |
| `CV_ENGINEERING_GUIDE.md` | CV-specific guidance |
| `ARCHITECTURE.md` | System design & data flow |

## 🤖 GitHub Actions (Optional)

The repository includes automatic progress updates via GitHub Actions.

Already configured! Just ensure:
1. `.github/workflows/update-stats.yml` exists
2. Actions enabled in repo settings

Every time you push, your progress auto-updates!

## 💡 Pro Tips

1. **Solve daily** - Consistency beats intensity
2. **Document well** - Future you will thank you
3. **Connect to CV** - Think about real applications
4. **Review regularly** - Revisit hard problems

## 🎨 Customization

### Change Goals
Edit progress table in `README.md`

### Add Topics
Edit `stats/progress.json`

### Modify Template
Edit `PROBLEM_TEMPLATE.md`

### Badge Style
Change badge URLs in `README.md`

## 🆘 Need Help?

### Scripts won't run
```bash
chmod +x scripts/*.py
```

### Progress not updating
```bash
python -u scripts/update_progress.py
```

### Git push fails
```bash
git pull --rebase origin main
git push
```

## ✅ Next Steps

1. ✅ Setup complete
2. 📝 Create first problem: `./quickstart.sh`
3. 🎯 Set your goals in README.md
4. 🔥 Start solving!

---

**Ready to go?** Run `./quickstart.sh` to create your first problem!

Happy coding! 🚀
