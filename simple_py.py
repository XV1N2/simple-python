import os
import subprocess

class Math():
    "simple mathematics"
    def add(self,  num1, num2):
        result = num1 + num2
        print(result)
    
    def subtraction(self,  num1, num2):
        result = num1 - num2
        print(result)
    
    def division(self,  num1, num2):
        result = num1 / num2
        print(result)
    
    def multiplication(self,  num1, num2):
        result = num1 * num2
        print(result)
    
    def modulus(self,  num1, num2):
        result = num1 % num2
        print(result)
    
    def exponentiation(self,  num1, num2):
        result = num1 ** num2
        print(result)
    
    def floor(self,  num1, num2):
        result = num1 // num2
        print(result)

class File():
    def readfile(self, path):
        "path=your path to file"
        read = open(path, "r").read()
        print(read)
    
    def createfile(self, file):
        f = open(f"{file}", "x")
        print(f"{file} created")

    def deletefile(self, file):
        os.remove(path=file)
        print(f"{file} deleted")

    def writefile(self, file, text):
        f = open(f"{file}", "w")
        f.write(text)
        print("Success writing")

def newinput(text, text1):
    result = str(text) + "".join(text1)
    print(result)

def loop(text):
    "Make infinite loop"
    while True:
        print(text)

def for_loop(time, text):
    for i in range(time):
        print(text)

def ping(domain, buffer, loop):
    if buffer == 0 and loop:
        res = subprocess.call(["ping", domain, "-t"])
    elif buffer == 0:
        res = subprocess.call(["ping", domain])
    else:
        res = subprocess.call(["ping", domain, "-t", "-l", buffer])
    return res
