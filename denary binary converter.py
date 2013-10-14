#Daniel Rees
#11/10/13
#Stretch and challenge excersise (iteration)
#"Write a program which will convert a given denary number up to 255 into its 8-bit binary equivalent."

print("This program will convert any denary number from 1 to 255 \nto its corresponding 8-BIT Binary word.")
exityn=True

while exityn:

    number_to_convert = None
    number_to_convert_error=True

    while number_to_convert_error:
        print()
        number_to_convert= int(input("Please enter a number between 1 and 255: "))
        o_number_to_convert= number_to_convert #Saving original number in variable so it can be used later in the script
        if number_to_convert <= 255 and number_to_convert >= 1:
            number_to_convert_error=False
        else:
            number_to_convert_error=True
            print("-ERROR- Number not in range. ")

    binary1 = (number_to_convert-128)
    if binary1 <0:
        binary1 = 0
    else:
        binary1 = 1
        number_to_convert= number_to_convert-128
    #minus number from 128

    binary2 = (number_to_convert-64)
    if binary2 <0:
        binary2 = 0
    else:
        binary2 = 1
        number_to_convert= number_to_convert-64
    #minus number from 64

    binary3 = (number_to_convert-32)
    if binary3 <0:
        binary3 = 0
    else:
        binary3 = 1
        number_to_convert= number_to_convert-32
    #minus number from 32

    binary4 = (number_to_convert-16)
    if binary4 <0:
        binary4 = 0
    else:
        binary4 = 1
        number_to_convert= number_to_convert-16
    #minus number from 16

    binary5 = (number_to_convert-8)
    if binary5 <0:
        binary5 = 0
    else:
        binary5 = 1
        number_to_convert= number_to_convert-8
    #minus number from 8

    binary6 = (number_to_convert-4)
    if binary6 <0:
        binary6 = 0
    else:
        binary6 = 1
        number_to_convert= number_to_convert-4
    #minus number from 4

    binary7 = (number_to_convert-2)
    if binary7 <0:
        binary7 = 0
    else:
        binary7 = 1
        number_to_convert= number_to_convert-2
    #minus number from 2

    binary8 = (number_to_convert-1)
    if binary8 <0:
        binary8 = 0
    else:
        binary8 = 1
        number_to_convert= number_to_convert-1
    #minus number from 1

    print()
    print("{0:2>} ->".format(o_number_to_convert))
    print("  128  64   32   16   08   04   02   01  ")
    print("  {0}    {1}    {2}    {3}    {4}    {5}    {6}    {7}".format(binary1, binary2, binary3, binary4, binary5, binary6, binary7, binary8))
    print()
    print("{0} is {1}{2}{3}{4} {5}{6}{7}{8} in 8-BIT Binary.".format(o_number_to_convert, binary1, binary2, binary3, binary4, binary5, binary6, binary7, binary8 ))

    yn=input("Would you like to convert another number to it's 8-BIT binary equivalent? y/n: ")
    if yn == "y" or yn == "yes":
        exityn=True
    else:
        exityn=False


input("Press enter to exit")
