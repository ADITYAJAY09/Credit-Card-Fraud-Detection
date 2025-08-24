# app.py

# This is the complete and final script for your Streamlit dashboard.
# It integrates all the fixes and features we've discussed.

# --- Import Libraries ---
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# --- Set Streamlit Page Configuration ---
# This sets the title and layout of the app for a wide, full-screen view.
st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide",
)

# --- Load Data from CSV ---
# The @st.cache_data decorator caches the data so it only loads once,
# which makes the app run much faster.
@st.cache_data
def load_data():
    """Loads and preprocesses the data from the CSV file."""
    try:
        df = pd.read_csv("reports/model_predictions_for_tableau.csv")
        # Corrected: Use 'Time' and 'Amount' columns from the CSV
        df['Time'] = pd.to_datetime(df['Time'], unit='s')
        
        # We need to map the 0 and 1 classes to descriptive labels for the charts
        class_mapping = {0: 'Legitimate', 1: 'Fraud'}
        df['Actual_Class'] = df['Actual_Class'].map(class_mapping)
        df['Predicted_Class'] = df['Predicted_Class'].map(class_mapping)
        
        return df
    except FileNotFoundError:
        st.error("Error: The file 'model_predictions_for_tableau.csv' was not found.")
        st.stop()

# Load the prepared data
df = load_data()

# --- Title and Header ---
st.markdown("<h1 style='text-align: center; color: white;'>Dashboard for monitoring fraud and money laundering transactions</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: lightgray;'>This dashboard showcases key metrics, alerts, and investigations for fraud detection.</p>", unsafe_allow_html=True)

# --- Layout: Main Columns ---
# This creates a two-column layout for the top section of the dashboard
col1, col2 = st.columns([1, 2.5])

with col1:
    st.header("Recent Activity")
    with st.container(border=True):
        # KPI: Total Transactions
        total_transactions = df.shape[0]
        st.subheader("Total transactions")
        st.title(f"{total_transactions:,}")

        # KPI: Unusual Transactions (based on model prediction)
        unusual_transactions = df[df['Predicted_Class'] == 'Fraud'].shape[0]
        st.subheader("Unusual transactions")
        st.title(f"{unusual_transactions:,}")

with col2:
    st.header("Daily Fraud and Verification")
    
    # --- Bar Chart: Daily Trend ---
    # Create a 'Time of day' column as a clean integer hour
    df_daily = df.copy()
    df_daily['Time of day'] = df_daily['Time'].dt.hour
    
    # Group by Time and Predicted Class to get the counts for the bar chart
    df_chart = df_daily.groupby(['Time of day', 'Predicted_Class']).size().unstack(fill_value=0).reset_index()
    
    # Create the stacked bar chart using Plotly Express
    fig = px.bar(
        df_chart,
        x='Time of day',
        y=['Legitimate', 'Fraud'], # Use the correct column names
        barmode='stack',
        title='Transactions by Time of Day',
        labels={'value': 'Transactions', 'Time of day': 'Time of day'},
        color_discrete_map={'Legitimate': '#F9A31A', 'Fraud': '#8C8C8C'}
    )
    
    # Update layout to match the image style and make it dark-themed
    fig.update_layout(
        plot_bgcolor="#464A50",
        paper_bgcolor="#464A50",
        font_color="#FFFFFF",
        title_font_color="#FFFFFF"
    )
    fig.update_xaxes(title_font_color="#FFFFFF", tickfont_color="#FFFFFF")
    fig.update_yaxes(title_font_color="#FFFFFF", tickfont_color="#FFFFFF")
    
    st.plotly_chart(fig, use_container_width=True)

# --- Layout: Alerts and Investigation ---
col_alerts, col_investigation = st.columns([2, 3])

with col_alerts:
    st.header("Unusual transaction alerts")
    with st.container(border=True):
        # We don't have this data, so we'll use a placeholder from the image
        st.markdown("<div style='background-color:#595959;padding:10px;'>Client **Johnson** did more than 10 transactions at same time a day totaling $550,000</div>", unsafe_allow_html=True)
        st.markdown("<div style='background-color:#595959;padding:10px;margin-top:10px;'>Client **Martha** did more than 25 transactions in same month totaling $2,550,000</div>", unsafe_allow_html=True)

with col_investigation:
    st.header("Ongoing investigation")
    with st.container(border=True):
        # This is a placeholder table to match the image
        investigation_data = {
            'Bank': ['Federal Bank USA', 'Bank of Canada', 'Bank of America'],
            'Client': ['Johnson', 'Martha', 'John'],
            'Assigned to': ['Agent Smith', 'Agent Smith', 'Agent Johnson'],
            'Progress': ['Investigation opened', 'In peer review', 'Confirmed as unusual']
        }
        st.dataframe(pd.DataFrame(investigation_data), hide_index=True, use_container_width=True)

# --- Layout: Donut Chart and Metrics ---
st.header("Today's Verification")

col_verification, col_empty = st.columns([1, 1])

with col_verification:
    
    # --- Donut Chart ---
    cm = confusion_matrix(df['Actual_Class'], df['Predicted_Class'])
    cm_df = pd.DataFrame(cm, index=['Actual Legitimate', 'Actual Fraud'], columns=['Predicted Legitimate', 'Predicted Fraud'])
    
    # Calculate Donut Chart Metrics
    verified_as_valid = cm_df.loc['Actual Legitimate', 'Predicted Legitimate']
    unassigned = cm_df.loc['Actual Legitimate', 'Predicted Fraud'] + cm_df.loc['Actual Fraud', 'Predicted Legitimate']
    confirmed_as_fraudulent = cm_df.loc['Actual Fraud', 'Predicted Fraud']
    
    pie_data = pd.DataFrame({
        'Status': ['Verified as Valid', 'Confirmed as Fraudulent', 'Unassigned'],
        'Count': [verified_as_valid, confirmed_as_fraudulent, unassigned]
    })
    
    fig_pie = px.pie(
        pie_data, 
        values='Count', 
        names='Status', 
        hole=0.6,
        color='Status',
        color_discrete_map={'Verified as Valid': '#F9A31A', 'Confirmed as Fraudulent': '#8C8C8C', 'Unassigned': '#FFFFFF'}
    )
    fig_pie.update_layout(showlegend=False)
    
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # --- Metrics for Donut Chart ---
    col_pie1, col_pie2 = st.columns(2)
    with col_pie1:
        st.metric(label="Verified as Valid", value=verified_as_valid)
    with col_pie2:
        st.metric(label="Confirmed as Fraudulent", value=confirmed_as_fraudulent)

