# str to char array
str = "abc"
to_array = list(str)
print(to_array)
# char array to str
str2 = "".join(to_array)
print(str2)
# str concatenate
a = "a"
b = "b"
c = "c"
ab = a.join(b)
# dont use '+' because its proved to  be costly, use .join() instead
