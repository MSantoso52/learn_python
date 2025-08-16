#Learning python repo
# *Overview*
Repository for learning python, this repo contain my 1st python code implementation OOP hello.py

# *Prerequisites*
To follow along this project you will needs:
- Python3 installed
  ```bash
  python3 --version
- Vim simple text editor
  ```bash
  vim --version
# *Project flow*
1. Create hello.py by using Vim editor:
   ```vim
   vim hello.py
2. Create class Hello to demontrate OOP in python3:
   ```vim
   class Hello:
     def __init__(self, name, age):
       self.name = name
       self.age = age
     ...

     def __repr__(self):
       return f'Hello {self._name} happy pythoning at {self._age} years old!'
3. Run hello.py on bash terminal:
   ```bash
   python3 hello.py
