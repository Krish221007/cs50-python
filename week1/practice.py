# a list of 3 fruits
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# a dictionary of my info
my_info = {"Name": "Krish", "Age": "19", "City": "Noida"}
for n in my_info:
    print(n, my_info[n], sep=": ")

# printing a 4x4 square using nested for loops
def main():
    print_square(4)

def print_square(size):
    for i in range(size):
        print("#"*size)

    

main()



    