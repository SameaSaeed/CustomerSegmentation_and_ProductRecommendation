# Streamlit app
import streamlit as st
import pickle

st.title("Customer Segment Lookup")

# Load pickle
with open("customer_segments.pkl", "rb") as f:
    customer_segments = pickle.load(f)

# Input
customer_id_input = st.text_input("Enter Customer ID:")

if st.button("Get Segment"):
    if customer_id_input:
        segment = customer_segments.get(customer_id_input, "Customer not found")
        st.write(f"Customer Segment: **{segment}**")
    else:
        st.write("Please enter a Customer ID.")
