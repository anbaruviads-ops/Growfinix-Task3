from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_career_advice(education, skills, interests, mbti):

    try:

        prompt = f"""
Education: {education}
Skills: {skills}
Interests: {interests}
Personality: {mbti}

Suggest careers, salary, future scope and roadmap.
"""

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception:

        interests = interests.lower()

        if "ai" in interests or "machine learning" in interests:

            return """
Recommended Careers:
- AI Engineer
- Machine Learning Engineer
- Data Scientist

Salary:
10-35 LPA

Future Scope:
Very High

Roadmap:
Python
Machine Learning
Deep Learning
Generative AI
"""

        elif "web" in interests or "react" in interests:

            return """
Recommended Careers:
- Frontend Developer
- Full Stack Developer
- React Developer

Salary:
6-20 LPA

Future Scope:
High

Roadmap:
HTML
CSS
JavaScript
React
Next.js
"""

        elif "cyber" in interests:

            return """
Recommended Careers:
- Cyber Security Analyst
- Security Engineer
- Penetration Tester

Salary:
8-30 LPA

Future Scope:
Very High
"""

        else:

            return """
Recommended Careers:
- Software Engineer
- Data Analyst
- IT Consultant

Salary:
5-15 LPA

Future Scope:
Good
"""