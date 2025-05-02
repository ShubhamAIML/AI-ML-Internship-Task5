# 🩺 **Heart Disease Prediction Project**  

**Welcome to the Heart Disease Prediction Project!**  

This project is part of my **AI & ML Internship Task 5** at **Elevate**, focusing on tree-based models for classification. I trained both a **Decision Tree** and a **Random Forest Classifier** on the **Heart Disease Dataset**, evaluated their performance, and built an additional **Flask web app** to make predictions accessible to users. The app is deployed on **Render** for live usage! 🚀  

---

### 📜 **Project Overview**  

This project was designed to explore **tree-based models (Decision Trees and Random Forests)** for classification tasks, as outlined in **Task 5: Decision Trees and Random Forests** of my internship. The objectives were:  

- Train a **Decision Tree Classifier** and visualize the tree.  
- Analyze **overfitting** and control tree depth.  
- Train a **Random Forest Classifier** and compare its accuracy with the Decision Tree.  
- Interpret **feature importances** to understand key factors in heart disease prediction.  
- Evaluate the models using standard metrics (**accuracy, precision, recall, F1-score**).  

As an additional effort, I built a **Flask web application** to allow users to input their health metrics and get heart disease predictions in real-time. The app is live on **Render!** 🌐  

---

### 🔗 **Live Demo**  

