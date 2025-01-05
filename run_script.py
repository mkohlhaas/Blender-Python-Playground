import os
import sys
import easybpy as ez

scriptFile = "hello.py"

cwd = os.getcwd()
print(cwd)
# sys.path.append(cwd)
print(sys.path)
# ez.create_sphere()


# Compile and execute script file
# file = os.path.join(cwd, scriptFile)
# print(file)
# print(open(file).read())
# print(scriptFile)
# x = compile(open(file).read(), scriptFile, "exec")
