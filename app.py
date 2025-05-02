from flask import Flask, request, render_template, redirect, url_for, jsonify, make_response, session
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for session management

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')

# Define feature names and expected ranges/values
FEATURES = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
]
RANGES = {
    'age': (20, 100),           # Reasonable age range
    'sex': [0, 1],             # 0 = female, 1 = male
    'cp': [0, 1, 2, 3],        # Chest pain type
    'trestbps': (80, 200),     # Resting blood pressure (mm Hg)
    'chol': (100, 600),        # Cholesterol (mg/dl)
    'fbs': [0, 1],             # Fasting blood sugar (0 = <=120, 1 = >120)
    'restecg': [0, 1, 2],      # Resting ECG results
    'thalach': (60, 220),      # Maximum heart rate
    'exang': [0, 1],           # Exercise-induced angina (0 = no, 1 = yes)
    'oldpeak': (0, 6.2),       # ST depression
    'slope': [0, 1, 2],        # Slope of ST segment
    'ca': [0, 1, 2, 3],        # Number of major vessels
    'thal': [1, 2, 3]          # Thalassemia
}

# Feature descriptions for tooltips
FEATURE_INFO = {
    'age': 'Age in years',
    'sex': 'Gender (0 = female, 1 = male)',
    'cp': 'Chest pain type (0 = Typical Angina, 1 = Atypical Angina, 2 = Non-Anginal Pain, 3 = Asymptomatic)',
    'trestbps': 'Resting blood pressure in mm Hg on admission to the hospital',
    'chol': 'Serum cholesterol in mg/dl',
    'fbs': 'Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)',
    'restecg': 'Resting electrocardiographic results (0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy)',
    'thalach': 'Maximum heart rate achieved',
    'exang': 'Exercise induced angina (1 = yes, 0 = no)',
    'oldpeak': 'ST depression induced by exercise relative to rest',
    'slope': 'Slope of the peak exercise ST segment (0 = Upsloping, 1 = Flat, 2 = Downsloping)',
    'ca': 'Number of major vessels (0-3) colored by fluoroscopy',
    'thal': 'Thalassemia (1 = Normal, 2 = Fixed defect, 3 = Reversible defect)'
}

@app.route('/', methods=['GET'])
def index():
    # Clear session form data unless it's a back navigation
    if not request.headers.get('Referer', '').endswith('/predict'):
        session.pop('form_data', None)
    form_data = session.get('form_data', None)
    response = make_response(render_template('index/index.html', feature_info=FEATURE_INFO, ranges=RANGES, form_data=form_data, errors=None))
    # Prevent browser caching to avoid BFCache issues
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # For JSON requests
        if request.is_json:
            data = request.json
            input_data = []
            
            for feature in FEATURES:
                if feature not in data:
                    return jsonify({
                        'success': False,
                        'error': f"Missing feature: {feature}"
                    }), 400
                
                value = data[feature]
                # Convert to float and validate
                try:
                    value = float(value)
                except ValueError:
                    return jsonify({
                        'success': False,
                        'error': f"Invalid value for {feature}: must be a number"
                    }), 400
                
                # Validate ranges
                if feature in ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']:
                    if value not in RANGES[feature]:
                        return jsonify({
                            'success': False,
                            'error': f"Invalid value for {feature}: {value}"
                        }), 400
                else:
                    min_val, max_val = RANGES[feature]
                    if not (min_val <= value <= max_val):
                        return jsonify({
                            'success': False,
                            'error': f"{feature} out of range ({min_val}-{max_val})"
                        }), 400
                
                input_data.append(value)
            
            # Make prediction
            input_array = np.array([input_data])
            prediction = int(model.predict(input_array)[0])
            probability = float(model.predict_proba(input_array)[0][1])
            
            return jsonify({
                'success': True,
                'prediction': prediction,
                'probability': probability,
                'message': "Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected"
            })
        
        # For form submissions
        else:
            # Check for intentional submission
            if request.form.get('submission_intent') != 'predict':
                return redirect(url_for('index'))
            
            input_data = []
            errors = []
            
            for feature in FEATURES:
                value = request.form.get(feature)
                if value is None or value == '':
                    errors.append(f"Missing value for {feature}")
                    continue

                # Convert to float and validate
                try:
                    value = float(value)
                except ValueError:
                    errors.append(f"Invalid value for {feature}: must be a number")
                    continue
                
                # Validate ranges
                if feature in ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']:
                    if value not in RANGES[feature]:
                        errors.append(f"Invalid value for {feature}: {value}")
                else:
                    min_val, max_val = RANGES[feature]
                    if not (min_val <= value <= max_val):
                        errors.append(f"{feature} out of range ({min_val}-{max_val})")
                
                input_data.append(value)
            
            # Store form data in session for back navigation
            session['form_data'] = request.form.to_dict()
            
            if errors:
                return render_template('index/index.html', 
                                      errors=errors, 
                                      feature_info=FEATURE_INFO, 
                                      ranges=RANGES,
                                      form_data=request.form)
            
            # Prepare input for model
            input_array = np.array([input_data])
            
            # Make prediction
            prediction = int(model.predict(input_array)[0])
            probability = float(model.predict_proba(input_array)[0][1])
            
            # Format probability as percentage
            probability_percent = round(probability * 100, 1)
            
            result = {
                'prediction': prediction,
                'probability': probability_percent,
                'message': "Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected",
                'data': dict(zip(FEATURES, input_data))
            }
            
            response = make_response(render_template('result/result.html', result=result, feature_info=FEATURE_INFO))
            response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            return response
    
    except Exception as e:
        if request.is_json:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
        else:
            return render_template('index/index.html', 
                                  errors=[f"An error occurred: {str(e)}"],
                                  feature_info=FEATURE_INFO,
                                  ranges=RANGES,
                                  form_data=request.form)

@app.route('/reset', methods=['GET'])
def reset():
    # Clear session form data for "Make Another Prediction" or "Home"
    session.pop('form_data', None)
    return redirect(url_for('index'))

@app.route('/clear-session', methods=['POST'])
def clear_session():
    # Clear session form data for reset button
    session.pop('form_data', None)
    return jsonify({'success': True})

@app.route('/about')
def about():
    response = make_response(render_template('about.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True)
