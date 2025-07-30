import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="BT Dashboard", layout="wide")
st.title("📘IISU BT Performance Dashboard")

tabs = st.tabs(["Weekly Analysis", "Monthly Report + ML", "Question Paper Analysis"])

# ============================================
# TAB 1: Weekly Performance Analysis
# ============================================
with tabs[0]:
    st.header("📅 Weekly BT Level Performance")
    weekly_file = st.file_uploader("Upload Weekly Student Marks", type=["xlsx"], key="week")
    bt_mapping = {
        1: ['Q1', 'Q2'],
        2: ['Q3', 'Q4'],
        3: ['Q5'],
        4: ['Q6', 'Q7'],
        5: ['Q8'],
        6: ['Q9', 'Q10']
    }
    if weekly_file:
        wdf = pd.read_excel(weekly_file)
        student_col = 'Student' if 'Student' in wdf.columns else wdf.columns[0]
        wdf['Date'] = pd.to_datetime(wdf['Week_Date'], errors='coerce')
        result = wdf[[student_col, 'Date']].copy()
        for level, qs in bt_mapping.items():
            result[f"BT{level}_Accuracy(%)"] = wdf[qs].sum(axis=1) / len(qs) * 100
        result["Total_Score"] = wdf[[f"Q{i}" for i in range(1, 11)]].sum(axis=1)
        result["Overall_Accuracy(%)"] = result["Total_Score"] / 10 * 100
        st.dataframe(result)

# ============================================
# TAB 2: Monthly Analysis + ML + Graphs
# ============================================
with tabs[1]:
    st.header("📈 Monthly Report, Graphs & Prediction")
    monthly_file = st.file_uploader("Upload 4-week Combined File", type=["xlsx"], key="month")

    if monthly_file:
        mdf = pd.read_excel(monthly_file)
        student_col = 'Student' if 'Student' in mdf.columns else mdf.columns[0]
        mdf['Month'] = mdf['Month'].astype(str)
        full_result = mdf[[student_col, 'Month']].copy()

        for w in range(1, 5):
            week_total = mdf[[f"W{w}_Q{i}" for i in range(1, 11)]].sum(axis=1)
            full_result[f"W{w}_Accuracy(%)"] = week_total / 10 * 100

        full_result["Monthly_Avg_Accuracy"] = full_result[
            [f"W{w}_Accuracy(%)" for w in range(1, 5)]].mean(axis=1)

        st.subheader("📊 Monthly Performance Table")
        st.dataframe(full_result)

        st.subheader("📈 Weekly Trend for a Student")
        selected = st.selectbox("Select Student", full_result[student_col])
        selected_row = full_result[full_result[student_col] == selected].iloc[0]
        trend = pd.DataFrame({
            "Week": [f"W{w}" for w in range(1, 5)],
            "Accuracy": [selected_row[f"W{w}_Accuracy(%)"] for w in range(1, 5)]
        })
        fig = px.line(trend, x="Week", y="Accuracy", markers=True, title=f"Trend for {selected}")
        st.plotly_chart(fig)

        if st.button("🤖 Predict Next Month Performance"):
            try:
                X = mdf[[f"W{w}_Q{i}" for w in range(1, 5) for i in range(1, 11)]]
                y = mdf['Monthly_Label'] if 'Monthly_Label' in mdf.columns else None
                if y is not None:
                    le = LabelEncoder()
                    y_encoded = le.fit_transform(y)
                    clf = RandomForestClassifier()
                    clf.fit(X, y_encoded)
                    preds = clf.predict(X)
                    full_result['Predicted_Label'] = le.inverse_transform(preds)
                else:
                    st.warning("Monthly_Label column not found for training.")
            except Exception as e:
                st.error(f"ML Error: {e}")

        st.subheader("💡 Student Recommendations")
        def make_reco(row):
            recos = []
            if row['Monthly_Avg_Accuracy'] < 50:
                recos.append("Needs support on core concepts")
            if row['W4_Accuracy(%)'] < row['W1_Accuracy(%)']:
                recos.append("Declining trend — encourage revision")
            if 'Predicted_Label' in row and row['Predicted_Label'] == 'Poor':
                recos.append("High risk student — 1-on-1 help suggested")
            return "; ".join(recos) if recos else "Keep up the good work"

        full_result['Recommendation'] = full_result.apply(make_reco, axis=1)
        st.dataframe(full_result)

