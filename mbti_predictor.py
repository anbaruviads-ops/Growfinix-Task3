import joblib

model = joblib.load(
    "models/mbti_rf.pkl"
)

def predict_mbti(text):

    prediction = model.predict([text])

    return prediction[0]