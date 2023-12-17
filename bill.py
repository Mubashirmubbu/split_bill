import streamlit as st
import pandas as pd

def split_bill(total_amount, tax, tip, discounts, names):
    # Calculate the total bill amount
    total_bill = (total_amount + tax) - discounts
    # Calculate the total tip
    total_tip = total_bill * (tip / 100)
    # Calculate the final bill including tip
    final_bill = total_bill + total_tip
    # Calculate the amount to be paid by each person
    amount_per_person = final_bill / len(names)

    # Create a DataFrame for displaying the results
    data = {
        'Name': names,
        'Total Amount': [total_amount] * len(names),
        'Tax': [tax] * len(names),
        'Discounts': [discounts] * len(names),
        'Tip': [total_tip] * len(names),
        'Final Bill': [final_bill] * len(names),
        'Amount Per Person': [amount_per_person] * len(names),
    }

    df = pd.DataFrame(data)
    return df

def main():
    st.title("Bill Splitting App")

    # User input
    total_amount = st.number_input("Enter Total Amount of the Bill", value=0.0, step=1.0)
    tax = st.number_input("Enter Tax Amount", value=0.0, step=1.0)
    tip = st.number_input("Enter Tip Percentage", value=0.0, step=1.0)
    discounts = st.number_input("Enter Discounts Applied", value=0.0, step=1.0)

    # Allow users to enter names in a multi-line text area
    names = st.text_area("Enter Names of People Splitting the Bill", "")

    names_list = [name.strip() for name in names.split('\n') if name.strip()]

    if st.button("Split Bill"):
        if not names_list:
            st.warning("Please enter at least one name.")
        else:
            # Call the split_bill function
            result_df = split_bill(total_amount, tax, tip, discounts, names_list)

            # Display the results in a table
            st.table(result_df)

if __name__ == "__main__":
    main()
