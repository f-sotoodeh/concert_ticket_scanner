"""
Concert Ticket Scanner - Terminal-based ticket validation system.
"""

import sys
from argparse import ArgumentParser
from pathlib import Path

from pandas.io.formats.format import return_docstring

from core.history import load_session_history, save_scan_history
from core.scanner import interactive_scan
from core.session import ScanSession
from core.summary import print_summary
from core.ticket_loader import load_and_validate_tickets


def quit(error_message=None):
    """
    Quit the program, optionally displaying an error message.
    """
    print("\033c", end="")  # Clear terminal
    exit_code = 0
    if error_message:
        print(error_message, file=sys.stderr)
        exit_code = 1
    sys.exit(exit_code)


def setup_argparser():
    """
    Set up the argument parser for the CLI.
    """
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
    history_path = csv_path.with_stem(csv_path.stem + "_history")
    if not csv_path.exists():
        quit(f"Error: CSV file not found at {csv_path}")

    # Load tickets
    try:
        df = load_and_validate_tickets(csv_path)
    except ValueError as e:
        quit(f"Error loading CSV: {e}")
        return

    match args.mode:
        case "scan":
            session = ScanSession()
            print("Ticket Scanner - Enter codes (type 'quit' to exit)\n")
            interactive_scan(df, session, history_path)
            # After scan ends, save history and update CSV
            df.to_csv(csv_path, index=False)
            print("\nScan session ended. Tickets updated.")

        case "summary":
            session = load_session_history(history_path)
            print_summary(df, session)

        case "reset":
            # Clear history file
            history_path = Path("data/session_history.json")
            history_path.unlink(missing_ok=True)
            print("Session history cleared.")

            if input("Do you want to mark all tickets as used? (y/n): ").lower() == "y":
                df["status"] = "used"
                df.to_csv(csv_path, index=False)
                print("All tickets marked as used.")
                return
            elif (
                input("Do you want to mark all tickets as unused? (y/n): ").lower()
                == "y"
            ):
                df["status"] = "unused"
                df.to_csv(csv_path, index=False)
                print("All tickets marked as unused.")


if __name__ == "__main__":
    main()
