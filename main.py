import streamlit as st
import pandas as pd 
# import numpy as np

import matplotlib.pyplot as plt



st.title("Data Dashboard")

uploaded_file = st.file_uploader("choose a CSV file",type="csv")


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Data Filtrer")

    cols = df.columns.tolist()

    slct_col = st.selectbox("select column to filter by",cols)

    unique_vals = df[slct_col].unique()

    slct_val = st.selectbox("select value", unique_vals)

    filtered_df = df[df[slct_col]==slct_val]
    st.write(filtered_df)

    st.subheader("Data Visualization || Plot Data")

    x_col = st.selectbox("select x-axis column",cols)
    y_col = st.selectbox("select y-axis column", cols)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_col)[y_col])
else:
    st.info("Please upload a CSV file...")