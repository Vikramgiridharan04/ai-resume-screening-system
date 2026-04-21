# AI Resume Screening System

## Smart Resume Filtering Using Machine Learning & NLP

AI Resume Screening System is a web-based recruitment tool that helps HR teams and recruiters automatically rank resumes based on a given job description.

Instead of manually reviewing hundreds of resumes, this system uses Natural Language Processing (NLP) and Machine Learning techniques such as **Text Cleaning, TF-IDF Vectorization, and Cosine Similarity** to identify the most relevant candidates quickly and accurately.

---

## Live Problem This Project Solves

Recruiters often face:

* Too many resumes for one opening
* Manual screening takes hours
* Strong candidates get missed
* No clear ranking process
* Skill mismatch between JD and resumes

This project solves that by automating first-level resume filtering.

---

## Key Features

### Resume Upload & Parsing

* Upload multiple resumes in PDF format
* Automatically extracts text from resumes

### Job Description Matching

* Paste any job description
* Compares resumes against JD

### Intelligent Ranking

* Scores resumes using similarity percentage
* Displays top candidates first

### Skill Extraction

* Detects common technical skills from resumes

### Missing Skills Analysis

* Shows which required skills are missing

### Clean Web Interface

* User-friendly Flask web application

---

## Tech Stack

### Backend

* Python
* Flask

### Machine Learning / NLP

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* Text Preprocessing

### File Processing

* PDFPlumber
* Docx2txt

### Frontend

* HTML
* CSS
* Bootstrap (optional upgrades)

---

## Machine Learning Concepts Used

### Text Cleaning

Removes punctuation, stopwords, unwanted symbols.

### Tokenization

Breaks sentences into meaningful words.

### TF-IDF

Measures important keywords in resumes and JD.

### Cosine Similarity

Calculates similarity score between resume and job description.

---

## Folder Structure

```bash
ai-resume-screening-system/
│── app.py
│── requirements.txt
│── .gitignore
│── templates/
│   └── index.html
│── utils/
│   ├── cleaner.py
│   ├── matcher.py
│   ├── parser.py
│   └── skills.py
│── static/
```

## Installation & Run Locally

```bash
git clone https://github.com/Vikramgiridharan04/ai-resume-screening-system.git
cd ai-resume-screening-system

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## Example Workflow

1. Paste Job Description
2. Upload Candidate Resumes
3. Click Analyze
4. Get Ranked Candidates
5. Review Skills & Gaps

---

## Future Improvements

* BERT / Transformer based matching
* ATS Score Prediction
* Resume Category Classification
* Candidate Dashboard
* Email Shortlisting
* Resume Summarization using LLMs
* Cloud Deployment

---

## Why This Project Matters

This project demonstrates real-world skills in:

* Machine Learning
* NLP
* Python Development
* Flask Web Apps
* Problem Solving
* HR Tech Automation

---

## Author

**Vikram Giridharan**
Aspiring ML / AI Developer focused on building practical AI solutions.

---

## If You Like This Project

Star the repository and connect for collaboration.
