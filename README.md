# DBH
A Decimal, Binary, and Hexadecimal converter and calculator designed for learning. Creates a table of the math
behind the conversion. 

## Requirements:
Python3
pip
virtualenv

## Installation:
1. Create a virtualenv:
```bash
    python -m virtualenv .env
```
2. Start virtual environment
```bash
    .env/Scripts/Activate.<Your extension based on your command line>
```
3. Install python dependencies from requirements.txt
```bash
    pip install -r requirements.txt
```
4. Run DBH
```bash
python DBH.py <flag> <value> <-t for table>
```
    


## usage:
```bash
 DBH.py [-h] [-db DEC_TO_BIN] [-dh DEC_TO_HEX] [-bd BIN_TO_DEC] [-bh BIN_TO_HEX] [-hd HEX_TO_DEC] [-hb HEX_TO_BIN] [-ct] [-t]

Learning tool for Number conversion

options:

  **-h, --help**         show this help message and exit 
  
  **-db, --dec-to-bin**  Decimal to Binary Converted
  
  **-dh, --dec-to-hex**  Decimal to Hexadecimal Converter
  
  **-bd, --bin-to-dec**  Binary to Decimal Converter
  
  **-bh, --bin-to-hex**  Binary to Hexadecimal Converter
  
  **-hd, --hex-to-dec**  Hexidecimal to Decimal Converter
  
  **-hb, --hex-to-bin** Hexadecimal to Binary Converter
  
  **-ct, --conversion-table** Prints table of all base number conversion between hex, bin, and dec
  
  **-t, --table**           Prints table of the requested number conversion
```

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
