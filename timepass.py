import streamlit as st
from datetime import date

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", 15, 90, step=1)
    dob = st.date_input("Enter your date of birth:", date(2000, 1, 1))

    if st.button("Submit"):
        today = date.today()

        next_birthday = date(today.year, dob.month, dob.day)

        if next_birthday < today:
            next_birthday = date(today.year + 1, dob.month, dob.day)

        days_remaining = (next_birthday - today).days

        st.write(f"Hello {name}")

        if days_remaining == 0:
            st.balloons()           
            st.success("🎉 Happy Birthday!")
        else:
            st.info(f"🎂 {days_remaining} days remaining until your birthday")
