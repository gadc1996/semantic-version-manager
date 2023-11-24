import pytest
from unittest.mock import mock_open, patch
from semversion import version

@pytest.fixture
def file_content():
    return "1.2.3"

@pytest.fixture
def mock_open_file(file_content):
    with patch("builtins.open", new_callable=mock_open, read_data=file_content) as m:
        yield m

def test_get_version(mock_open_file, file_content):
    with patch("builtins.open", mock_open_file):
        result = version()
        assert result == file_content

def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError("File not found")):
        with pytest.raises(FileNotFoundError):
            version()
