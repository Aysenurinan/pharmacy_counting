
# coding: utf-8

# In[1]:


from decimal import Decimal

out_file = open('top_cost_drug.txt', 'w')

out_file.write('drug_name,num_prescriber,total_cost\n')

drug_dict = {}

with open('itcont.txt', 'r') as big_file:
#with open('de_cc_data.txt', 'r') as big_file:
#with open('file50.txt', 'r') as big_file:
    line = big_file.readline() ## skip the header
    line = big_file.readline()
    while line:
        ## Some entries have comma in certain fields. Do not use those
        ## commas when splitting by comma
        quotelist = line.split('\"')

        linelist = []
        for i in range(0, len(quotelist)):
            # Only odd elements of quote split may contain commas
            if (i%2==0):
                even_list = quotelist[i].split(',')
                even_list = filter(None, even_list) ## Remove null element
                linelist.extend(even_list)
            else:
                linelist.append(quotelist[i])       
        linelist[-1] = linelist[-1].strip()  ## Remove new line from last element
        
        #Some entries have single name instead of "first name, last name"
        ID             = linelist[0]         ## ID
        last_name      = linelist[1]         ## Last name
        if (len(linelist)<5):                 
            first_name = ""                  ## No first name
        else:
            first_name = linelist[2]         ## First name
        drug_name      = linelist[-2]        ## Drug name
        cost           = Decimal(linelist[-1]) ## Cost
        #cost           = float(linelist[-1]) ## Cost    

        user_ID = ID + last_name + first_name
        
        if drug_name not in drug_dict:
            drug_dict[drug_name] = {}

        if user_ID in drug_dict[drug_name]:
            #print('ERROR: Drug name listed one more time for this User ID')
            #print(line)
            #print(drug_dict[drug_name][user_ID])
            drug_dict[drug_name][user_ID] = drug_dict[drug_name][user_ID] + cost 
        else:
            drug_dict[drug_name][user_ID] = cost
        line = big_file.readline()

output_list=[]
        
for drug_name_key, drug_name_value in drug_dict.items():
    total_cost = sum(drug_name_value.values())
    num_users  = len(drug_name_value)
    output_list.append([drug_name_key, num_users, total_cost])
    
# Sort list by drug name in ascending order first
output_list=sorted(output_list, key=lambda x: (x[0]))
output_list=sorted(output_list, key=lambda x: (x[2]), reverse=True)
    
for entry in output_list:
    out_value = str(entry[0]) + "," + str(entry[1]) + "," + str(entry[2]) + "\n"
    out_file.write(out_value)

out_file.close()

