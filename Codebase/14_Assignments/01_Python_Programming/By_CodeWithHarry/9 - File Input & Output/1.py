# WAPP to read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle'

# Update the file path to point to the correct Desktop path with OneDrive
file_path = r'C:\Users\Robin Raj\oneDrive\Desktop\poem.txt'

# Open the file using the absolute path
with open(file_path, 'r') as f:
    content = f.read()
    
    # Check if the word 'twinkle' is in the content (case-insensitive)
    if 'twinkle' in content.lower():
        print("The word 'twinkle' is present in the file.")
    else:
        print("The word 'twinkle' is not present in the file.")
