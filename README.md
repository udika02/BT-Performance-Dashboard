# 📘 IISU BT Performance Dashboard
A powerful and interactive web application to analyze student performance using Bloom’s Taxonomy (BT) and generate insights through machine learning and visual reporting.

# 📖 Introduction
The BT Performance Dashboard is a user-friendly, Streamlit-powered web tool designed to assist educators and academic institutions in evaluating student outcomes at various Bloom’s Taxonomy levels. It simplifies the process of tracking cognitive-level progress, analyzing question paper complexity, and predicting future academic performance — all based on weekly and monthly data inputs.

# ✅ Features
Upload and analyze weekly student scores by BT levels.

Upload monthly performance data across four weeks.

Visualize trends using interactive charts.

Predict next month’s academic label using ML-based predictions.

Classify question papers into BT levels automatically.

Evaluate question paper cognitive load based on BT scoring.

Download results and BT-tagged question sheets.

Receive personalized recommendations for students based on performance.

# 🧠 About BT Levels
The app follows Bloom’s Taxonomy to classify student tasks/questions into six levels:

Remember – recall facts, definitions

Understand – explain concepts, describe processes

Apply – solve problems, use information in new ways

Analyze – differentiate, examine relationships

Evaluate – critique, justify decisions

Create – design, produce original work

Each level is assigned a weighted score to quantify learning depth.

# 📁 File Input Details
The dashboard supports three types of Excel files:

Weekly Report – Contains one week’s performance (Q1 to Q10).

Monthly Report – Combines 4-week data with optional performance label.

Question Paper File – Contains question text with optional BT levels.

# 🚀 Getting Started
To run this app locally, follow these steps:

Install the required libraries:

```
pip install streamlit pandas plotly scikit-learn openpyxl
```
Run the Streamlit app:

```
streamlit run bt_analysis_app.py
```

The dashboard will open in your default web browser.

# 📸 Preview

<img width="1777" height="673" alt="image" src="https://github.com/user-attachments/assets/1c75bd73-7d04-4073-9b91-13c493571aaa" />

<img width="1741" height="707" alt="BT_Level Graph" src="https://github.com/user-attachments/assets/7469c719-ff91-4091-b935-d061a8686817" />


# 🤝 Contributing
Contributions are welcome! If you’d like to improve this project—whether it’s fixing bugs, enhancing features, or improving UI—feel free to fork the repository and create a pull request.

