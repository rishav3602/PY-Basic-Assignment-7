"""
21. How would you write a regex that matches the full name of someone whose last 
name is Watanabe? You can assume that the first name that comes before it will always
e one word that begins with a capital letter. The regex must match the following:
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:
'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)

"""

"""
Answer...
To match the full name of someone whose last name is Watanabe and the first name 
is always one word that begins with a capital letter, you can use the following 
regular expression:


This regular expression will match strings that start with a capital letter, 
followed by zero or more lowercase letters, then a whitespace character, and 
finally the last name 'Watanabe'. The ^ and $ anchors ensure that the entire 
string is matched from start to end.

This regular expression will match the following strings:

'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
But will not match the following strings:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a non-letter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)

"""