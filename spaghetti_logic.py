def calculate_totals(data, rate=1.15):
    """Calculate totals by applying a rate increase to each data point."""
    return [d * rate for d in data]

def print_totals(totals):
    """Print each total with formatted output."""
    for total in totals:
        print(f"Total: {total:.2f}")

def log_totals(totals, filename="log.txt"):
    """Log the list of totals to a file."""
    with open(filename, "a") as f:
        f.write(str(totals) + "\n")

def process_data(data, rate=1.15, log_file="log.txt"):
    """Process data by calculating totals, printing them, and logging."""
    totals = calculate_totals(data, rate)
    print_totals(totals)
    log_totals(totals, log_file)
    return totals
