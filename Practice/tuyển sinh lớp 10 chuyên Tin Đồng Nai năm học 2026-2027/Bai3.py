e = input()
s = e.upper()
a = s.count("D")
b = s.count("N")

if a>b:
    print("D")
elif a<b:
    print("N")
else:
    print("H")