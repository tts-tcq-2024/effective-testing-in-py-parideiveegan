import io
import unittest
import unittest.mock
from misaligned import print_color_map
from AlignedOutput import AlignedOutput

class TestPrintColourMap(unittest.TestCase):
     @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
     def assert_stdout(self,expected_output, mock_stdout):
          print_color_map()
          self.assertEqual(mock_stdout.getvalue(), expected_output)
     def test_IsPrintOutputAligned(self):
          mapping_output = AlignedOutput()
          self.assert_stdout(mapping_output)
     def test_return_result(self):
          self.assertEqual(print_color_map(),25)
if __name__ == '__main__':
     unittest.main()
