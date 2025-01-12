"""
In Python, the == operator is used to compare the values of two objects,
while the is operator 'is' used to compare the identity of two objects.
When comparing strings using ==, you are comparing their values (contents),
whereas when using is, you are comparing their identities (memory addresses).
"""
str1 = "hello"
str2 = "hello"

print(str1 is str2)  # True, because Python interns the string "hello"
print(str1 == str2)  # True, values are the same

str3 = "world"
str4 = "world"

print(str3 is str4)  # True, Python interns "world" as well
print(str3 == str4)  # True, values are the same

str5 = "hello, world"
str6 = "hello, world"

print(str5 is str6)  # False, Python doesn't intern longer strings ?????
print(str5 == str6)  # True, values are the same
