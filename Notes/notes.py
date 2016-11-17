#                _   _                               _            
#    _ __  _   _| |_| |__   ___  _ __    _ __   ___ | |_ ___  ___ 
#   | '_ \| | | | __| '_ \ / _ \| '_ \  | '_ \ / _ \| __/ _ \/ __|
#   | |_) | |_| | |_| | | | (_) | | | | | | | | (_) | ||  __/\__ \
#   | .__/ \__, |\__|_| |_|\___/|_| |_| |_| |_|\___/ \__\___||___/
#   |_|    |___/                                                  


#you can search of items in a string:
#   stirng_to_search.find(x)

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

#text = "all tip files are tipped" #test string to find no zips

# ENTER CODE BELOW HERE
zip1 = text.find("zip")
text_2 = text[zip1 + 1:]
#print text_2.find("zip",zip1 +1) #this did not work because there is no need for a second string definition.

print text.find("zip",zip1 + 1)

print 
# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function

#there is an alternative way to solve this problem with out adding
#a variable

# note you can add the starting parameter after the search term in find.

print text.find("zip",text.find("zip") + 1)
