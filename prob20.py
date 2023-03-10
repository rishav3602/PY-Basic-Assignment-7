"""
20. How would you write a regex that match a number with comma for every three digits? 
It must match the given following:
'42'
'1,234'
'6,368,745'
but not the following:
'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)

"""

"""
Answer...
^\d{1,3}(,\d{3})*$
This regular expression will match strings that start with one to three digits,
followed by zero or more groups of a comma and three digits. The ^ and $ anchors 
ensure that the string starts and ends with a matching pattern, respectively.

This regular expression will match the following strings:

'42'
'1,234'
'6,368,745'
But will not match the following strings:

'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)


"""