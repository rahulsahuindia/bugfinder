import argparse
import sys
from bugfinder.scanner import BugFinder

def main():
    parser = argparse.ArgumentParser(description='BugFinder - Automated bug detection tool')
    parser.add_argument('path', help='Path to the repository to scan')
    parser.add_argument('--format', choices=['json', 'sarif'], default='json', help='Output format')
    args = parser.parse_args()

    finder = BugFinder(args.path)
    results = finder.scan()
    output = finder.report(format=args.format)
    print(output)
    # Return exit code based on findings
    if any(results.values()):
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
