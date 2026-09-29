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
# FASTAPI BACKEND
# =========================================================

API_URL = "https://mpg-predicter-backend-n1rodm7va-rat7050s-projects.vercel.app"

PREDICT_URL = f"{API_URL}/predict"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
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

                # =================================================
                # CALL DEPLOYED FASTAPI
                # =================================================

                response = requests.post(
                    PREDICT_URL,
                    params={
                        "horsepower": float(horsepower)
                    },
                    timeout=60
                )

                # =================================================
                # SUCCESS
                # =================================================

                if response.status_code == 200:

                    try:

                        result = response.json()

                    except ValueError:

                        st.error(
                            "❌ Backend returned invalid JSON."
                        )

                        st.code(
                            response.text,
                            language="text"
                        )

                        st.stop()

                    # ---------------------------------------------
                    # GET MPG
                    # ---------------------------------------------

                    if "predicted_mpg" not in result:

                        st.error(
                            "❌ Invalid API response."
                        )

                        st.json(result)

                        st.stop()

                    mpg = float(
                        result["predicted_mpg"]
                    )

                    # ---------------------------------------------
                    # SUCCESS MESSAGE
                    # ---------------------------------------------

                    st.success(
                        "Prediction completed successfully!"
                    )

                    # ---------------------------------------------
                    # MPG
                    # ---------------------------------------------

                    st.metric(
                        "🚗 Predicted MPG",
                        f"{mpg:.2f} MPG"
                    )

                    st.write("")

                    # ---------------------------------------------
                    # HORSEPOWER
                    # ---------------------------------------------

                    st.metric(
                        "⚙️ Horsepower",
                        f"{horsepower:.0f} HP"
                    )


                # =================================================
                # API ERROR
                # =================================================

                else:

                    st.error(
                        f"Prediction failed "
                        f"(HTTP {response.status_code})"
                    )

                    st.code(
                        response.text,
                        language="text"
                    )


            # =====================================================
            # CONNECTION ERROR
            # =====================================================

            except requests.exceptions.ConnectionError:

                st.error(
                    "⚠️ Cannot connect to the FastAPI backend."
                )

                st.info(
                    "Check your Vercel backend deployment."
                )


            # =====================================================
            # TIMEOUT
            # =====================================================

            except requests.exceptions.Timeout:

                st.error(
                    "⏱️ Backend request timed out."
                )


            # =====================================================
            # OTHER REQUEST ERROR
            # =====================================================

            except requests.exceptions.RequestException as e:

                st.error(
                    f"❌ API request error: {e}"
                )


            # =====================================================
            # UNKNOWN ERROR
            # =====================================================

            except Exception as e:

                st.error(
                    f"❌ Unexpected error: {e}"
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
