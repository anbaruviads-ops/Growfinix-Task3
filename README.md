# AI Career Counseling Chatbot

An AI-powered Career Counseling Chatbot that helps users discover suitable career paths based on their education, skills, interests, and personality type.

The system predicts the user's MBTI personality type using Machine Learning and provides career recommendations with salary insights, future scope, and learning roadmaps.

## Features

* Career counseling chatbot
* MBTI personality prediction
* Career recommendations
* Salary range suggestions
* Future scope analysis
* Learning roadmap generation
* SQLite database for chat history
* Flask REST API backend
* Streamlit frontend UI
* OpenAI GPT integration (with local fallback recommendations)
* PDF career report generation
* Interest visualization graphs

## Tech Stack

### Backend

* Python
* Flask
* SQLite

### Machine Learning

* Scikit-Learn
* Random Forest Classifier
* TF-IDF Vectorization

### Frontend

* Streamlit

### AI

* OpenAI GPT-4o API (optional)
* Rule-based fallback recommendation system

## Project Structure

```text
chatbot-counselor-ai/
│
├── app.py
├── config.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── mbti.csv
│
├── models/
│   └── mbti_rf.pkl
│
├── database.py
├── mbti_predictor.py
├── train_mbti.py
├── career_recommender.py
├── graph_generator.py
├── report_generator.py
│
├── frontend/
│   └── streamlit_app.py
│
├── graphs/
├── reports/
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/chatbot-counselor-ai.git

cd chatbot-counselor-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Dataset Setup

Download the MBTI Personality Dataset and place it inside:

```text
data/mbti.csv
```

Expected columns:

```text
type
posts
```

## Train MBTI Model

```bash
python train_mbti.py
```

This generates:

```text
models/mbti_rf.pkl
```

## Running Backend

```bash
python app.py
```

Backend runs on:

```text
http://127.0.0.1:5000
```

## Running Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend runs on:

```text
http://localhost:8501
```

## Sample Input

```json
{
  "name": "Anbu",
  "education": "B.Tech",
  "skills": "Python, SQL, Machine Learning",
  "interests": "AI, Data Science"
}
```

## Sample Output

```json
{
  "mbti": "INTJ",
  "recommendation": "AI Engineer, Machine Learning Engineer, Data Scientist",
  "salary": "10-35 LPA",
  "future_scope": "Very High"
}
```

## API Endpoint

### Home

```http
GET /
```

Response

```json
{
  "message": "Career Counseling API Running"
}
```

### Career Recommendation

```http
POST /career
```

Request

```json
{
  "name": "Anbu",
  "education": "B.Tech",
  "skills": "Python",
  "interests": "AI"
}
```

Response

```json
{
  "success": true,
  "mbti": "INTJ",
  "recommendation": "AI Engineer"
}
```

## Database

SQLite database stores:

* User Name
* Education
* Skills
* Interests
* MBTI Type
* Recommendations

## Future Improvements

* Resume analysis
* Career roadmap generation
* Interview preparation chatbot
* Skill gap analysis
* Job recommendation system
* Course recommendation engine
* Multi-language support


