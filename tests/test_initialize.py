import pytest
from unittest.mock import mock_open, patch
from semversion import initialize
from semversion.constants import SEMVERSION_FILE


@pytest.fixture
def mock_file_content():
    return "0.1.0"


@pytest.fixture
def mock_open_file(mock_file_content):
    with patch(
        "builtins.open", new_callable=mock_open, read_data=mock_file_content
    ) as m:
        yield m


def test_initialize(mock_open_file):
    with patch("builtins.open", mock_open_file):
        initialize()
    mock_open_file.assert_called_once_with(SEMVERSION_FILE, "w")
    assert mock_open_file().write.called_once_with("0.1.0")
