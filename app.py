from flask import Flask, request, jsonify

from mbti_predictor import predict_mbti
from career_recommender import generate_career_advice

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Career Counseling API Running"
    })


@app.route("/career", methods=["POST"])
def career():

    try:

        data = request.get_json()

        name = data.get("name", "")
        education = data.get("education", "")
        skills = data.get("skills", "")
        interests = data.get("interests", "")

        try:
            mbti = predict_mbti(
                interests + " " + skills
            )
        except:
            mbti = "INTJ"

        recommendation = generate_career_advice(
            education,
            skills,
            interests,
            mbti
        )

        return jsonify({
            "success": True,
            "name": name,
            "mbti": mbti,
            "recommendation": recommendation
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=False)