# Heart Disease Prediction App 💓

❤️ Welcome to the Heart Disease Prediction App! This Flask-based web application uses a Random Forest model to predict the likelihood of heart disease based on user inputs. The app features a modern UI with a heart icon ❤️, responsive input fields, and convenient reset/GitHub icons. Let's dive in! 🚀

## Model Training Overview 🧠

🌳 **This project was part of the AI & ML Internship Task 5: Decision Trees and Random Forests**, with the objective to learn tree-based models for classification. Using the UCI Heart Disease dataset (heart.csv and cleaned_heart.csv), I followed these steps:

### Decision Tree Classifier 🌲
- ✅ Trained a Decision Tree Classifier using Scikit-learn
- 📊 Visualized the tree structure (saved as decision_tree.png) using Graphviz
- 🔍 Analyzed overfitting by experimenting with tree depth (plotted in dt_accuracy_vs_depth.png)
- 📈 Evaluated performance using cross-validation

### Random Forest Classifier 🌳
- 🌟 Trained a Random Forest model with 100 trees using Scikit-learn
- 🎯 Compared its accuracy (~0.85 on the test set) with the Decision Tree
- 🔑 Interpreted feature importances (visualized in feature_importances.png)
- ✔️ Evaluated using cross-validation, confirming higher accuracy and stability

**After comparing both models, I chose the Random Forest model for the Flask web app due to its superior accuracy, ability to handle complex datasets, and feature importance insights.** The trained model was saved as random_forest_model.pkl.

## App Overview 📖

💻 This app predicts heart disease using 13 clinical features with:

- ❤️ A heading with heart icon
- 🔄 Reset (⟳) and GitHub icons
- 🖥️ Three input fields per row
- 📱 Responsive design (works on mobile)
- 📊 Separate result page

### Features ✨
- 🌳 **Model**: Random Forest Classifier (~0.85 accuracy)
- ✅ **Input Validation**: Ensures proper value ranges
- 🎨 **Responsive UI**: Vibrant indigo-amber theme
- 🔗 **Icons**: Reset form (⟳) and GitHub link
- 🌀 **Animations**: Smooth slide-in effects
- 📈 **Visualizations**: Includes decision_tree.png, dt_accuracy_vs_depth.png, feature_importances.png

## Prerequisites 🛠️
Before running the app, ensure you have:
- 🐍 Python 3.6+
- 📦 Required packages: `flask joblib numpy pandas scikit-learn matplotlib seaborn`
- 📂 Dataset files (heart.csv and cleaned_heart.csv) already in folder

## Setup and Installation ⚙️

1. **Clone the Repository**:
```bash
git clone https://github.com/ShubhamAIML/heart-disease-prediction.git
cd heart-disease-prediction
```

2. **Train the Models (Optional)**:
   - If you want to retrain, ensure you generate:
     - random_forest_model.pkl
     - decision_tree_model.pkl
     - Visualizations: decision_tree.png, dt_accuracy_vs_depth.png, feature_importances.png

3. **Prepare the Flask App**:
   - Ensure app.py and template files are in place

## Running the App 🏃‍♂️

1. **Start the Flask Server**:
```bash
python app.py
```

2. **Access the App**:
   - Open browser to: http://127.0.0.1:5000
   - See form page with heart icon ❤️ and action buttons

## Usage 📋

1. **Fill the Form**:
   - Enter values for 13 features
   - Form has:
     - 📏 Continuous Features (Age, BP, Cholesterol)
     - 🏷️ Categorical Features (Sex, Chest Pain Type)

2. **Predict**:
   - Click "Predict" button
   - See results: 
     - ✅ "No Heart Disease" (green)
     - ❗ "Heart Disease Detected" (red)

3. **Additional Actions**:
   - 🔄 Reset form with reset icon
   - 🔗 Visit GitHub via icon
   - ↩️ "Back to Form" from results

## File Structure 📁
```
heart-disease-prediction/
├── templates/
│   ├── index.html
│   └── result.html
├── app.py
├── random_forest_model.pkl
├── decision_tree_model.pkl
├── heart.csv
├── cleaned_heart.csv
├── visualizations/
│   ├── decision_tree.png
│   ├── dt_accuracy_vs_depth.png
│   └── feature_importances.png
└── README.md
```

## Deployment 🚀
For production:
```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
```

## Credits 🙌
- Dataset: UCI Machine Learning Repository
- Developer: ShubhamAIML (GitHub)
- Icons: Material Design, GitHub
- Styling: Tailwind CSS, Google Fonts

## License 📜
MIT License

❤️ **Happy predicting!** If you have questions, open an issue on GitHub. ❤️
