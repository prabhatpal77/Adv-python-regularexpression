# The groupof regular expression charectors which are represent in " " and preceeded by r charactor
# is recognized by the python interpretor as a regular expression patter.
import re
regex=r"[a-zA-Z]+\d+"
matches=re.findall(regex, """June24, August9, Dec12, 12Feb""")
for match in matches:
    print("Full match:",match)
