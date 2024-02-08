#!/usr/bin/python3
"""
Test Module for console
"""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
sys.path.append('../')
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            expected_output = (
                    "Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  count  create  destroy  help  quit  show  update"
            )
            HBNBCommand().onecmd("help")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_quit_command(self, mock_stdout):
    #     with patch('builtins.input', return_value='quit'):
    #         self.assertTrue(self.console.cmdloop())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_create_command(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['create BaseModel', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn(
    #             "Please enter a class name and its attributes", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_show_command(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['show BaseModel', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn("** instance id missing **", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_destroy_command(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['destroy BaseModel', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn("** instance id missing **", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_all_command(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['all', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn("BaseModel", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_update_command(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['update BaseModel', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn("** instance id missing **", mock_stdout.getvalue())

    # # Additional test cases for each command

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_help_specific_command(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['help create', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn("Create a new instance of BaseModel",
    #                       mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_create_invalid_class(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['create InvalidClass', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_show_invalid_class(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['show InvalidClass', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_destroy_invalid_class(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['destroy InvalidClass', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_update_invalid_class(self, mock_stdout):
    #     with patch('builtins.input', side_effect=['update InvalidClass', 'EOF']):
    #         self.console.cmdloop()
    #         self.assertIn("** class doesn't exist **", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
