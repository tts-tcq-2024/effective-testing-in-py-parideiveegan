import io
import unittest
import unittest.mock
from misaligned import print_color_map

class TestPrintColourMap(unittest.TestCase):
     @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
     def assert_stdout(self,expected_output, mock_stdout):
          print_color_map()
          self.asserEqual(mock_stdout.getvalue(), expected_output)
     def test_print_output(self):
          major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
          minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
          mapping_output = ""
          for i, major in enumerate(major_colors):
               for j, minor in enumerate(minor_colors):
                    number = "i * 5 + j"
                    number = number.rjust(2,' ')
                    major_colour = major.ljust(6,' ')
                    minor_colour = minor.ljust(6,' ')
                    output_string = number+ ' | ' + major + ' | ' + minor
                    mapping_output += output_string + '\n'       
          self.assert_stdout(mapping_output)
     def test_return_result(self):
          self.assertEqual(print_color_map(),25)
if __name__ == '__main__':
     unittest.main()
