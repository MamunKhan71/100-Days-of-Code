# -*- coding: utf-8 -*-
"""Google Play Store App Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lS6o2WCL82JP0in8gNqRTUWwe4Fq032F

# Introduction

In this notebook, we will do a comprehensive analysis of the Android app market by comparing thousands of apps in the Google Play store.

# About the Dataset of Google Play Store Apps & Reviews

**Data Source:** <br>
App and review data was scraped from the Google Play Store by Lavanya Gupta in 2018. Original files listed [here](
https://www.kaggle.com/lava18/google-play-store-apps).

# Import Statements
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

"""# Notebook Presentation"""

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

"""# Read the Dataset"""

df_apps = pd.read_csv('/content/drive/MyDrive/100 Days of Code/Google Play Store Project/apps.csv')

"""# Data Cleaning

**Challenge**: How many rows and columns does `df_apps` have? What are the column names? Look at a random sample of 5 different rows with [.sample()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html).
"""

df_apps.head()

df_apps.shape

df_apps.columns.values

"""### Drop Unused Columns

**Challenge**: Remove the columns called `Last_Updated` and `Android_Version` from the DataFrame. We will not use these columns. 
"""

df_apps.drop(["Last_Updated", "Android_Ver"], inplace=True, axis=1)

df_apps.sample(5)



"""### Find and Remove NaN values in Ratings

**Challenge**: How may rows have a NaN value (not-a-number) in the Ratings column? Create DataFrame called `df_apps_clean` that does not include these rows. 
"""

df_apps.isna().sum()

df_apps_clean = df_apps.dropna()

df_apps_clean.isna().sum()

"""### Find and Remove Duplicates

**Challenge**: Are there any duplicates in data? Check for duplicates using the [.duplicated()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) function. How many entries can you find for the "Instagram" app? Use [.drop_duplicates()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) to remove any duplicates from `df_apps_clean`. 

"""

df_apps_clean.duplicated()

duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
df_apps_clean[df_apps_clean.App == 'Instagram']

df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])

df_apps_clean[df_apps_clean.App == 'Instagram']

df_apps_clean.shape

"""# Find Highest Rated Apps

**Challenge**: Identify which apps are the highest rated. What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?
"""

df_max = df_apps_clean[df_apps_clean.Rating == df_apps_clean.Rating.max()]
 df_max

"""# Find 5 Largest Apps in terms of Size (MBs)

**Challenge**: What's the size in megabytes (MB) of the largest Android apps in the Google Play Store. Based on the data, do you think there could be limit in place or can developers make apps as large as they please? 
"""

df_size = df_apps_clean[df_apps_clean.Size_MBs == df_apps_clean.Size_MBs.values.max()]
df_size

"""# Find the 5 App with Most Reviews

**Challenge**: Which apps have the highest number of reviews? Are there any paid apps among the top 50?
"""

top_apps = df_apps_clean.sort_values('Reviews', ascending=False)
top_apps.head()

"""# Plotly Pie and Donut Charts - Visualise Categorical Data: Content Ratings"""

ratings = df_apps_clean.Content_Rating.value_counts()
ratings

import plotly.express as px

fig = px.pie(labels=ratings.index, values=ratings.values, title="Content Rating", names=ratings.index, hole=.6)

fig.update_traces(textposition='inside', textinfo='percent', textfont_size=15)

fig.show()

"""# Numeric Type Conversion: Examine the Number of Installs

**Challenge**: How many apps had over 1 billion (that's right - BILLION) installations? How many apps just had a single install? 

Check the datatype of the Installs column.

Count the number of apps at each level of installations. 

Convert the number of installations (the Installs column) to a numeric data type. Hint: this is a 2-step process. You'll have make sure you remove non-numeric characters first. 
"""

df_apps_clean.head()

billion_apps = df_apps_clean.info()
billion_apps

df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()

df_apps_clean

df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', '')
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
df_apps_clean[['App', 'Price']].sort_values('Price', ascending=False)[:20]



"""# Find the Most Expensive Apps, Filter out the Junk, and Calculate a (ballpark) Sales Revenue Estimate

Let's examine the Price column more closely.

**Challenge**: Convert the price column to numeric data. Then investigate the top 20 most expensive apps in the dataset.

Remove all apps that cost more than $250 from the `df_apps_clean` DataFrame.

Add a column called 'Revenue_Estimate' to the DataFrame. This column should hold the price of the app times the number of installs. What are the top 10 highest grossing paid apps according to this estimate? Out of the top 10 highest grossing paid apps, how many are games?

"""



"""### The most expensive apps sub $250"""

df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values('Price', ascending=False).head(5)

"""### Highest Grossing Paid Apps (ballpark estimate)"""

