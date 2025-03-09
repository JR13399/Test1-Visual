
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('university_student_dashboard_data.csv')

# Group by Term and calculate totals for Applications, Admitted, and Enrolled
term_data = df.groupby('Term').agg({
    'Applications': 'sum',
    'Admitted': 'sum',
    'Enrolled': 'sum'
}).reset_index()

# Display the total applications, admissions, and enrollments per term
st.write("Total Applications, Admissions, and Enrollments per Term", term_data)

# Plot the trends for Applications, Admissions, and Enrollments
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(term_data['Term'], term_data['Applications'], label='Applications', marker='o')
ax.plot(term_data['Term'], term_data['Admitted'], label='Admitted', marker='o')
ax.plot(term_data['Term'], term_data['Enrolled'], label='Enrolled', marker='o')
ax.set_xlabel('Term')
ax.set_ylabel('Count')
ax.set_title('Applications, Admissions, and Enrollments per Term')
ax.legend()

st.pyplot(fig)


# Plot the Retention Rate trends over time
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Term'], df['Retention Rate (%)'], label='Retention Rate (%)', marker='o', color='tab:blue')
ax.set_xlabel('Term')
ax.set_ylabel('Retention Rate (%)')
ax.set_title('Retention Rate Trends Over Time')
ax.legend()

st.pyplot(fig)


# Group by Year and calculate the average Student Satisfaction for each year
yearly_satisfaction = df.groupby('Year')['Student Satisfaction (%)'].mean().reset_index()

# Plot the Student Satisfaction trends over the years
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(yearly_satisfaction['Year'], yearly_satisfaction['Student Satisfaction (%)'], label='Student Satisfaction (%)', marker='o', color='tab:green')
ax.set_xlabel('Year')
ax.set_ylabel('Student Satisfaction (%)')
ax.set_title('Student Satisfaction Scores Over the Years')
ax.legend()

st.pyplot(fig)


# Group by Term or Year and calculate total enrollments for each department
department_enrollment = df[['Term', 'Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']].groupby('Term').sum().reset_index()

# Plot the Enrollment Breakdown by Department
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(department_enrollment['Term'], department_enrollment['Engineering Enrolled'], label='Engineering', marker='o', color='tab:blue')
ax.plot(department_enrollment['Term'], department_enrollment['Business Enrolled'], label='Business', marker='o', color='tab:orange')
ax.plot(department_enrollment['Term'], department_enrollment['Arts Enrolled'], label='Arts', marker='o', color='tab:green')
ax.plot(department_enrollment['Term'], department_enrollment['Science Enrolled'], label='Science', marker='o', color='tab:red')

ax.set_xlabel('Term')
ax.set_ylabel('Enrollments')
ax.set_title('Enrollment Breakdown by Department')
ax.legend()

st.pyplot(fig)


# Filter data for Spring and Fall terms
spring_fall_data = df[df['Term'].isin(['Spring', 'Fall'])]

# Plot comparison for Applications, Admissions, and Enrollments between Spring and Fall terms
fig, ax = plt.subplots(figsize=(10, 6))

# Applications Comparison
ax.plot(spring_fall_data[spring_fall_data['Term'] == 'Spring']['Year'], 
        spring_fall_data[spring_fall_data['Term'] == 'Spring']['Applications'], 
        label='Spring Applications', marker='o', color='tab:blue')

ax.plot(spring_fall_data[spring_fall_data['Term'] == 'Fall']['Year'], 
        spring_fall_data[spring_fall_data['Term'] == 'Fall']['Applications'], 
        label='Fall Applications', marker='o', color='tab:orange')

# Admissions Comparison
ax.plot(spring_fall_data[spring_fall_data['Term'] == 'Spring']['Year'], 
        spring_fall_data[spring_fall_data['Term'] == 'Spring']['Admitted'], 
        label='Spring Admissions', marker='o', color='tab:green')

ax.plot(spring_fall_data[spring_fall_data['Term'] == 'Fall']['Year'], 
        spring_fall_data[spring_fall_data['Term'] == 'Fall']['Admitted'], 
        label='Fall Admissions', marker='o', color='tab:red')

# Enrollments Comparison
ax.plot(spring_fall_data[spring_fall_data['Term'] == 'Spring']['Year'], 
        spring_fall_data[spring_fall_data['Term'] == 'Spring']['Enrolled'], 
        label='Spring Enrollments', marker='o', color='tab:purple')

ax.plot(spring_fall_data[spring_fall_data['Term'] == 'Fall']['Year'], 
        spring_fall_data[spring_fall_data['Term'] == 'Fall']['Enrolled'], 
        label='Fall Enrollments', marker='o', color='tab:brown')

ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_title('Comparison Between Spring and Fall Term Trends')
ax.legend()

st.pyplot(fig)



# Group data by Term and sum enrollments for each department
department_enrollment = df[['Term', 'Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']].groupby('Term').sum().reset_index()

# Plot comparison for each department's enrollment alongside Retention Rate and Satisfaction Levels
fig, ax1 = plt.subplots(figsize=(12, 8))

# Enrollment trends for departments
ax1.plot(department_enrollment['Term'], department_enrollment['Engineering Enrolled'], label='Engineering Enrolled', marker='o', color='tab:blue')
ax1.plot(department_enrollment['Term'], department_enrollment['Business Enrolled'], label='Business Enrolled', marker='o', color='tab:orange')
ax1.plot(department_enrollment['Term'], department_enrollment['Arts Enrolled'], label='Arts Enrolled', marker='o', color='tab:green')
ax1.plot(department_enrollment['Term'], department_enrollment['Science Enrolled'], label='Science Enrolled', marker='o', color='tab:red')

# Set axis labels for enrollment plot
ax1.set_xlabel('Term')
ax1.set_ylabel('Enrollments')
ax1.set_title('Departmental Enrollment Trends')

# Add a second axis to plot Retention Rate and Student Satisfaction
ax2 = ax1.twinx()

# Plot Retention Rate
ax2.plot(df['Term'], df['Retention Rate (%)'], label='Retention Rate (%)', marker='x', color='tab:purple', linestyle='--')

# Plot Student Satisfaction
ax2.plot(df['Term'], df['Student Satisfaction (%)'], label='Student Satisfaction (%)', marker='x', color='tab:brown', linestyle='--')

# Set axis labels for Retention Rate and Satisfaction plot
ax2.set_ylabel('Percentage (%)')

# Add legends for both axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Display the plot
st.pyplot(fig)
