import streamlit as st
import numpy as np
import joblib

# Load the saved model and scaler
rf_model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Set page configuration
st.set_page_config(page_title="Fraud Detection App", layout="centered")

# App Title
st.title("Credit Card Fraud Detection")
st.write("Predict if a transaction is fraudulent based on input features.")

# Input Fields
st.subheader("Enter Transaction Details")

distance_from_home = st.number_input(
    "Distance from Home (miles)", min_value=0.0, max_value=100.0, step=0.1, value=10.0
)

distance_from_last_transaction = st.number_input(
    "Distance from Last Transaction (miles)", min_value=0.0, max_value=100.0, step=0.1, value=5.0
)

ratio_to_median_purchase_price = st.number_input(
    "Ratio to Median Purchase Price", min_value=0.0, max_value=10.0, step=0.1, value=1.0
)

repeat_retailer = st.selectbox("Is this a repeat retailer?", ["Yes", "No"])
used_chip = st.selectbox("Was a chip used?", ["Yes", "No"])
used_pin_number = st.selectbox("Was a PIN used?", ["Yes", "No"])
online_order = st.selectbox("Was this an online order?", ["Yes", "No"])

# Convert categorical inputs to numeric
repeat_retailer = 1.0 if repeat_retailer == "Yes" else 0.0
used_chip = 1.0 if used_chip == "Yes" else 0.0
used_pin_number = 1.0 if used_pin_number == "Yes" else 0.0
online_order = 1.0 if online_order == "Yes" else 0.0

# Add default values for other features
# Adjust based on your original feature set
other_features = [0.0, 0.0, 0.0]  # Default values for the 3 other features
input_data = [
    distance_from_home, 
    distance_from_last_transaction, 
    ratio_to_median_purchase_price, 
    repeat_retailer, 
    used_chip, 
    used_pin_number, 
    online_order
] + other_features  # Add other feature defaults

input_data = np.array(input_data).reshape(1, -1)

# Predict Button
if st.button("Predict Fraud"):
    # Scale the input data
    input_data_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = rf_model.predict(input_data_scaled)
    probability = rf_model.predict_proba(input_data_scaled)[0][1]  # Probability of fraud

    # Display results
    st.write("---")
    if prediction[0] == 1:
        st.error(f"🚨 **Warning: This transaction is likely fraudulent!**")
        st.write(f"Confidence Level: **{probability * 100:.2f}%**")
    else:
        st.success(f"✅ **This transaction is NOT fraudulent.**")
        st.write(f"Confidence Level: **{(1 - probability) * 100:.2f}%**")

    st.write("---")

# Footer
st.markdown("""
    <div style="text-align: center;">
        <p>Made by <strong>Caleb Osagie</strong></p>
    </div>
""", unsafe_allow_html=True)
