# ask user for his name and remove white while capitalizing theuser's name
name = input("What's your name?").strip().title()  

#split users name into first and last name
first, last = name.split(" ")
#say hello to the user
print(f"Hello, {first}")

