import unittest
from unittest.mock import mock_open, patch
import semversion


class TestIncrement(unittest.TestCase):
    mock_file_content = "0.1.0"

    @patch("builtins.open", new_callable=mock_open, read_data=mock_file_content)
    def test_increment_major(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            result = semversion.increment(semversion.MAJOR)
            expected_version = "1.0.0"
            self.assertEqual(result, expected_version)

    @patch("builtins.open", new_callable=mock_open, read_data=mock_file_content)
    def test_increment_minor(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            result = semversion.increment(semversion.MINOR)
            expected_version = "0.2.0"
            self.assertEqual(result, expected_version)

    @patch("builtins.open", new_callable=mock_open, read_data=mock_file_content)
    def test_increment_patch(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            result = semversion.increment(semversion.PATCH)
            expected_version = "0.1.1"
            self.assertEqual(result, expected_version)

    @patch("builtins.open", side_effect=FileNotFoundError("File not found"))
    def test_file_not_found(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            with self.assertRaises(FileNotFoundError, msg="Expected FileNotFoundError"):
                semversion.increment(semversion.PATCH)
