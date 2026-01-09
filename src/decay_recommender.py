def get_recommendation(memory_strength):
    if memory_strength < 0.4:
        return "Revise Now"
    elif memory_strength < 0.7:
        return "Revise Soon"
    else:
        return "Safe"

if __name__ == "__main__":
    test_values = [0.2, 0.5, 0.8]
    for val in test_values:
        print(val, "→", get_recommendation(val))
