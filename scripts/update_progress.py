#!/usr/bin/env python3
"""
LeetCode Progress Updater
Scans the problems directory and updates README.md and progress.json
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict


def scan_problems(repo_root):
    """Scan the problems directory and collect all solved problems."""
    problems = []
    problems_dir = repo_root / "problems"
    
    for difficulty in ['easy', 'medium', 'hard']:
        diff_dir = problems_dir / difficulty
        if not diff_dir.exists():
            continue
        
        for problem_dir in sorted(diff_dir.iterdir()):
            if not problem_dir.is_dir():
                continue
            
            readme_path = problem_dir / "README.md"
            if not readme_path.exists():
                continue
            
            # Parse README to extract problem info
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract problem number and name from title
            title_match = re.search(r'^#\s*(\d+)\.\s*(.+)$', content, re.MULTILINE)
            if not title_match:
                continue
            
            number = int(title_match.group(1))
            name = title_match.group(2).strip()
            
            # Extract topics
            topics_match = re.search(r'\*\*Topics\*\*:\s*(.+?)$', content, re.MULTILINE)
            topics = topics_match.group(1).strip() if topics_match else ""
            
            # Extract date
            date_match = re.search(r'\*\*Date Solved\*\*:\s*(\d{4}-\d{2}-\d{2})', content)
            date_solved = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")
            
            problems.append({
                'number': number,
                'name': name,
                'difficulty': difficulty,
                'topics': topics,
                'date_solved': date_solved,
                'path': str(problem_dir.relative_to(repo_root)).replace('\\', '/')
            })
    
    return sorted(problems, key=lambda x: x['number'])


def calculate_streak(problems):
    """Calculate current and longest streak."""
    if not problems:
        return 0, 0
    
    # Get unique dates and sort them
    dates = sorted(set(p['date_solved'] for p in problems))
    dates = [datetime.strptime(d, "%Y-%m-%d").date() for d in dates]
    
    if not dates:
        return 0, 0
    
    # Calculate current streak
    today = datetime.now().date()
    current_streak = 0
    
    # Check if last date is today or yesterday
    if dates[-1] >= today - timedelta(days=1):
        current_streak = 1
        for i in range(len(dates) - 2, -1, -1):
            if (dates[i + 1] - dates[i]).days <= 1:
                current_streak += 1
            else:
                break
    
    # Calculate longest streak
    longest_streak = 1
    temp_streak = 1
    
    for i in range(1, len(dates)):
        if (dates[i] - dates[i-1]).days <= 1:
            temp_streak += 1
            longest_streak = max(longest_streak, temp_streak)
        else:
            temp_streak = 1
    
    return current_streak, longest_streak


def update_progress_json(repo_root, problems):
    """Update the progress.json file."""
    stats_path = repo_root / "stats" / "progress.json"
    
    # Load existing progress or create new
    if stats_path.exists():
        with open(stats_path, 'r', encoding='utf-8') as f:
            progress = json.load(f)
    else:
        progress = {
            "total_solved": 0,
            "easy_solved": 0,
            "medium_solved": 0,
            "hard_solved": 0,
            "current_streak": 0,
            "longest_streak": 0,
            "last_solved_date": None,
            "topics": {},
            "problems": [],
            "achievements": {}
        }
    
    # Count by difficulty
    easy_count = sum(1 for p in problems if p['difficulty'] == 'easy')
    medium_count = sum(1 for p in problems if p['difficulty'] == 'medium')
    hard_count = sum(1 for p in problems if p['difficulty'] == 'hard')
    
    # Count by topic
    topic_counts = defaultdict(int)
    for problem in problems:
        topics = [t.strip().lower() for t in problem['topics'].split(',')]
        for topic in topics:
            if topic:
                topic_counts[topic] += 1
    
    # Calculate streaks
    current_streak, longest_streak = calculate_streak(problems)
    
    # Update achievements
    achievements = {
        "first_problem": len(problems) >= 1,
        "ten_problems": len(problems) >= 10,
        "fifty_problems": len(problems) >= 50,
        "hundred_problems": len(problems) >= 100,
        "first_hard": hard_count >= 1,
        "week_streak": longest_streak >= 7,
        "month_streak": longest_streak >= 30
    }
    
    # Update progress
    progress['total_solved'] = len(problems)
    progress['easy_solved'] = easy_count
    progress['medium_solved'] = medium_count
    progress['hard_solved'] = hard_count
    progress['current_streak'] = current_streak
    progress['longest_streak'] = longest_streak
    progress['last_solved_date'] = problems[-1]['date_solved'] if problems else None
    progress['topics'] = dict(topic_counts)
    progress['problems'] = problems
    progress['achievements'] = achievements
    
    # Save progress
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2)
    
    return progress


def update_readme(repo_root, progress):
    """Update the README.md file with current progress."""
    readme_path = repo_root / "README.md"
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update badges
    total = progress['total_solved']
    easy = progress['easy_solved']
    medium = progress['medium_solved']
    hard = progress['hard_solved']
    
    content = re.sub(
        r'\[!\[Problems Solved\].*?\]\(problems/\)',
        f'[![Problems Solved](https://img.shields.io/badge/solved-{total}-brightgreen.svg)](problems/)',
        content
    )
    content = re.sub(
        r'\[!\[Easy\].*?\]\(problems/easy/\)',
        f'[![Easy](https://img.shields.io/badge/easy-{easy}-success.svg)](problems/easy/)',
        content
    )
    content = re.sub(
        r'\[!\[Medium\].*?\]\(problems/medium/\)',
        f'[![Medium](https://img.shields.io/badge/medium-{medium}-orange.svg)](problems/medium/)',
        content
    )
    content = re.sub(
        r'\[!\[Hard\].*?\]\(problems/hard/\)',
        f'[![Hard](https://img.shields.io/badge/hard-{hard}-red.svg)](problems/hard/)',
        content
    )
    
    # Update progress table
    easy_pct = f"{(easy/total*100):.1f}" if total > 0 else "0"
    medium_pct = f"{(medium/total*100):.1f}" if total > 0 else "0"
    hard_pct = f"{(hard/total*100):.1f}" if total > 0 else "0"
    total_pct = "100.0" if total > 0 else "0"
    
    table = f"""| Difficulty | Solved | Total | Percentage |
