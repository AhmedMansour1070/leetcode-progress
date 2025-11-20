#!/bin/bash

# Quick Start Demo Script
# This script demonstrates how to use the LeetCode progress tracker

echo "🚀 LeetCode Progress Tracker - Quick Start Demo"
echo "================================================"
echo ""

# Check if we're in the right directory
if [ ! -f "scripts/create_problem.py" ]; then
    echo "❌ Error: Please run this script from the repository root"
    exit 1
fi

echo "📁 Current directory structure:"
tree -L 2 -I '__pycache__|*.pyc' . 2>/dev/null || find . -maxdepth 2 -type d | grep -v ".git"
echo ""

echo "📝 Creating an example problem..."
python scripts/create_problem.py \
    --number 1 \
    --name "Two Sum" \
    --difficulty easy \
    --topics "arrays,hash-table"

echo ""
echo "📊 Updating progress..."
python scripts/update_progress.py

echo ""
echo "✅ Demo complete!"
echo ""
echo "📖 Next steps:"
echo "   1. Check 'problems/easy/0001-two-sum/' to see the generated files"
echo "   2. Edit solution.py to add your solution"
echo "   3. Run 'python scripts/update_progress.py' after solving"
echo "   4. Check README.md to see updated stats"
echo ""
echo "💡 To create your own problem:"
echo "   python scripts/create_problem.py -n <number> -N \"<name>\" -d <difficulty> -t \"<topics>\""
echo ""
echo "🌟 Happy coding!"
