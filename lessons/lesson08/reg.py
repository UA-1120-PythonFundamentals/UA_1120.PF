text = """SoftServe Academy Internship is an opportunity to apply all acquired practical and theoretical skills within a real project. You will fully immerse yourself in the environment of working with a team, you will understand why it is important to meet deadlines and take responsibility for your part of the work. Every project has a mentor and tech expert to guide interns through knowledge and experience. This stage is the final step before receiving a job offer. Up to 70% of graduates become SoftServe associates."""

print(text)

import re

result = re.match("SoftServe", text)
print(result)
print(result.group(0))
result = re.match("Academy", text)
print(result)

result = re.search("Academy", text)
print(result)
print(result.group(0))
result = re.search("is", text)
print(result)
print(result.group(0))
result = re.findall("is", text)
print(result)
pattern = re.compile("is")
result = pattern.findall(text)
print(result)

result = pattern.split(text)
print(result)

pattern = re.compile("[a-z]")
result = pattern.split(text)
print(result)
pattern = re.compile("\d")
result = pattern.findall(text)
print(result)
pattern = re.compile("..a....")
result = pattern.findall(text)
print(result)
pattern = re.compile("\d{2}")
result = pattern.findall(text)
print(result)
pattern = re.compile("[a-z]{2}")
result = pattern.findall(text)
print(result)