import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('twitter_data.csv')

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Calculate total likes, shares, and tweets per author
total_likes_per_author = df.groupby('author')['number_of_likes'].sum()
total_shares_per_author = df.groupby('author')['number_of_shares'].sum()
total_tweets_per_author = df.groupby('author').size()

# Create a figure with 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Extract individual axes
ax1, ax2 = axes.flatten()

# Plot 1: Total Likes and Shares per Author
total_likes_and_shares = pd.DataFrame({
    'Total Likes': total_likes_per_author,
    'Total Shares': total_shares_per_author
}).fillna(0)

total_likes_and_shares.plot(kind='bar', ax=ax1, color=['skyblue', 'salmon'])
ax1.set_title('Total Likes and Shares per Author')
ax1.set_xlabel('Author')
ax1.set_ylabel('Count')
ax1.legend(title='Metrics')
ax1.tick_params(axis='x', rotation=70)  # Rotate x labels for better readability

# Plot 2: Total Number of Tweets per Author
total_tweets_per_author.plot(kind='bar', color='lightblue', ax=ax2)
ax2.set_title('Total Number of Tweets per Author')
ax2.set_xlabel('Author')
ax2.set_ylabel('Total Number of Tweets')
ax2.tick_params(axis='x', rotation=70)  # Rotate x labels for better readability

# Adjust layout to fit labels and titles
plt.tight_layout()

# Show the plot
plt.show()
