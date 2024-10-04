# input_info.py
import streamlit as st
from database import add_customer

def input_customer_info():
    st.header("Customer Registration")

    # Input fields for customer registration
    name = st.text_input("Customer Name")
    ssn = st.text_input("Social Security Number")

    # Debt and income as integer inputs
    debt = st.number_input("Total Debt ($)", min_value=0, step=1, format="%d")
    income = st.number_input("Monthly Income ($)", min_value=0, step=1, format="%d")

    # Submit button to register the customer
    if st.button("Submit Customer Info"):
        if name and ssn and debt > 0 and income > 0:
            if add_customer(name, ssn, debt, income):
                st.success(f"Customer {name} registered successfully!")
            else:
                st.error("Failed to register customer. Please try again.")
        else:
            st.error("Please fill all the fields correctly.")
