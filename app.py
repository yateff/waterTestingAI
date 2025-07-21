import streamlit as st
import numpy as np
import pickle

# Feature names
features = [
    "ph", "Hardness", "Solids", "Chloramines", "Sulfate",
    "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"
]

# Page config
st.set_page_config(page_title="Water Potability Classifier", layout="centered")

# Title and subtitle
st.title("💧 Water Potability Prediction App")
st.markdown("Enter water quality measurements and select a classification algorithm to predict if water is potable.")

# Input fields
input_data = []
cols = st.columns(3)
for i, feature in enumerate(features):
    val = cols[i % 3].number_input(feature, step=0.1)
    input_data.append(val)

# Classifier selection
classifier = st.selectbox("Choose Classification Algorithm", ["Logistic Regression","SVM", "Decision Tree", "KNN", "Random Forest"])

# Map selection to model files
model_paths = {
    "Logistic Regression": "models/logistic_regression.pkl",
    "SVM": "models/svm.pkl",
    "Decision Tree": "models/decision_tree.pkl",
    "KNN": "models/knn.pkl",
    "Random Forest": "models/random_forest.pkl"
}

# Predict button
if st.button("Predict Potability"):
    try:
        with open(model_paths[classifier], "rb") as f:
            model = pickle.load(f)

        input_array = np.array([input_data])
        prediction = model.predict(input_array)[0]
        result = "✅ Potable" if prediction == 1 else "❌ Not Potable"

        st.subheader("Prediction Result")
        st.success(result)
    except Exception as e:
        st.error(f"Error: {e}")