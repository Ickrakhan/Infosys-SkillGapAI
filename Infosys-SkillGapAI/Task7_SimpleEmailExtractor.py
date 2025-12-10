# Task 7: Simple Email Extractor (No Regex)

text = input("Enter the text: ")

# Split text into individual words
words = text.split()

email_found = None

for word in words:
    if "@" in word:
        email_found = word
        break

if email_found:
    print("Extracted Email:", email_found)
else:
    print("No email detected")
