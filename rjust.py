#The four values(Decimal,Octal,HexaDecimal,Binary) must be printed on a single line in the order specified above for each i from 1 to number . 
# Each value should be space-padded to match the width of the binary value of number and 
# the values should be separated by a singl
def print_numbers(number):
    width=len(bin(number)[2:])    # slicing of binary number in order to find the length.so that,we can maintain the space-padded b/w numbers
    for i in range(1,number+1):
        print(
            str(i).rjust(width), #why str? because rjust() works on string .
            oct(i)[2:].rjust(width),
            hex(i)[2:].upper().rjust(width),   #rjust(width) maintain the space .start numbering with right side.
            bin(i)[2:].rjust(width)
        )
num=int(input("Enter any number:"))
print_numbers(num)