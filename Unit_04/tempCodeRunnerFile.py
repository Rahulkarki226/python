import re
txt = "Hello! World, How are you?"
print(re.findall("[\w\s]",txt))