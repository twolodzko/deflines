import argparse
import glob

from deflines import ModuleAnalyzer


def parse_args():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [PATTERN]",
        description="Calculate number of lines and cyclomatic complexity for each function and method in the module.",
    )
    parser.add_argument(
        "pattern",
        help="pattern to identify files to be analyzed",
        type=str,
        nargs="?",
        default="**/*.py",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    for file in glob.glob(args.pattern, recursive=True):
        results = ModuleAnalyzer.process(file)

        for result in results:
            print(result)


if __name__ == "__main__":
    main()
