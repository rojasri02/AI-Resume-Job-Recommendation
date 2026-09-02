import pandas as pd

# Load Job Dataset
jobs = pd.read_csv("dataset/job_dataset.csv")

# Load Resume Dataset
resumes = pd.read_csv("dataset/ml_resume_dataset_4500.csv")

print("JOB DATASET")
print(jobs.shape)
print(jobs.columns)

print("\nRESUME DATASET")
print(resumes.shape)
print(resumes.columns)
print("\nJOB DATASET INFO")
print(jobs.info())

print("\nJOB MISSING VALUES")
print(jobs.isnull().sum())

print("\nRESUME DATASET INFO")
print(resumes.info())

print("\nRESUME MISSING VALUES")
print(resumes.isnull().sum())

print("\nMISSING TITLE ROW")
print(jobs[jobs["Title"].isna()])
# Fill missing Job Title
jobs.loc[jobs["JobID"] == "AI017", "Title"] = "AI Engineer"

# Check whether Title has any missing values
print("\nMissing Title values after cleaning:")
print(jobs["Title"].isnull().sum())
# Check whether Title has any duplicates
print("\nJOB DUPLICATES:")
print(jobs.duplicated().sum())

print("\nRESUME DUPLICATES:")
print(resumes.duplicated().sum())

print("\nRESUME LABELS:")
print(resumes["label"].value_counts())

print("\nRESUME CURRENT TITLES:")
print(resumes["current_title"].value_counts().head(20))

print("\nJOB TITLES:")
print(jobs["Title"].value_counts().head(20))

print("\nSAMPLE RESUMES:")
print(resumes[["skills", "current_title", "raw_text", "label"]].head(5))

print("\nSAMPLE JOBS:")
print(jobs[["Title", "Skills", "Keywords"]].head(5))



print("\nSAMPLE RESUME SKILLS:")
print(resumes["skills"].head(10).to_string(index=False))

print("\nSAMPLE JOB SKILLS:")
print(jobs["Skills"].head(10).to_string(index=False))

print("\nSAMPLE JOB KEYWORDS:")
print(jobs["Keywords"].head(10).to_string(index=False))

# Clean Resume Skills
resumes["skills_clean"] = (
    resumes["skills"]
    .str.lower()
    .str.split(",")
    .apply(lambda x: [skill.strip() for skill in x])
)

# Clean Job Skills
jobs["skills_clean"] = (
    jobs["Skills"]
    .str.lower()
    .str.split(";")
    .apply(lambda x: [skill.strip() for skill in x])
)

print("\nCLEANED RESUME SKILLS:")
print(resumes["skills_clean"].head())

print("\nCLEANED JOB SKILLS:")
print(jobs["skills_clean"].head())


# Calculate skill match percentage
def calculate_match(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    if len(job_set) == 0:
        return 0

    matched_skills = resume_set.intersection(job_set)

    score = (len(matched_skills) / len(job_set)) * 100

    return round(score, 2)


# Test with the first resume
resume_skills = resumes.loc[0, "skills_clean"]

jobs["match_score"] = jobs["skills_clean"].apply(
    lambda job_skills: calculate_match(resume_skills, job_skills)
)

# Get Top 5 recommended jobs
top_jobs = jobs.sort_values(
    by="match_score",
    ascending=False
).head(5)

print("\nTOP 5 RECOMMENDED JOBS")
print(
    top_jobs[
        ["Title", "ExperienceLevel", "Skills", "match_score"]
    ].to_string(index=False)
)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Combine important job information
jobs["job_text"] = (
    jobs["Title"].fillna("") + " " +
    jobs["Skills"].fillna("") + " " +
    jobs["Responsibilities"].fillna("") + " " +
    jobs["Keywords"].fillna("")
)

# Use the first resume as a test
resume_text = resumes.loc[0, "raw_text"]

# Combine resume and all job texts
all_text = [resume_text] + jobs["job_text"].tolist()

# Convert text into TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(all_text)

# Compare resume with every job
similarity_scores = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:]
).flatten()

# Store similarity score
jobs["similarity_score"] = similarity_scores * 100

# Get Top 5 jobs
top_jobs = jobs.sort_values(
    by="similarity_score",
    ascending=False
).head(5)

print("\nTOP 5 NLP JOB RECOMMENDATIONS")

print(
    top_jobs[
        ["Title", "ExperienceLevel", "similarity_score"]
    ].to_string(index=False)
)


# Skill matching score
skill_scores = jobs["match_score"]

# NLP similarity score
nlp_scores = jobs["similarity_score"]

# Final weighted score
jobs["final_score"] = (
    skill_scores * 0.5 +
    nlp_scores * 0.5
)

# Top 5 final recommendations
final_recommendations = jobs.sort_values(
    by="final_score",
    ascending=False
).head(5)

print("\nFINAL JOB RECOMMENDATIONS")

print(
    final_recommendations[
        [
            "Title",
            "ExperienceLevel",
            "match_score",
            "similarity_score",
            "final_score"
        ]
    ].to_string(index=False)
)


print("\nFIRST RESUME DETAILS")

