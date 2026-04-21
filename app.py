import os
from flask import Flask, render_template, request
from utils.cleaner import clean_text
from utils.matcher import rank_resumes
from utils.parser import extract_text
from utils.skills import extract_skills

app = Flask(__name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():

    results = []

    if request.method == "POST":

        jd = clean_text(request.form["jd"])
        files = request.files.getlist("resumes")

        resume_texts = []
        raw_texts = []
        names = []

        for file in files:

            if file.filename.endswith(".pdf"):

                path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(path)

                text = extract_text(path)

                raw_texts.append(text)
                resume_texts.append(clean_text(text))
                names.append(file.filename)

        if resume_texts:

            scores = rank_resumes(jd, resume_texts)

            jd_skills = extract_skills(jd)

            for i in range(len(names)):

                resume_skills = extract_skills(raw_texts[i])

                matched = []
                missing = []

                for skill in jd_skills:
                    if skill in resume_skills:
                        matched.append(skill)
                    else:
                        missing.append(skill)

                results.append({
                    "name": names[i],
                    "score": round(scores[i] * 100, 2),
                    "skills": ", ".join(resume_skills),
                    "matched": ", ".join(matched),
                    "missing": ", ".join(missing)
                })

            results = sorted(results, key=lambda x: x["score"], reverse=True)

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)