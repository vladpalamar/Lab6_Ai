dataset = [
    {"Weather": "Sunny", "Moisture": "High", "Breeze": "Weak", "Game": "No"},
    {"Weather": "Sunny", "Moisture": "High", "Breeze": "Strong", "Game": "No"},
    {"Weather": "Overcast", "Moisture": "High", "Breeze": "Weak", "Game": "Yes"},
    {"Weather": "Rain", "Moisture": "High", "Breeze": "Weak", "Game": "Yes"},
    {"Weather": "Rain", "Moisture": "Normal", "Breeze": "Weak", "Game": "Yes"},
    {"Weather": "Rain", "Moisture": "Normal", "Breeze": "Strong", "Game": "No"},
    {"Weather": "Overcast", "Moisture": "Normal", "Breeze": "Strong", "Game": "Yes"},
    {"Weather": "Sunny", "Moisture": "Normal", "Breeze": "Weak", "Game": "Yes"},
    {"Weather": "Sunny", "Moisture": "Normal", "Breeze": "Strong", "Game": "Yes"},
    {"Weather": "Rain", "Moisture": "Normal", "Breeze": "Weak", "Game": "Yes"},
    {"Weather": "Sunny", "Moisture": "High", "Breeze": "Strong", "Game": "No"},
    {"Weather": "Overcast", "Moisture": "High", "Breeze": "Strong", "Game": "Yes"},
    {"Weather": "Overcast", "Moisture": "Normal", "Breeze": "Weak", "Game": "Yes"},
    {"Weather": "Rain", "Moisture": "High", "Breeze": "Strong", "Game": "No"},
]

yes_count = sum(1 for d in dataset if d["Game"] == "Yes")
no_count = sum(1 for d in dataset if d["Game"] == "No")
total_count = len(dataset)

prob_yes = yes_count / total_count
prob_no = no_count / total_count

def find_probability(feature, value, outcome):
    filtered = [d for d in dataset if d[feature] == value and d["Game"] == outcome]
    return len(filtered) / (yes_count if outcome == "Yes" else no_count)

weather_yes = find_probability("Weather", "Rain", "Yes")
moisture_yes = find_probability("Moisture", "High", "Yes")
breeze_yes = find_probability("Breeze", "Strong", "Yes")

weather_no = find_probability("Weather", "Rain", "No")
moisture_no = find_probability("Moisture", "High", "No")
breeze_no = find_probability("Breeze", "Strong", "No")

yes_data_prob = weather_yes * moisture_yes * breeze_yes * prob_yes
no_data_prob = weather_no * moisture_no * breeze_no * prob_no

final_prob = yes_data_prob + no_data_prob
result_yes = yes_data_prob / final_prob
result_no = no_data_prob / final_prob

print(f"P(Yes) = {result_yes:.2f}")
print(f"P(No) = {result_no:.2f}")

if result_yes > result_no:
    print("Гра відбудеться.")
else:
    print("Гра не відбудеться.")
