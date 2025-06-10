import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

st.title("📊 Netflix User Behavior Analysis")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/KumariAnjaliRout/netflix-user-behavior-analysis/main/netflix_titles.csv"
    return pd.read_csv(url)

df = load_data()

# Data cleaning
df = df.dropna(subset=['director', 'cast', 'country'])
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df = df.dropna(subset=['date_added'])
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

st.subheader("🗂 Dataset Preview")
st.dataframe(df.head())

# Plot 1: Content type distribution
st.subheader("📺 Distribution of Content Types")
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x='type', palette='Set2', ax=ax1)
st.pyplot(fig1)

# Plot 2: Top 10 countries by content
st.subheader("🌍 Top 10 Countries by Content")
top_countries = df['country'].value_counts().head(10)
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='mako', ax=ax2)
st.pyplot(fig2)

# Plot 3: Content added over the years
st.subheader("📅 Content Added Over the Years")
content_by_year = df['year_added'].value_counts().sort_index()
fig3, ax3 = plt.subplots(figsize=(10, 5))
content_by_year.plot(kind='line', marker='o', color='coral', ax=ax3)
ax3.set_xlabel("Year")
ax3.set_ylabel("Number of Titles")
ax3.grid(True)
st.pyplot(fig3)

# Plot 4: Top 10 genres
st.subheader("🎭 Top 10 Genres")
all_genres = df['listed_in'].str.split(', ', expand=True).stack()
top_genres = all_genres.value_counts().head(10)
fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='coolwarm', ax=ax4)
st.pyplot(fig4)
