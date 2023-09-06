# Palmer-Penguins-Analysis
Exploring data analysis using Matplotlib, NumPy and SciPy

## Base
Since it was my first attempt at analyzing a Data Set, I focused on one variable and tried finding reasons of those changes (if it had any noticable changes). Before I get started I just printed out the the type of entries (NumPy ndarray) and the amounts of rows and columns. Afterwards I printed the first instance to check if the header of the Palmer Penguins File gets skipped.

## Bill length
As already told, I focused on one variable and that one was the Bill Length, which was a Float-Value represented in Millimeters (in the file it was called "bill_length_mm").
First I printed out all information about it and its correlations. To avoid the problems of NaN-Values I had to use the nan-methods, because there were some entities without any specific details. 


![image](https://github.com/MiladWazirZada/Palmer-Penguins-Analysis/assets/82714284/4ffb95a0-4213-4a36-85cd-e6e33483a783)

This graph shows the number of occurences refering to their bill length. Nothing particularly special, but the graph can be interpreted as two different Gaussian distributions or as one whole one. <br />
Firstly, I plotted it as if it was a normal Gaussian distribution:

![image](https://github.com/MiladWazirZada/Palmer-Penguins-Analysis/assets/82714284/e7c28c46-49f8-4bdf-9419-0b688c24033f)

and afterwards I've tried linking it to either their evlolution over the years or their gender. <br />
I noticed


