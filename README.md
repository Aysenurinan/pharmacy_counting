## pharmacy_counting

This is a repository created for Insight coding challenge.

In this repository we are asked to create the output file, top_cost_drug.txt, that contains comma (,) separated fields in each line.

Each line of this file should contain these fields:

drug_name: the exact drug name as shown in the input dataset
num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
total_cost: total cost of the drug across all prescribers
For example

So, if the input data, itcont.txt, is

id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500

then the output file, top_cost_drug.txt, should contain the following lines

drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
