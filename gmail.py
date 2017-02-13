import re
r=re.match('\w+@\w+.\w+','abc@gmail.com')
c=r.group()
print(c)
