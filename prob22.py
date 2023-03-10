"""
22. How would you write a regex that matches a sentence where the first 
word is either Alice, Bob, or Carol; the second word is either eats, pets, 
or throws; the third word is apples, cats, or baseballs; and the sentence 
ends with a period? This regex should be case-insensitive. It must match the following:
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:
'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'

"""

"""
Answer...
To match a sentence where the first word is either Alice, Bob, or Carol; the second 
word is either eats, pets, or throws; the third word is either apples, cats, or 
baseballs; and the sentence ends with a period in a case-insensitive way, you can 
use the following regular expression:

This regular expression will match the following strings:

'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
But will not match the following strings:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.' (which has a number in the sentence)

"""