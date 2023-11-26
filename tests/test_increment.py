import pytest
from unittest.mock import mock_open, patch
import semversion


@pytest.fixture
def mock_file_content():
    return "0.1.0"


@pytest.fixture
def mock_open_file(mock_file_content):
    with patch(
        "builtins.open", new_callable=mock_open, read_data=mock_file_content
    ) as m:
        yield m


def test_increment_major(mock_open_file):
    with patch("builtins.open", mock_open_file):
        result = semversion.increment(semversion.MAJOR)
        expected_version = "1.0.0"
        assert result == expected_version


def test_increment_minor(mock_open_file):
    with patch("builtins.open", mock_open_file):
        result = semversion.increment(semversion.MINOR)
        expected_version = "0.2.0"
        assert result == expected_version


def test_increment_patch(mock_open_file):
    with patch("builtins.open", mock_open_file):
        result = semversion.increment(semversion.PATCH)
        expected_version = "0.1.1"
        assert result == expected_version


def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError("File not found")):
        with pytest.raises(FileNotFoundError):
            semversion.increment(semversion.PATCH)
