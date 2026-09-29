import streamlit as st
import requests
import os


# =========================================================
# CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="MPG Predictor",
    page_icon="🚗",
    layout="wide"
)


# =========================================================
# API CONFIGURATION
# =========================================================

API_URL = os.getenv(
    "API_URL",
    "https://mpg-predicter-backend-n1rodm7va-rat7050s-projects.vercel.app"
)

PREDICT_URL = f"{API_URL}/predict"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f5f7fb;
    }

    .main-title {
        font-size: 44px;
        font-weight: 800;
        color: #172033;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #687386;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 26px;
        font-weight: 700;
        color: #172033;
    }

    [data-testid="stMetric"] {
        background-color: #eef8f2;
        padding: 18px;
        border-radius: 12px;
    }

    div.stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


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

left, right = st.columns(
    2,
    gap="large"
)


# =========================================================
# VEHICLE INPUT
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

        predict_button = st.button(
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

        if predict_button:

            try:

                # --------------------------------------------------
                # API REQUEST
                # --------------------------------------------------

                response = requests.post(
                    PREDICT_URL,
                    params={
                        "horsepower": horsepower
                    },
                    timeout=30
                )


                # --------------------------------------------------
                # SUCCESS
                # --------------------------------------------------

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


                # --------------------------------------------------
                # API ERROR
                # --------------------------------------------------

                else:

                    try:

                        error_data = response.json()

                        error_message = error_data.get(
                            "detail",
                            "Unknown API error"
                        )

                    except Exception:

                        error_message = response.text


                    st.error(
                        f"Prediction failed: {error_message}"
                    )


            # ------------------------------------------------------
            # CONNECTION ERROR
            # ------------------------------------------------------

            except requests.exceptions.Timeout:

                st.error(
                    "⏱️ API request timed out."
                )


            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Could not connect to the FastAPI backend."
                )

                st.info(
                    "Please check whether the Vercel API is running."
                )


            except Exception as e:

                st.error(
                    f"Unexpected error: {str(e)}"
                )


        else:

            st.info(
                "Enter horsepower and click "
                "**Predict MPG** to get the prediction."
            )


# =========================================================
# MODEL INFORMATION
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


col1, col2, col3 = st.columns(
    3,
    gap="medium"
)


# =========================================================
# MODEL
# =========================================================

with col1:

    with st.container(border=True):

        st.markdown("### 🤖 Model")

        st.write(
            "Polynomial Regression"
        )


# =========================================================
# INPUT
# =========================================================

with col2:

    with st.container(border=True):

        st.markdown("### 📥 Input")

        st.write(
            "Horsepower"
        )


# =========================================================
# OUTPUT
# =========================================================

with col3:

    with st.container(border=True):

        st.markdown("### 📤 Output")

        st.write(
            "Miles Per Gallon (MPG)"
        )


# =========================================================
# API INFORMATION
# =========================================================

st.write("")
st.write("")

st.markdown(
    '<div class="section-title">'
    '🌐 API Information'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

st.code(
    API_URL,
    language="text"
)

st.markdown(
    f"""
    **API Documentation:**  
    `{API_URL}/docs`

    **Health Check:**  
    `{API_URL}/health`
    """
)


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")

st.caption(
    "Built with Python • FastAPI • Streamlit • "
    "Scikit-learn • Polynomial Regression"
)
