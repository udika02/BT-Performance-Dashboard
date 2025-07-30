📘 IISU BT Performance Dashboard
An interactive Streamlit application designed for evaluating and visualizing student performance using Bloom’s Taxonomy (BT). The app enables detailed analysis of weekly and monthly academic trends, integrates machine learning for predictive insights, and classifies question papers by cognitive levels.

🔍 Overview
This dashboard offers educators, institutions, and curriculum designers a powerful tool to:

Track student performance across BT levels.

Predict monthly academic outcomes using machine learning.

Automatically classify and evaluate question papers for cognitive load.

🚀 Key Features
🗓 Weekly BT-Level Performance
Upload weekly student assessments.

Automatic calculation of accuracy per BT level.

Visual and tabular summaries.

📊 Monthly Analysis + ML Prediction
Analyze 4-week performance trends.

Predict next-month performance using Random Forest Classifier.

Generate student-specific recommendations based on accuracy trends and model outcomes.

🧠 Question Paper Analysis
Automatically classify questions using BT-level keywords.

Compute BT scores and evaluate overall cognitive load.

Visual summaries and downloadable tagged files.

📂 Expected File Formats
File	                         Purpose	                       Key Columns
Weekly_report.xlsx	           Weekly student marks	           Student, Week_Date, Q1 to Q10
Monthly_report.xlsx     	     Combined 4-week report	         Student, Month, W1_Q1 to W4_Q10, Monthly_Label (optional)
ML_BT_Level_Questions.xlsx	   Question paper tagging	         Question Text, BT_Level (optional)

⚙️ Getting Started
Prerequisites
Ensure Python ≥ 3.7 is installed. Install dependencies via:

bash
Copy
Edit
pip install streamlit pandas plotly scikit-learn openpyxl
Running the Application
bash
Copy
Edit
streamlit run bt_analysis_app.py
🧠 BT Level Classification Logic
BT Level	Common Action Verbs	Score
Remember	define, list, state, name	5
Understand	explain, describe, summarize	5
Apply	apply, use, solve	10
Analyze	analyze, differentiate, compare	10
Evaluate	evaluate, justify, critique	20
Create	create, design, develop	20

📈 Cognitive Load Interpretation
Total BT Score	Interpretation	Indicator
≥ 150	High-Order Focused	🟢
100 – 149	Balanced Cognitive Load	🟡
< 100	Low Cognitive Load	🔴

🛠 Tech Stack
Frontend: Streamlit

Backend/Data: Python, pandas, scikit-learn

Visualization: Plotly

File Handling: openpyxl

📎 Sample Use Cases
Academic performance monitoring

Automated Bloom’s Taxonomy classification

Question paper quality assurance

Adaptive support recommendations for students

📬 Contact & Contributions
For feature requests, bugs, or contributions, please open an issue or submit a pull request on GitHub.

