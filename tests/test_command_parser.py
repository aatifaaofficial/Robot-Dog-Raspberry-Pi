from robot_dog.voice.command_parser import CommandParser


def test_command_parser_walk():
    result = CommandParser.parse("walk forward")
    assert result["command"] == "walk_forward"


def test_command_parser_stop():
    result = CommandParser.parse("stop")
    assert result["command"] == "stop"
