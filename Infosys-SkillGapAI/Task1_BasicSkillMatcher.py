# Task 1 - Basic Skill Matcher

resume = input("Enter your resume skills (comma-separated): ")
job = input("Enter job required skills (comma-separated): ")

# Convert to lists
resume_list = resume.lower().split(",")
job_list = job.lower().split(",")

# Remove extra spaces
resume_list = [s.strip() for s in resume_list]
job_list = [s.strip() for s in job_list]

# Matching , Missing
matched = []
missing = []

for skill in job_list:
    if skill in resume_list:
        matched.append(skill)
    else:
        missing.append(skill)

print("\nMatched Skills:", matched)
print("Missing Skills:", missing)
