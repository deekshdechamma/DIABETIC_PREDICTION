import streamlit as st
import numpy as np
import pickle
from pathlib import Path

MODEL_FILENAME = "diabetes_model.pkl"

# MUST be first Streamlit command
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered",
)

class SimpleDiabetesModel:
    def predict(self, X):
        # Use only symptom answers for mock predictions.
        # Columns: [age, gender, symptom1, ..., symptom14].
        symptom_sum = X[0][2:].sum()
        return np.array([1 if symptom_sum >= 3 else 0])


def get_model_path():
    return Path(__file__).resolve().parent / MODEL_FILENAME


def save_default_model(model_path: Path):
    model = SimpleDiabetesModel()
    try:
        with open(model_path, "wb") as f:
            pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)
        return model
    except Exception:
        return model


@st.cache_resource
def load_model():
    model_path = get_model_path()
    if model_path.exists():
        try:
            with open(model_path, "rb") as f:
                return pickle.load(f), True
        except Exception:
            fallback_model = SimpleDiabetesModel()
            try:
                with open(model_path, "wb") as f:
                    pickle.dump(fallback_model, f, protocol=pickle.HIGHEST_PROTOCOL)
            except Exception:
                pass
            return fallback_model, False

    model = save_default_model(model_path)
    return model, True


model, model_loaded = load_model()

if not model_loaded:
    st.info(
        f"No valid model file was found. A default demo model has been created at {get_model_path()} "
        "and will be used for predictions."
    )


def convert_yes_no(val):
    return 1 if val == "Yes" else 0


def get_yes_no_input(label):
    return st.selectbox(label, ["No", "Yes"])

st.title("🩺 Diabetes Prediction System")
st.markdown(
    "Use the form below to enter the patient's details and symptoms. "
    "This demo app uses a fallback model when the saved model file is unavailable."
)

with st.form(key="prediction_form"):
    st.subheader("Patient Information")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
        gender = st.selectbox("Gender", ["Female", "Male"])

    with col2:
        st.write("\n")
        st.info("All symptom fields are required for the demo prediction.")

    st.subheader("Symptoms")
    col1, col2 = st.columns(2)

    with col1:
        polyuria = get_yes_no_input("Polyuria")
        polydipsia = get_yes_no_input("Polydipsia")
        sudden_weight_loss = get_yes_no_input("Sudden Weight Loss")
        weakness = get_yes_no_input("Weakness")
        polyphagia = get_yes_no_input("Polyphagia")
        genital_thrush = get_yes_no_input("Genital Thrush")
        visual_blurring = get_yes_no_input("Visual Blurring")
        itching = get_yes_no_input("Itching")

    with col2:
        irritability = get_yes_no_input("Irritability")
        delayed_healing = get_yes_no_input("Delayed Healing")
        partial_paresis = get_yes_no_input("Partial Paresis")
        muscle_stiffness = get_yes_no_input("Muscle Stiffness")
        alopecia = get_yes_no_input("Alopecia")
        obesity = get_yes_no_input("Obesity")

    submit_button = st.form_submit_button("🔮 Predict Diabetes Risk")

if submit_button:
    input_data = np.array([
        [
            age,
            1 if gender == "Male" else 0,
            convert_yes_no(polyuria),
            convert_yes_no(polydipsia),
            convert_yes_no(sudden_weight_loss),
            convert_yes_no(weakness),
            convert_yes_no(polyphagia),
            convert_yes_no(genital_thrush),
            convert_yes_no(visual_blurring),
            convert_yes_no(itching),
            convert_yes_no(irritability),
            convert_yes_no(delayed_healing),
            convert_yes_no(partial_paresis),
            convert_yes_no(muscle_stiffness),
            convert_yes_no(alopecia),
            convert_yes_no(obesity),
        ]
    ])

    try:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.error("⚠️ High chance of Diabetes detected.")
            st.write(
                "This is a demo prediction. Consult a medical professional for an accurate diagnosis."
            )
        else:
            st.success("✅ Low chance of Diabetes detected.")
            st.write(
                "This result is based on the demo model. For real medical advice, consult a doctor."
            )
    except Exception as e:
        st.warning("There was a problem making the prediction.")
        st.error(f"Prediction error: {e}")
        st.write(
            "Please check your input values and try again, or confirm that the model file is valid."
        )