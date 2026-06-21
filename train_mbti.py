import pandas as pd

from sklearn.pipeline import Pipeline

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.ensemble import RandomForestClassifier

import joblib

df = pd.read_csv("data/mbti.csv")

X = df["posts"]

y = df["type"]

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            max_features=5000
        )
    ),
    (
        "rf",
        RandomForestClassifier(
            n_estimators=100
        )
    )
])

model.fit(X,y)

joblib.dump(
    model,
    "models/mbti_rf.pkl"
)

print("Model Saved")