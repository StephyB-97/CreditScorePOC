import streamlit as st
from input_info import input_customer_info
from database import get_customer_info
from calculate_DTI import calculate_credit_score

# Function to inject custom CSS for button styling
def set_sidebar_button_style():
    st.markdown(
        """
        <style>
        .sidebar .stButton > button {
            width: 100%;  /* Set button width to 100% */
            height: 50px; /* Set button height */
            font-size: 16px; /* Set font size */
            background-color: #0077B3; /* Customize background color */
            color: white; /* Set text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Add border radius */
            transition: background-color 0.3s ease; /* Smooth transition for hover effect */
        }
        .sidebar .stButton > button:hover {
            background-color: #005999; /* Darker background color on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to set the button style
set_sidebar_button_style()

# Streamlit UI
st.title("Customer Credit Score Analyzer")

# Sidebar for button navigation
st.sidebar.header("Navigation")
register_customer_page = st.sidebar.button("Register Customer")
access_customer_info_page = st.sidebar.button("Access Customer Information")

# Page control variable to remember the last action (clicking one of the buttons)
if 'page' not in st.session_state:
    st.session_state.page = "Register Customer"  # Default page

# Update the page state based on button clicks
if register_customer_page:
    st.session_state.page = "Register Customer"
elif access_customer_info_page:
    st.session_state.page = "Access Customer Information"

# Display content based on the selected page
if st.session_state.page == "Register Customer":
    input_customer_info()  # Call the function to display the registration form

elif st.session_state.page == "Access Customer Information":
    st.header("Customer Information Lookup")

    search_ssn = st.text_input("Enter SSN to Retrieve Info")

    # Button to retrieve customer information
    if st.button("Retrieve Info"):
        customer = get_customer_info(search_ssn)
        if customer:
            # Display customer information
            st.markdown(f"Customer Name: {customer['name']}")
            st.markdown(f"Total Debt: ${customer['debt']}")
            st.markdown(f"Monthly Income: ${customer['income']}")

            # Calculate credit score based on retrieved debt and income
            credit_score = calculate_credit_score(customer['income'], customer['debt'])
            st.write(f"Credit Score: {credit_score}")
        else:
            st.error("Customer not found.")
