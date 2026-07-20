import streamlit as st
import joblib

# ---------- Page config ----------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #2E7D32;
        color: white;
        font-weight: 600;
        padding: 0.6em 0;
        border-radius: 10px;
        border: none;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #1B5E20;
        color: white;
    }
    .result-box {
        background-color: #E8F5E9;
        border-left: 6px solid #2E7D32;
        padding: 1.2em;
        border-radius: 10px;
        margin-top: 1em;
        font-size: 1.2em;
        font-weight: 600;
        color: #1B5E20;
    }
    h1 {
        color: #1B5E20;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Load model ----------
model = joblib.load("house_price_model.joblib")

# ---------- Header ----------
st.title("🏠 House Price Prediction")
st.caption("Estimate California housing prices using a trained regression model.")
st.divider()

# ---------- Sidebar info ----------
with st.sidebar:
    st.header("ℹ️ About")
    st.write(
        "This app predicts median house value based on the California "
        "Housing dataset features. Fill in the property and area details "
        "on the right, then click **Predict**."
    )
    st.markdown("---")
    st.write("Built with **Streamlit** + **scikit-learn**")

# ---------- Input form ----------
st.subheader("📋 Property Details")

col1, col2 = st.columns(2)

with col1:
    MedInc = st.number_input("💰 Median Income (10k USD)", min_value=0.0, step=0.1)
    HouseAge = st.number_input("🏗️ House Age (years)", min_value=0.0, step=1.0)
    AveRooms = st.number_input("🛋️ Average Rooms", min_value=0.0, step=0.1)
    AveBedrms = st.number_input("🛏️ Average Bedrooms", min_value=0.0, step=0.1)

with col2:
    Population = st.number_input("👥 Population", min_value=0.0, step=1.0)
    AveOccup = st.number_input("🧍 Average Occupancy", min_value=0.0, step=0.1)
    Latitude = st.number_input("🧭 Latitude", min_value=0.0, step=0.01)
    Longitude = st.number_input("🧭 Longitude", min_value=0.0, step=0.01)

st.divider()

# ---------- Prediction ----------
if st.button("🔮 Predict"):
    with st.spinner("Calculating prediction..."):
        prediction = model.predict([[
            MedInc, HouseAge, AveRooms, AveBedrms,
            Population, AveOccup, Latitude, Longitude
        ]])

    st.markdown(
        f"""<div class="result-box">
        🏡 Predicted House Price: <br>${prediction[0]*100000:,.2f}
        </div>""",
        unsafe_allow_html=True,
    )
    st.balloons()
