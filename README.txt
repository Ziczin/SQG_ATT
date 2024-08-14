Use "start.bat" to quickly start the program.
Use "start_add.bat" if you need additional output.
Use "start_log.bat" if you need more detailed service information.

config.cfg and text.txt files generated when running via .bat files

The repository contains: a control file, a file with a character replacement function, a file with a logging class with the ability to disable, a file that generates lines similar to the lines in the technical specification.

Parameters:
cfg - Path to the configuration file
text - Path to the file being processed
--log - Enables display of file contents
--genall - Generate all files - both genconf and gentext
--genconf - help="Generate configuration file
--gettext - Generate text file
--show count - Shows the number of replacements
--show original - Shows the original line

(If the files are missing, but the corresponding parameters for generation are specified, then the files will be created at the specified paths)