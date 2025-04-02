import argparse
import datetime
import sys

import pytest

from src.main import valid_date, parse_args  # Import the valid_date and parse_args functions


class TestArgParser:
    def test_valid_arguments(self, mocker):
        test_argv = ["main.py", "2023-01-01", "2023-12-31"]
        mocker.patch.object(sys, "argv", test_argv)
        args = parse_args()
        assert args.start_date == datetime.datetime(2023, 1, 1)
        assert args.end_date == datetime.datetime(2023, 12, 31)

    def test_missing_arguments(self, mocker):
        test_argv = ["main.py"]  # Missing required arguments
        mocker.patch.object(sys, "argv", test_argv)
        with pytest.raises(SystemExit):
            parse_args()

    def test_extra_arguments(self, mocker):
        test_argv = ["main.py", "2023-01-01", "2023-12-31", "additional_argument"]
        mocker.patch.object(sys, "argv", test_argv)
        with pytest.raises(SystemExit):
            parse_args()

    @pytest.mark.parametrize("invalid_date", ["invalid_date", "2023-31-12"])
    def test_invalid_date(self, mocker, invalid_date):
        test_argv = ["main.py", invalid_date, "2023-12-31"]
        mocker.patch.object(sys, "argv", test_argv)
        with pytest.raises(SystemExit):
            parse_args()


class TestValidDate:
    def test_valid_date(self):
        assert valid_date("2023-01-01") == datetime.datetime(2023, 1, 1)
        assert valid_date("2000-02-29") == datetime.datetime(2000, 2, 29)  # Leap year

    def test_invalid_date_format(self):
        with pytest.raises(argparse.ArgumentTypeError):
            valid_date("2023/01/01")  # Incorrect format
        with pytest.raises(argparse.ArgumentTypeError):
            valid_date("01-01-2023")  # Shouldn't be accepted

    def test_out_of_range_date(self):
        with pytest.raises(argparse.ArgumentTypeError):
            valid_date("2023-02-30")  # Invalid day
        with pytest.raises(argparse.ArgumentTypeError):
            valid_date("2023-13-01")  # Invalid month

    def test_empty_date_string(self):
        with pytest.raises(argparse.ArgumentTypeError):
            valid_date("")  # Empty date string
