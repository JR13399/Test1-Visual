import streamlit as st
import pandas as pd
import plotly.express as px

# Load data (replace with your file)
data = pd.read_csv("university_student_dashboard_data.csv")
data['Term'] = pd.to_datetime(data['Term'])
data['Year'] = data['Term'].dt.year
data['Month'] = data['Term'].dt.month
data['Season'] = data['Month'].apply(lambda x: 'Spring' if 1 <= x <= 6 else 'Fall')

# Title
st.title("University Dashboard")

# Admissions/Enrollments
st.header("Admissions")
term_summary = data.groupby('Term').sum().reset_index()
st.plotly_chart(px.line(term_summary, x='Term', y=['Applications', 'Admissions', 'Enrollments']))

# Retention
st.header("Retention")
retention = data.groupby('Term')['RetentionRate'].mean().reset_index()
st.plotly_chart(px.line(retention, x='Term', y='RetentionRate'))

# Satisfaction
st.header("Satisfaction")
satisfaction = data.groupby('Year')['SatisfactionScore'].mean().reset_index()
st.plotly_chart(px.line(satisfaction, x='Year', y='SatisfactionScore'))

# Department Enrollments
st.header("Department Enrollments")
dept_enroll = data.groupby(['Term', 'Department'])['Enrollments'].sum().reset_index()
st.plotly_chart(px.bar(dept_enroll, x='Term', y='Enrollments', color='Department'))

# Spring vs Fall
st.header("Spring vs Fall")
season_data = data.groupby(['Year', 'Season']).mean().reset_index()
st.plotly_chart(px.bar(season_data, x='Year', y='Enrollments', color='Season'))
st.plotly_chart(px.bar(season_data, x='Year', y='RetentionRate', color='Season'))
st.plotly_chart(px.bar(season_data, x='Year', y='SatisfactionScore', color='Season'))

# Department Comparisons
st.header("Department Comparisons")
dept_metrics = data.groupby('Department').mean().reset_index()
st.plotly_chart(px.bar(dept_metrics, x='Department', y='RetentionRate'))
st.plotly_chart(px.bar(dept_metrics, x='Department', y='SatisfactionScore'))
st.plotly_chart(px.bar(dept_metrics, x='Department', y='Enrollments'))

st.header("Insights")
st.write("Look for trends in the graphs. Low retention or satisfaction? Investigate why. Compare departments to see which are doing well.")
