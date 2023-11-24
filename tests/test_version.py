import unittest
from unittest.mock import mock_open, patch
from semversion import version


class TestVersion(unittest.TestCase):
    def setUp(self):
        self.file_content = "1.2.3"
        self.mock_file = mock_open(read_data=self.file_content)

    @patch("builtins.open", new_callable=mock_open, read_data="1.2.3")
    def test_get_version(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            result = version()
            self.assertEqual(result, self.file_content)

    @patch("builtins.open", side_effect=FileNotFoundError("File not found"))
    def test_file_not_found(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            with self.assertRaises(FileNotFoundError, msg="Expected FileNotFoundError"):
                version()