Try the **Heart Disease Prediction Tool** here:  
👉 **[Heart Disease Prediction App](https://heart-disease-prediction-e8pu.onrender.com/)** 👈  

---

### 📊 **Model Performance**  

I trained both a **Decision Tree Classifier** and a **Random Forest Classifier** on the **Heart Disease Dataset**. Below are the performance metrics for both models:  

#### **Decision Tree (Default Parameters) 🌳**  
- **Training Accuracy:** 1.0000  
- **Testing Accuracy:** 0.7377  
- **Testing Precision:** 0.7407  
- **Testing Recall:** 0.6897  
- **Testing F1-Score:** 0.7143  

#### **Random Forest (Default Parameters) 🌲🌲🌲**  
- **Training Accuracy:** 1.0000  
- **Testing Accuracy:** 0.8361  
- **Testing Precision:** 0.7879  
- **Testing Recall:** 0.8966  
- **Testing F1-Score:** 0.8387  

#### **Model Comparison 📈**  
- **Decision Tree Testing Accuracy:** 0.7377  
- **Random Forest Testing Accuracy:** 0.8361  
- **Accuracy Difference (RF - DT):** 0.0984  

**Conclusion:** The **Random Forest Classifier** outperformed the Decision Tree by **9.84%** in testing accuracy. Due to its better performance, I chose the **Random Forest model** for deployment in the Flask app. 🎉  

---

### 🧠 **Feature Importances**  

Understanding which features contribute most to heart disease prediction is crucial. Below are the **feature importances** for both models:  

#### **Decision Tree Feature Importances**  
| Feature    | Importance |  
|------------|------------|  
| cp         | 0.289914   |  
| oldpeak    | 0.151688   |  
| trestbps   | 0.097842   |  
| age        | 0.094165   |  
| ca         | 0.087659   |  

#### **Random Forest Feature Importances**  
| Feature    | Importance |  
|------------|------------|  
| thalach    | 0.138781   |  
| cp         | 0.131618   |  
| oldpeak    | 0.117095   |  
| thal       | 0.101598   |  
| ca         | 0.090493   |  

#### **Key Insights 🔍**  
- For the **Decision Tree**, **cp (chest pain type)** was the most important feature (~29%).  
- For the **Random Forest**, **thalach (maximum heart rate)** was the most important (13.88%), followed by **cp (13.16%)**.  
- Features like **fbs (fasting blood sugar)** had minimal impact in both models.  

---

### 🏗️ **Folder Structure**  

Here’s the structure of the **heart-disease-prediction/** repository with comments for each folder and file:  

```
heart-disease-prediction/  
├── static/                          # 🖼️ Static assets (CSS, JS)  
│   ├── index/                       # 📝 Index page assets  
│   │   ├── index.css                # 🎨 Index page styles  
│   │   └── index.js                 # ⚙️ Index page interactivity  
│   └── result/                      # 📊 Result page assets  
│       ├── result.css               # 🎨 Result page styles  
│       └── result.js                # ⚙️ Result page interactivity  
├── templates/                       # 📄 HTML templates  
│   ├── index/                       # 🏠 Input form templates  
│   │   └── index.html               # 📜 Input form page  
│   └── result/                      # ✅ Result page templates  
│       └── result.html              # 📜 Prediction result page  
├── Procfile                         # ⚙️ Render deployment config  
├── README.md                        # 📖 Project documentation  
├── app.py                           # 🐍 Flask app  
├── requirements.txt                 # 📋 Project dependencies  
├── cleaned_heart.csv                # 📊 Cleaned dataset  
├── decision_tree.png                # 🌳 Decision Tree visualization  
├── decision_tree_model.pkl          # 💾 Pre-trained Decision Tree  
├── dt_accuracy_vs_depth.png         # 📈 Accuracy vs. depth plot  
├── feature_importances.png          # 📊 Feature importance plot  
├── heart.csv                        # 📊 Original dataset  
├── random_forest_model.pkl          # 💾 Pre-trained Random Forest  
├── train_model.py                   # 🧠 Model training script  
└── task_5.pdf                       # 📜 Task description  
```

---

### 🌟 **Flask Web Application**  

I built a **Flask web application** to make the heart disease prediction model accessible to users. Features include:  

✅ **User-Friendly Interface** – Clean, responsive form with tooltips explaining each feature.  
✅ **Input Validation** – Ensures all inputs are valid before prediction.  
✅ **Loading Animation** – Visually appealing animation during prediction.  
✅ **Prediction Results** – Displays the prediction and probability of heart disease.  
✅ **Input Summary** – Shows a summary of the user’s input data.  
✅ **Print Option** – Allows users to print the results.  

**Live App:** 👉 [https://heart-disease-prediction-e8pu.onrender.com/](https://heart-disease-prediction-e8pu.onrender.com/)  

---

### 🚀 **Deployment**  

The Flask app is deployed on **Render**:  
1. Pushed the project to **GitHub**.  
2. Created a **web service on Render**.  
3. Configured build settings (`requirements.txt`, start command: `gunicorn app:app`).  
4. Deployed the app with the **random_forest_model.pkl** file.  

---

### 📝 **How to Run Locally**  

To run the project locally:  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/ShubhamAIML/heart-disease-prediction.git  
   cd heart-disease-prediction  
   ```

2. **Set Up a Virtual Environment:**  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```

3. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt  
   ```

4. **Run the Flask App:**  
   ```bash
   python app.py  
   ```

5. **Access the App:**  
   Open your browser and go to **[http://localhost:5000](http://localhost:5000)**.  

---

### 🛠️ **Technologies Used**  

- **Python 🐍** – Model training and Flask app.  
- **Scikit-learn 📚** – Decision Tree and Random Forest models.  
- **Flask 🌐** – Web application framework.  
- **HTML/CSS/JavaScript 🖥️** – Front-end development.  
- **Render ☁️** – Deployment platform.  
- **Pandas & NumPy 📊** – Data preprocessing.  
- **Graphviz 📈** – Decision Tree visualization.  
- **GitHub 📂** – Version control.  

---

### ❓ **Interview Questions & Answers**  

**1. How does a decision tree work?**  
A decision tree splits the dataset into subsets based on feature values, creating a tree-like structure. At each node, it selects the feature that best separates the data (using metrics like Gini impurity or entropy). It recursively splits until a stopping criterion is met (e.g., max depth). For classification, the leaf nodes represent class labels.  

**2. What is entropy and information gain?**  
Entropy measures the impurity of a dataset (higher entropy = more mixed classes). Information gain is the reduction in entropy after splitting on a feature. It’s calculated as:  
**Information Gain = Entropy(parent) - Σ(Entropy(child) * weight of child).**  
Decision trees choose the feature with the highest information gain for splitting.  

**3. How is random forest better than a single tree?**  
A Random Forest is an ensemble of decision trees, reducing overfitting by averaging predictions (bagging). It introduces randomness (e.g., feature sampling), making it more robust and accurate. In my project, the Random Forest achieved **0.8361 testing accuracy** compared to the Decision Tree’s **0.7377**.  

**4. What is overfitting and how do you prevent it?**  
Overfitting occurs when a model learns noise in the training data, performing poorly on new data. My Decision Tree had a **training accuracy of 1.0** but a **testing accuracy of 0.7377**, indicating overfitting. To prevent it, I:  
- Limited tree depth (visualized in `dt_accuracy_vs_depth.png`).  
- Used a **Random Forest**, which reduced overfitting (testing accuracy: **0.8361**).  

**5. What is bagging?**  
Bagging (Bootstrap Aggregating) involves training multiple models on different subsets of the training data (sampled with replacement) and averaging their predictions. Random Forest uses bagging to improve stability and accuracy.  

**6. How do you visualize a decision tree?**  
I used **Graphviz** to visualize the Decision Tree, exporting it as `decision_tree.png`. Scikit-learn’s `export_graphviz` function was used to generate the tree structure, which Graphviz rendered.  

**7. How do you interpret feature importance?**  
Feature importance in tree-based models measures how much each feature contributes to reducing impurity. In my Random Forest, **thalach (13.88%)** and **cp (13.16%)** were the most important features, indicating they are key predictors of heart disease.  

**8. What are the pros/cons of random forests?**  
✅ **Pros:** High accuracy, handles large datasets, reduces overfitting, provides feature importance.  
❌ **Cons:** Slower to train/predict, less interpretable than a single tree, requires more memory.  

---

### 📚 **What I Learned**  

- Training and evaluating **tree-based models**.  
- Visualizing **Decision Trees** and analyzing overfitting.  
- Interpreting **feature importances**.  
- Building and deploying a **Flask web app**.  
- Writing clean, modular code with proper error handling.  

---

### 📜 **Disclaimer**  

This project is for **educational purposes only**. The predictions are **not a substitute for professional medical advice**. Consult a healthcare professional for proper diagnosis. ⚕️  

© **2025 Heart Disease Predictor. All rights reserved.**  

--- 
