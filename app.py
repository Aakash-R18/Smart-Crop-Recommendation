import streamlit as st
import joblib
import numpy as np
from crop_info import crop_info

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Smart Crop Recommendation System",
    page_icon="🌱",
    layout="wide"
)

# ----------------------------------
# Sidebar
# ----------------------------------
st.sidebar.title("🌱 About")

st.sidebar.info("""
### Smart Crop Recommendation System

This application recommends the most suitable crop based on soil nutrients and weather conditions using Machine Learning.

### Algorithm Used
- Random Forest Classifier

### Developed Using
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
""")

# ----------------------------------
# Load Model
# ----------------------------------
model = joblib.load("crop_recommendation_model.pkl")
encoder = joblib.load("label_encoder.pkl")

# ----------------------------------
# Title
# ----------------------------------
st.title("🌱 Smart Crop Recommendation System")

st.markdown("""
### Machine Learning Based Crop Prediction

Predict the most suitable crop using soil nutrients and environmental conditions.

Please enter all the required parameters below.
""")

st.divider()

# ----------------------------------
# Input Fields
# ----------------------------------
col1, col2 = st.columns(2)

with col1:
    nitrogen = st.number_input("Nitrogen (N)", min_value=0.0)
    phosphorus = st.number_input("Phosphorus (P)", min_value=0.0)
    potassium = st.number_input("Potassium (K)", min_value=0.0)
    temperature = st.number_input("Temperature (°C)")

with col2:
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

st.divider()

# ----------------------------------
# Predict Button
# ----------------------------------
if st.button("🌾 Predict Crop", use_container_width=True):

    # Input Validation
    if ph < 0 or ph > 14:
        st.error("❌ Soil pH must be between 0 and 14.")
        st.stop()

    if humidity < 0 or humidity > 100:
        st.error("❌ Humidity must be between 0 and 100.")
        st.stop()

    if rainfall < 0:
        st.error("❌ Rainfall cannot be negative.")
        st.stop()

    # Prepare Input
    input_data = np.array([[
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    ]])

    # Prediction
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)

    crop = encoder.inverse_transform(prediction)[0]
    confidence = np.max(probabilities) * 100

    # ----------------------------------
    # Result
    # ----------------------------------

    st.success("✅ Prediction Completed Successfully!")

    st.subheader("🌾 Recommended Crop")

    st.markdown(f"## {crop.upper()}")

    st.metric(
        label="Prediction Confidence",
        value=f"{confidence:.2f}%"
    )

    st.progress(min(confidence / 100, 1.0))

    # ----------------------------------
    # Crop Information
    # ----------------------------------

    if crop.lower() in crop_info:

        info = crop_info[crop.lower()]

        with st.expander("🌱 Crop Information", expanded=True):

            st.write(f"**Growing Season:** {info['season']}")
            st.write(f"**Water Requirement:** {info['water']}")
            st.write(f"**Ideal Soil pH:** {info['ph']}")

            st.write("**Description:**")
            st.info(info['description'])

# ----------------------------------
# Footer
# ----------------------------------
st.divider()

st.caption(
    "Smart Crop Recommendation System | Developed using Machine Learning with Streamlit"
)