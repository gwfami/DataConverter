Census Data Converter

This program converts multi-row census data into single-row records separated by tildes (~), saved as a CSV file. No software installation is needed.

How to Use:
1. Copy the program file (CensusConverter) to your desktop.
2. Double-click CensusConverter.
3. Choose your input file (e.g., input.txt) from your computer.
4. Choose where to save the output file (e.g., output.csv).
5. Wait for the "Success" message. The output file will be created.

Input File Format:
- Create a text file with census records separated by "||".
- The first record does not need a "||" before it.
- Ignore blank lines within records.
- The first line of each record is treated as the full name, split into Given Name and Surname.
- Example: (NOTE:  The "More" with a line before it and nothing else on the line should be removed, but it may not be present.)

- Change:

    Violet N Williams
    Principal
    Minnesota, State Census, 1905
	
    Census  1905 
    Wright, Minnesota, United States 
    Birth  1877 
    Minnesota 
    		
    More
	
    Carrie L Nelson
    Principal
    Minnesota, State Census, 1905
	
    Census  1905 
    Wright, Minnesota, United States 
    Birth  1850 
    Sweden 
    		
    More
	
    Andrew Nelson
    ...

- To:

    Violet N Williams
    Principal
    Minnesota, State Census, 1905
	
    Census  1905 
    Wright, Minnesota, United States 
    Birth  1877 
    Minnesota 
    		
    ||
    Carrie L Nelson
    Principal
    Minnesota, State Census, 1905
	
    Census  1905 
    Wright, Minnesota, United States 
    Birth  1850 
    Sweden 
    		
    ||
    Andrew Nelson
    ...


Output:
- The output is a CSV file with a header and one row per record. The first line is split into Full Name, Given Name, and Surname, followed by remaining lines joined by ~. Example:
  Full Name~Given Name~Surname~Type~Census~Other~Location~Birth Year~Where Born
  Violet N Williams~Violet N~Williams~Principal~Minnesota, State Census, 1905~Census  1905~Wright, Minnesota, United States~Birth  1877~Minnesota

Troubleshooting:
- If you see "No input file selected," click "Open" and choose a text file.
- Ensure records are separated by "||".
- Blank lines are ignored.
- Process the output in a spreadsheet to align fields like Type, Census, etc.
- For help, contact [Bruce at tiptoptemp@yahoo.com].

Sample File:
- A sample input.txt is included with the "||" already in place.  