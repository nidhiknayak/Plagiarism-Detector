# Importing SequenceMatcher 
# from difflib module 
from difflib import SequenceMatcher 

# Declaring string variables 
string1 = 'purple palace'
string2 = 'purple place'

# Using the SequenceMatcher() 
match = SequenceMatcher(None, string1, string2) 

# convert above output into ratio 
# and multiplying it with 100 
result = match.ratio() * 100

# Display the final result 
print(int(result), "%") 
