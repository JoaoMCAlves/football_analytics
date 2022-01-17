

"""============================================================================
===============================================================================

Script that contains all the necessary functions to scrape data from understat

===============================================================================
============================================================================"""

import requests
from bs4 import BeautifulSoup as soup
import json
import pandas as pd

#####UNDERSTAT
 
def readfromurl(url):
    # shot location, shot result, the xG(expected goals) and Season
    # HAALAND'S PLAYER ID IN UNDERSTAT IS 8260

    # example url
    #url ='https://understat.com/player/8260'
    html = requests.get(url)
    parse_soup = soup(html.content,'lxml')
    scripts = parse_soup.find_all('script')
    strings = scripts[3].string
    ind_start = strings.index("('")+2
    ind_end = strings.index("')")
    json_data = strings[ind_start:ind_end]
    json_data = json_data.encode('utf8').decode('unicode_escape')
    data = json.loads(json_data)
    x = []
    y = []
    xg = []
    result = []
    season = []
    for i,_ in enumerate(data):
        for key in data[i]:
            if key=='X':
                x.append(data[i][key])
            if key=='Y':
                y.append(data[i][key])
            if key=='xG':
                xg.append(data[i][key])
            if key=='result':
                result.append(data[i][key])
            if key=='season':
                season.append(data[i][key])
    columns = ['X','Y','xG','Result','Season']
    df_understat = pd.DataFrame([x, y, xg, result, season], index=columns)
    df_understat = df_understat.T
    df_understat = df_understat.apply(pd.to_numeric,errors='ignore')
    df_understat['X'] = df_understat['X'].apply(lambda x:x*100)
    df_understat['Y'] = df_understat['Y'].apply(lambda x:x*100)

    return df_understat