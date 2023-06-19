class Candidate:
    def __init__(self, name, experience, skills):
        self.name = name
        self.experience = experience
        self.skills = skills

class Job:
    def __init__(self, title, required_experience, required_skills):
        self.title = title
        self.required_experience = required_experience
        self.required_skills = required_skills

def find_matching_candidates(job, candidates):
    matching_candidates = []
    for candidate in candidates:
        if (candidate.experience >= job.required_experience and
                all(skill in candidate.skills for skill in job.required_skills)):
            matching_candidates.append(candidate)
    return matching_candidates

# Get job details from the user
job_title = input("Enter the job title: ")
required_experience = int(input("Enter the required experience (in years): "))
required_skills = input("Enter the required skills (comma-separated): ").split(",")

# Create the job object
job = Job(job_title, required_experience, [skill.strip() for skill in required_skills])

# Get candidate details from the user
candidates = []
num_candidates = int(input("Enter the number of candidates: "))
for i in range(num_candidates):
    print(f"\nEnter details for candidate {i+1}:")
    candidate_name = input("Enter candidate name: ")
    candidate_experience = int(input("Enter candidate experience (in years): "))
    candidate_skills = input("Enter candidate skills (comma-separated): ").split(",")
    candidate = Candidate(candidate_name, candidate_experience, [skill.strip() for skill in candidate_skills])
    candidates.append(candidate)

# Find matching candidates
matching_candidates = find_matching_candidates(job, candidates)

# Print the matching candidates
print("\nMatching candidates for the job:", job.title)
if len(matching_candidates) > 0:
    for candidate in matching_candidates:
        print(candidate.name)
else:
    print("No matching candidates found.")


