from pathlib import Path

sample= Path("read_demo.txt")
sample.write_text("Firstline\nSecondline\nThirdline\n")

print("Iteration for reading")
with sample.open(mode="r",encoding="utf-8") as file:
    for line in file:
        print(f" -> {line.strip()}")

print("read() for reading: ")

with sample.open(mode="r", encoding="utf-8") as file:
    print(file.read())

print("readline() for reading: ")

with sample.open(mode="r",encoding="utf-8") as file:
    print(file.readline())

print("readlines() for reading")

with sample.open(mode="r", encoding="utf-8") as file:
    print(file.readlines())

 #---------------------------------------------------------------- 

#

write_demo= Path("write_demo.txt")

with write_demo.open(mode="w", encoding="utf-8") as file:
    file.write("lineA\n")
    file.write("lineB\n")


lines_to_write = [
    "user,ip,role",
    "alice,10.0.0.0,admin",
    "bob,10.0.0.1,dev",
    "charlie,10.0.02,audit"
]   

with write_demo.open(mode="w", encoding="utf-8") as file:
    file.writelines(f"{line}\n" for line in lines_to_write)
