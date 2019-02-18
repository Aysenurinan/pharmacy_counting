# pharmacy_counting

This is a repository created for *Insight coding challenge*.

In this repository we are asked to create the output file, top_cost_drug.txt, that contains comma (,) separated fields in each line.

Each line of this file should contain these fields:

drug_name: the exact drug name as shown in the input dataset
num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
total_cost: total cost of the drug across all prescribers
For example

So, if the input data, itcont.txt, is

id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost<br/>
1000000001,Smith,James,AMBIEN,100<br/>
1000000002,Garcia,Maria,AMBIEN,200<br/>
1000000003,Johnson,James,CHLORPROMAZINE,1000<br/>
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000<br/>
1000000005,Smith,David,BENZTROPINE MESYLATE,1500<br/>

then the output file, top_cost_drug.txt, should contain the following lines

drug_name,num_prescriber,total_cost<br/>
CHLORPROMAZINE,2,3000<br/>
BENZTROPINE MESYLATE,1,1500<br/>
AMBIEN,2,300<br/>

For this challenge, I did not use any external libraries, like csv. However, I only used ```decimal```
in order to have nice "total_cost" values.


## Approach to solving the coding challenge:
- I created a multidimensional dictionary; where my first dictionary checked each line of the input file for the **drug name**.
My second dictionary, checked the **id** and lastly, corresponding **drug_cost** is saved as values to our multidimensional dictionary.
- After ensuring that my python code worked on two small input files, which are 'itcont.txt' and first fifty lines of the original big data file('file50.txt'), I decided to try my code on the original input data('de_cc_data.txt')
- I received some errors:
  - Some entries had comma in certain areas
  - Some entries had single name instead of last name and first name<br/>
<br/>
I fixed those problems and the code runs without any errors.

