# LeetCode Progress Tracker - Complete Overview

## 🎯 What Is This?

A **complete automation system** for tracking your LeetCode problem-solving journey, with special focus on **Computer Vision engineering applications**.

### Key Features

✅ **Automatic Progress Tracking** - Counts by difficulty, topic, and date  
✅ **Visual Dashboard** - Beautiful README with badges and stats  
✅ **Streak Tracking** - Daily solving consistency  
✅ **Achievement System** - Unlock milestones  
✅ **GitHub Integration** - Auto-updates via Actions  
✅ **CV Engineering Focus** - Links problems to CV concepts  
✅ **Structured Templates** - Consistent documentation  
✅ **Zero Manual Work** - Scripts handle everything  

## 📦 What's Included

### Core Files
- `README.md` - Main dashboard (auto-updated)
- `PROBLEM_TEMPLATE.md` - Template for problem docs
- `.gitignore` - Git ignore rules
- `LICENSE` - MIT License
- `config.sh` - Configuration options

### Scripts (`scripts/`)
- `create_problem.py` - Generates problem structure
- `update_progress.py` - Updates all statistics

### Documentation
- `GETTING_STARTED.md` - Quick setup guide (START HERE!)
- `QUICK_REFERENCE.md` - Command cheat sheet
- `SETUP.md` - Detailed installation
- `CONTRIBUTING.md` - Workflow best practices
- `CV_ENGINEERING_GUIDE.md` - CV-specific mapping
- `PROJECT_OVERVIEW.md` - This file

### Automation
- `.github/workflows/update-stats.yml` - Auto-update on push
- `quickstart.sh` - Demo script

### Data
- `stats/progress.json` - All statistics in JSON
- `problems/` - Your solved problems (empty initially)

## 🚀 Quick Start

```bash
# 1. Initialize
git init
git add .
git commit -m "Initial commit"

# 2. Create first problem
python scripts/create_problem.py -n 1 -N "Two Sum" -d easy -t "arrays,hash-table"

# 3. Update progress
python scripts/update_progress.py

# 4. Push to GitHub
git remote add origin https://github.com/YOU/leetcode-progress.git
git push -u origin main
```

## 📊 How It Works

### 1. Create Problem
```bash
python scripts/create_problem.py [options]
```
Creates directory with README.md, solution.py, notes.md

### 2. Solve & Document
Edit the generated files with your solution

### 3. Update Statistics
```bash
python scripts/update_progress.py
```
Scans all problems and updates README.md + stats/progress.json

### 4. GitHub Auto-Updates
Push to GitHub → Actions run → Progress auto-updates

## 🎓 For Computer Vision Engineers

### Why This Matters

LeetCode problems teach patterns used in CV:
- **Arrays** → Image operations
- **Dynamic Programming** → Video analysis
- **Graphs** → Scene understanding
- **Trees** → Feature hierarchies
- **Sliding Windows** → Object detection

### Specific Connections

See `CV_ENGINEERING_GUIDE.md` for:
- 200+ problem recommendations
- CV application mappings
- Study plan for CV engineers
- Code templates with CV context

## 📁 Directory Structure

```
leetcode-progress/
├── README.md                      # Dashboard (auto-updated)
├── GETTING_STARTED.md             # Start here!
├── QUICK_REFERENCE.md             # Commands
├── SETUP.md                       # Details
├── CONTRIBUTING.md                # Workflow
├── CV_ENGINEERING_GUIDE.md        # CV focus
├── PROJECT_OVERVIEW.md            # This file
│
├── .github/workflows/
│   └── update-stats.yml          # Auto-update
│
├── scripts/
│   ├── create_problem.py         # Create structure
│   └── update_progress.py        # Update stats
│
├── stats/
│   └── progress.json             # All data
│
└── problems/
    ├── easy/
    ├── medium/
    └── hard/
```

## 🔧 Key Commands

| Command | Purpose |
|---------|---------|
| `python scripts/create_problem.py -n X -N "Name" -d DIFF -t "topics"` | Create problem |
| `python scripts/update_progress.py` | Update all stats |
| `./quickstart.sh` | Run demo |
| `git add . && git commit -m "..." && git push` | Push to GitHub |

## 📈 What Gets Tracked

