import streamlit as st
import requests

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MPG Predictor",
    page_icon="🚗",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

/* Main title */
.main-title {
    font-size: 44px;
    font-weight: 800;
    color: #172033;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    color: #687386;
    margin-bottom: 30px;
}

/* Section title */
.section-title {
    font-size: 26px;
    font-weight: 700;
    color: #172033;
}

/* Prediction metric */
[data-testid="stMetric"] {
    background-color: #eef8f2;
    padding: 18px;
    border-radius: 12px;
}

/* Button */
div.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🚗 MPG Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict vehicle fuel efficiency using Polynomial Regression'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# MAIN COLUMNS
# =========================================================

left, right = st.columns(2, gap="large")


# =========================================================
# VEHICLE INFORMATION
# =========================================================

with left:

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">'
            '🔧 Vehicle Information'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        horsepower = st.number_input(
            "Horsepower",
            min_value=40.0,
            max_value=250.0,
            value=150.0,
            step=5.0
        )

        st.caption(
            "Enter the engine horsepower of the vehicle."
        )

        st.write("")

        predict = st.button(
            "🚀 Predict MPG"
        )


# =========================================================
# PREDICTION RESULT
# =========================================================

with right:

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">'
            '📊 Prediction Result'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        if predict:

            try:

                response = requests.post(
                    "https://mpg-predicter-backend-n1rodm7va-rat7050s-projects.vercel.app/predict",
                    params={
                        "horsepower": horsepower
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    mpg = result["predicted_mpg"]

                    st.success(
                        "Prediction completed successfully!"
                    )

                    st.metric(
                        "🚗 Predicted MPG",
                        f"{mpg:.2f} MPG"
                    )

                    st.write("")

                    st.metric(
                        "⚙️ Horsepower",
                        f"{horsepower:.0f} HP"
                    )

                else:

                    st.error(
                        "Prediction failed. Please try again."
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "⚠️ Backend API is not running."
                )

                st.info(
                    "Start the backend first:\n\n"
                    "`uvicorn backend.main:app --reload`"
                )

        else:

            st.info(
                "Enter horsepower and click "
                "**Predict MPG** to get the prediction."
            )


# =========================================================
# ABOUT MODEL
# =========================================================

st.write("")
st.write("")
st.write("")

st.markdown(
    '<div class="section-title">'
    '🧠 About the Model'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


# =========================================================
# MODEL INFORMATION
# =========================================================

col1, col2, col3 = st.columns(3, gap="medium")


# Model
with col1:

    with st.container(border=True):

        st.markdown("### 🤖 Model")

        st.write(
            "Polynomial Regression"
        )


# Input
with col2:

    with st.container(border=True):

        st.markdown("### 📥 Input")

        st.write(
            "Horsepower"
        )


# Output
with col3:

    with st.container(border=True):

        st.markdown("### 📤 Output")

        st.write(
            "Miles Per Gallon (MPG)"
        )


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")

st.caption(
    "Built with Python • FastAPI • Streamlit • Scikit-learn"
)
