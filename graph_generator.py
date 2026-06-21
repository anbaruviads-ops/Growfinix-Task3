import matplotlib.pyplot as plt

def generate_graph(interests):

    labels = interests.split(",")

    values = []

    score = 100

    for item in labels:
        values.append(score)
        score -= 10

    plt.figure(figsize=(8,5))

    plt.bar(labels,values)

    plt.title(
        "Interest Analysis"
    )

    plt.savefig(
        "graphs/interests.png"
    )

    return "graphs/interests.png"