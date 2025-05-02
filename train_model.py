import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image
import joblib
import os

# Set random seed for reproducibility
np.random.seed(42)

# 1. Load and Clean the Dataset
# Load the heart disease dataset
data = pd.read_csv('heart.csv')

# Display first 5 rows of original dataset
print("First 5 rows of original dataset:\n", data.head())

# Check for missing values
print("\nMissing values:\n", data.isnull().sum())

# Check for invalid values (e.g., negative age, chol, etc.)
invalid_rows = data[(data['age'] <= 0) | (data['chol'] <= 0) | (data['trestbps'] <= 0) |
                   (data['thalach'] <= 0) | (data['oldpeak'] < 0)]
print("Invalid rows:\n", invalid_rows)

# Handle duplicates
data = data.drop_duplicates()
print("Shape after removing duplicates:", data.shape)

# Save cleaned dataset
cleaned_file = 'cleaned_heart.csv'
data.to_csv(cleaned_file, index=False)
print(f"Cleaned dataset saved as {cleaned_file}")

# Display first 5 rows of cleaned dataset
cleaned_data = pd.read_csv(cleaned_file)
print("\nFirst 5 rows of cleaned dataset:\n", cleaned_data.head())

# 2. Prepare Data for Training
# Separate features and target
X = data.drop('target', axis=1)
y = data['target']

# Split data into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Decision Tree Classifier
# Initialize and train the model with default parameters
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)

# Make predictions
y_train_pred_dt = dt_classifier.predict(X_train)
y_test_pred_dt = dt_classifier.predict(X_test)

# Calculate metrics
dt_train_accuracy = accuracy_score(y_train, y_train_pred_dt)
dt_test_accuracy = accuracy_score(y_test, y_test_pred_dt)
dt_test_precision = precision_score(y_test, y_test_pred_dt)
dt_test_recall = recall_score(y_test, y_test_pred_dt)
dt_test_f1 = f1_score(y_test, y_test_pred_dt)

print("\nDecision Tree - Default Parameters:")
print(f"Training Accuracy: {dt_train_accuracy:.4f}")
print(f"Testing Accuracy: {dt_test_accuracy:.4f}")
print(f"Testing Precision: {dt_test_precision:.4f}")
print(f"Testing Recall: {dt_test_recall:.4f}")
print(f"Testing F1-Score: {dt_test_f1:.4f}")

# 4. Visualize the Decision Tree
# Export the tree to a DOT file
dot_data = export_graphviz(
    dt_classifier,
    out_file=None,
    feature_names=X.columns,
    class_names=['No Heart Disease', 'Heart Disease'],
    filled=True,
    rounded=True,
    special_characters=True
)

# Create graph from DOT data
graph = pydotplus.graph_from_dot_data(dot_data)

# Save and display the tree as a PNG file
tree_image_file = 'decision_tree.png'
graph.write_png(tree_image_file)
print(f"Decision Tree visualization saved as {tree_image_file}")
print("Displaying Decision Tree:")
display(Image(filename=tree_image_file))

# 5. Analyze Overfitting by Controlling Tree Depth
# Test different max_depth values
depths = range(1, 11)
dt_train_accuracies = []
dt_test_accuracies = []

for depth in depths:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    dt_train_accuracies.append(accuracy_score(y_train, dt.predict(X_train)))
    dt_test_accuracies.append(accuracy_score(y_test, dt.predict(X_test)))

# Plot and display training vs. testing accuracy
plt.figure(figsize=(10, 6))
plt.plot(depths, dt_train_accuracies, label='Decision Tree Training Accuracy', marker='o')
plt.plot(depths, dt_test_accuracies, label='Decision Tree Testing Accuracy', marker='o')
plt.xlabel('Max Depth')
plt.ylabel('Accuracy')
plt.title('Decision Tree Accuracy vs. Max Depth')
plt.legend()
plt.grid(True)
plt.savefig('dt_accuracy_vs_depth.png')
print("Decision Tree Accuracy vs. Depth plot saved as dt_accuracy_vs_depth.png")
print("Displaying Accuracy vs. Depth Plot:")
plt.show()

# 6. Train Random Forest Classifier
# Initialize and train the model with default parameters
rf_classifier = RandomForestClassifier(random_state=42, n_estimators=100)
rf_classifier.fit(X_train, y_train)

