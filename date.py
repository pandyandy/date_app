# date_app.py

import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def add_or_subtract(date, unit, value, operation):
    if unit == "days":
        if operation == "Add":
            return date + timedelta(days=value)
        if operation == "Subtract":
            return date - timedelta(days=value)
    elif unit == "weeks":
        if operation == "Add":
            return date + timedelta(weeks=value)
        if operation == "Subtract":
            return date - timedelta(weeks=value)
    elif unit == "months":
        if operation == "Add":
            return date + relativedelta(months=value)
        if operation == "Subtract":
            return date - relativedelta(months=value)
    return date

def main():
    st.title('Venouškův kalkulátor dnů 🕺🏻')
    
    # 1. Let the user select a date
    user_date = st.date_input("Select a specific date:", datetime.now())

    # 2. Choose whether to add or subtract days/weeks/months
    operation = st.radio("Choose an operation:", ["Add", "Subtract"], horizontal=True)
    value = st.slider("Amount:", 1, 100)
    unit = st.radio("Unit of time:", ["days", "weeks", "months"], horizontal=True)

    # 3. Calculate
    result_date = add_or_subtract(user_date, unit, value, operation)

    day_name = result_date.strftime('%A')  # Get the name of the day

    if day_name == "Sunday":
        suggested_date = result_date - timedelta(days=2)
        st.write(f"If you {operation.lower()} {value} {unit} from/to {user_date.strftime('%d.%m.%Y')}, the resulting date is: {result_date.strftime('%d.%m.%Y')} which is a {day_name}. Since Sundays might not be ideal for termination of the contract, we suggest the closest Friday: {suggested_date.strftime('%d.%m.%Y')}. 💓")
    else:
        st.write(f"If you {operation.lower()} {value} {unit} from/to {user_date.strftime('%d.%m.%Y')}, the resulting date is: {result_date.strftime('%d.%m.%Y')} which is a {day_name}. 💓")

if __name__ == "__main__":
    main()
