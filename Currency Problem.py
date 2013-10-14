#Daniel Rees
#16/9/13
#Currency problem

firstnumber = int(input("please enter an integer: "))

twenties = firstnumber//20
remainder = firstnumber%20

print ("You can have {0} twenty pound note(s), ".format(twenties))

tens = remainder//10
remainder = remainder%10

print ("and {0} ten pound note(s), ".format(tens))

fives = remainder//5
remainder = remainder%5

print ("and {0} five pound note(s), ".format(fives))

twos = remainder//2
remainder = remainder%2

print ("and {0} two pound coin(s), ".format(twos))

ones = remainder//1
remainder= remainder%1

print ("and {0} one pound coin(s). ".format(ones))

input ("press enter to exit") 
