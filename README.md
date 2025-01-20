# DBH
A Decimal, Binary, and Hexadecimal converter and calculator designed for learning. Creates a table of the math
behind the conversion. 

usage: DBH.py [-h] [-db DEC_TO_BIN] [-dh DEC_TO_HEX] [-bd BIN_TO_DEC] [-bh BIN_TO_HEX] [-hd HEX_TO_DEC] [-hb HEX_TO_BIN] [-ct] [-t]

Learning tool for Number conversion

options:
  -h, --help            show this help message and exit 
  
  -db DEC_TO_BIN, --dec-to-bin DEC_TO_BIN  Decimal to Binary Converted
  
  -dh DEC_TO_HEX, --dec-to-hex DEC_TO_HEX Decimal to Hexadecimal Converter
  
  -bd BIN_TO_DEC, --bin-to-dec BIN_TO_DEC Binary to Decimal Converter
  
  -bh BIN_TO_HEX, --bin-to-hex BIN_TO_HEX Binary to Hexadecimal Converter
  
  -hd HEX_TO_DEC, --hex-to-dec HEX_TO_DEC Hexidecimal to Decimal Converter
  
  -hb HEX_TO_BIN, --hex-to-bin HEX_TO_BIN Hexadecimal to Binary Converter
  
  -ct, --conversion-table Prints table of all base number conversion between hex, bin, and dec
  
  -t, --table           Prints table of the requested number conversion
  

## TODO List:
- Handle decimal to binary --COMPLETE--
    - create -db flag --COMPLETE--
    - handle negative numbers
- Handle decimal to hexadecimal --COMPLETE--
    - create -dh flag --COMPLETE--
- Handle binary to decimal --COMPLETE--
    - create -bd flag --COMPLETE--
- Handle binary to hexadecimal --COMPLETE--
    - create -bh flag --COMPLETE--
- Handle hexadecimal to decimal --COMPLETE--
    - create -hd flag --COMPLETE--
- Handle hexadecimal to binary --COMPLETE--
    - create -hb flag --COMPLETE--
- Create table showing the conversion of the number --COMPLETE--
    - Create -t flag --COMPLETE--
- Create table to show the different values for hex 1 - 15 --COMPLETE--
