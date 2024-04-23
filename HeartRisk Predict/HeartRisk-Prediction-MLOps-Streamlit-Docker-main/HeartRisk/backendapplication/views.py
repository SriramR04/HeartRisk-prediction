from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor
import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

class predict_calories(APIView):
    def get(self, request):
        # Handle GET request (if needed)
        return Response({'message': 'GET request received'}, status=status.HTTP_200_OK)

    def post(self, request):
        # Extract input values from request
        age = float(request.data.get('age'))
        height = float(request.data.get('height'))
        weight = float(request.data.get('weight'))
        gender = request.data.get('gender')
        duration = float(request.data.get('duration'))
        heart_rate = float(request.data.get('heartRate'))
        body_temp = float(request.data.get('bodyTemp'))
        
        # Load data from CSV
        df = pd.read_csv("C:\\Users\\MANOJ\\Downloads\\calories_data.csv")

        # Encode categorical variables
        label_encoder = LabelEncoder()
        df['Gender'] = label_encoder.fit_transform(df['Gender'])

        # Split data into independent and dependent variables
        X = df[['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']]
        y = df['Calories']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Feature scaling
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Create and fit the model
        model = XGBRegressor()
        model.fit(X_train_scaled, y_train)
        gender_encoded = label_encoder.transform([gender])[0]  # transform expects an iterable

        # Make sure the input data has the same column names as the training data
        input_data = pd.DataFrame({
            'Gender': [gender_encoded],  # Use the encoded gender
            'Age': [age],
            'Height': [height],
            'Weight': [weight],
            'Duration': [duration],
            'Heart_Rate': [heart_rate],
            'Body_Temp': [body_temp]
        })

        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)

        # Convert prediction to standard Python float
        prediction = float(prediction)

        print('Received POST request with data:', request.data)

        # Return the prediction
        # Return the prediction
        return JsonResponse({'prediction': prediction}, status=status.HTTP_200_OK)

