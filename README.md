# Resume Screening AI

## Overview
Resume Screening AI is a Python-based application that leverages Natural Language Processing (NLP) and Machine Learning to automate the evaluation of resumes against job descriptions. The system extracts and processes text from resumes and job descriptions, calculates similarity scores using TF-IDF and cosine similarity, and ranks candidates based on their suitability for a given job.

---

## Features

- **Resume Upload**: Add candidate resumes to the database.
- **Job Description Upload**: Add job descriptions and required skills.
- **Automated Screening**: Process resumes and rank them based on their relevance to the job description.
- **Results Display**: View top candidates for a specific job.

---

## Tech Stack

- **Backend**: Python ( SQLAlchemy, Pandas, NLTK)
- **Database**: MySQL
- **Machine Learning**: Scikit-learn (TF-IDF and Cosine Similarity)

---

## Installation

### Prerequisites

- Python 3.7+
- MySQL Server
- Required Python packages -
flask==2.3.2
flask_sqlalchemy==3.0.5
pandas==2.0.3
scikit-learn==1.3.2
nltk==3.8.1
SQLAlchemy==2.0.21
pymysql==1.1.0


### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/resume-screening-ai.git
   cd resume-screening-ai
   ```

2. **Set Up the Database**:
   - Create a MySQL database named `resume_ai`:
     ```sql
     CREATE DATABASE resume_ai;
     ```
   - Run the SQL script in `setup.sql` to create tables.

3. **Install Dependencies**:
   ```bash
   pip install -r "requirements"
   ```

4. **Configure Connection**:
   - Update the `create_engine` connection string in `app.py` with your MySQL credentials:
     ```python
     engine = create_engine("mysql+pymysql://username:password@localhost/resume_ai")
     ```
---

## Usage

### Upload Job Description
1. Go to the "Upload Job Description" section.
2. Enter the job title and required skills.
3. Submit the form to add the job description to the database.

### Upload Resumes
1. Navigate to the "Upload Resume" section.
2. Provide the candidate’s name, email, and resume text.
3. Submit the form to store the resume.

### Run Screening
1. Enter the Job ID in the "Run Screening" section.
2. Submit to calculate similarity scores.

### View Results
1. Navigate to `/view_results/<job_id>` (replace `<job_id>` with the actual ID).
2. View ranked candidates based on their scores.

---

## Future Enhancements

- **File Uploads**: Allow users to upload resumes and job descriptions as files (PDF/Word).
- **Advanced NLP**: Use pre-trained models (e.g., BERT) for better semantic matching.
- **Real-time Results**: Implement asynchronous processing for immediate feedback.
- **Admin Panel**: Add user authentication and admin controls.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## Acknowledgments

- Inspired by the need for efficient candidate screening in hiring processes.
- Libraries: [NLTK](https://www.nltk.org/), [Scikit-learn](https://scikit-learn.org/), [SQLAlchemy](https://www.sqlalchemy.org/).

---

## Contact

For questions or suggestions, feel free to contact:
- **Email**: officialbusiness9818@gmail.com
- **GitHub**: [Vansh-kap-98](https://github.com/Vansh-kap-98)

