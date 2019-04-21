import re
line="I love python"
count=len(re.findall(r'\w+',line))
print(count)
