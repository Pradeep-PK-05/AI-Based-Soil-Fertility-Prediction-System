# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load dataset
file_path = "dataset1.csv"
data = pd.read_csv(file_path)
print("✅ Dataset Loaded Successfully!\n")

# 2️⃣ Show basic info
print("Dataset Info:")
print(data.info())
print("\nMissing Values:\n", data.isnull().sum())

# 3️⃣ Separate features and target
X = data.drop("Output", axis=1)
y = data["Output"]

# 4️⃣ Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5️⃣ Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6️⃣ Evaluate model
y_pred = model.predict(X_test)
print("\n🎯 Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 7️⃣ Confusion matrix visualization
plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Greens')
plt.title("Confusion Matrix")
plt.show()

# 8️⃣ Save trained model
joblib.dump(model, "soil_fertility_model.pkl")
print("\n💾 Model saved as 'soil_fertility_model.pkl'")

# 9️⃣ Define crop recommendations
crop_suggestions = {
    0: ["Millets", "Pulses", "Groundnut"],
    1: ["Maize", "Cotton", "Sunflower"],
    2: ["Rice", "Wheat", "Sugarcane", "Vegetables"]
}

# 🔟 Test sample prediction
sample = X_test.iloc[0].values.reshape(1, -1)
predicted_class = model.predict(sample)[0]

print("\n🧠 Predicted Fertility Level:", predicted_class)
print("🌾 Recommended Crops:", ", ".join(crop_suggestions[predicted_class]))
