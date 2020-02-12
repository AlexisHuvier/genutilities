import os

text = ""
direct = os.path.dirname(os.path.abspath(__file__))
for i in os.listdir(direct):
    if i not in ["launch_tests.py"] and i.endswith(".py"):
        text += direct + "\\" + i + " "
os.system("python -m unittest -v "+text[:-1])