import streamlit as st
import requests

st.title("AI Career Counselor")

name = st.text_input("Name")

education = st.selectbox(
    "Education",
    ["School", "Diploma", "B.Tech", "M.Tech", "MBA"]
)

skills = st.text_area("Skills")

interests = st.text_area("Interests")

if st.button("Get Advice"):

    try:

        response = requests.post(
            "http://127.0.0.1:5000/career",
            json={
                "name": name,
                "education": education,
                "skills": skills,
                "interests": interests
            }
        )

        result = response.json()

        if result["success"]:

            st.subheader("Predicted MBTI")
            st.write(result["mbti"])

            st.subheader("Career Recommendation")
            st.write(result["recommendation"])

        else:

            st.error(result["error"])

    except Exception as e:

        st.error(str(e))