# ============================================
# TAB 3: Question Paper BT Analysis
# ============================================
# BT scoring based on Table 1.1
bt_score_map = {
    "Remember": 5,
    "Understand": 5,
    "Apply": 10,
    "Analyze": 10,
    "Evaluate": 20,
    "Create": 20
}

# BT classifier (simple keyword-based)
def classify_bt_level(question):
    question = question.lower()
    if any(word in question for word in ['define', 'list', 'name', 'state']):
        return 'Remember'
    elif any(word in question for word in ['explain', 'describe', 'summarize']):
        return 'Understand'
    elif any(word in question for word in ['apply', 'use', 'solve']):
        return 'Apply'
    elif any(word in question for word in ['analyze', 'differentiate', 'compare']):
        return 'Analyze'
    elif any(word in question for word in ['evaluate', 'justify', 'critique']):
        return 'Evaluate'
    elif any(word in question for word in ['create', 'design', 'develop']):
        return 'Create'
    else:
        return 'Unknown'

# Difficulty Interpretation based on Table 1.2
def interpret_score(total_score):
    if total_score >= 150:
        return "Excellent (High-order focused)", "🟢"
    elif total_score >= 100:
        return "Moderate (Balanced)", "🟡"
    else:
        return "Low cognitive load", "🔴"

# TAB 3: Question Paper BT Level Analysis
with tabs[2]:
    st.header("📋 Question Paper BT Level Analysis")
    qp_file = st.file_uploader("Upload Question Paper BT Tagging", type=["xlsx"], key="qp")

    if qp_file:
        qdf = pd.read_excel(qp_file)

        # Add BT_Level if not present
        if 'BT_Level' not in qdf.columns or qdf['BT_Level'].isnull().all():
            st.info("BT_Level column missing or empty – auto-tagging questions.")
            qdf['BT_Level'] = qdf['Question Text'].apply(classify_bt_level)

        # Assign scores per question based on BT_Level
        qdf['BT_Score'] = qdf['BT_Level'].map(bt_score_map).fillna(0)

        # Summary Table
        bt_summary = qdf.groupby("BT_Level")['BT_Score'].agg(['count', 'sum']).reset_index()
        bt_summary.columns = ['BT_Level', 'Count', 'Total_Score']
        bt_summary['Percentage'] = round((bt_summary['Count'] / bt_summary['Count'].sum()) * 100, 2)

        st.subheader("📊 BT Level Score Summary")
        st.dataframe(bt_summary)

        # Graph
        fig = px.bar(bt_summary, x="BT_Level", y="Total_Score", title="BT Score Distribution", color="BT_Level")
        st.plotly_chart(fig)

        # Total Score and Difficulty
        total_score = qdf['BT_Score'].sum()
        difficulty, emoji = interpret_score(total_score)
        bt_score_map = {
    "Remember":   5,
    "Understand": 5,
    "Apply":     10,
    "Analyze":   10,
    "Evaluate":  20,
    "Create":    20
}

        st.subheader("📈 Paper Cognitive Load Evaluation")
        st.markdown(f"**Total BT Score:** `{total_score}`")
        st.markdown(f"**Paper Quality:** {emoji} **{difficulty}**")

        # Option to download updated file
        st.download_button("📥 Download BT-Tagged File", data=qdf.to_csv(index=False), file_name="BT_Analyzed_Question_Paper.csv")