import wikipedia
import pandas as pd
import numpy as np
import requests
import re
S = requests.Session()
df = pd.read_csv('datasets/plants_unique.csv')
plant_names = np.array(df.iloc[:,0])

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
	"action": "query",
	"format": "json",
	"prop": "pageimages",
    "piprop": "original", 
    "titles": "",
    "redirects":1
}
HEADERS = {
    "User-Agent":'plant-character-classification 1.0'
}
names_links = pd.DataFrame(columns=['Names', 'Links', 'Page Title'])
names_links['Names'] = plant_names
x= 0
for name in plant_names:
    print(x)
    x=x+1
    print(name)
    query = f"{name} plant"
    page_name = wikipedia.search(query,1)
    page_title = page_name[0]
    PARAMS["titles"]=page_title
    r = S.get(URL, params=PARAMS, headers=HEADERS)
    data = r.json()
    image_url = list(data['query']['pages'].values())[0]['original']['source']
    image_data = S.get(image_url,params=None,headers= HEADERS).content
    media_type = image_url.rsplit(".",1)[-1].lower()
    no_space_name = re.sub("\s", "_", name)
    file_name = f"content/{no_space_name}.{media_type}"
    names_links.loc[names_links["Names"] == name, 'Links'] = image_url
    names_links.loc[names_links['Names'] == name, 'Page Title'] = page_title
    
    with open(file_name,"wb") as f:
        f.write(image_data)


combined = pd.concat([df,names_links], axis=1)
names_links.to_csv('plants_links.csv', index=False)