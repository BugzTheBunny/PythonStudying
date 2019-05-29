#Intruduction to \t - which is a tab.

tabby_cat = "\tIm tabbed in."
persian_cat = "Im split\non a line."
backslash_cat = "Im \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass	
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat) 

#Study Drill
#Explanation - The only reason i would use triple single instead of triple double, is if there is 
#a triple quote inside the string itself.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass	
'''
print(fat_cat)
