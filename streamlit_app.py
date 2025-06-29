import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💸 Loan Default Predictor")

# Input fields
gender = st.selectbox("Gender", ['M', 'F'])
loan_type = st.selectbox("Loan Type", ['type1', 'type2'])
approv_in_adv = st.selectbox("Approval in Advance", ['pre', 'nopre'])
loan_purpose = st.selectbox("Loan Purpose", ['p1', 'p2', 'p3', 'p4'])
credit_worthiness = st.selectbox("Credit Worthiness", ['l1', 'l2'])
loan_amount = st.number_input("Loan Amount", value=100000)
lump_sum_payment = st.selectbox("Lump Sum Payment", ['lpsm', 'not_lpsm'])
year = st.selectbox("Application Year", [2019, 2020])

# Encoding
input_dict = {
    "gender": 1 if gender == 'M' else 0,
    "loan_type": 1 if loan_type == 'type2' else 0,
    "approv_in_adv": 1 if approv_in_adv == 'pre' else 0,
    "loan_purpose": {'p1': 0, 'p2': 1, 'p3': 2, 'p4': 3}[loan_purpose],
    "credit_worthiness": 1 if credit_worthiness == 'l2' else 0,
    "loan_amount": loan_amount,
    "lump_sum_payment": 1 if lump_sum_payment == 'lpsm' else 0,
    "year": year
}

input_df = pd.DataFrame([input_dict])

# Prediction
if st.button("Predict Default Risk"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ The loan is likely to default.")
    else:
        st.success("✅ The loan is unlikely to default.")