|------------|--------|-------|------------|
| Easy       | {easy}      | TBD   | {easy_pct}%         |
| Medium     | {medium}      | TBD   | {medium_pct}%         |
| Hard       | {hard}      | TBD   | {hard_pct}%         |
| **Total**  | **{total}**  | **TBD** | **{total_pct}%**   |"""
    
    content = re.sub(
        r'\| Difficulty \| Solved \| Total \| Percentage \|.*?\| \*\*Total\*\*.*?\|',
        table,
        content,
        flags=re.DOTALL
    )
    
    # Update recent solutions
    recent_problems = progress['problems'][-5:] if progress['problems'] else []
    recent_solutions = "\n".join([
        f"- [{p['number']}. {p['name']}]({p['path']}/README.md) - *{p['difficulty'].capitalize()}* - {p['date_solved']}"
        for p in reversed(recent_problems)
    ])
    
    if not recent_solutions:
        recent_solutions = "No solutions yet. Start solving!"
    
    content = re.sub(
        r'<!-- RECENT_SOLUTIONS_START -->.*?<!-- RECENT_SOLUTIONS_END -->',
        f'<!-- RECENT_SOLUTIONS_START -->\n{recent_solutions}\n<!-- RECENT_SOLUTIONS_END -->',
        content,
        flags=re.DOTALL
    )
    
    # Update topics
    topics_list = []
    for topic, count in sorted(progress['topics'].items(), key=lambda x: x[1], reverse=True):
        topics_list.append(f"- {topic.replace('-', ' ').title()}: {count} problems")
    
    topics_text = "\n".join(topics_list) if topics_list else "No topics yet."
    
    content = re.sub(
        r'<!-- TOPICS_START -->.*?<!-- TOPICS_END -->',
        f'<!-- TOPICS_START -->\n{topics_text}\n<!-- TOPICS_END -->',
        content,
        flags=re.DOTALL
    )
    
    # Update streak
    streak_text = f"""Current Streak: {progress['current_streak']} days
Longest Streak: {progress['longest_streak']} days"""
    
    content = re.sub(
        r'<!-- STREAK_START -->.*?<!-- STREAK_END -->',
        f'<!-- STREAK_START -->\n{streak_text}\n<!-- STREAK_END -->',
        content,
        flags=re.DOTALL
    )
    
    # Update last updated timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = re.sub(
        r'\*\*Last Updated\*\*:.*$',
        f'**Last Updated**: {timestamp}',
        content,
        flags=re.MULTILINE
    )
    
    # Save README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    # Get repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    print("🔍 Scanning problems directory...")
    problems = scan_problems(repo_root)
    print(f"   Found {len(problems)} solved problems")
    
    print("📊 Updating progress.json...")
    progress = update_progress_json(repo_root, problems)
    
    print("📝 Updating README.md...")
    update_readme(repo_root, progress)
    
    print("\n✅ Progress updated successfully!")
    print(f"\n📈 Summary:")
    print(f"   Total: {progress['total_solved']}")
    print(f"   Easy: {progress['easy_solved']}")
    print(f"   Medium: {progress['medium_solved']}")
    print(f"   Hard: {progress['hard_solved']}")
    print(f"   Current Streak: {progress['current_streak']} days")
    print(f"   Longest Streak: {progress['longest_streak']} days")
    
    # Show new achievements
    new_achievements = [k for k, v in progress['achievements'].items() if v]
    if new_achievements:
        print(f"\n🏆 Achievements:")
        for achievement in new_achievements:
            print(f"   ✓ {achievement.replace('_', ' ').title()}")


if __name__ == "__main__":
    main()