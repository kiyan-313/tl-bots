import re
text="سلام من جمال هستم شماره ام 09039454225است ایمیلم samoraiitanha@gmail.com هست"
phone_pattern=r'09\d{9}'
phone=re.findall(phone_pattern,text)
print("شماره موبایل:",phone)


email_pattern=r"\w+@\w+\.\w+"
email=re.findall(email_pattern,text)
print("ایمیل:",email)
