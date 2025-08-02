import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("Farm_Irrigation_System.pkl")

# Page configuration
st.set_page_config(page_title="Smart Sprinkler Predictor", page_icon="💧", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .title {
            font-size: 2.8rem;
            color: #00796b;
            text-align: center;
            margin-top: -30px;
            font-weight: bold;
        }
        .subtitle {
            font-size: 1.1rem;
            color: #555;
            text-align: center;
            margin-bottom: 30px;
        }
        .sprinkler-on {
            background: linear-gradient(90deg, #d0f0c0, #b2ebf2);
            padding: 12px;
            border-radius: 10px;
            font-weight: bold;
            color: #1b5e20;
            margin: 6px 0;
        }
        .sprinkler-off {
            background: linear-gradient(90deg, #ffcdd2, #f8bbd0);
            padding: 12px;
            border-radius: 10px;
            font-weight: bold;
            color: #b71c1c;
            margin: 6px 0;
        }
        .predict-btn > button {
            background-color: #00796b;
            color: white;
            padding: 10px 20px;
            font-weight: bold;
            border-radius: 10px;
        }
        .footer {
            margin-top: 40px;
            text-align: center;
            font-size: 0.9rem;
            color: #777;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
st.sidebar.title("📘 System Info")
st.sidebar.markdown("""
This app uses a machine learning model to predict whether each sprinkler 
unit (1–20) should be **ON** or **OFF** based on real-time sensor inputs 
scaled between **0.0 and 1.0**.

🚿 Efficient irrigation  
🌿 Crop health focus  
📊 Smart automation
""")

# Header
st.markdown('<div class="title">💧 Smart Sprinkler Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Use the sliders below to simulate real-time sensor data (scaled 0–1)</div>', unsafe_allow_html=True)

# Sensor inputs
sensor_values = []
st.markdown("### 🌱 Sensor Inputs")

for i in range(0, 20, 5):
    cols = st.columns(5)
    for j in range(5):
        idx = i + j
        with cols[j]:
            val = st.slider(f"Sensor {idx + 1}", 0.0, 1.0, 0.5, 0.01, key=f"sensor_{idx}")
            sensor_values.append(val)

# Prediction button
st.markdown("<div class='predict-btn'>", unsafe_allow_html=True)
if st.button("🔍 Predict Sprinkler Status"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("## 🧠 Prediction Results")

    col1, col2 = st.columns(2)
    for i, status in enumerate(prediction):
        result_text = f"Sprinkler {i+1} (Parcel_{i}): {'✅ ON' if status == 1 else '❌ OFF'}"
        css_class = "sprinkler-on" if status == 1 else "sprinkler-off"
        if i % 2 == 0:
            with col1:
                st.markdown(f"<div class='{css_class}'>{result_text}</div>", unsafe_allow_html=True)
        else:
            with col2:
                st.markdown(f"<div class='{css_class}'>{result_text}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>")
st.markdown('<div class="footer">© 2025 Smart Irrigation | ML-Powered Sprinkler Optimization</div>', unsafe_allow_html=True)