print("Skills:", resumes.loc[0, "skills"])
print("Current Title:", resumes.loc[0, "current_title"])
print("Experience:", resumes.loc[0, "years_experience"])
print("Degree:", resumes.loc[0, "highest_degree"])
print("Raw Text:", resumes.loc[0, "raw_text"])

print("\nJOB EXPERIENCE LEVELS:")
print(jobs["ExperienceLevel"].value_counts())

print("\nRESUME EXPERIENCE RANGE:")
print(resumes["years_experience"].describe())


# ==========================================
# IMPROVED FINAL JOB RECOMMENDATION SYSTEM
# ==========================================

# Get first resume
resume = resumes.loc[0]

resume_experience = resume["years_experience"]

# ------------------------------------------------
# 1. Improved Skill Matching
# ------------------------------------------------

def skill_match_score(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    if not job_set:
        return 0

    matched = resume_set.intersection(job_set)

    return (len(matched) / len(resume_set)) * 100


jobs["skill_score"] = jobs["skills_clean"].apply(
    lambda x: skill_match_score(
        resumes.loc[0, "skills_clean"],
        x
    )
)


# ------------------------------------------------
# 2. Experience Matching
# ------------------------------------------------

def experience_score(years, experience_level):
    
    level = str(experience_level).lower()

    if "fresher" in level or "entry" in level:
        required_min = 0
        required_max = 1

    elif "junior" in level:
        required_min = 1
        required_max = 3

    elif "mid" in level:
        required_min = 2
        required_max = 6

    elif "senior" in level:
        required_min = 5
        required_max = 10

    elif "lead" in level:
        required_min = 7
        required_max = 15

    elif "experienced" in level:
        required_min = 2
        required_max = 15

    else:
        required_min = 0
        required_max = 15

    if required_min <= years <= required_max:
        return 100

    # Small penalty for nearby experience
    if years < required_min:
        difference = required_min - years
    else:
        difference = years - required_max

    score = max(0, 100 - (difference * 15))

    return score


jobs["experience_score"] = jobs["ExperienceLevel"].apply(
    lambda x: experience_score(
        resume_experience,
        x
    )
)


# ------------------------------------------------
# 3. NLP Similarity
# ------------------------------------------------

# Give more importance to skills and job title
resume_text = (
    str(resume["skills"]) + " " +
    str(resume["skills"]) + " " +
    str(resume["current_title"]) + " " +
    str(resume["highest_degree"])
)

jobs["recommendation_text"] = (
    jobs["Title"].fillna("") + " " +
    jobs["Skills"].fillna("") + " " +
    jobs["Skills"].fillna("") + " " +
    jobs["Keywords"].fillna("")
)

all_text = [resume_text] + jobs["recommendation_text"].tolist()

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

tfidf_matrix = vectorizer.fit_transform(all_text)

similarity_scores = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:]
).flatten()

jobs["nlp_score"] = similarity_scores * 100


# ------------------------------------------------
# 4. FINAL WEIGHTED SCORE
# ------------------------------------------------

jobs["final_score"] = (
    jobs["skill_score"] * 0.60 +
    jobs["nlp_score"] * 0.25 +
    jobs["experience_score"] * 0.15
)


# ------------------------------------------------
# 5. TOP 5 RECOMMENDATIONS
# ------------------------------------------------

final_recommendations = jobs.sort_values(
    by="final_score",
    ascending=False
).head(5)

print("\n==========================================")
print("FINAL JOB RECOMMENDATIONS")
print("==========================================")

print(
    final_recommendations[
        [
            "Title",
            "ExperienceLevel",
            "skill_score",
            "nlp_score",
            "experience_score",
            "final_score"
        ]
    ].to_string(index=False)
)


# ==========================================
# IMPROVED SKILL + KEYWORD MATCHING
# ==========================================

def get_combined_skills(job_row):
    skills = str(job_row["Skills"]).lower().split(";")
    keywords = str(job_row["Keywords"]).lower().split(";")

    combined = set()

    for item in skills + keywords:
        item = item.strip()
        if item:
            combined.add(item)

    return combined


# Create combined job skills
jobs["combined_skills"] = jobs.apply(
    get_combined_skills,
    axis=1
)


# Calculate skill + keyword score
def combined_match(resume_skills, job_skills):

    resume_set = set(resume_skills)

    if not job_skills:
        return 0

    matched = resume_set.intersection(job_skills)

    return (len(matched) / len(resume_set)) * 100


jobs["combined_skill_score"] = jobs["combined_skills"].apply(
    lambda x: combined_match(
        resumes.loc[0, "skills_clean"],
        x
    )
)


# New final score
jobs["improved_score"] = (
    jobs["combined_skill_score"] * 0.65 +
    jobs["nlp_score"] * 0.20 +
    jobs["experience_score"] * 0.15
)


# Sort by score
sorted_jobs = jobs.sort_values(
    by="improved_score",
    ascending=False
)


# Keep different job titles
recommendations = sorted_jobs.drop_duplicates(
    subset=["Title"]
).head(5)


print("\n==========================================")
print("TOP 5 IMPROVED JOB RECOMMENDATIONS")
print("==========================================")

print(
    recommendations[
        [
            "Title",
            "ExperienceLevel",
            "combined_skill_score",
            "nlp_score",
            "experience_score",
            "improved_score"
        ]
    ].to_string(index=False)
)