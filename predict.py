import pickle

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# User input
hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance (%): "))
previous_marks = float(input("Enter previous marks: "))

# Prediction
prediction = model.predict([[hours, attendance, previous_marks]])

print("📊 Predicted Marks:", round(prediction[0], 2))
