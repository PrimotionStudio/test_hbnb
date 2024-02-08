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

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("quit")
            self.assertEqual(mock_stdout.getvalue().strip(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_base_model_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_city_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show City")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_amenity_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show Amenity")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_place_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show Place")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_review_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show Review")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_state_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show State")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_user_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show User")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("update")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("destroy")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_base_model_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_user_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create User")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_place_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create Place")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_city_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create City")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_state_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create State")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_review_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create Review")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_amenity_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create Amenity")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

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
