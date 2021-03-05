from os import system
from py_compile import compile

print("compiler python started")
data=raw_input("file : ")
out=raw_input("output : ")
compile(data, out)
print("file saved in "+out)
