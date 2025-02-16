def string_reverse(s):
    if s=="":
        return s
    else:
        return string_reverse(s[1:])+s[0]

string=input()
print(string_reverse(string))
