import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())  # removes extra newline spaces
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python read_file.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    read_file(file_path)

if __name__ == "__main__":
    main()