# Make predictions
y_train_pred_rf = rf_classifier.predict(X_train)
y_test_pred_rf = rf_classifier.predict(X_test)

# Calculate metrics
rf_train_accuracy = accuracy_score(y_train, y_train_pred_rf)
rf_test_accuracy = accuracy_score(y_test, y_test_pred_rf)
rf_test_precision = precision_score(y_test, y_test_pred_rf)
rf_test_recall = recall_score(y_test, y_test_pred_rf)
rf_test_f1 = f1_score(y_test, y_test_pred_rf)

print("\nRandom Forest - Default Parameters:")
print(f"Training Accuracy: {rf_train_accuracy:.4f}")
print(f"Testing Accuracy: {rf_test_accuracy:.4f}")
print(f"Testing Precision: {rf_test_precision:.4f}")
print(f"Testing Recall: {rf_test_recall:.4f}")
print(f"Testing F1-Score: {rf_test_f1:.4f}")

# 7. Compare Decision Tree and Random Forest
print("\nModel Comparison:")
print(f"Decision Tree Testing Accuracy: {dt_test_accuracy:.4f}")
print(f"Random Forest Testing Accuracy: {rf_test_accuracy:.4f}")
print(f"Accuracy Difference (RF - DT): {(rf_test_accuracy - dt_test_accuracy):.4f}")

# 8. Interpret Feature Importances
# Decision Tree feature importances
dt_feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': dt_classifier.feature_importances_
}).sort_values(by='Importance', ascending=False)

# Random Forest feature importances
rf_feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_classifier.feature_importances_
}).sort_values(by='Importance', ascending=False)

print("\nDecision Tree Feature Importances:")
print(dt_feature_importance)
print("\nRandom Forest Feature Importances:")
print(rf_feature_importance)

# Plot and display feature importances
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.barh(dt_feature_importance['Feature'], dt_feature_importance['Importance'])
plt.title('Decision Tree Feature Importances')
plt.xlabel('Importance')
plt.subplot(1, 2, 2)
plt.barh(rf_feature_importance['Feature'], rf_feature_importance['Importance'])
plt.title('Random Forest Feature Importances')
plt.xlabel('Importance')
plt.tight_layout()
plt.savefig('feature_importances.png')
print("Feature Importances plot saved as feature_importances.png")
print("Displaying Feature Importances Plot:")
plt.show()

# 9. Evaluate Using Cross-Validation
# Perform 5-fold cross-validation
dt_cv_scores = cross_val_score(dt_classifier, X, y, cv=5, scoring='accuracy')
rf_cv_scores = cross_val_score(rf_classifier, X, y, cv=5, scoring='accuracy')

print("\nCross-Validation Results:")
print(f"Decision Tree CV Accuracy: {dt_cv_scores.mean():.4f} (± {dt_cv_scores.std():.4f})")
print(f"Random Forest CV Accuracy: {rf_cv_scores.mean():.4f} (± {rf_cv_scores.std():.4f})")

# 10. Save Trained Models
# Save Decision Tree model with max_depth=5 (based on typical performance)
best_dt_classifier = DecisionTreeClassifier(max_depth=5, random_state=42)
best_dt_classifier.fit(X_train, y_train)
joblib.dump(best_dt_classifier, 'decision_tree_model.pkl')
print("Trained Decision Tree model saved as decision_tree_model.pkl")

# Save Random Forest model
joblib.dump(rf_classifier, 'random_forest_model.pkl')
print("Trained Random Forest model saved as random_forest_model.pkl")

# 11. Print Summary
print("\nSummary:")
print(f"- Cleaned dataset shape: {data.shape}")
print(f"- Decision Tree Testing Accuracy: {dt_test_accuracy:.4f}")
print(f"- Random Forest Testing Accuracy: {rf_test_accuracy:.4f}")
print(f"- Visualizations saved and displayed: {tree_image_file}, dt_accuracy_vs_depth.png, feature_importances.png")
print(f"- Models saved: decision_tree_model.pkl, random_forest_model.pkl")
print(f"- Cross-Validation: DT {dt_cv_scores.mean():.4f}, RF {rf_cv_scores.mean():.4f}")
