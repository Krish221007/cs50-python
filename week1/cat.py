#using the 'while' loop
i = 0
while i <= -1:
    print ("meow")
    i = i+1


# using the 'for' loop
# this one is lil better
for _ in range(0):
    print ("meow") 
# ' _ ' here is just a variable, any other can be used here too



# we could have just used this: for the same result
print (f"meow\n"*0, end="")



#lets ask the user how many times they want to "meow" 
while True:
    n = int(input("How many times do you want to meow? "))
    if n>0:
        break

for _ in range (n):
    print ("meow")

 # more in meow.py using meow as a proper function