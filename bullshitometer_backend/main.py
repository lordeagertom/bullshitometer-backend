import argparse
import datetime


def valid_date(s: str) -> datetime.datetime:
    """
    Converts a string to a datetime object if it matches the specified date format.
    Raises an error if the string does not conform to the expected format.

    :param s: The date string to be validated and converted.
    :return: A datetime object corresponding to the parsed date.
    :raises argparse.ArgumentTypeError: If the input string does not match the required date format "%Y-%m-%d".
    """
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError as err:
        raise argparse.ArgumentTypeError(f"not a valid date: {s!r}") from err


def parse_args():
    parser = argparse.ArgumentParser(description='Provide start and end dates for the analysis.')
    parser.add_argument("start_date", help="Start date in YYYY-MM-DD format", type=valid_date)
    parser.add_argument("end_date", help="End date in YYYY-MM-DD format", type=valid_date)
    return parser.parse_args()


def main():
    """Main function to handle parsed arguments."""
    args = parse_args()
    print(f"Arguments received: {args}")


if __name__ == '__main__':
    main()
