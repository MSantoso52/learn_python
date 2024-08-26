#! /usr/bin/sh
'''
    Hello world in OOP style
'''
class Hello:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def getName(self)->str:
        return self._name

    def getAge(self)->int:
        return self._age

    def setName(self, name):
        self._name = name

    def setAge(self, age):
        try:
            age = int(age)
            self._age = age
        except ValueError:
            print("Invalid value entered!")

    def __repr__(self):
        return f'Hello {self._name} happy pythoning at {self._age} years old!'

if __name__=='__main__':

    hello = Hello('Mulyo Santoso', 43)

    print(hello.__repr__())

    new_name = input("Enter your name: ")
    hello.setName(new_name)

    new_age = input("Enter your age: ")
    hello.setAge(new_age)

    print(hello.__repr__())

