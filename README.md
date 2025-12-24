# Concert Ticket Scanner

A terminal-based ticket scanning system for concert/event entry.

## Features
- Load ticket list from CSV
- Interactive scanning mode
- Validate tickets (unused, format, existence)
- Prevent duplicate entry
- Track scan history
- Show session and overall statistics
- Persistent ticket status updates

## Requirements
- Python 3.8+
- Pandas
- argparse
- Pytest
- (Optional: textual for enhanced TUI)

## CSV Structure
The tickets CSV must have exactly these columns:

| Column   | Description                  | Example       |
|----------|------------------------------|---------------|
| code     | Unique ticket code           | ABC123        |
| category | Ticket type VIP / REGULAR    | VIP           |
| status   | Current status               | unused        |

Allowed status values: `unused`, `used`, `invalid`, `cancelled`

Example `tickets.csv`:
```csv
code,category,status
ABC123,VIP,unused
XYZ789,REGULAR,unused
DEF456,VIP,used
