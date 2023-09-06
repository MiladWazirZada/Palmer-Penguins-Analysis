# Palmer Penguins (penguins.csv)
# github.com/mcnakhaee/palmerpenguins/blob/master
# Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and
# Environmental Variability within a Community of Antarctic Penguins
# (Genus Pygoscelis). PLoS ONE 9(3): e90081
# https://doi.org/10.1371/journal.pone.0090081

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

dtypes = [("species", "U16"), ("island", "U16"),
          ("bill_length_mm", float), ("bill_depth_mm", float),
          ("flipper_length_mm", float), ("body_mass_g", float),
          ("sex", "U16"), ("year", float)]

data = np.genfromtxt("penguins.csv", delimiter=",", dtype=dtypes,
                     names=True, missing_values="NA",
                     filling_values=np.nan, encoding=None)

print(type(data), data.shape)
# an example to check if the header of the File gets skipped
print(data[0])

# all information about the bill_length_mm and its correlations

bill_l_mm = data["bill_length_mm"]
minValue = np.nanmin(bill_l_mm)
maxValue = np.nanmax(bill_l_mm)
# print("min:", minValue,
#      "max:", maxValue,
#      "range:", maxValue - minValue,
#      "std:", np.nanstd(bill_l_mm),
#      "n:", len(bill_l_mm) - np.sum(np.isnan(bill_l_mm)))
plt.hist(bill_l_mm, bins="auto")
plt.xlabel("Ranges of Bill Length in mm")
plt.ylabel("Number of Occurences")
# Shows bimodal-distribution but could also still (perhaps) classify as a Gaussian distribution
plt.show()

# Using the st.norm.fit method for a Gaussian distribution
# ignoring nan-Values
no_nan_lill_length = ~np.isnan(bill_l_mm)
valid_bill_length = bill_l_mm[no_nan_lill_length]

# Create Mu, Sigma Values & a linear space "x"
mu, sigma = st.norm.fit(valid_bill_length)
x = np.linspace(np.nanmin(bill_l_mm) - 0.5, np.nanmax(bill_l_mm) + 0.5, 50)

# Plot the Linear Space & PDF
plt.plot(x, st.norm(mu, sigma).pdf(x), label="Gaussian")
plt.hist(bill_l_mm, density=True, bins=60, label="Histogram")
plt.xlabel("Bill Length in mm")
plt.ylabel("Probability Density")
plt.legend()
plt.show()


# Checking if the Bill Length changes over the Years and if there are correlations
bill_l_mm = data["bill_length_mm"]
years = data["year"]

bill_length_over_years = [bill_l_mm[data["year"] == year] for year in (2007, 2008, 2009)]
for bill_length_years in bill_length_over_years:
    plt.hist(bill_length_years, density=True, bins=60)

plt.xlabel("Bill Length in mm")
plt.ylabel("Probability Density")
plt.legend([2007,2008,2009])
# There is no noticeable correlation other than the values increasing from 2007 to 2008
# and then decreasing abnormally (Perhaps other reasons not noticeable via these Datas)
plt.show()

# Checking if the Bill Length of these Penguins have certain resemblances to gender
bill_l_mm = data["bill_length_mm"]
gender = data["sex"]

# NaN-Values and empty values get put into
missing_genders = (gender == "") | (gender == "NA")

# Create a list of bill lengths by gender, excluding missing or empty values
bill_length_by_gender = []

for gender_value in ("male", "female"):
    # Filter data by gender (excluding missing or empty values)
    gender_mask = (gender == gender_value) & (~np.isnan(bill_l_mm))
    bill_length_by_gender.append(bill_l_mm[gender_mask])

# Plot histograms for each gender
for bill_length_gender in bill_length_by_gender:
    plt.hist(bill_length_gender, density=True, bins=60)

plt.xlabel("Bill Length in mm")
plt.ylabel("Probability Density")
plt.legend(["Male", "Female"])
# There is no noticeable correlation other than a shifted Graph
plt.show()


# Question: Did the body mass increase over the years?
# How to check?
# Average Values over the years
body_mass = data["body_mass_g"]
years = data["year"]

# ignoring nan-Values
no_nan_years_and_mass = ~np.isnan(body_mass) & ~np.isnan(years)
valid_body_mass = body_mass[no_nan_years_and_mass]
valid_years = years[no_nan_years_and_mass]

# Average body mass (in g) per Year of observation
unique_years = np.unique(valid_years)
avg_body_mass = [np.mean(valid_body_mass[valid_years == year]) for year in unique_years]

# Create a histogram
plt.bar(unique_years, avg_body_mass, color='blue', alpha=0.7)
plt.xlabel("Year")
plt.ylabel("Body Mass (g)")
plt.title("Histogram of average Body Mass (in g) over the Years")
plt.xticks(unique_years)  # Set x-axis tick positions
plt.show()
