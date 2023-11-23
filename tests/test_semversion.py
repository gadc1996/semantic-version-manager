import unittest
from unittest.mock import mock_open, patch
from semantic_versioning import Version

class TestSemVersion(unittest.TestCase):
    def setUp(self):
        self.file_content = "1.2.3"
        self.mock_file = mock_open(read_data=self.file_content)

    @patch("builtins.open", new_callable=mock_open, read_data="1.2.3")
    def test_get_version(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            result = Version.get()
            self.assertEqual(result, self.file_content)

    @patch("builtins.open", new_callable=mock_open, read_data="1.2.3")
    def test_increment_patch(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            result = Version.increment(Version.PATCH)
            expected_version = "1.2.4"
            self.assertEqual(result, expected_version)

    @patch("builtins.open", new_callable=mock_open, read_data="1.2.3")
    def test_increment_major(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            result = Version.increment(Version.MAJOR)
            expected_version = "2.0.0"
            self.assertEqual(result, expected_version)

    @patch("builtins.open", new_callable=mock_open, read_data="1.2.3")
    def test_increment_minor(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            result = Version.increment(Version.MINOR)
            expected_version = "1.3.0"
            self.assertEqual(result, expected_version)

    @patch("builtins.open", new_callable=mock_open)
    def test_initialize(self, mock_open_file):
        with patch("builtins.open", mock_open_file):
            Version.initialize()

        mock_open_file.assert_called_once_with(Version.FILE_PATH, "w")
        handle = mock_open_file()
        handle.write.assert_called_once_with(Version.DEFAULT_VERSION)

if __name__ == "__main__":
    unittest.main()
