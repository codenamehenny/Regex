#1. Python Regular Expressions Deep Dive
#@Task 1: Email Extraction Enhancement
#Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). 
#Modify the script to extract all email addresses except those from the specified domain.

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)

#Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.
#(?!exclude\.com\b) was added to give flexibility in looking for exclude.com so that findall would work even if it wasn't located