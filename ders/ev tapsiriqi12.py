website = 'http://www.google.com'
course = 'Our course is best in the World, STEP IT ACADEMY Azerbaijan'
"""tapsiriq1"""
a='Hello programmers'
a = a[:6] + "P" + a[7:]
print(a)
"""tapsiriq2"""
rep=""
s ="qwertyuiqwopzercdscgnvxbhgmjlma"
for i in s:
      if s.count(s[s.find(i)])>1 and not rep==i:
            print(i)
            rep+=i
"""tapsiriq3"""
a = ' Hello World '
print(a.strip(),end="")
print("check")
"""tapsiriq4"""
print(course.lower())
"""tapsiriq5"""
if website.startswith("www") or website.startswith("http://www") or website.startswith("://www") and website.endswith("com"):
      print("yes")
else:
      print("no")