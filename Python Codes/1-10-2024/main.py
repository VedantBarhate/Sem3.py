import re

text = "Python C Cpp Html Css JS"
pattern = r"\b\w{3}\b"

out = re.findall(pattern, text)

# if out:
#     word = out.group()
#     print(word)

print(out)

# print(out.start())
# print(out.end())