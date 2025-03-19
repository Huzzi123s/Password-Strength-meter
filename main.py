import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 5:
        remarks = "Strong 🔥"
    elif strength >= 3:
        remarks = "Moderate 👍"
    else:
        remarks = "Weak ❌"

    return strength, remarks

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength, remarks = check_password_strength(password)
    st.subheader(f"Strength: {remarks}")