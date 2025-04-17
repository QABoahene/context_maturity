# 🎵 Context Maturity Project

**Author:** Q.A. Boahene  
**Created:** April 2025  
**License:** MIT  
**Version:** 1.0.0

---

## 📌 Project Overview

The **Context Maturity Project** explores how the lyrical themes, sentiments, and complexity of an artist's discography evolve over time. It combines data science, AI, and visual storytelling in a Streamlit-powered web experience.

---

## 🔍 Core Features

- 🎼 Lyric + album data collection (Musixmatch + Spotify)  
- 🧹 NLP preprocessing (cleaning, formatting, filtering)  
- 🧠 Zero-shot theme detection using transformer models  
- 😃 Sentiment, diversity, and readability analysis  
- 📊 Visualisation of trends and word clouds  
- 🌐 Streamlit UI with artist selector  
- 🚀 Deployment via Streamlit Cloud  

---

## 📁 Project Structure

```
context_maturity/
├── data/                # Raw, processed, and external datasets
├── notebooks/           # Jupyter notebooks for analysis & prototyping
├── src/                 # Source code for data, models, visualisations
├── streamlit_app/       # Frontend web UI (Streamlit)
├── reports/             # Output visualisations and figures
├── tests/               # Unit tests
```

---

## 🚀 Getting Started

### 📦 Install Requirements

Run the following command to install required dependencies:

```
pip install -r requirements.txt
```

### 🖼️ Launch the Web App

Start the Streamlit interface:

```
streamlit run streamlit_app/app.py
```

---

## 📈 Roadmap

1. Data collection and cleaning  
2. Lyric analysis using zero-shot & sentiment models  
3. Streamlit app for interactive exploration  
4. Deployment & YouTube walkthrough series  

---

## 🤝 Contributions

Feel free to fork this repo and open a PR!  
Bug reports and feature suggestions welcome via Issues.