🌪️ Climate Risk and Disaster Management: NOAA Atlantic Hurricane Dataset (1975-2024)

This project explores the NOAA Atlantic Hurricane dataset (1975-2024) to analyze and understand the impact of hurricanes on climate risk and disaster management. The dataset includes various storm information, such as the storm's ID, date/time, location (latitude/longitude), status, category, wind speed, pressure, and hurricane-force diameter.

📊 Dataset Overview

The dataset contains historical hurricane data, which can be used to understand patterns, assess risks, and aid in disaster management planning.

🔑 Key Columns:

Storm ID: Unique identifier for each storm

Date/Time: Timestamp of the storm data entry

Location (Latitude/Longitude): Geographic coordinates of the storm

Storm Status: Indicates whether the storm is active, dissipated, etc.

Category: Hurricane category (e.g., 1-5)

Wind Speed: Maximum sustained wind speed

Pressure: Atmospheric pressure at storm center

Hurricane Force Diameter: The size of the storm's hurricane-force winds

🗓️ Data Timeline:

1975-2024: The dataset spans 49 years of hurricane data.

Data Granularity: From 1979 onwards, data is available every 6 hours. For earlier years, some data may be missing.

🎯 Project Objective

Understanding the Data: The first phase of this project involves loading the dataset, exploring its structure, and identifying missing values to prepare it for further analysis.

Analysis Goals: Once the data is cleaned, the aim is to uncover trends in hurricane occurrences, categories, and their impact on different regions.

🛠️ Getting Started
📥 Requirements

To run this project, you will need the following Python libraries:

Pandas

Matplotlib

Seaborn (optional, for data visualization)

You can install them using:

pip install pandas matplotlib seaborn

⚙️ Steps:
1. Import Necessary Libraries

Begin by importing the libraries required for data analysis:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

2. Load the Dataset

Load the NOAA Atlantic Hurricane dataset (CSV file):

df = pd.read_csv('path_to_your_dataset.csv')

3. Explore the Dataset

Check basic information, descriptive statistics, and missing values:

# Basic Information
df.info()

# Descriptive Statistics
df.describe()

# Missing Values Check
df.isnull().sum()

4. Data Cleaning

Address missing values and prepare the dataset for analysis.

5. Save the Notebook

Once the exploration is complete, save your notebook in .ipynb format.