# Task 3 - Experience Extractor

sentence = input("Enter a sentence with experience (example: I have 3 years of experience):\n")

# Split the sentence into words
words = sentence.split()

experience_years = None

# Look for any word that is a number
for word in words:
    if word.isdigit():      # checks if the word is a number
        experience_years = int(word)
        break

if experience_years is not None:
    print(f"Experience Detected : {experience_years} Years")
else:
    print("No numeric experience found.")
