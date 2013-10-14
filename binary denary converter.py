#Daniel Rees
#14/10/213
#Binary Denary converter

print("This program will convert any 8-BIT binary number to its Denary equivalent. ")
exityn = False

while not exityn:
    binary_error=True
    while binary_error:
        binary_number= input("Please enter the 8-BIT Binary number you wish to convert: ")
        original_binary_nunber= binary_number

        if len(binary_number) >=1 and len(binary_number) <=8:
            binary_error=False
        elif binary_number [0] != "0" or binary_number [0] != "1":
            binary_error=True
            print("-ERROR- Binary word is incorrect, only use Base 2 Values")
        else:
            binary_error=True
            print("-ERROR- Binary word is of incorrect length! ")

        print("Error checking passed. ")

    
