from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_desc, resumes):

    docs = [job_desc] + resumes

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(docs)

    jd_vector = vectors[0]
    resume_vectors = vectors[1:]

    scores = cosine_similarity(jd_vector, resume_vectors)[0]

    return scores