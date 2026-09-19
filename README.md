🤖 AI Resume Job Recommendation System

An AI-powered web application that analyzes a candidate's resume and provides personalized job recommendations based on skills, experience, education, and career profile.

The system extracts important information from an uploaded resume, calculates a resume score, identifies relevant career fields, recommends suitable jobs, and highlights potential skill gaps.

---

📌 Project Overview

Finding suitable job opportunities from a resume can be difficult when there are many different job roles and requirements.

The AI Resume Job Recommendation System helps simplify this process by analyzing a candidate's resume and matching the detected skills with available job opportunities.

The application provides:

- Resume analysis
- Resume scoring
- Skill extraction
- Education and experience detection
- Career field identification
- Job recommendations
- Job match percentage
- Job details
- Skill gap analysis
- Career insights
- Resume history
- Saved job recommendations
- Candidate profile

---

✨ Key Features

📄 Resume Upload

Upload a resume in PDF or DOCX format for analysis.

The system extracts the text from the uploaded resume and processes the information automatically.

🔍 Resume Analysis

The application analyzes the resume and identifies:

- Candidate name
- Education
- Experience
- Skills
- Career field
- Resume score

📊 Resume Score

A resume score is calculated based on factors such as:

- Candidate information
- Education
- Experience
- Number of detected skills
- Resume content
- Projects
- Certifications

The score is presented as a percentage to give the candidate an overview of the detected resume information.

🧠 Skill Extraction

The system detects technical and professional skills from the resume.

Some supported skills include:

- Python
- Java
- C
- C++
- SQL
- HTML
- CSS
- JavaScript
- React
- Flask
- Django
- Machine Learning
- Deep Learning
- Artificial Intelligence
- Data Science
- Data Analysis
- Pandas
- NumPy
- Scikit-learn
- TensorFlow
- NLP
- Statistics
- Excel
- Power BI
- AWS
- Azure
- Git
- GitHub

💼 Job Recommendation

The system compares the candidate's detected skills with available job requirements and recommends relevant job opportunities.

Each recommendation provides information such as:

- Job title
- Company
- Location
- Salary
- Experience
- Job type
- Required skills
- Job description
- Education requirement
- Resume match percentage

🎯 Job Match Percentage

The application calculates how closely the candidate's detected skills match the skills required for each job.

Matched skills are also displayed to help the candidate understand why a job is relevant.

📋 Job Details

Candidates can open individual job recommendations and view detailed information about:

- Job title
- Company
- Location
- Salary
- Experience requirement
- Job type
- Required skills
- Description
- Education
- Matched skills
- Resume match percentage

📈 Skill Gap Analysis

The system identifies skills detected in available job requirements that are not currently detected in the candidate's resume.

This helps candidates understand potential areas for skill development.

💡 Career Insights

The application provides career-related insights based on the candidate's detected:

- Career field
- Skills
- Resume score
- Recommended jobs

🗂️ Resume History

The application maintains a history of previously analyzed resumes during the application session.

The system stores information such as:

- Candidate name
- Resume filename
- Resume score
- Skills
- Education
- Experience
- Career field

The latest 20 resume analyses are retained.

🔖 Saved Jobs

The application provides a saved-jobs section based on the generated job recommendations, allowing recommended opportunities to be viewed again.

👤 Candidate Profile

The profile page displays the candidate's analyzed resume information, including:

- Name
- Education
- Experience
- Career field
- Skills
- Resume score
- Resume filename

---

🛠️ Technologies Used

Frontend

- HTML5
- CSS3
- Responsive Web Design

Backend

- Python
- Flask

Data Processing

- Pandas
- NumPy

Machine Learning / NLP

- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Skill-based matching

Resume Processing

- PyPDF
- python-docx

Dataset

- Job Dataset
- Resume Dataset

---

🧠 Recommendation Approach

The project uses multiple factors to identify suitable job opportunities.

1. Skill Matching

The candidate's detected skills are compared with the skills required by each job.

2. Experience Matching

The candidate's experience is compared with different job experience levels such as:

- Fresher / Entry Level
- Junior
- Mid Level
- Senior
- Lead
- Experienced

3. Text Similarity

The system uses TF-IDF vectorization and cosine similarity to compare resume-related information with job-related information.

4. Combined Recommendation

The recommendation system considers skill matching, experience compatibility, and text similarity to generate relevant job recommendations.

---

🔄 System Workflow

             ┌─────────────────────┐
             │   Upload Resume      │
             │    PDF / DOCX        │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Extract Resume Text │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Resume Analysis     │
             │                     │
             │ • Name              │
             │ • Education         │
             │ • Experience        │
             │ • Skills            │
             │ • Career Field      │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Calculate Resume    │
             │ Score               │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Job Matching        │
             │                     │
             │ • Skills            │
             │ • Experience        │
             │ • Text Similarity   │
             └──────────┬──────────┘
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
    ┌──────────────────┐   ┌──────────────────┐
    │ Job Recommendations│   │ Skill Gap        │
    │                  │   │ Analysis         │
    └─────────┬────────┘   └──────────────────┘
              │
              ▼
    ┌──────────────────────┐
    │ Job Details & Career │
    │ Insights             │
    └──────────────────────┘

---

🖥️ Application Pages

The application contains the following main pages:

Page| Description
Home| Introduction to ResumeAI
About| Information about the application
Upload Resume| Upload PDF/DOCX resume
Analysis| Display extracted resume information
Jobs| Display recommended jobs
Job Details| Display detailed information about a selected job
Skill Gap| Show missing or potentially useful skills
Dashboard| Resume summary and recommendations
Career Insights| Career-related information
Resume History| Previously analyzed resume records
Saved Jobs| Display saved/recommended jobs
Profile| Display analyzed candidate profile

