import streamlit as st
import requests

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="MPG Predictor",
    page_icon="🚗",
    layout="centered"
)

# --------------------------------------------------
# API URL
# --------------------------------------------------

API_URL = "https://mpg-predicter-backend-n1rodm7va-rat7050s-projects.vercel.app"

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🚗 MPG Predictor")

st.write(
    "Predict vehicle fuel efficiency using "
    "Polynomial Regression."
)

st.divider()

# --------------------------------------------------
# Input
# --------------------------------------------------

horsepower = st.number_input(
    "Enter Horsepower",
    min_value=1.0,
    max_value=500.0,
    value=150.0,
    step=1.0
)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🚀 Predict MPG", use_container_width=True):

    try:

        response = requests.post(
            f"{API_URL}/predict",
            params={
                "horsepower": horsepower
            },
            timeout=60
        )

        # ------------------------------------------
        # Successful Response
        # ------------------------------------------

        if response.status_code == 200:

            result = response.json()

            predicted_mpg = result["predicted_mpg"]

            st.success("Prediction successful!")

            st.metric(
                label="Predicted MPG",
                value=f"{predicted_mpg:.2f} MPG"
            )

            st.info(
                f"Horsepower: {result['horsepower']} HP"
            )

        # ------------------------------------------
        # API Error
        # ------------------------------------------

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

            st.code(
                response.text,
                language="text"
            )

    # ----------------------------------------------
    # Connection Error
    # ----------------------------------------------

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to the FastAPI server."
        )

    # ----------------------------------------------
    # Timeout
    # ----------------------------------------------

    except requests.exceptions.Timeout:

        st.error(
            "⏱️ API request timed out."
        )

    # ----------------------------------------------
    # Invalid JSON
    # ----------------------------------------------

    except ValueError:

        st.error(
            "❌ API returned an invalid response."
        )

        st.code(
            response.text,
            language="text"
        )

    # ----------------------------------------------
    # Other Errors
    # ----------------------------------------------

    except Exception as e:

        st.error(
            f"Unexpected error: {e}"
        )

# --------------------------------------------------
# API Information
# --------------------------------------------------

st.divider()

st.subheader("🌐 API")

st.write(
    "FastAPI Backend:"
)

st.code(API_URL)

st.write(
    "Swagger Documentation:"
)

st.code(f"{API_URL}/docs")
