#!/usr/bin/python3
"""Test module for HBNBCommand class"""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()
        self.storage_patcher = patch('models.storage')
        self.storage_mock = self.storage_patcher.start()

    def tearDown(self):
        """Tear down test environment"""
        self.storage_patcher.stop()

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        """Test help command"""
        with patch('builtins.input', side_effect=['help', 'EOF']):
            self.console.cmdloop()

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        """Test show command"""
        with patch('builtins.input', side_effect=['show BaseModel', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        """Test destroy command"""
        with patch('builtins.input', side_effect=['destroy BaseModel', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_command(self, mock_stdout):
        """Test all command"""
        with patch('builtins.input', side_effect=['all', 'EOF']):
            self.console.cmdloop()
            self.assertIn("BaseModel", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        """Test update command"""
        with patch('builtins.input', side_effect=['update BaseModel', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        """Test create command with invalid class"""
        with patch('builtins.input',
                   side_effect=['create InvalidClass', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        """Test show command with invalid class"""
        with patch('builtins.input', side_effect=['show InvalidClass', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class(self, mock_stdout):
        """Test destroy command with invalid class"""
        with patch('builtins.input',
                   side_effect=['destroy InvalidClass', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class(self, mock_stdout):
        """Test update command with invalid class"""
        with patch('builtins.input',
                   side_effect=['update InvalidClass', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_edge_cases(self, mock_stdout):
        """Test invalid input edge cases"""
        invalid_inputs = ['', '    ', '$%#&', 'invalid_input']
        for invalid_input in invalid_inputs:
            with patch('builtins.input', side_effect=[invalid_input, 'EOF']):
                self.console.cmdloop()

    def test_create_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
