def extract_skills(text):

    skill_list = [
        "python",
        "sql",
        "flask",
        "machine learning",
        "java",
        "excel",
        "aws",
        "pandas",
        "react",
        "django",
        "docker",
        "api",
        "power bi",
        "tableau"
    ]

    found = []

    text = text.lower()

    for skill in skill_list:
        if skill in text:
            found.append(skill)

    return found