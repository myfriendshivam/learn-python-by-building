# File handling with try except

# file = open("04_order.txt", "w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()

with open("04_order.txt", "w") as file:
    file.write("ginger tea - 4 cups")

# it acctually invoked dunder file.__enter__() and then close another dunder call file.__exit__()
# with automatically call all dunder for you
