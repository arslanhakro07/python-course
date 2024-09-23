import os

# Specify the directory you want to list (use '.' for the current directory)
directory = '/'  # Change this to the path of the directory you want to list

# Get the list of files and directories
contents = os.listdir(directory)

# Print the contents
print(f"Contents of the directory '{directory}':")
for item in contents:
    print(item)
