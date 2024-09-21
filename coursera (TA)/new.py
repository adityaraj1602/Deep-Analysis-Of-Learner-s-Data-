import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r'C:\.vscode\coursera (TA)\Coursera MASKED data.xlsx'  # Corrected path using raw string
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Data Cleaning and Preparation
df['Completed'].fillna('No', inplace=True)
df['Learning Hours Spent'].fillna(0, inplace=True)
df.drop_duplicates(inplace=True)
df['Course Name'] = df['Course Name'].str.title()

# Ensure 'Course Grade' is present and clean
if 'Course Grade' in df.columns:
    df['Course Grade'].fillna(0, inplace=True)

# Data Exploration and Analysis
# Descriptive Statistics
descriptive_stats = df.describe(include='all')
print(descriptive_stats)

# Distribution of Course Durations
sns.histplot(df['Duration(in hrs)'], bins=10)
plt.title('Distribution of Course Durations')
plt.xlabel('Duration (in hours)')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
plt.show()

# Courses Completed by Department
completed_courses_by_dept = df[df['Completed'] == 'Yes'].groupby('Department')['Course Name'].count()
completed_courses_by_dept.plot(kind='bar')
plt.title('Courses Completed by Department')
plt.xlabel('Department')
plt.ylabel('Number of Courses Completed')
plt.savefig('bar_chart.png')
plt.show()

# Completion Rate by Department
completion_rate_by_dept = df.groupby('Department')['Completed'].value_counts(normalize=True).unstack().fillna(0)['Yes'] * 100
completion_rate_by_dept.plot(kind='bar')
plt.title('Completion Rate by Department')
plt.xlabel('Department')
plt.ylabel('Completion Rate (%)')
plt.savefig('completion_rate.png')
plt.show()

# Average Learning Hours Spent per Course by Department
avg_learning_hours_by_dept = df.groupby('Department')['Learning Hours Spent'].mean()
avg_learning_hours_by_dept.plot(kind='bar')
plt.title('Average Learning Hours Spent per Course by Department')
plt.xlabel('Department')
plt.ylabel('Average Learning Hours Spent')
plt.savefig('avg_learning_hours.png')
plt.show()

# Top 5 Most Popular Courses
top_5_courses = df['Course Name'].value_counts().head(5)
top_5_courses.plot(kind='bar')
plt.title('Top 5 Most Popular Courses')
plt.xlabel('Course Name')
plt.ylabel('Number of Enrollments')
plt.savefig('top_5_courses.png')
plt.show()

# Learning Hours Distribution by Course
plt.figure(figsize=(10, 8))
sns.boxplot(data=df, x='Course Name', y='Learning Hours Spent')
plt.xticks(rotation=90)
plt.title('Learning Hours Distribution by Course')
plt.xlabel('Course Name')
plt.ylabel('Learning Hours Spent')
plt.savefig('learning_hours_distribution.png')
plt.show()

# Department-wise Course Enrollment Trends
df.set_index('Enrollment Time', inplace=True)
dept_enrollment_trends = df.groupby('Department').resample('M')['Course Name'].count().unstack(level=0).fillna(0)
dept_enrollment_trends.plot()
plt.title('Department-wise Course Enrollment Trends')
plt.xlabel('Time')
plt.ylabel('Number of Enrollments')
plt.legend(title='Department')
plt.savefig('dept_enrollment_trends.png')
plt.show()

# Completion Rate by Program
completion_rate_by_program = df.groupby('Program Name')['Completed'].value_counts(normalize=True).unstack().fillna(0)['Yes'] * 100
completion_rate_by_program.plot(kind='bar')
plt.title('Completion Rate by Program')
plt.xlabel('Program Name')
plt.ylabel('Completion Rate (%)')
plt.savefig('completion_rate_by_program.png')
plt.show()

# Impact of Learning Hours on Completion
sns.boxplot(data=df, x='Completed', y='Learning Hours Spent')
plt.title('Impact of Learning Hours on Completion')
plt.xlabel('Completed')
plt.ylabel('Learning Hours Spent')
plt.savefig('learning_hours_impact.png')
plt.show()

# Top Performing Departments
top_performing_depts = df[df['Completed'] == 'Yes'].groupby('Department')['Learning Hours Spent'].mean().sort_values(ascending=False)
top_performing_depts.plot(kind='bar')
plt.title('Top Performing Departments by Average Learning Hours')
plt.xlabel('Department')
plt.ylabel('Average Learning Hours Spent')
plt.savefig('top_performing_depts.png')
plt.show()

# Average Completion Time by Department
df['Completion Time'] = pd.to_datetime(df['Completion Time'], errors='coerce')
df['Completion Time (days)'] = (df['Completion Time'] - df.index).dt.days
avg_completion_time_by_dept = df.groupby('Department')['Completion Time (days)'].mean().dropna()
avg_completion_time_by_dept.plot(kind='bar')
plt.title('Average Completion Time by Department')
plt.xlabel('Department')
plt.ylabel('Average Completion Time (days)')
plt.savefig('avg_completion_time.png')
plt.show()

# KPI Graphs - Course Grade
if 'Course Grade' in df.columns:
    # Distribution of Course Grades
    sns.histplot(df['Course Grade'], bins=10)
    plt.title('Distribution of Course Grades')
    plt.xlabel('Course Grade')
    plt.ylabel('Frequency')
    plt.savefig('course_grade_distribution.png')
    plt.show()

    # Learning Hours vs. Course Grade
    sns.scatterplot(data=df, x='Learning Hours Spent', y='Course Grade')
    plt.title('Learning Hours vs. Course Grade')
    plt.xlabel('Learning Hours Spent')
    plt.ylabel('Course Grade')
    plt.savefig('learning_hours_vs_course_grade.png')
    plt.show()

    # Average Course Grade by Department
    avg_course_grade_by_dept = df.groupby('Department')['Course Grade'].mean()
    avg_course_grade_by_dept.plot(kind='bar')
    plt.title('Average Course Grade by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Course Grade')
    plt.savefig('avg_course_grade_by_dept.png')
    plt.show()

# Advanced Analysis
# Trend Analysis
df['Enrollment Time'] = pd.to_datetime(df['Enrollment Time'], errors='coerce')
df['Completion Time'] = pd.to_datetime(df['Completion Time'], errors='coerce')

df.set_index('Enrollment Time').resample('M')['Course Name'].count().plot()
plt.title('Courses Enrolled Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Courses')
plt.savefig('enrollment_trend.png')
plt.show()

df.set_index('Completion Time').resample('M')['Course Name'].count().plot()
plt.title('Courses Completed Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Courses')
plt.savefig('completion_trend.png')
plt.show()

# Completion Time Analysis
sns.histplot(df['Completion Time (days)'].dropna(), bins=20)
plt.title('Distribution of Completion Time (days)')
plt.xlabel('Completion Time (days)')
plt.ylabel('Frequency')
plt.savefig('completion_time_distribution.png')
plt.show()

# Correlation Analysis
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
plt.show()

# Summary Report by Department
summary_report = df.groupby(['Department', 'Program Name']).agg({
    'Duration(in hrs)': 'sum',
    'Course Name': 'count',
    'Course Grade': 'mean'
}).rename(columns={'Course Name': 'Total Courses', 'Course Grade': 'Average Grade'}).reset_index()
print(summary_report)
