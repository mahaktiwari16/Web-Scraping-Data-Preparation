import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Book Data Analysis",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 Book Web Scraping & Data Analysis")

st.write(
    "This application displays and analyzes book data "
    "collected using Python web scraping."
)

# Load cleaned CSV
df = pd.read_csv("books_cleaned.csv")

# Sidebar filter
st.sidebar.header("Filters")

rating = st.sidebar.multiselect(
    "Select Rating",
    sorted(df["Rating"].unique()),
    default=sorted(df["Rating"].unique())
)

# Apply filter
filtered_df = df[df["Rating"].isin(rating)]

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Books", len(filtered_df))

with col2:
    st.metric(
        "Average Price",
        f"£{filtered_df['Price'].mean():.2f}"
    )

with col3:
    st.metric(
        "Highest Price",
        f"£{filtered_df['Price'].max():.2f}"
    )

with col4:
    st.metric(
        "Average Rating",
        f"{filtered_df['Rating'].mean():.2f}"
    )

# Dataset
st.subheader("📋 Book Dataset")
st.dataframe(filtered_df, use_container_width=True)

# Rating chart
st.subheader("⭐ Rating Distribution")

rating_counts = filtered_df["Rating"].value_counts().sort_index()

st.bar_chart(rating_counts)

# Price statistics
st.subheader("💰 Price Statistics")

st.write(filtered_df["Price"].describe())

# Download button
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇️ Download CSV",
    data=csv,
    file_name="books_filtered.csv",
    mime="text/csv"
)