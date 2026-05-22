import re

line = "WARN: Disk usage at 91%"
pattern = r"WARN"

print(f"search '{pattern}':", bool(re.search(pattern, line)))
print(f"search '{pattern}':", bool(re.match(pattern, line)))


#-------------------------------------------

test= "ERROR code: E1234. cxge"

print(f"Dot matches any character: {re.findall(r"c..e",test)}")
print(f"Start anchor (finds): {re.findall(r"^Error",test)}")
print(f"Start anchor (does not find): {re.findall(r"^E1234", test)}")
print(f"End anchor: {re.findall(r"cxge$", test)}")
print(f"Character set: {re.findall(r"[E0-9]+", test)}")

#----------------------------------------------------

text = "The cat scattered 1024 catalogues"


print(f"Digits: {re.findall(r"\d+", text)}")
print(f"word characters: {re.findall(r"\w+", text)}")
print(f"whitespace: {re.findall(r"\bcat\b", text)}")










