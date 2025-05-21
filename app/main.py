import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data


@st.cache
def load_data():
    # Assuming CSV files are in the data directory
    benin = pd.read_csv('../../data/benin_clean.csv')
    sierraleone = pd.read_csv('../../data/sierraleone-bumbuna_clean.csv')
    togo = pd.read_csv('../../data/togo-dapaong_qc_clean.csv')
    return benin, sierraleone, togo


benin, sierraleone, togo = load_data()

# Sidebar for country selection
st.sidebar.title("Select Country")
countries = ['Benin', 'Sierra Leone', 'Togo']
selected_country = st.sidebar.selectbox("Country", countries)

# Display selected country data
if selected_country == 'Benin':
    df = benin
elif selected_country == 'Sierra Leone':
    df = sierraleone
else:
    df = togo

st.title(f"Solar Data for {selected_country}")

# Boxplot for GHI
st.subheader("GHI Distribution")
fig, ax = plt.subplots()
sns.boxplot(data=df, x='Country', y='GHI', ax=ax)
st.pyplot(fig)

# Top regions table
st.subheader("Top Regions by GHI")
top_regions = df.groupby('Region')['GHI'].mean(
).sort_values(ascending=False).head()
st.table(top_regions)
