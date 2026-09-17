import os
import shutil
with open("example.txt", "w") as setup_file:
    setup_file.write("Line 1: Welcome to Python File Handling.\n")
    setup_file.write("Line 2: This is an all-in-one cheat sheet.\n")
    setup_file.write("Line 3: Python makes it very clean to manage files.\n")
print("[System] 'example.txt' created successfully for testing.\n")


# Method A: Reading the entire file content at once into a string
with open("example.txt", "r") as file:
    entire_content = file.read()
    print("-> Method A (Entire Content):\n", entire_content)

# Method B: Reading line-by-line (Highly memory efficient for large files)
print("-> Method B (Line-by-Line loop):")
with open("example.txt", "r") as file:
    for line in file:
        # .strip() removes trailing newlines (\n) for clean terminal prints
        print("   Line Read:", line.strip())

# Method C: Reading specific single lines sequentially
print("\n-> Method C (readline):")
with open("example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print("   First line extracted: ", line1.strip())
    print("   Second line extracted:", line2.strip())
print("\n" + "="*40 + "\n")


# Mode 'w': Overwrites a file entirely or creates a fresh one if missing
with open("output.txt", "w") as file:
    file.write("This line completely overwrote the old content.\n")
    file.write("This is a secondary line in the fresh file.\n")
print("[System] Fresh 'output.txt' written successfully.")

# Mode 'a': Safely appends new lines to the bottom without erasing data
with open("output.txt", "a") as file:
    file.write("This line is appended safely at the bottom.\n")
print("[System] New line appended to 'output.txt'.")

# Writing a list of strings all at once using writelines()
line_list = ["List Line 1\n", "List Line 2\n"]
with open("output.txt", "a") as file:
    file.writelines(line_list)
print("[System] Appended list items using writelines().\n")


# Let's create a tiny dummy binary/byte array since we don't have a real image
dummy_binary_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00'

# Writing raw bytes to a file
with open("dummy_image.png", "wb") as binary_file:
    binary_file.write(dummy_binary_data)
print("[Binary] Created 'dummy_image.png' using 'wb' mode.")

# Reading raw bytes from a file and copying it to a backup file
with open("dummy_image.png", "rb") as source:
    raw_bytes = source.read()

with open("copied_image.png", "wb") as destination:
    destination.write(raw_bytes)
print("[Binary] Copied binary data to 'copied_image.png' successfully.\n")


with open("example.txt", "r") as file:
    print("Initial file cursor position:", file.tell())  # Starts at 0
    
    first_chunk = file.read(6)  # Read exactly 6 characters ("Line 1")
    print(f"Read chunk: '{first_chunk}'")
    print("File cursor position after reading:", file.tell())  # Moves to 6
    
    # Move pointer back to the beginning manually
    file.seek(0)
    print("Cursor position forced back via seek(0):", file.tell())
    
    # Read again from position 0
    print("Re-reading from position 0:", file.read(6))
print("\n" + "="*40 + "\n")


# Creating a new directory/folder safely without crashing if it exists
os.makedirs("sample_directory", exist_ok=True)
print("[OS] Directory 'sample_directory' created or verified.")

# Checking if a specific file exists before operating on it
if os.path.exists("copied_image.png"):
    print("[OS] Verified: 'copied_image.png' exists.")
    
    # Renaming a file
    os.rename("copied_image.png", "renamed_image.png")
    print("[OS] Renamed 'copied_image.png' to 'renamed_image.png'.")

# Safely cleaning up/deleting generated practice files
files_to_clean = ["dummy_image.png", "renamed_image.png"]
for target_file in files_to_clean:
    if os.path.exists(target_file):
        os.remove(target_file)
        print(f"[OS] Cleaned up and deleted file: {target_file}")