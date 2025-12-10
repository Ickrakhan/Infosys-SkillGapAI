# Task 6: Skill Frequency Checker

# Take resume paragraph input
text = input("Enter the resume text: ")

# Take skill to search
skill = input("Enter the skill to check: ")

# Convert both to lowercase
text_lower = text.lower()
skill_lower = skill.lower()

# Count occurrences
count = text_lower.count(skill_lower)

# Output
print(f"Skill '{skill}' appears {count} times.")
