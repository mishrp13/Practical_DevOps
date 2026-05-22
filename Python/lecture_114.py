import re

text = "aaaaa"

print(re.findall(r"a", text))
print(re.findall(r"a*", text))
print(re.findall(r"a+", text))
print(re.findall(r"a{2}", text))
print(re.findall(r"a{1,3}", text))


print(f"Non-greedy a*: {re.findall(r"a*?", text)}")
print(f"Non-greedy a+: {re.findall(r"a+?",text)}")
print(f"Non-greedy a{{1,3}}?: {re.findall(r"a{1,3}?",text)}")

#------------------------------


html = "<p>One</p>Two</p><></>"

print(f"Greedy: {re.findall(r"<.*>", html)}")
print(f"Non-greedy: {re.findall(r"<.*?>", html)}")

