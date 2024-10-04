import pandas as pd
import os

# Define the CSV file path
CSV_FILE_PATH = "customers.csv"


import pandas as pd


def add_customer(name, ssn, debt, income):
    """Add customer information to the CSV file."""
    customer = {
        'name': name,
        'ssn': ssn,
        'debt': debt,
        'income': income
    }

    # Read the existing CSV file or create a new DataFrame if it doesn't exist
    try:
        df = pd.read_csv('customers.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['name', 'ssn', 'debt', 'income'])

    # Create a DataFrame for the new customer
    new_customer_df = pd.DataFrame([customer])  # Note the brackets around customer

    # Concatenate the existing DataFrame with the new customer DataFrame
    df = pd.concat([df, new_customer_df], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    df.to_csv('customers.csv', index=False)

    print("Customer added successfully!")


# Retrieve customer info from the CSV file based on SSN
def get_customer_info(ssn):
    """Retrieve customer information based on SSN from the CSV file."""
    if os.path.exists(CSV_FILE_PATH):
        df = pd.read_csv(CSV_FILE_PATH)
        # Find the customer by SSN
        customer = df[df['ssn'] == ssn]
        if not customer.empty:
            return customer.iloc[0].to_dict()  # Return the first matching customer
        else:
            print("Customer not found.")
    else:
        print("No customer data found.")
    return None
