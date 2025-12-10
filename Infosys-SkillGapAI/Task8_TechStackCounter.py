# Task 8: Tech Stack Counter

programming_languages = ["python", "java", "c", "c++", "javascript", "ruby", "go"]
databases = ["mysql", "postgresql", "mongodb", "oracle", "sqlite"]
frameworks = ["django", "flask", "react", "angular", "spring", "node"]

tools = input("Enter your technologies (comma-separated): ").lower().split(",")

lang_count = 0
db_count = 0
framework_count = 0

for t in tools:
    t = t.strip()
    if t in programming_languages:
        lang_count += 1
    elif t in databases:
        db_count += 1
    elif t in frameworks:
        framework_count += 1

print("\n=== Tech Stack Summary ===")
print("Programming Languages:", lang_count)
print("Databases:", db_count)
print("Frameworks:", framework_count)
