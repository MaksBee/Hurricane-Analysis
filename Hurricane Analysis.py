#!/usr/bin/env python
# coding: utf-8

# # _Hurricane Analysis_
# #### By Max Balloch

# * 1: Convert the data in the damages data set to floats, while keeping the "Damage not recorded" data the same.
#    * 1.1: Data for damages 
#    * 1.2: Code + output
# * 2: A dictionary of each Hurricane, with sub-dictionaries with the associated data
#    * 2.1: Data
#    * 2.2: Code + output
# * 3: A dictionary similar to the last, but organized by year
# * 4: Count how often each area is affected
# * 5: A function to find the area with the most hurricanes, and how often it was hit
# * 6: Find the Hurricane with the highest deaths
# * 7: Categorize Hurricanes by their deaths caused
# * 8: Find the Hurricane with the greatest damage
# * 9: Categorize by damages caused on a given scale
# 

# ### 1.

# In[40]:


# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


# In[41]:


# create new list to put edited damages in
updated_damages = []
conversion = {"M": 1000000, "B": 1000000000}
for damage_amount in damages:
    # find the 3 different data types, 'Damages not found', 'M', and 'B'
    if damage_amount[-1] == "M":
        # after found type, convert to appropriate float and add to updated_damages list
        value = float(damage_amount[:-1]) * (conversion.get("M"))
        updated_damages.append(value)
    elif damage_amount[-1] == "B":
        value = float(damage_amount[:-1]) * (conversion.get("B"))
        updated_damages.append(value)
    else:
        updated_damages.append(damage_amount)
print(updated_damages)
    

        
    
        
        
    


# ### 2.

# In[42]:


names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
# created in 1.2

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# In[43]:


# first create main dictionary
data_by_name = {}
for i in range(len(names)):
    # add names with sub_dictionary to combined_data
    data_by_name[names[i]] = {}
for name in data_by_name:
    # add all correlating data pieces to one dictionary
    data_by_name[name] = {"Month": months[names.index(name)], "Year": years[names.index(name)], "Max sustained winds": max_sustained_winds[names.index(name)], "Areas affected": areas_affected[names.index(name)], "Deaths": deaths[names.index(name)], "Damages": updated_damages[names.index(name)]}
        
print(data_by_name)


# ### 3.

# In[44]:


# just a copy of the last cell with adjusted to key by year
data_by_year = {}
for i in range(len(years)):
    # add names with sub_dictionary to combined_data
    data_by_year[years[i]] = {}
for year in data_by_year:
    # add all correlating data pieces to one dictionary
    data_by_year[year] = {"Name": names[years.index(year)], "Month": months[years.index(year)], "Year": years[years.index(year)], "Max sustained winds": max_sustained_winds[years.index(year)], "Areas affected": areas_affected[years.index(year)], "Deaths": deaths[years.index(year)]}
    
print(data_by_year)


# ### 4.

# In[45]:


# first create dictionary of all areas equal to 0 
areas = {}
for hurricane in areas_affected:
    for place in hurricane:
        areas[place] = 0
# go back through the areas_affected list and + 1 each time they appear
for hurricane in areas_affected:
    for place in hurricane:
        areas[place] += 1
print(areas)


# ### 5.

# In[46]:


# go through, make the first key the highest, then compare the each to that, replacing if it is higher
highest_value = areas["Central America"]
highest_place = "none"
for place in areas.values():
    if place > highest_value:
        highest_value = place
# two searches, for the name and the value
for place, value in areas.items():
    if value == highest_value:
        highest_place = place

# print statement
print("The area with the most hurricanes is " + highest_place + ", with " + str(highest_value) + " occurances")


# ### 6.

# In[47]:


highest_deaths = 0
highest_death_cane = "None"
for hurricane in data_by_name.keys():
    if data_by_name[hurricane]["Deaths"] > highest_deaths:
        highest_deaths = data_by_name[hurricane]["Deaths"]
        highest_death_cane = hurricane

print("The Hurricane that caused the most deaths was " + highest_death_cane + ", with " + str(highest_deaths) + " deaths")


# ### 7.

# In[48]:


mortality_list = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": []}
for hurricane in data_by_name.keys():
    if data_by_name[hurricane]["Deaths"] == 0:
# mortality rate boundries
        mortality_list["0"].append(hurricane)
    elif 0 < data_by_name[hurricane]["Deaths"] < 100:
        mortality_list["1"].append(hurricane)
    elif 100 < data_by_name[hurricane]["Deaths"] < 500:
        mortality_list["2"].append(hurricane)
    elif 500 < data_by_name[hurricane]["Deaths"] < 1000:
        mortality_list["3"].append(hurricane)
    elif 1000 < data_by_name[hurricane]["Deaths"] < 10000:
        mortality_list["4"].append(hurricane)
    elif 10000 < data_by_name[hurricane]["Deaths"]:
        mortality_list["5"].append(hurricane)
print(mortality_list)


# ### 8.

# In[49]:


# simply find highest with comparing the data each time 
max_damages = 0
max_damages_cane = "None"
for hurricane in data_by_name.keys():
    if data_by_name[hurricane]["Damages"] == "Damages not recorded":
        damage = 0
    elif data_by_name[hurricane]["Damages"] > max_damages:
        max_damages = data_by_name[hurricane]["Damages"]
        max_damages_cane = hurricane
print("The Hurricane that caused the greatest damage was " + max_damages_cane + ", with " + str(max_damages) + " dollars of damage")
    

    
    


# ### 9.

# In[50]:


damage_scale_list = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": []}
for hurricane in data_by_name.keys():
    if data_by_name[hurricane]["Damages"] == "Damages not recorded" or 0:
# damage scale boundries
        damage_scale_list["0"].append(hurricane)
    elif 0 < data_by_name[hurricane]["Damages"] <= 100000000:
        damage_scale_list["1"].append(hurricane)
    elif 100000000 < data_by_name[hurricane]["Damages"] <= 1000000000:
        damage_scale_list["2"].append(hurricane)
    elif 1000000000 < data_by_name[hurricane]["Damages"] <= 10000000000:
        damage_scale_list["3"].append(hurricane)
    elif 10000000000 < data_by_name[hurricane]["Damages"] <= 50000000000:
        damage_scale_list["4"].append(hurricane)
    elif 50000000000 < data_by_name[hurricane]["Damages"]:
        damage_scale_list["5"].append(hurricane)
print(damage_scale_list)


# In[ ]:




