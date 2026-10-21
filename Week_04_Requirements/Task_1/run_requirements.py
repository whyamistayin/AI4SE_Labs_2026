"""Run the requirements network over a directory of .txt/.eml source files."""

import argparse
import logging
from pathlib import Path

from requirements_network.workflow import build_network


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a traceable software requirements document."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        required=True,
        help="Directory recursively containing .txt and/or .eml source files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/requirements.md"),
        help="Markdown destination (default: output/requirements.md).",
    )
    parser.add_argument(
        "--max-revision-rounds",
        type=int,
        default=2,
        help="Maximum normalization/review feedback rounds (default: 2).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable informational execution logs.",
    )
    args = parser.parse_args()
    if args.max_revision_rounds < 0:
        parser.error("--max-revision-rounds must be zero or greater")
    return args


def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    result = build_network().invoke(
        {
            "input_dir": str(args.input_dir),
            "output_path": str(args.output),
            "max_revision_rounds": args.max_revision_rounds,
            "revision_round": 0,
        }
    )
    print(f"Requirements document: {result['output_path']}")
    print(f"Review approved: {result.get('review_approved', False)}")
    print(f"Review rounds: {result.get('revision_round', 0)}")


if __name__ == "__main__":
    main()

