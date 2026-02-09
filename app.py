import streamlit as st
import joblib
import numpy as np

# -------------------------------------------------
# PAGE CONFIGURATION & BACKGROUND
# -------------------------------------------------
st.set_page_config(page_title="AI Soil Fertility Predictor 🌾", layout="wide")

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1600&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Base app font and text colors */
.stApp {
    font-family: 'Trebuchet MS', sans-serif;
    color: #2D1B0A; /* earthy brown text */
}

/* HEADINGS */
h1 {
    color: #D35400; /* deep orange */
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

h2 {
    color: #5D4037; /* rich brown */
    font-weight: 900;
}

h3 {
    color: #BF360C; /* dark red-orange */
    font-weight: 800;
}

h4 {
    color: #3E2723;
    font-weight: bold;
}

/* LABELS (Nutrient Names) */
label {
    font-weight: 900 !important;
    font-size: 1.1rem !important;
    color: #212121 !important; /* strong black */
}

/* INPUT BOXES */
div[data-baseweb="input"] > div {
    box-shadow: none !important;
    border: 2px solid #5D4037 !important; /* earthy brown border */
    border-radius: 10px;
}

input {
    background-color: #FAF3E0 !important; /* soft beige background */
    color: #1B1B1B !important; /* near black text */
    font-weight: bold !important;
}

/* BUTTONS */
.stButton>button {
    background: linear-gradient(90deg, #F57C00, #FFB300);
    color: #2B1D0E;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    padding: 0.6em 1.6em;
    transition: 0.3s;
    font-size: 1.05rem;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
}
.stButton>button:hover {
    background: linear-gradient(90deg, #E65100, #FB8C00);
    transform: scale(1.08);
}

/* COLOR CLASSES */
.orange-text { color: #E65100; }
.brown-text { color: #4E342E; }
.yellow-text { color: #F9A825; }
.red-text { color: #C62828; }
.black-text { color: #1B1B1B; }

</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
try:
    model = joblib.load("soil_fertility_model.pkl")
except:
    st.warning("⚠️ Model file not found! Please make sure 'soil_fertility_model.pkl' is in your folder.")
    st.stop()

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown("<h1 class='orange-text'>🌾 AI-Based Soil Fertility Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='brown-text'>Analyze soil nutrient levels to predict fertility and get smart crop recommendations 🌱</h3>", unsafe_allow_html=True)

# -------------------------------------------------
# INPUT SECTION
# -------------------------------------------------
st.markdown("<h2 class='black-text'>🧪 Enter Soil Nutrient Values</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=500.0, step=0.1)
    P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=500.0, step=0.1)
    K = st.number_input("Potassium (K)", min_value=0.0, max_value=500.0, step=0.1)
    pH = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.1)

with col2:
    EC = st.number_input("Electrical Conductivity (EC)", min_value=0.0, max_value=500.0, step=0.1)
    OC = st.number_input("Organic Carbon (OC)", min_value=0.0, max_value=500.0, step=0.1)
    S = st.number_input("Sulphur (S)", min_value=0.0, max_value=500.0, step=0.1)
    Zn = st.number_input("Zinc (Zn)", min_value=0.0, max_value=500.0, step=0.1)

with col3:
    Fe = st.number_input("Iron (Fe)", min_value=0.0, max_value=500.0, step=0.1)
    Cu = st.number_input("Copper (Cu)", min_value=0.0, max_value=500.0, step=0.1)
    Mn = st.number_input("Manganese (Mn)", min_value=0.0, max_value=500.0, step=0.1)
    B = st.number_input("Boron (B)", min_value=0.0, max_value=500.0, step=0.1)

# -------------------------------------------------
# PREDICTION
# -------------------------------------------------
if st.button("🔍 Predict Fertility Level"):
    features = np.array([[N, P, K, pH, EC, OC, S, Zn, Fe, Cu, Mn, B]])
    prediction = model.predict(features)[0]

    st.markdown("---")

    # COLOR-BASED OUTPUT
    if prediction == 0:
        color = "#FFAB91"
        title = "🟤 Low Fertility Soil"
        desc = "This soil lacks sufficient nutrients. Use organic manure, compost, and soil enrichment methods."
        crops = ["Millets", "Pulses", "Groundnut", "Sorghum", "Horse Gram"]

    elif prediction == 1:
        color = "#FFE082"
        title = "🟠 Moderate Fertility Soil"
        desc = "The soil has moderate nutrients. Maintain balance using crop rotation and organic supplements."
        crops = ["Maize", "Cotton", "Sunflower", "Barley", "Mustard"]

    elif prediction == 2:
        color = "#FFB74D"
        title = "🔴 High Fertility Soil"
        desc = "Soil is nutrient-rich — ideal for commercial and high-yield crops."
        crops = ["Rice", "Wheat", "Sugarcane", "Vegetables", "Banana", "Mango"]

    else:
        color = "#E0E0E0"
        title = "⚪ Unknown Level"
        desc = "Unable to classify fertility level — check input values or model integrity."
        crops = []

    st.markdown(
        f"""
        <div style='background-color:{color}; padding:25px; border-radius:15px;'>
            <h3 style='text-align:center; color:#3E2723;'>{title}</h3>
            <p style='font-size:17px; color:#212121; text-align:justify;'>{desc}</p>
            <h4 style='color:#BF360C;'>🌾 Recommended Crops:</h4>
            <ul style='font-size:16px; color:#4E342E;'>
                {''.join(f"<li>{crop}</li>" for crop in crops)}
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("""
---
<h4 style='color:#4E342E; text-align:center;'>
👨‍🌾 Developed for Smart Agriculture — Empowering Farmers with AI-driven Soil Insights.
</h4>
""", unsafe_allow_html=True)
