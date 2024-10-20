def AlignedOutput():
  major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
  minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
  mapping_output = ""
  for i, major in enumerate(major_colors):
    for j, minor in enumerate(minor_colors):
      number = str(i * 5 + j)
      number = number.rjust(2,' ')
      major_colour = major.ljust(6,' ')
      minor_colour = minor.ljust(6,' ')
      output_string = number+ ' | ' + major_colour + ' | ' + minor_colour
      mapping_output += output_string + '\n'   
