import argparse
from prettytable import PrettyTable

parser = argparse.ArgumentParser(description="Learning tool for Number conversion")
parser.add_argument("-db", "--dec-to-bin", type=int, help="Decimal to Binary Converter")
parser.add_argument("-dh", "--dec-to-hex", type=int, help="Decimal to Hexadecimal Converter")
parser.add_argument("-bd", "--bin-to-dec", type=str, help="Binary to Decimal Converter")
parser.add_argument("-bh", "--bin-to-hex", type=str,help="Binary to Hexadecimal Converter")
parser.add_argument("-hd", "--hex-to-dec", type=str, help="Hexidecimal to Decimal Converter")
parser.add_argument("-hb","--hex-to-bin", type=str, help="Hexadecimal to Binary Converter")
parser.add_argument("-t","--table", action="store_true", help="Prints table of the number conversion" )

# Constants
BINARY = "bin"
DECIMAL = "dec"
HEXADECIMAL = "hex"


def decimal_to_binary(num: int, create_table:bool=False):
    '''
    Responsible for converting decimal to binary
    '''
    print(f"\nDecimal {num} to binary: {bin(num)}\n")
    if create_table:
        table_generator(str(num), DECIMAL, BINARY)

def decimal_to_hexadecimal(num: int, create_table:bool=False):
    '''
    Responsible for converting decimal to hexadecimal
    '''
    print(f"\nDecimal {num} to binary: {hex(num)}\n")
    if create_table:
        table_generator(str(num), DECIMAL, HEXADECIMAL)

def binary_to_decimal(bin_str: str, create_table:bool=False):
    '''
    Converts binary to decimal
    '''
    print(F"\nBinary {bin_str} to decimal: {int(bin_str, base=2)}")
    if create_table:
        table_generator(bin_str, type=BINARY, to_type=DECIMAL)

def binary_to_hexadecimal(bin_str: str, create_table:bool=False):
    '''
    Converts binary to hexadecimal
    '''
    print(f"Binary {bin_str} to Hexadecimal: {hex(int(bin_str,2))}")
    if create_table:
        table_generator(bin_str, type=BINARY, to_type=HEXADECIMAL)

def hexadecimal_to_decimal(hex_str: str, create_table:bool=False):
    '''
    Converts hex to decimal
    '''
    if hex_str[0:2] != "0x":
        print("Hex must begin with 0x")
        return
    print(f"Hexadecimal {hex_str} to decimal: {int(hex_str,16)}")
    if create_table:
        table_generator(hex_str, type=HEXADECIMAL, to_type=DECIMAL)

def table_generator(value: str, type:str, to_type:str):
    '''
    Takes a value as a string, the original type, and the type of value being converted to and prints a table to show
    the math behind the conversion 
    '''
    table = PrettyTable()
    if type == DECIMAL:
        value = int(value)
        if to_type == BINARY:
            table.field_names = ["Step", "Conversion", "Value", "Has Remainder? (Binary)"]
            step = 1
            while value > 0:
                quotient = int(value/2)
                table.add_row([step, f"{value}/2", quotient, 1 if value % 2 != 0 else 0])
                value = quotient      
                step += 1 
        if to_type == HEXADECIMAL:
            table.field_names = ["Step", "Conversion", "Value", "Remainder value (Hexadecimal)"]
            step = 1
            while value > 0:
                quotient = int(value/16)
                remainder = hex(value % 16)
                table.add_row([step, f"{value}/16", quotient, remainder])
                value = quotient      
                step += 1 
    if type == BINARY:
        if to_type == DECIMAL:
            table.field_names = ["step", "Binary Position", "Digit", "Sum"]
            step: int = 1
            total: int = 0
            value = value[::-1]
            for x in range(len(value)-1, -1, -1):
                sum = 2**x * int(value[x])
                table.add_row([step, f"2^{x}", value[x], sum])
                total = total + sum
                step += 1
            table.add_row(["--","--","Total", total])
        if to_type == HEXADECIMAL:
            table.field_names = ["Step", "4-bits", "Decimal", "Hex"]
            step: int = 1
            while len(value) % 4 != 0:
                value = '0' + value
            for i in range(len(value),0, -4):
                bits = value[i-4:i]
                dec = int(bits, 2)
                table.add_row([step, bits, int(bits,2), hex(dec)[2:]])
                step = step + 1
    if type == HEXADECIMAL:
        if to_type == DECIMAL:
            table.field_names = ["Step", "Conversion", "Hex", "Decimal Value"]
            step = 1
            modified_value = value[2:]
            total = 0
            for x in range(len(modified_value)):
                hex = modified_value[len(modified_value)-x-1]
                hex_pos = f"16^{x}"
                decimal_val = int(hex, 16)*(16**x)
                total += decimal_val
                table.add_row([step, hex_pos, hex, decimal_val])
                step += 1        
            table.add_row(["","", "Total", total ])
             
    print(f"{table}\n")

if __name__ == "__main__":
    args = parser.parse_args()
    if args.dec_to_bin:
        decimal_to_binary(args.dec_to_bin, args.table)
    if args.dec_to_hex:
        decimal_to_hexadecimal(args.dec_to_hex, args.table)
    if args.bin_to_dec:
        binary_to_decimal(args.bin_to_dec, args.table)
    if args.bin_to_hex:
        binary_to_hexadecimal(args.bin_to_hex, args.table)
    if args.hex_to_dec:
        hexadecimal_to_decimal(args.hex_to_dec, args.table)

    
    