### Automatically Updated
- Total problems solved
- Count by difficulty (easy/medium/hard)
- Count by topic
- Current solving streak
- Longest streak ever
- Recent 5 solutions
- Achievement badges
- Last solved date

### Manual (Optional)
- Problem notes
- Solution explanations
- Complexity analysis
- Alternative approaches
- CV connections

## 🏆 Achievements

| Achievement | Requirement |
|-------------|-------------|
| First Problem | 1 solved |
| Ten Problems | 10 solved |
| Fifty Problems | 50 solved |
| Hundred Problems | 100 solved |
| First Hard | 1 hard solved |
| Week Streak | 7 days consecutive |
| Month Streak | 30 days consecutive |

## 🎨 Customization

### Easy Changes
- Badge styles (edit README.md URLs)
- Progress goals (edit README.md table)
- Problem template (edit PROBLEM_TEMPLATE.md)
- Topics (edit stats/progress.json)

### Advanced Changes
- Script logic (edit Python scripts)
- Auto-update behavior (edit workflow YAML)
- Achievement thresholds (edit update_progress.py)

## 📚 Documentation Guide

| Document | When to Read |
|----------|--------------|
| `GETTING_STARTED.md` | First time setup |
| `QUICK_REFERENCE.md` | Need commands fast |
| `SETUP.md` | Detailed installation |
| `CONTRIBUTING.md` | Learning workflow |
| `CV_ENGINEERING_GUIDE.md` | CV applications |
| `PROJECT_OVERVIEW.md` | Understanding system |

## 💡 Best Practices

1. **Consistency** - Solve problems daily
2. **Documentation** - Fill all template sections
3. **CV Connection** - Link to real applications
4. **Testing** - Verify solutions work
5. **Review** - Revisit old problems

## 🔄 Typical Workflow

```
Morning:  Create problem structure
↓
Day:      Solve problem
↓
Evening:  Document solution
↓
Update:   Run update_progress.py
↓
Commit:   Push to GitHub
↓
Auto:     GitHub Actions update
```

## 🐛 Common Issues

### Scripts don't run
```bash
chmod +x scripts/*.py quickstart.sh
```

### Progress doesn't update
```bash
python -u scripts/update_progress.py
```

### Git push fails
```bash
git pull --rebase origin main
```

## 🌟 Features in Detail

### Smart Problem Creation
- Auto-generates directory structure
- Creates README from template
- Includes solution file with tests
- Adds notes file for insights

### Intelligent Progress Tracking
- Parses all problem READMEs
- Counts by multiple dimensions
- Calculates streaks automatically
- Detects achievements
- Updates JSON database

### Beautiful Dashboard
- Live badge counts
- Progress percentages
- Recent solutions list
- Topic distribution
- Streak display
- Clean formatting

### GitHub Integration
- Auto-updates on push
- No manual work needed
- Keeps history clean
- Professional appearance

## 📊 Stats Format

### README.md (Visual)
- Badges for quick view
- Tables for detailed breakdown
- Lists for recent activity
- Summaries for topics

### progress.json (Data)
```json
{
  "total_solved": 0,
  "easy_solved": 0,
  "medium_solved": 0,
  "hard_solved": 0,
  "current_streak": 0,
  "longest_streak": 0,
  "topics": {},
  "problems": [],
  "achievements": {}
}
```

## 🎯 Goals & Motivation

### Why Track Progress?
- See growth over time
- Maintain consistency
- Identify weak topics
- Build portfolio
- Interview preparation
- Professional development

### Public Benefits
- Shows dedication
- Demonstrates skills
- GitHub activity
- Portfolio piece
- Networking tool

## 🚀 Next Steps

1. Read `GETTING_STARTED.md`
2. Run `./quickstart.sh`
3. Solve your first problem
4. Push to GitHub
5. Share your progress!

## 📞 Support

- Check documentation files
- Review example structure
- Test with quickstart.sh
- Verify permissions
- Check Python version

## 🎓 Learning Resources

- [LeetCode](https://leetcode.com/)
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Visualgo](https://visualgo.net/)

---

**Ready to start tracking your progress?**

Read `GETTING_STARTED.md` and run `./quickstart.sh`!

Happy coding! 🚀
