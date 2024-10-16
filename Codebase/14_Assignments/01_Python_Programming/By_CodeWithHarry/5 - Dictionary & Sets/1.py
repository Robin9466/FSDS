hindi_english_dict = {}  # Create an empty dictionary

# Add Hindi words and their English translations
hindi_english_dict["नमस्ते"] = "Hello"
hindi_english_dict["धन्यवाद"] = "Thank you"
# ... add more words

# Get user input
hindi_word = input("Enter a Hindi word: ")

# Search the dictionary
if hindi_word in hindi_english_dict:
    english_translation = hindi_english_dict[hindi_word]
    print(f"The English translation of '{hindi_word}' is: {english_translation}")
else:
    print("Word not found in the dictionary.")