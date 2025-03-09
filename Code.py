!pip install streamlit plotly

import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
file_path = "university_student_dashboard_data.csv"
df = pd.read_csv(file_path)

# Sidebar Filters
years = sorted(df['Year'].unique())
terms = df['Term'].unique()
selected_year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)
selected_term = st.sidebar.radio("Select Term", terms)

df_filtered = df[(df['Year'] == selected_year) & (df['Term'] == selected_term)]

# KPIs
st.title("University Admissions Dashboard")
st.metric("Total Applications", df_filtered['Applications'].values[0])
st.metric("Total Admitted", df_filtered['Admitted'].values[0])
st.metric("Total Enrolled", df_filtered['Enrolled'].values[0])

# Retention & Satisfaction Trends
fig_retention = px.line(df, x='Year', y='Retention Rate (%)', color='Term', title="Retention Rate Over Time")
fig_satisfaction = px.line(df, x='Year', y='Student Satisfaction (%)', color='Term', title="Satisfaction Score Over Time")
st.plotly_chart(fig_retention)
st.plotly_chart(fig_satisfaction)

# Enrollment Breakdown
fig_enrollment = px.bar(df_filtered.melt(id_vars=['Year', 'Term'], 
                                         value_vars=['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']),
                         x='variable', y='value', title="Enrollment Breakdown by Department")
st.plotly_chart(fig_enrollment)

# Spring vs Fall Comparison
fig_comparison = px.bar(df, x='Year', y='Enrolled', color='Term', barmode='group', title="Enrollment Trends: Spring vs Fall")
st.plotly_chart(fig_comparison)