---

📸 Screenshots

🏠 Home Page

"Home Page" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/home%201.png)

📄 Resume Upload

"Resume Upload" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/Resume%20Upload%202.png)

📊 Resume Analysis

"Resume Analysis" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/Resume%20Analysis%203.png)

💼 Job Recommendations

"Job Recommendations" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/Job%20recommendations%204.png)

💼 Job Recommendations

"Job Recommendations" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/Job%20recommendations%205.png)

🎯 Skill Gap Analysis

"Skill Gap Analysis" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/Skill%20Gap%20analysis%206.png)

📊 Dashboard

"Dashboard" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/Dashboard%207.png)

💡 Career Insights

"Career Insights" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/carrer%20insights%208.png)

🗂️ Resume History

"Resume History" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/Resume%20history%209.png)

💾 Saved Jobs

"Saved jobs" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/Saved%20jobs%2010.png)

💾 Saved Jobs

"Saved Jobs" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/saved%20jobs%2011.png)

👤 Profile

"Profile" (https://github.com/rojasri02/AI-Resume-Job-Recommendation/blob/main/Ai%20resume%20screenshots/profile%2012.png)


---

🎥 Demo Video

Watch the complete project demonstration:

"▶️ Watch AI Resume Job Recommendation System Demo" (https://drive.google.com/file/d/1PkLHA-SxIz3uCValRB3CV4naHlpWo4Sp/view?usp=sharing)

---

📑 Project Report

The complete project documentation is available here:

📘 AI Resume Job Recommendation – (https://drive.google.com/file/d/17y56yniec7jWlnGDrnTNbzMB9oGxlqK0/view?usp=sharing)

The report contains:

1.Abstract
2.Introduction
3.Problem Statement
4.Objectives
5.Existing System
6.Proposed System
7.System Requirements
8.Technologies Used
9.System Architecture
10.Modules
11.Dataset Description
12.Methodology
13.Implementation
14.Results
15.Advantages
16.Limitations
17.Future Enhancements
18.Conclusion
19.References

---

📑 Research Paper

The research paper for this project is available here:

📄 AI Resume Job Recommendation – (https://drive.google.com/file/d/1ftYlG5rgrVqxxuzDD_QaJs7tuup7gYGf/view?usp=sharing)

The paper discusses:

🔬 Problem definition
🧠 Proposed methodology
🤖 NLP-based recommendation
📊 Dataset
⚙️ System architecture
🎯 Recommendation process
📈 Output discussion
⚠️ Limitations
🚀 Future enhancements

---

🖼️ Project Poster

"Project Poster" (assets/project-poster.png)

---

📂 Project Structure

AI-Resume-Job-Recommendation/
│
├── app.py
│
├── dataset/
│   ├── job_dataset.csv
│   └── ml_resume_dataset_4500.csv
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── upload.html
│   ├── analysis.html
│   ├── dashboard.html
│   ├── jobs.html
│   ├── job_details.html
│   ├── skill_gap.html
│   ├── career_insights.html
│   ├── resume_history.html
│   ├── saved_jobs.html
│   └── profile.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── screenshots/
│   ├── home.png
│   ├── upload.png
│   ├── analysis.png
│   ├── dashboard.png
│   ├── jobs.png
│   ├── job_details.png
│   ├── skill_gap.png
│   ├── career_insights.png
│   ├── resume_history.png
│   └── profile.png
│
├── assets/
│   └── project-poster.png
│
├── requirements.txt
├── test.py
└── README.md

---

⚙️ Installation

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_LINK

2. Navigate to the Project Folder

cd AI-Resume-Job-Recommendation

3. Create a Virtual Environment

python -m venv venv

4. Activate the Virtual Environment

Windows

venv\Scripts\activate

5. Install Dependencies

pip install -r requirements.txt

---

▶️ How to Run

Start the Flask application:

python app.py

The application will run locally.

Open the URL displayed in the terminal in your web browser.

---

📊 Datasets

The project uses two datasets.

Job Dataset

Contains information related to job opportunities, including:

- Job ID
- Job title
- Experience level
- Years of experience
- Skills
- Responsibilities
- Keywords

Resume Dataset

Contains resume-related information including:

- Resume ID
- Candidate name
- Years of experience
- Highest degree
- Skills
- Current title
- Portfolio information
- Raw resume text
- Label

---

🧪 Testing

The project includes a "test.py" file for checking and analyzing the datasets.

The testing process includes:

- Dataset shape
- Dataset columns
- Missing values
- Duplicate records
- Resume labels
- Job titles
- Resume skills
- Job skills
- Skill matching
- TF-IDF similarity
- Cosine similarity
- Job recommendation scores

---

🚀 Future Enhancements

Possible future improvements include:

- Advanced resume parsing
- More job categories
- Larger job datasets
- Improved NLP-based matching
- Personalized career recommendations
- Real-time job API integration
- User authentication
- Database-based resume history
- Cloud deployment
- Advanced skill recommendations
- Learning-resource recommendations for missing skills

---

🎯 Project Objectives

The main objectives of this project are:

1. Automate basic resume information extraction.
2. Identify skills and career fields from resumes.
3. Calculate an informative resume score.
4. Match candidate skills with job requirements.
5. Recommend relevant job opportunities.
6. Identify potential skill gaps.
7. Provide useful career-related insights through a web interface.

---

👩‍💻 Author

Rojasri K

B.Tech Information Technology Student

Aspiring Machine Learning Engineer

---

⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---
