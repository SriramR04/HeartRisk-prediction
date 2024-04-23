import streamlit as st
import requests

# Frontend components
st.title('Calories Prediction ')
age = st.number_input('Age', min_value=0, max_value=120)
height = st.number_input('Height (cm)', min_value=0)
weight = st.number_input('Weight (kg)', min_value=0)
gender = st.radio('Gender', ['male', 'female'])
duration = st.number_input('Duration (minutes)', min_value=0)
heart_rate = st.number_input('Heart Rate (bpm)', min_value=0)
body_temp = st.number_input('Body Temperature (°C)', min_value=0)

# Backend logic
if st.button('Predict'):
    # Prepare data payload
    payload = {
        'age': age,
        'height': height,
        'weight': weight,
        'gender': gender,
        'duration': duration,
        'heartRate': heart_rate,
        'bodyTemp': body_temp
    }
    # Make HTTP POST request to Django backend
    response = requests.post('http://127.0.0.1:8000/', json=payload)
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.write(f'Predicted Calories: {prediction}')
    else:
        st.error('Failed to get prediction from backend')
