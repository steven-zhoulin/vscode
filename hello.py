#!/usr/bin/python3

import platform

print(platform.system())
print(platform.architecture())
print(platform.machine())
print(platform.processor())
print(platform.release())
print(platform.uname())

for i in range(10):
    print("vscode: %d" % i)
