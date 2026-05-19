import pathlib
from pathlib import Path

try:

    with open("config.txt", "w", encoding="utf-8") as file:
        file.write("Setting=value\n")
        file.write("another=value\n")

    with open("config.txt", "r", encoding="utf-8") as file:
        contents= file.read()
        print("contents of file")
        print(contents)

except OSError as e:
    print(f"Error: {e}")


#-----------------------------------------------------

path = Path("demo.txt")

with path.open(mode="w", encoding="utf-8") as file:
    file.write("Initial line\n")

with path.open(mode="a", encoding="utf-8") as file:
    file.write("Appended line\n")


try:

    with path.open(mode="x", encoding="utf-8") as file:
        file.write("This will execute if the file does not exist")
except FileExistsError as e:
    print(f"Error : {e}")