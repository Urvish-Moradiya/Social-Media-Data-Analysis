import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('facebook_data.csv')

bins = [0, 20, 30, 40, 50, 60, 100]
labels = ['<20', '21-30', '31-40', '41-50', '51-60', '60+']

# Create an age group column
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

# Count the number of users in each age group
age_group_counts = df['age_group'].value_counts().sort_index()

# Count the number of users by gender
gender_counts = df['gender'].value_counts()

# Create a figure with 2 subplots (side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

# Plot the age distribution
ax1.bar(age_group_counts.index, age_group_counts.values, color='blue')
ax1.set_title('Number of Users by Age Group')
ax1.set_xlabel('Age Group')
ax1.set_ylabel('Number of Users')
ax1.tick_params(axis='x', rotation=45)  # Rotate x labels for better readability

# Plot the gender distribution
ax2.bar(gender_counts.index, gender_counts.values, color=['skyblue', 'pink'])
ax2.set_title('Number of Users by Gender')
ax2.set_xlabel('Gender')
ax2.set_ylabel('Number of Users')

# Adjust layout to fit labels and titles
plt.tight_layout()

# Show the plot
plt.show()