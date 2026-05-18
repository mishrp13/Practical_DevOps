from pathlib import Path

course_parent= Path(".")

for i, child in enumerate(course_parent.iterdir()):
    print(f" {child.name}: {child.is_dir()}")
    if i>=4: break


print("Python files recursively: ")

for i , child in enumerate(course_parent.glob("**/*.py")):
    print(f"{child}")
    if i>=10: break

#-----------------------------------------------------
test_file= Path("demo.txt")
test_file.write_text("Hello , from Pathlib", encoding="utf-8")
print(f"Readback: {test_file.read_text(encoding="utf-8")}")

with test_file.open(mode="a", encoding="utf-8" ) as file:
    file.write("\nAppended line!")

print(f"Read back: {test_file.read_text(encoding="utf-8")}")

test_file.unlink()









