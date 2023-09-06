import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date',parse_dates=True)

# Clean data
top25, bottom25 = df.quantile(0.975),df.quantile(0.025)
df = df[(df >= bottom25) & (df <= top25)].dropna() # Boolean array where value > bottom 2.5% or values < upper 2.5% is TRUE and then used to filter df

def draw_line_plot():
    fig,ax = plt.subplots(figsize=(20,7))
    ax.plot(df['value'],color = 'red')
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',xlabel='Date',ylabel='Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df.index.month
    df_bar['year'] = df.index.year
    df_bar = df_bar.groupby(['year','month'])['value'].mean().unstack()
    ax = df_bar.plot(kind='bar',)
    fig = ax.get_figure()
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    ax.set(xlabel='Years',ylabel='Average Page Views')
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()