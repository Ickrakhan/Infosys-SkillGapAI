# Task 2 - Resume Word Matcher 

resume_text = input("Enter your resume text paragraph:\n")

# Convert everything to lowercase
text = resume_text.lower()

# Split into words
words = text.split()

# Count total words
total_words = len(words)

# Count unique words
unique_words = len(set(words))

# Find most repeated word
word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

# Get the word with the maximum count
most_repeated = max(word_count, key=word_count.get)
most_repeated_count = word_count[most_repeated]

print("\n=== Resume Word Analysis ===")
print("Total Words:", total_words)
print("Unique Words:", unique_words)
print("Most Repeated Word:", most_repeated)
print("Repeated:", most_repeated_count, "times")
