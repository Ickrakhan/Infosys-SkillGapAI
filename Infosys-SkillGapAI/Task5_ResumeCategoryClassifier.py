# Task 5 - Resume Category Classifier (Simple if-elif)

skills_input = input("Enter your skills (comma-separated): ")

# Convert to lowercase list
skills = [s.strip().lower() for s in skills_input.split(",")]

# Category keywords
data_ml = ["python", "machine learning", "data analysis", "sql", "statistics", "deep learning"]
web_dev = ["html", "css", "javascript", "react", "node", "bootstrap"]
software_dev = ["java", "c++", "c#", "oop", "git", "linux", "api"]

category = "Other"   # default

for skill in skills:
    if skill in data_ml:
        category = "Data / Machine Learning"
        break
    elif skill in web_dev:
        category = "Web Development"
        break
    elif skill in software_dev:
        category = "Software Development"
        break

print("\nPredicted Resume Category:", category)
