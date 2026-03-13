import matplotlib.pyplot as plt
import seaborn as sns

def plot_gdp_trends(df):
    """Plot GDP trend for top 5 countries"""
    latest_year = df['Year'].max()
    top_countries = df[df['Year'] == latest_year].sort_values(by='GDP', ascending=False)['Country'].head(5)
    df_top = df[df['Country'].isin(top_countries)]
    
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df_top, x='Year', y='GDP', hue='Country', marker='o')
    plt.title('Top 5 Countries by GDP Over Time')
    plt.ylabel('GDP (USD)')
    plt.xlabel('Year')
    plt.show()
