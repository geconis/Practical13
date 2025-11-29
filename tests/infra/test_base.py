import pytest
from base import Command


def test_command_requires_execute():
    cmd = Command("test")
    with pytest.raises(NotImplementedError):
        cmd.execute([])
