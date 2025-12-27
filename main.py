"""
Concert Ticket Scanner - Terminal-based ticket validation system.
"""

import sys
from argparse import ArgumentParser
from pathlib import Path

from core.models import ScanSession
from core.session import create_new_session, load_session, save_session, reset_session
from core.scanner import interactive_scan
from core.summary import print_summary
from core.ticket_loader import load_and_validate_tickets


def setup_argparser():
    parser = ArgumentParser(description="Concert Ticket Scanner CLI")
    parser.add_argument(
        "mode",
        choices=["scan", "summary", "reset"],
        help="Operation mode: scan (interactive), summary (report), reset (clear history)",
    )
    parser.add_argument(
        "-f", "--file", default="data/tickets.csv", help="Path to the tickets CSV file"
    )
    return parser


def main():
    parser = setup_argparser()
    args = parser.parse_args()

    csv_path = Path(args.file)
    if not csv_path.exists():
        print(f"Error: CSV file not found at {csv_path}", file=sys.stderr)
        sys.exit(1)

    try:
        df = load_and_validate_tickets(csv_path)
    except ValueError as e:
        print(f"Error loading CSV: {e}", file=sys.stderr)
        sys.exit(1)

    if args.mode == "scan":
        print("Ticket Scanner - Enter codes (type 'quit' to exit)\n")

        session = create_new_session()
        interactive_scan(df, session)

        save_session(session)
        df.to_csv(csv_path, index=False)

        print("\nScan session ended. Tickets updated.")

    elif args.mode == "summary":
        session = load_session()
        print_summary(df, session)

    elif args.mode == "reset":
        reset_session()

        df["status"] = "valid"
        df.to_csv(csv_path, index=False)

        print("Session history and ticket statuses reset.")


if __name__ == "__main__":
    main()
