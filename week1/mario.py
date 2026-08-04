#lets try to create a visual representaion of a mario block
for _ in range(0):
    print("#")

#lets define a func for the same just to have a diff approach
#and also make it more reusable
def main():
    print_coloumn(0)


def print_coloumn(height):
    for _ in range(height):
        print("#")

main()

#for the func we can rather write:
def print_coloumn(height):
    print("#\n"*height, end="")


#lets try to create the "question mark" block from mario
def main():
    print_row(0)

def print_row(width):
    print("?"*width)


main()  

#lets try to create a square block 
def main():
    print_square(3)


def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")

        print()  # Moves to the next line after each row) 


main()

#same with a diff approach for a shorter code
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#"*size)

main()
