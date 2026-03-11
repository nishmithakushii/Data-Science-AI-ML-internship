# Wine Quality Prediction (Rule-based approach)

def predict_wine_quality(alcohol, acidity, sulphates, sugar, pH):

    score = 0

    # Alcohol effect
    if alcohol >= 12:
        score += 2
    elif alcohol >= 10:
        score += 1

    # Acidity balance
    if 5 <= acidity <= 8:
        score += 2
    elif 3 <= acidity <= 10:
        score += 1

    # Sulphates improve preservation
    if sulphates >= 0.7:
        score += 2
    elif sulphates >= 0.5:
        score += 1

    # Sugar level
    if sugar <= 5:
        score += 2
    elif sugar <= 10:
        score += 1

    # pH balance
    if 3.0 <= pH <= 3.5:
        score += 2
    else:
        score += 1

    # Final wine quality score
    quality = min(score, 10)

    return quality


# Example wine sample
alcohol = 11.5
acidity = 6.5
sulphates = 0.8
sugar = 4.0
pH = 3.2


quality_score = predict_wine_quality(alcohol, acidity, sulphates, sugar, pH)

print("Predicted Wine Quality Score:", quality_score)