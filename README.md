# Table of Contents
1. [Description of the problem](README.md#description)
2. [Input dataset and output file](README.md#data)
3. [Approach](README.md#approach)
4. [Testing the code](README.md#testing)

# Description of the problem

In this problem, we are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order.

# Input dataset and output file

The original dataset was obtained from the Centers for Medicare & Medicaid Services. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The input dataset identifies prescribers by their **ID**, **last name**, and **first name**. It also describes the specific prescriptions that were dispensed at their direction, listed by **drug name** and the **cost** of the medication. 

The program code creates the output file, **top_cost_drug.txt**, that contains comma (,) separated fields in each line.

Each line of this file contains these fields:

drug_name: the exact drug name as shown in the input dataset
num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
total_cost: total cost of the drug across all prescribers

For example:

So, if the input data, itcont.txt, is

id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost<br/>
1000000001,Smith,James,AMBIEN,100<br/>
1000000002,Garcia,Maria,AMBIEN,200<br/>
1000000003,Johnson,James,CHLORPROMAZINE,1000<br/>
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000<br/>
1000000005,Smith,David,BENZTROPINE MESYLATE,1500<br/>

then the output file, top_cost_drug.txt, contains the following lines:

drug_name,num_prescriber,total_cost<br/>
CHLORPROMAZINE,2,3000<br/>
BENZTROPINE MESYLATE,1,1500<br/>
AMBIEN,2,300<br/>

# Approach

For this challenge, I did not use any external libraries, like csv. 
However, since I cared about the accuracy of rounding for "total_cost" values , I used decimal type. (```decimal```)

1. The code opened the input file and read each line.
2. Skipped the header, which is: <br/>id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost<br/>
3. Some entries had comma in certain fields, i.e. inside the last name, first name or the cost. For this reason, the code did not use commas when splitting by comma
4. I generated a multidimensional dictionary; where the first dimension of the dictionary indexed by the **drug name**, while the second dimension of the dictionary is indexed by **prescriber id** and the values of this two dimensional dictionary is the **drug_cost**
5. 

- After ensuring that my python code worked on two small input files, which are 'itcont.txt' and a portion of the original big data file ('file50.txt'), I decided to try my code on the original input data('de_cc_data.txt')
- I received some errors:
  - Some entries had comma in certain areas
  - Some entries had single name instead of last name and first name<br/>
<br/>
I fixed those problems and the code runs without any errors.

