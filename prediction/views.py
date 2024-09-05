# prediction/views.py
from django.shortcuts import render
from .forms import PredictionForm
from .preprocessing import add_title_and_encode
import joblib
import pandas as pd
import os

# Define the directory for models
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models')

# Load the model and scaler
model = joblib.load(os.path.join(MODEL_DIR, 'gbm_model.pkl'))
scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.pkl'))

def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Convert form data to DataFrame
            df = pd.DataFrame([data])
            # Apply preprocessing
            df_preprocessed = add_title_and_encode(df)
            # Apply scaling
            X = scaler.transform(df_preprocessed)
            # Make prediction
            prediction1 = model.predict(X)
            result = 'survived' if prediction1 == 1 else 'not survived'
            return render(request, 'prediction_result.html', {'result': result})

    else:
        form = PredictionForm()
    return render(request, 'predict_form.html', {'form': form})