df_apps_clean['Revenue Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
df_apps_clean.sort_values('Revenue Estimate', ascending=False).head(10)

"""# Plotly Bar Charts & Scatter Plots: Analysing App Categories"""







"""### Vertical Bar Chart - Highest Competition (Number of Apps)"""



"""### Horizontal Bar Chart - Most Popular Categories (Highest Downloads)"""

df_apps_clean.Category.nunique()

top10_category = df_apps_clean.Category.value_counts()[:10]
top10_category

bar = px.bar(x=top10_category.index, y=top10_category.values)
bar.show()

category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)
h_bar = px.bar(x=category_installs.Installs, y =category_installs.index, orientation='h')
h_bar.update_layout(xaxis_title='Number of downlaods', yaxis_title='Category')
h_bar.show()

"""### Category Concentration - Downloads vs. Competition

**Challenge**: 
* First, create a DataFrame that has the number of apps in one column and the number of installs in another:

<img src=https://imgur.com/uQRSlXi.png width="350">

* Then use the [plotly express examples from the documentation](https://plotly.com/python/line-and-scatter/) alongside the [.scatter() API reference](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html)to create scatter plot that looks like this. 

<img src=https://imgur.com/cHsqh6a.png>

*Hint*: Use the size, hover_name and color parameters in .scatter(). To scale the yaxis, call .update_layout() and specify that the yaxis should be on a log-scale like so: yaxis=dict(type='log') 
"""

newCat = df_apps_clean.groupby('Category').agg({'App': pd.Series.count, 'Installs': pd.Series.sum})
newCat.sort_values('App', ascending=False)

cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})

cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how='inner')
cat_merged_df.sort_values('Installs', ascending=False)

new_shape = px.scatter(
    cat_merged_df, x='App', 
    y='Installs', 
    title='Category Concentration', 
    size='App', 
    hover_name=cat_merged_df.index, 
    color='Installs',
)
new_shape.update_layout(
    xaxis_title='Number of Apps(Lower=More Concentrated)', 
    yaxis_title = "Installs", 
    yaxis=dict(type='log'), 
)
new_shape.show()

"""# Extracting Nested Data from a Column

**Challenge**: How many different types of genres are there? Can an app belong to more than one genre? Check what happens when you use .value_counts() on a column with nested values? See if you can work around this problem by using the .split() function and the DataFrame's [.stack() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html). 

"""

df_genres = len(df_apps_clean.Genres.unique())
df_genres

df_genres = df_apps_clean.Genres.value_counts()
df_genres

stack = df_apps_clean.Genres.str.split(';', expand=True).stack()

"""# Colour Scales in Plotly Charts - Competition in Genres

**Challenge**: Can you create this chart with the Series containing the genre data? 

<img src=https://imgur.com/DbcoQli.png width=400>

Try experimenting with the built in colour scales in Plotly. You can find a full list [here](https://plotly.com/python/builtin-colorscales/). 

* Find a way to set the colour scale using the color_continuous_scale parameter. 
* Find a way to make the color axis disappear by using coloraxis_showscale.
"""



"""# Grouped Bar Charts: Free vs. Paid Apps per Category"""



"""**Challenge**: Use the plotly express bar [chart examples](https://plotly.com/python/bar-charts/#bar-chart-with-sorted-or-ordered-categories) and the [.bar() API reference](https://plotly.com/python-api-reference/generated/plotly.express.bar.html#plotly.express.bar) to create this bar chart: 

<img src=https://imgur.com/LE0XCxA.png>

You'll want to use the `df_free_vs_paid` DataFrame that you created above that has the total number of free and paid apps per category. 

See if you can figure out how to get the look above by changing the `categoryorder` to 'total descending' as outlined in the documentation here [here](https://plotly.com/python/categorical-axes/#automatically-sorting-categories-by-name-or-total-value). 
"""



"""# Plotly Box Plots: Lost Downloads for Paid Apps

**Challenge**: Create a box plot that shows the number of Installs for free versus paid apps. How does the median number of installations compare? Is the difference large or small?

Use the [Box Plots Guide](https://plotly.com/python/box-plots/) and the [.box API reference](https://plotly.com/python-api-reference/generated/plotly.express.box.html) to create the following chart. 

<img src=https://imgur.com/uVsECT3.png>

"""



"""# Plotly Box Plots: Revenue by App Category

**Challenge**: See if you can generate the chart below: 

<img src=https://imgur.com/v4CiNqX.png>

Looking at the hover text, how much does the median app earn in the Tools category? If developing an Android app costs $30,000 or thereabouts, does the average photography app recoup its development costs?

Hint: I've used 'min ascending' to sort the categories. 
"""



"""# How Much Can You Charge? Examine Paid App Pricing Strategies by Category

**Challenge**: What is the median price price for a paid app? Then compare pricing by category by creating another box plot. But this time examine the prices (instead of the revenue estimates) of the paid apps. I recommend using `{categoryorder':'max descending'}` to sort the categories.
"""




