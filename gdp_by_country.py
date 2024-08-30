from bs4 import BeautifulSoup
import requests
import pandas as pd
from icecream import ic

url = 'https://www.worldometers.info/gdp/gdp-by-country/'

html_data = requests.get(url)

soup = BeautifulSoup(html_data.content, 'lxml')

rows = soup.find_all('tr')

# test the scrapping from web
for i in range(5):
    ic(rows[i].text.strip())

'''(output)
ic| rows[i].text.strip(): ('# Country GDP (nominal, 2022)  GDP (abbrev.) GDP  growth Population (2022)  '
                           'GDP  per capita  Share of World GDP')
ic| rows[i].text.strip(): ('1 United States $25,462,700,000,000 $25.463 trillion 2.06% 341,534,046 '
                           '$74,554 25.32%')
ic| rows[i].text.strip(): ('2 China $17,963,200,000,000 $17.963 trillion 2.99% 1,425,179,569 $12,604 '
                           '17.86%')
ic| rows[i].text.strip(): '3 Japan $4,231,140,000,000 $4.231 trillion 1.03% 124,997,578 $33,850 4.21%'
ic| rows[i].text.strip(): '4 Germany $4,072,190,000,000 $4.072 trillion 1.79% 84,086,227 $48,429 4.05%'
'''

# Using rows[0] as table description with certain modification
desc = [rows[0].text.strip()]
ic(desc)

desc = desc[0].split()
#ic(description)

'''(output)
desc: ['#','Country','GDP','(nominal,','2022)','GDP','(abbrev.)','GDP','growth','Population','(2022)','GDP','per','capita',
            'Share','of','World','GDP']
'''

#description = description[0:1] + [' '.join(description[1:3])] + description[3:]

desc = desc[0:2] + [' '.join(desc[2:5])] + [' '.join(desc[5:7])] + [' '.join(desc[7:9])] + [' '.join(desc[9:11])] + [' '.join(desc[11:14])]\
        + [' '.join(desc[14:])]
ic(desc)
'''(output)
ic| desc: ['#','Country','GDP (nominal, 2022)','GDP (abbrev.)','GDP growth','Population (2022)','GDP per capita','Share of World GDP']
'''

# create country data
ic(rows[1].text) # first country United State
ic(rows[177].text) # last country Tuvalu

country = list()
for i in range(1,178):
    ct = rows[i].text.strip()
    country.append(ct)

ic(country[:2])
'''(output)
ic| country[:2]: ['1 United States $25,462,700,000,000 $25.463 trillion 2.06% 341,534,046 $74,554 25.32%',
                  '2 China $17,963,200,000,000 $17.963 trillion 2.99% 1,425,179,569 $12,604 17.86%']
'''

# split list become data for each country
country = [i.split() for i in country]

ic(country[:2])
'''(output)
ic| country[:2]: [['1','United','States','$25,462,700,000,000','$25.463','trillion','2.06%','341,534,046','$74,554','25.32%'],
                  ['2','China','$17,963,200,000,000','$17.963','trillion','2.99%','1,425,179,569','$12,604','17.86%']]
'''

# list correction to make list 8 x 177
def len_list(lst):
    ln = list()
    l1 = l2 = l3 = l4 = l5 = l6 = l7 = 0    

    for i in lst:
        if len(i) == 5:
            l1 += 1
        elif len(i) == 6:
            l2 += 1
        elif len(i) == 7:
            l3 += 1
        elif len(i) == 9:
            l4 += 1
        elif len(i) == 10:
            l5 += 1
        elif len(i) == 11:
            l6 += 1
        elif len(i) == 12:
            l7 += 1
        else:
            pass
    ln = [l1, l2, l3, l4, l5, l6, l7]
    return ln

ic(len_list(country))
ic(sum(len_list(country)))

'''(output)
ic| len_list(country): [0, 0, 0, 145, 21, 8, 3]
ic| sum(len_list(country)): 177
'''

# display error list type
def lst_num(lst, num):
    no = 1
    for i in lst:
        if len(i) == num and no > 0:
            ic("Length list", num)
            print(i)
            no -= 1

print('\n-----Display List Examples length > 8-----')
for i in range(8,13):
    lst_num(country, i)

country = [i[:3] + [' '.join(i[3:5])] + i[5:] if len(i) == 9 else i for i in country]
country = [i[:4] + [' '.join(i[4:6])] + i[6:] if len(i) == 10 else i for i in country]
country = [i[:5] + [' '.join(i[5:7])] + i[7:] if len(i) == 11 else i for i in country]
country = [i[:6] + [' '.join(i[6:8])] + i[8:] if len(i) == 12 else i for i in country]

# list_correction(country) --> col GDP (abbrev.) 
ic(len_list(country))
print('\n-----After GDP(abbrev.) correction-----')
print(country[1]) # display China
print(country[0]) # display US
print(country[27]) # display UEA
print(country[168]) # display SK&N 

'''(outout)
-----After GDP(abbrev.) correction-----
['2', 'China', '$17,963,200,000,000', '$17.963 trillion', '2.99%', '1,425,179,569', '$12,604', '17.86%']
['1', 'United', 'States', '$25,462,700,000,000', '$25.463 trillion', '2.06%', '341,534,046', '$74,554', '25.32%']
['28', 'United', 'Arab', 'Emirates', '$507,535,000,000', '$508 billion', '7.41%', '10,242,086', '$49,554', '0.50%']
['169', 'Saint', 'Kitts', '&', 'Nevis', '$961,563,259', '$962 million', '9.00%', '46,709', '$20,586', '0.00%']
'''

# list correction(country) --> col Country
country = [i[:1] + [' '.join(i[1:3])] + i[3:] if len(i) == 9 else i for i in country] 
country = [i[:1] + [' '.join(i[1:4])] + i[4:] if len(i) == 10 else i for i in country] 
country = [i[:1] + [' '.join(i[1:5])] + i[5:] if len(i) == 11 else i for i in country]

ic(len_list(country))
print('\n-----After Country correction-----')
print(country[1]) # display China
print(country[0]) # display US
print(country[27]) # display UEA
print(country[168]) # display SK&N 
print()

'''(output)
-----After Country correction-----
['2', 'China', '$17,963,200,000,000', '$17.963 trillion', '2.99%', '1,425,179,569', '$12,604', '17.86%']
['1', 'United States', '$25,462,700,000,000', '$25.463 trillion', '2.06%', '341,534,046', '$74,554', '25.32%']
['28', 'United Arab Emirates', '$507,535,000,000', '$508 billion', '7.41%', '10,242,086', '$49,554', '0.50%']
['169', 'Saint Kitts & Nevis', '$961,563,259', '$962 million', '9.00%', '46,709', '$20,586', '0.00%']
'''

# create dataframe
df = pd.DataFrame(country, columns=desc)
ic(df)

# convert to csv file
df.to_csv('GDP by Country.csv', index=False)

# EOF
