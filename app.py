import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('loan_eligibility_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the fitted preprocessor
with open('preprocessor.pkl', 'rb') as preprocessor_file:
    preprocessor = pickle.load(preprocessor_file)

# Streamlit UI
st.title("Loan Eligibility Prediction")
st.write("Please enter the following details:")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term (in months)", min_value=0)
credit_history = st.selectbox("Credit History", [0, 1])

# Create a DataFrame for the input data
input_data = {
    'Gender': gender,
    'Married': married,
    'Dependents': dependents,
    'Education': education,
    'Self_Employed': self_employed,
    'Property_Area': property_area,
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_amount_term,
    'Credit_History': credit_history
}
input_df = pd.DataFrame(input_data, index=[0])

# Preprocess the input data
input_df_prepared = preprocessor.transform(input_df)

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_df_prepared)
    prediction_proba = model.predict_proba(input_df_prepared)

    # Output prediction result
    if prediction[0] == 1:
        st.success("Congratulations! You meet the eligibility criteria for the loan.")
    else:
        st.error("We regret to inform you that you do not meet the eligibility criteria for the loan at this time")
        
    # Displaying each probability with a label
    st.write("Probability of 'Not Eligible':", prediction_proba[0][0])
    st.write("Probability of 'Eligible':", prediction_proba[0][1])
