from sqlalchemy import create_engine
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

#sql connector
engine = create_engine("mysql+pymysql://root:Vansh9818@localhost/resume_ai")

#resumes
resumes = pd.read_sql("SELECT * FROM resumes", con=engine)
print(resumes)

#NLP
nltk.download("stopwords")

#reading tables
resumes = pd.read_sql("SELECT id, resume_text FROM resumes", con=engine)
job_descriptions = pd.read_sql("SELECT id, skills_required FROM job_descriptions", con=engine)

#preprocess
def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    tokens = nltk.word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_tokens)

resumes["processed_text"] = resumes["resume_text"].apply(preprocess_text)
job_descriptions["processed_skills"] = job_descriptions["skills_required"].apply(preprocess_text)

#TF-IDF
all_texts = resumes["processed_text"].tolist() + job_descriptions["processed_skills"].tolist()
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_texts)

#separator 
resume_vectors = tfidf_matrix[:len(resumes)]
job_vectors = tfidf_matrix[len(resumes):]

# calculations
results = []
for i, job_vector in enumerate(job_vectors):
    scores = cosine_similarity(job_vector, resume_vectors).flatten()
    for j, score in enumerate(scores):
        results.append({"job_id": job_descriptions["id"].iloc[i], "resume_id": resumes["id"].iloc[j], "score": score})

results_df = pd.DataFrame(results)
#committing results
results_df.to_sql("results", con=engine, if_exists="replace", index=False)
print("Results stored in the database!")

#mysql part
job_id = 1
top_resumes = pd.read_sql(f"""
    SELECT r.name, r.email, rs.score
    FROM results rs
    JOIN resumes r ON rs.resume_id = r.id
    WHERE rs.job_id = {job_id}
    ORDER BY rs.score DESC
    LIMIT 5
""", con=engine)
print(top_resumes)
