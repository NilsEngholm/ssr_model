import xml.etree.ElementTree as ET
import pandas as pd
import requests
import time as tm

# categories
mens_distances = [500, 1000, 1500, 5000, 10000]
womens_distances = [500, 1000, 1500, 3000, 5000]
years = list(range(2014, 2024))
genders = ['f', 'm']

# api call fn
def make_masterlist(sex, year, distance, quantity):
    # make url base
    url = f'https://speedskatingresults.com/api/xml/topn?gender={sex}&season={year}&distance={distance}&max={quantity}'
    print(f"Fetching URL: {url}")
    response = requests.get(url)
    if response.status_code == 200: # check 4 success
        try:
            root = ET.fromstring(response.content)
            return root
        except ET.ParseError:
            print(f'Error parsing XML for {distance}m from {year}')
            return None
    else:
        print(f'Failed to retrieve data: {response.status_code}')
        return None

def parse_result_to_df(root): # parse data
    data = []
    columns = ["Rank", "Family Name", "Given Name", "Nationality", "Time", "Date", "Location", "Event"]
    
    for result in root.findall('result'):
        rank = result.find('rank').text
        time = result.find('time').text
        skater = result.find('skater')
        family_name = skater.find('familyname').text
        given_name = skater.find('givenname').text
        nationality = skater.find('country').text
        date = result.find('date').text
        location = result.find('location').text
        event = result.find('event').text
        data.append([rank, family_name, given_name, nationality, time, date, location, event]) # add to data to df
    
    df = pd.DataFrame(data, columns=columns)
    return df

def get_speedskating_data(sex, year, distance, quantity):
    root = make_masterlist(sex, year, distance, quantity)
    if root is not None:
        df = parse_result_to_df(root)
        return df
    else:
        return pd.DataFrame()  # empty df if no data retrieved

# empty list to store DataFrames
all_data = []

# like a billion 4loops to pull from variables
for gender in genders:
    distances = mens_distances if gender == 'm' else womens_distances
    for year in years:
        for distance in distances:
            print(f"Processing {gender} {year} {distance}m")
            df = get_speedskating_data(gender, year, distance, 100)
            if not df.empty:
                df['Gender'] = gender
                df['Year'] = year
                df['Distance'] = distance
                all_data.append(df)
            tm.sleep(1)  # 1sec delay to avoid rate limit

# concatenate dfs into one
final_df = pd.concat(all_data, ignore_index=True)

# save the final df
final_df.to_csv('speedskating_results_with_index.csv', index=True)
final_df.to_csv('speedskating_results_without_index.csv', index=False)

print("Data saved successfully.")