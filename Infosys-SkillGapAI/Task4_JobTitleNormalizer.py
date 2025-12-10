# Task 4 - Job Title Normalizer

title = input("Enter job title:\n")

# Step 1: Remove special characters
clean_title = ""
for char in title:
    if char.isalnum() or char.isspace():     # keep letters, numbers, spaces
        clean_title += char

# Step 2: Convert to Title Case
normalized_title = clean_title.title()

print("Normalized Job Title:", normalized_title)
