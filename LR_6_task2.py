import pandas as pd
from collections import defaultdict
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url_data = "https://raw.githubusercontent.com/susanli2016/Machine-Learning-with-Python/master/data/renfe_small.csv"
dataset = pd.read_csv(url_data)

dataset = dataset[["price", "train_type", "origin", "destination", "train_class"]].dropna()

price_ranges = [
    dataset["price"].min(),
    dataset["price"].quantile(0.33),
    dataset["price"].quantile(0.66),
    dataset["price"].max()
]
dataset["price_segment"] = pd.cut(dataset["price"], bins=price_ranges, labels=["low", "medium", "high"])

feature_distribution = defaultdict(lambda: defaultdict(int))
category_totals = defaultdict(int)

for _, entry in dataset.iterrows():
    price_segment = entry["price_segment"]
    category_totals[price_segment] += 1
    for attribute in ["train_type", "origin", "destination", "train_class"]:
        feature_distribution[attribute][(entry[attribute], price_segment)] += 1

def probability_given_category(attribute, value, category):
    count = feature_distribution[attribute].get((value, category), 0)
    total = category_totals[category]
    return count / total if total else 0

def compute_category_probability(category, conditions):
    prior_prob = category_totals[category] / len(dataset)
    likelihood = 1
    for attribute, value in conditions.items():
        likelihood *= probability_given_category(attribute, value, category)
    return prior_prob * likelihood

ticket_params = {
    "train_type": "AVE",
    "origin": "MADRID",
    "destination": "SEVILLA",
    "train_class": "Turista"
}

posterior_results = {}
for segment in category_totals.keys():
    posterior_results[segment] = compute_category_probability(segment, ticket_params)

total_posterior = sum(posterior_results.values())
normalized_results = {seg: prob / total_posterior for seg, prob in posterior_results.items()}

print("Ймовірності для кожної категорії ціни квитка -->")
for segment, prob in normalized_results.items():
    print(f"{str(segment).capitalize()}: {prob:.2f}")
