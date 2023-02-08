from time import sleep

print("Hello operator, what is your name?")
myName = input()
print("Welcome," + myName)
print("The length of your name is:")
print(len(myName))
print("what is your age?")
my_age = input()
print("You will be " + str(int(my_age) + 1) + " in a year")
sleep(20) #window won't close for 20 seconds
