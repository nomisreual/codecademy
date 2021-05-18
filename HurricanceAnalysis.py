# names of hurricanes
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
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def updateDamages(damage_list):

    damages_updated = []

    for damage in damage_list:
        if 'not' in damage:
            damages_updated.append(damage)
        elif 'M' in damage:
            damages_updated.append(
                float(damage[:-1]) * 1000000
            )
        else:
            damages_updated.append(
                float(damage[:-1]) * 1000000000
            )

    return damages_updated

# this function does not do the trick as it does not properly convert M/B entries

#print(updateDamages(damages))

# write your construct hurricane dictionary function here:

def hurricanes_dict_name(months, years, max_wind, areas_affe, dmg, deaths):

    dictionary_details = {}

    for i in range(0, len(names) - 1):
        dictionary_details[names[i]] = {
            "Month": months[i],
            "Year": years[i],
            "Maximum Sustained Wind": max_wind[i],
            "Areas Affected": areas_affe[i],
            "Damage": dmg[i],
            "Deaths": deaths[i]
        }
    return dictionary_details

hurricanes_dictionary = hurricanes_dict_name(months, years, max_sustained_winds, areas_affected, updateDamages(damages), deaths)

#for key in hurricanes_dictionary.keys():
#    print("{}:".format(key))
#    print(hurricanes_dictionary[key])    


# write your construct hurricane by year dictionary function here:

## assuming year can serve as a unique identifier

def hurricanes_dict_year(hurricanes):

    new_dict = {}

    for key, value in hurricanes.items():
        year = value.pop("Year")
        value.update({"Name": key})
        new_dict[year] = value        
    
    return new_dict


#print(hurricanes_dict_year(hurricanes_dictionary))

# write your count affected areas function here:

def count_affected(dict):

    affected_count = {}
    
    for value in dict.values():
        regions = value.get("Areas Affected")
        for region in regions:
            if affected_count.get(region) == None:
                affected_count[region] = 1
            else:
                affected_count[region] += 1
    
    return affected_count

region_count = count_affected(hurricanes_dictionary)

# write your find most affected area function here:

# assuming there is an area affected strictly the most

def get_most_affected(dict):

    reg_cou = count_affected(dict)

    count = 0
    most_affected = ""

    for key, value in reg_cou.items():
        if value > count:
            count = value
            most_affected = key

    return (most_affected, count)

most_affected = get_most_affected(hurricanes_dictionary)
print(most_affected)

# write your greatest number of deaths function here:

## assuming there is a max deaths value

def most_casualties(dict):
    count = 0
    name = ""

    for key, value in dict.items():
        if value.get("Deaths") > count:
            count = value.get("Deaths")
            name = key
    return (name, count)

most_deaths = most_casualties(hurricanes_dictionary)
print(most_deaths)

# write your catgeorize by mortality function here:

def hurricanes_by_mortality(dict):

    # one dictionary for each mortality rating:

    mort_0 = {}
    mort_1 = {}
    mort_2 = {}
    mort_3 = {}
    mort_4 = {}

    for key, value in dict.items():
        if value.get("Deaths") == 0:
            mort_0.update({key: value})
        elif value.get("Deaths") <= 100:
            mort_1.update({key: value})
        elif value.get("Deaths") <= 500:
            mort_2.update({key: value})
        elif value.get("Deaths") <= 1000:
            mort_3.update({key: value})
        else:
            mort_4.update({key: value})

    # by mortality dictionary

    by_mortality = {
        0: mort_0,
        1: mort_1,
        2: mort_2,
        3: mort_3,
        4: mort_4
    }
            
    return by_mortality

for key, value in hurricanes_by_mortality(hurricanes_dictionary).items():
    print(key)
    print(value.keys())






# write your greatest damage function here:

## assuming there is a max damage value

def max_dmg(dict, print_msg = True):
    count = 0.0
    name = ""

    for key, value in dict.items():
        if type(value.get("Damage")) == str: # skip not recorded dmg instances
            continue 
        if value.get("Damage") > count:
            count = value.get("Damage")
            name = key

    if print_msg == True:
        print("The hurricane {} in {} caused {}$ worth of damage.".format(
            name, dict.get(name)["Year"], count
        ))

    return (name, count)


max_dmg(hurricanes_dictionary)


# write your catgeorize by damage function here:

def hurricanes_by_dmg(dict):

    # one dictionary for each mortality rating:

    dmg_0 = {}
    dmg_1 = {}
    dmg_2 = {}
    dmg_3 = {}
    dmg_4 = {}

    for key, value in dict.items():

        if type(value.get("Damage")) == str: # ignoring dmg not recorded
            continue

        if value.get("Damage") == 0:
            dmg_0.update({key: value})
        elif value.get("Damage") <= 100000000:
            dmg_1.update({key: value})
        elif value.get("Damage") <= 1000000000:
            dmg_2.update({key: value})
        elif value.get("Damage") <= 10000000000:
            dmg_3.update({key: value})
        else:
            dmg_4.update({key: value})

    # by mortality dictionary

    by_dmg = {
        0: dmg_0,
        1: dmg_1,
        2: dmg_2,
        3: dmg_3,
        4: dmg_4
    }
            
    return by_dmg

for key, value in hurricanes_by_dmg(hurricanes_dictionary).items():
    print(key)
    print(value.keys())
