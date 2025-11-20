#!/usr/bin/env python3
"""
LeetCode Problem Creator
Creates a new problem file from template and updates the repository structure.
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
import re


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def create_problem_file(number, name, difficulty, topics, description=""):
    """Create a new problem file from template."""
    
    # Validate difficulty
    difficulty = difficulty.lower()
    if difficulty not in ['easy', 'medium', 'hard']:
        print(f"Error: Difficulty must be 'easy', 'medium', or 'hard'")
        sys.exit(1)
    
    # Get repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    # Read template
    template_path = repo_root / "PROBLEM_TEMPLATE.md"
    if not template_path.exists():
        print(f"Error: Template file not found at {template_path}")
        sys.exit(1)
    
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Generate problem slug
    problem_slug = slugify(name)
    
    # Format date
    date_solved = datetime.now().strftime("%Y-%m-%d")
    
    # Replace template variables
    content = template.replace("{problem_number}", str(number))
    content = content.replace("{problem_name}", name)
    content = content.replace("{difficulty}", difficulty.capitalize())
    content = content.replace("{topics}", topics)
    content = content.replace("{date}", date_solved)
    content = content.replace("{problem_slug}", problem_slug)
    content = content.replace("{problem_description}", description or "Add problem description here")
    
    # Create directory structure
    problem_dir = repo_root / "problems" / difficulty / f"{number:04d}-{problem_slug}"
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Create README file
    readme_path = problem_dir / "README.md"
    with open(readme_path, 'w') as f:
        f.write(content)
    
    # Create solution file
    solution_path = problem_dir / "solution.py"
    solution_template = f'''"""
LeetCode {number}: {name}
Difficulty: {difficulty.capitalize()}
Topics: {topics}
Date: {date_solved}
"""

class Solution:
    def solutionMethod(self):
        """
        Write your solution here
        """
        pass


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test_input = None
    expected = None
    result = solution.solutionMethod(test_input)
    print(f"Test 1: {{'input': {{test_input}}, 'expected': {{expected}}, 'result': {{result}}, 'passed': {{result == expected}}}}")
'''
    
    with open(solution_path, 'w') as f:
        f.write(solution_template)
    
    # Create notes file
    notes_path = problem_dir / "notes.md"
    notes_content = f"""# Notes for {name}

## Initial Thoughts


## Debugging Notes


## Optimization Ideas


## Related Concepts in CV


"""
    with open(notes_path, 'w') as f:
        f.write(notes_content)
    
    print(f"✅ Created problem files at: {problem_dir}")
    print(f"   - README.md (problem description)")
    print(f"   - solution.py (code solution)")
    print(f"   - notes.md (personal notes)")
    print(f"\n📝 Next steps:")
    print(f"   1. Fill in the problem description in README.md")
    print(f"   2. Write your solution in solution.py")
    print(f"   3. Run: python scripts/update_progress.py")
    print(f"   4. Commit and push your changes")
    
    return problem_dir


def main():
    parser = argparse.ArgumentParser(
        description="Create a new LeetCode problem file structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/create_problem.py --number 1 --name "Two Sum" --difficulty easy --topics "arrays,hash-table"
  python scripts/create_problem.py -n 42 -N "Trapping Rain Water" -d hard -t "arrays,two-pointers,dp"
        """
    )
    
    parser.add_argument('-n', '--number', type=int, required=True,
                      help='Problem number (e.g., 1, 42, 200)')
    parser.add_argument('-N', '--name', type=str, required=True,
                      help='Problem name (e.g., "Two Sum")')
    parser.add_argument('-d', '--difficulty', type=str, required=True,
                      choices=['easy', 'medium', 'hard'],
                      help='Problem difficulty')
    parser.add_argument('-t', '--topics', type=str, required=True,
                      help='Comma-separated topics (e.g., "arrays,hash-table")')
    parser.add_argument('--description', type=str, default="",
                      help='Optional problem description')
    
    args = parser.parse_args()
    
    create_problem_file(
        number=args.number,
        name=args.name,
        difficulty=args.difficulty,
        topics=args.topics,
        description=args.description
    )


if __name__ == "__main__":
    main()
