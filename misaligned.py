import io
import unittest
import unittest.mock

class TestPrintColourMap(unittest.TestCase):
     @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self,expected_output, mock_stdout):        
        print_color_map()
        self.asserEqual(mock_stdout.getvalue(), expected_output)
    def test_only_numbers(self):
        major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
        minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
        mapping_output = ""
        for i, major in enumerate(major_colors):
            for j, minor in enumerate(minor_colors):
                number = i * 5 + j
                number = number.rjust(2,' ')
                major_colour = major.ljust(6,' ')
                minor_colour = minor.ljust(6,' ')
                output_string = number+ ' | ' + major + ' | ' + minor
                mapping_output += output_string + '\n'       
        self.assert_stdout(mappring_output)
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")
