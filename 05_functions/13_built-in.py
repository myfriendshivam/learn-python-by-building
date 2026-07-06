# Documenting your function & Built-in function
# learner built-in function throught document

def chai_flavor(flavor = "masala"):
    chai = "ginger"  # ------------> None
    """Return the flavor of chai."""
    chai = "ginger"  # ------------> fine
    return flavor

print(chai_flavor.__doc__) # Dunder -> __doc__
print(chai_flavor.__name__)

help(len)

# Python Imports, Modules and Init file
# Importing Objects/function

#  masala_chai.py ----> new_branch.py
                        #    import masala_chai.py
                        #    masala_chai.brew() 

# from masala_chai.py import brew
# brew()

# from masala_chai.py import brew as start_brewing
# start_brewing()

# from datetime import datetime
# from requests

# from chai_shop.utils import discount, calculate_tax

#  chai_business/
#       recipes/
#               flavor.py
#       utils/
#               discounts.py
# main.py

# from masala_chai import *  ---> never write like this

#   __init__.py ---> this file never need in python 3.3
# turn folder into a pyton package

# What is a benefit of using as when importing in Python?
# -> it shortens long module names