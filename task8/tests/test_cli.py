import pytest
from unittest.mock import patch
from calculator import main
import sys

@pytest.fixture
def run_cli_with_input(monkeypatch, capsys):
    def _run_cli(input_commands):
        input_generator = iter(input_commands)
        monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
        
        # We need to explicitly exit the main loop for testing
        # Patching sys.exit is one way, or we can ensure 'exit' is in input_commands
        main.main() # Run the main loop without expecting StopIteration here
        
        captured = capsys.readouterr()
        return captured.out.splitlines(), captured.err.splitlines() # Return both stdout and stderr
    return _run_cli

def test_basic_arithmetic_operations(run_cli_with_input):
    commands = [
        "2 + 3",
        "10 - 5",
        "2 * 4",
        "9 / 3",
        "exit"
    ]
    stdout_lines, stderr_lines = run_cli_with_input(commands) # Unpack the tuple
    
    # Expected output will include the prompt "> "
    # So we check every other line for the result
    assert "5" in stdout_lines
    assert "5" in stdout_lines
    assert "8" in stdout_lines
    assert "3" in stdout_lines
    assert len(stderr_lines) == 0 # No errors to stderr

def test_floating_point_arithmetic(run_cli_with_input):
    commands = [
        "1.5 + 2.5",
        "5.0 - 1.5",
        "2.5 * 2.0",
        "7.0 / 2.0",
        "exit"
    ]
    stdout_lines, stderr_lines = run_cli_with_input(commands) # Unpack the tuple
    assert "4" in stdout_lines
    assert "3.5" in stdout_lines
    assert "5" in stdout_lines
    assert "3.5" in stdout_lines
    assert len(stderr_lines) == 0 # No errors to stderr

def test_invalid_expression_handling(run_cli_with_input):
    commands = [
        "1 +",
        "abc + 2",
        "1 % 2", # New test case
        "1 $ 2", # New test case
        "1 ++ 2", # New test case
        "exit"
    ]
    stdout_lines, stderr_lines = run_cli_with_input(commands) # Unpack the tuple
    assert len([line for line in stdout_lines if line.strip() != '' and line != '>']) == 0 # No output to stdout
    assert stderr_lines.count("Error: Invalid expression") == 5 # Expect 5 invalid expression errors in stderr

def test_division_by_zero_handling(run_cli_with_input):
    commands = [
        "10 / 0",
        "exit"
    ]
    stdout_lines, stderr_lines = run_cli_with_input(commands) # Unpack the tuple
    assert len([line for line in stdout_lines if line.strip() != '' and line != '>']) == 0 # No output to stdout
    assert "Error: Division by zero" in stderr_lines

def test_exit_and_quit_commands(run_cli_with_input):
    commands = [
        "exit",
        "quit"
    ]
    stdout_lines, stderr_lines = run_cli_with_input(commands) # Unpack the tuple
    # The output should not contain any error message, just the prompts and then exit
    assert not any("Error" in line for line in stderr_lines) # Check stderr
    assert len([line for line in stdout_lines if line.strip() != '' and line != '>']) == 0 # No results to stdout

def test_empty_input_handling(run_cli_with_input):
    commands = [
        "",         # Empty input
        "   ",      # Whitespace only input
        "1 + 2",
        "exit"
    ]
    stdout_lines, stderr_lines = run_cli_with_input(commands) # Unpack the tuple
    # The empty inputs should not produce any output (neither error nor result)
    # The output should only contain the result of "1 + 2" which is "3"
    assert "3" in stdout_lines
    assert len([line for line in stdout_lines if line.strip() != '' and line != '>']) == 1 # Only one actual output line (the result)
    assert len(stderr_lines) == 0 # No errors to stderr

def test_help_command(run_cli_with_input):
    commands = [
        "help",
        "exit"
    ]
    stdout_lines, stderr_lines = run_cli_with_input(commands) # Unpack the tuple
    assert "Supported operations: +, -, *, /" in stdout_lines
    assert "Examples:" in stdout_lines
    assert "  3 + 4" in stdout_lines
    assert "  10.5 / 2.5" in stdout_lines
    assert "  exit" in stdout_lines
    assert len(stderr_lines) == 0 # No errors to stderr

def test_float_limit_warnings(monkeypatch, capsys): # Removed run_cli_with_input from args
    # Expressions that produce results close to float limits
    commands = [
        f"{sys.float_info.max / 3} * 2", # Should trigger max limit warning
        f"{sys.float_info.min * 3} / 2", # Should trigger min limit warning
        "exit"
    ]
    input_generator = iter(commands)
    monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
    
    main.main() # Run the main loop
    
    captured = capsys.readouterr() # capture stdout AND stderr
    
    assert "Warning: Result is approaching float max limit." in captured.err
    assert "Warning: Result is approaching float min limit (denormalized)." in captured.err



