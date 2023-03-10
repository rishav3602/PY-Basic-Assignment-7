"""
4. From a Match item, how do you get the actual strings that match the pattern?
"""

"""
Answer...

Import the regex module with import re.
Create a Regex object with the re.compile() function.(pass raw string)
Pass the string you want to search into the Regex object’s search() method. 
This returns a Match object.
Call the Match object’s group() method to return a string of the actual matched text.

"""