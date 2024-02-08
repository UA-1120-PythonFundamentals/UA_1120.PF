import unittest
from functions import greeting_by_name, get_symbol_position, merge
from functions_with_errors import greeting_by_name as greeting_with_errors, \
    get_symbol_position as get_symbol_position_with_errors, merge as merge_with_errors

class TestFunctions(unittest.TestCase):

    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name("John"), "Hello John!", "Incorrect greeting")
        self.assertEqual(greeting_with_errors("John"), "Hello John!", "Incorrect greeting")

    def test_get_symbol_position_correct_symbol(self):
        self.assertEqual(get_symbol_position("abc", "b"), 2, "Incorrect symbol position")
        self.assertEqual(get_symbol_position_with_errors("abc", "b"), 2, "Incorrect symbol position")

    def test_get_symbol_position_incorrect_symbol(self):
        self.assertEqual(get_symbol_position("abc", "xy"), "Error! Symbol can be string with only one letter", "Incorrect error message")
        self.assertEqual(get_symbol_position_with_errors("abc", "xy"), "Error! Symbol can be string with only one letter", "Incorrect error message")

    def test_get_symbol_position_symbol_not_found(self):
        self.assertEqual(get_symbol_position("abc", "z"), "Not found", "Symbol not found error")
        self.assertEqual(get_symbol_position_with_errors("abc", "z"), "Not found", "Symbol not found error")

    def test_merge_dict1_immutable(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merged_dict = merge(dict1, dict2)
        self.assertNotEqual(id(dict1), id(merged_dict), "Input dictionary 1 should be immutable")

    def test_merge_dict2_immutable(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merged_dict = merge(dict1, dict2)
        self.assertNotEqual(id(dict2), id(merged_dict), "Input dictionary 2 should be immutable")

    def test_merge_result(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merged_dict = merge(dict1, dict2)
        self.assertEqual(merged_dict, {'a': 1, 'b': 3, 'c': 4}, "Incorrect merged dictionary")

if __name__ == '__main__':
    unittest.main()