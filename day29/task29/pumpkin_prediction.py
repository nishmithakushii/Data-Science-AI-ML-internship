# Pumpkin Seed Type Prediction (Rule-Based)

def predict_seed_type(area, perimeter, major_axis, minor_axis, roundness):

    # Rule-based classification
    if area > 50000 and roundness > 0.70:
        seed_type = "Cercevelik"
    
    elif major_axis > 300 and minor_axis > 150:
        seed_type = "Cercevelik"
    
    else:
        seed_type = "Urgup Sivrisi"

    return seed_type


# Example pumpkin seed measurements
area = 52000
perimeter = 900
major_axis = 310
minor_axis = 170
roundness = 0.75


# Predict seed type
result = predict_seed_type(area, perimeter, major_axis, minor_axis, roundness)

print("Predicted Pumpkin Seed Type:", result)