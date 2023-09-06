# Palmer-Penguins-Analysis
Exploring data analysis using Matplotlib, NumPy and SciPy

## Base
Since it was my first attempt at analyzing a Data Set, I focused on one variable and tried finding reasons of those changes (if it had any noticable ones). Before I get started I just printed out the the type of entries (NumPy ndarray) and the amounts of rows and columns. Afterwards I printed the first instance to check if the header of the Palmer Penguins File gets skipped.

## Bill length
As already told, I focused on one variable and that one was the Bill Length, which was a Float-Value represented in Millimeters (in the file it was called "bill_length_mm").
First I printed out all information about it and its correlations. To avoid the problems of NaN-Values I had to use the nan-methods, because there were some entities without any specific details. 

![image](https://github.com/MiladWazirZada/Palmer-Penguins-Analysis/assets/82714284/4ffb95a0-4213-4a36-85cd-e6e33483a783)

This graph shows the number of occurences refering to their bill length. Nothing particularly special, but the graph can be interpreted as two different Gaussian distributions or as one whole one. <br />
<br />

## Probability density of the range of values
Firstly, I plotted it as if it was a normal Gaussian distribution:

![image](https://github.com/MiladWazirZada/Palmer-Penguins-Analysis/assets/82714284/e7c28c46-49f8-4bdf-9419-0b688c24033f)

## But what if it is a bimodal distribution?
I've tried linking it to either their evlolution over the years or their gender. <br />

### Over the years:

![image](https://github.com/MiladWazirZada/Palmer-Penguins-Analysis/assets/82714284/b2389358-102c-4940-b026-ee66ba886c2c)

I noticed that overall the values decreased, however they spiked in 2008 much more and then dropped. The density was much smaller, but it doesn't really show anything of notice. <br />

### Is gender the cause of the bimodal distribution?
In nature, one can observe variations in the anatomical and behavioral characteristics exhibited by various animal species. This phenomenon is also represented in this graph:

![image](https://github.com/MiladWazirZada/Palmer-Penguins-Analysis/assets/82714284/f66b7e18-df51-4728-bcff-3839e6885442)

## Conclusion
This observation strongly suggests that the disparities evident in the first graph may be because of gender-specific variations in bill length among Palmer penguins.

## Body Mass

Towards the end of the document, I have presented data illustrating the average body mass (in g) across the different years. This was mainly to try out Matplotlibs different vizualisation strategies.
