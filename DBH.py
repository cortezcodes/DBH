import argparse
from prettytable import PrettyTable

parser = argparse.ArgumentParser(description="Learning tool for Number conversion")
parser.add_argument("-db", "--dec-to-bin", type=int, help="Decimal to Binary Converter")
parser.add_argument("-t","--table", action="store_true", help="Prints table of the number conversion" )
BINARY = "bin"
DECIMAL = "dec"


def decimal_to_binary(num: int, create_table:bool=False):
    '''
    Responsible for converting decimal to binary
    '''
    print(f"\nDecimal {num} to binary: {bin(num)}\n")
    if create_table:
        table_generator(str(num), DECIMAL, BINARY)

def table_generator(value: str, type:str, to_type:str):
    '''
    Takes a value as a string, the original type, and the type of value being converted to and prints a table to show
    the math behind the conversion 
    '''
    table = PrettyTable()
    if type == DECIMAL:
        value = int(value)
        if to_type == BINARY:
            table.field_names = ["conversion", "value", "remainder"]
            while value > 0:
                quotient = int(value/2)
                table.add_row([f"{value}/2", quotient, 1 if value % 2 != 0 else 0])
                value = quotient        
    print(f"{table}\n")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    if args.dec_to_bin:
        decimal_to_binary(args.dec_to_bin, args.table)
    
    