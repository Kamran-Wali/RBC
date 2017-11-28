
# WeatherPy

#### Analysis
#### Observable Trend 1    
#### Observable Trend 2
#### Observable Trend 3


```python
# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests as req
import time
import seaborn as sns
from citipy import citipy
import csv
```

## Generate Cities List


```python
# Generate Cities Dataframe using the Citypy Library
# Downside to this code is that it generate a complete new list of cities everytime this cell is refreshed / Create a unqiue city list. 
Coordinates = []
for i in range(1200):
    Lat = np.random.randint(-90,90)
    Lng = np.random.randint(-180,180)
    pairs=(Lat,Lng)
    Coordinates.append(pairs)
print(Coordinates[:10])
```

    [(-57, 121), (-42, 55), (-63, 25), (-84, -55), (-38, 69), (77, -175), (70, 67), (21, -148), (-11, 149), (-25, -175)]
    


```python
# Generate the city list:
Cities = []
for coordinate_pair in Coordinates:
    Lat,Lng = coordinate_pair
    city_obj=citipy.nearest_city(Lat,Lng)
    if city_obj not in Cities:
        Cities.append(city_obj)
len(Cities)
```




    526



## Perform API Calls


```python
#API Information
api_key = "96b392d27de5ad004a079b28fe040981"
url = "http://api.openweathermap.org/data/2.5/weather?"
units = "Imperial"
```


```python
#Query URl
target_url = url + "appid=" + api_key + "&units" + units + "&q="
target_url
```




    'http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q='




```python
# Generate the API Workload
Weather = []

# Set Counter
row_count = 0
set = 

for i, city in enumerate(Cities):
    data = req.get(query_url + city.city_name).json()
    print("Processing Record "+ str(i+1) + " of Set " + str(set) + "|" + city.city_name)
    print(query_url + city.city_name)
    Weather.append(data)
    row_count +=1
```

    Processing Record 1 of Set 0|puerto escondido
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=puerto escondido
    Processing Record 2 of Set 0|nikolskoye
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nikolskoye
    Processing Record 3 of Set 0|arraial do cabo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=arraial do cabo
    Processing Record 4 of Set 0|nanortalik
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nanortalik
    Processing Record 5 of Set 0|cape town
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cape town
    Processing Record 6 of Set 0|kapaa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kapaa
    Processing Record 7 of Set 0|torbay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=torbay
    Processing Record 8 of Set 0|rikitea
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=rikitea
    Processing Record 9 of Set 0|albany
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=albany
    Processing Record 10 of Set 0|polessk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=polessk
    Processing Record 11 of Set 0|pastavy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=pastavy
    Processing Record 12 of Set 0|lebu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lebu
    Processing Record 13 of Set 0|bolshaya irba
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bolshaya irba
    Processing Record 14 of Set 0|carnarvon
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=carnarvon
    Processing Record 15 of Set 0|busselton
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=busselton
    Processing Record 16 of Set 0|bose
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bose
    Processing Record 17 of Set 0|taolanaro
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=taolanaro
    Processing Record 18 of Set 0|hirtshals
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hirtshals
    Processing Record 19 of Set 0|khatanga
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=khatanga
    Processing Record 20 of Set 0|sorong
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sorong
    Processing Record 21 of Set 0|nazarovo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nazarovo
    Processing Record 22 of Set 0|karasjok
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=karasjok
    Processing Record 23 of Set 0|kavieng
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kavieng
    Processing Record 24 of Set 0|yellowknife
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=yellowknife
    Processing Record 25 of Set 0|east london
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=east london
    Processing Record 26 of Set 0|dikson
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=dikson
    Processing Record 27 of Set 0|punta arenas
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=punta arenas
    Processing Record 28 of Set 0|esperance
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=esperance
    Processing Record 29 of Set 0|cidreira
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cidreira
    Processing Record 30 of Set 0|attawapiskat
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=attawapiskat
    Processing Record 31 of Set 0|inhambane
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=inhambane
    Processing Record 32 of Set 0|airai
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=airai
    Processing Record 33 of Set 0|nouakchott
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nouakchott
    Processing Record 34 of Set 0|mataura
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mataura
    Processing Record 35 of Set 0|hithadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hithadhoo
    Processing Record 36 of Set 0|tiksi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tiksi
    Processing Record 37 of Set 0|kutahya
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kutahya
    Processing Record 38 of Set 0|saladoblanco
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=saladoblanco
    Processing Record 39 of Set 0|kingaroy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kingaroy
    Processing Record 40 of Set 0|nizhneyansk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nizhneyansk
    Processing Record 41 of Set 0|barrow
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=barrow
    Processing Record 42 of Set 0|salta
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=salta
    Processing Record 43 of Set 0|hobart
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hobart
    Processing Record 44 of Set 0|guerrero negro
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=guerrero negro
    Processing Record 45 of Set 0|itarema
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=itarema
    Processing Record 46 of Set 0|naliya
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=naliya
    Processing Record 47 of Set 0|mar del plata
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mar del plata
    Processing Record 48 of Set 0|vaini
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=vaini
    Processing Record 49 of Set 0|jaen
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=jaen
    Processing Record 50 of Set 0|hermanus
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hermanus
    Processing Record 51 of Set 0|mount gambier
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mount gambier
    Processing Record 52 of Set 0|manicaragua
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=manicaragua
    Processing Record 53 of Set 0|ushuaia
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ushuaia
    Processing Record 54 of Set 0|taganak
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=taganak
    Processing Record 55 of Set 0|aklavik
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=aklavik
    Processing Record 56 of Set 0|provideniya
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=provideniya
    Processing Record 57 of Set 0|bambous virieux
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bambous virieux
    Processing Record 58 of Set 0|souillac
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=souillac
    Processing Record 59 of Set 0|pangkalanbuun
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=pangkalanbuun
    Processing Record 60 of Set 0|butaritari
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=butaritari
    Processing Record 61 of Set 0|kassala
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kassala
    Processing Record 62 of Set 0|port alfred
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=port alfred
    Processing Record 63 of Set 0|hasaki
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hasaki
    Processing Record 64 of Set 0|sitka
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sitka
    Processing Record 65 of Set 0|sampit
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sampit
    Processing Record 66 of Set 0|lincoln
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lincoln
    Processing Record 67 of Set 0|coquimbo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=coquimbo
    Processing Record 68 of Set 0|atuona
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=atuona
    Processing Record 69 of Set 0|rungata
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=rungata
    Processing Record 70 of Set 0|qaanaaq
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=qaanaaq
    Processing Record 71 of Set 0|tarakan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tarakan
    Processing Record 72 of Set 0|utiroa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=utiroa
    Processing Record 73 of Set 0|marrakesh
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=marrakesh
    Processing Record 74 of Set 0|sentyabrskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sentyabrskiy
    Processing Record 75 of Set 0|alta floresta
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=alta floresta
    Processing Record 76 of Set 0|barentsburg
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=barentsburg
    Processing Record 77 of Set 0|new norfolk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=new norfolk
    Processing Record 78 of Set 0|broome
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=broome
    Processing Record 79 of Set 0|tsihombe
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tsihombe
    Processing Record 80 of Set 0|puerto ayora
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=puerto ayora
    Processing Record 81 of Set 0|grand river south east
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=grand river south east
    Processing Record 82 of Set 0|nuqui
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nuqui
    Processing Record 83 of Set 0|penhold
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=penhold
    Processing Record 84 of Set 0|illoqqortoormiut
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=illoqqortoormiut
    Processing Record 85 of Set 0|kadykchan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kadykchan
    Processing Record 86 of Set 0|avera
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=avera
    Processing Record 87 of Set 0|dingle
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=dingle
    Processing Record 88 of Set 0|kuruman
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kuruman
    Processing Record 89 of Set 0|quatre cocos
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=quatre cocos
    Processing Record 90 of Set 0|vao
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=vao
    Processing Record 91 of Set 0|macaboboni
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=macaboboni
    Processing Record 92 of Set 0|port elizabeth
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=port elizabeth
    Processing Record 93 of Set 0|kazalinsk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kazalinsk
    Processing Record 94 of Set 0|termoli
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=termoli
    Processing Record 95 of Set 0|bereda
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bereda
    Processing Record 96 of Set 0|husavik
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=husavik
    Processing Record 97 of Set 0|georgetown
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=georgetown
    Processing Record 98 of Set 0|saint-augustin
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=saint-augustin
    Processing Record 99 of Set 0|saldanha
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=saldanha
    Processing Record 100 of Set 0|trinidad
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=trinidad
    Processing Record 101 of Set 0|bugasong
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bugasong
    Processing Record 102 of Set 0|deputatskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=deputatskiy
    Processing Record 103 of Set 0|pacific grove
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=pacific grove
    Processing Record 104 of Set 0|lata
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lata
    Processing Record 105 of Set 0|san patricio
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=san patricio
    Processing Record 106 of Set 0|jvari
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=jvari
    Processing Record 107 of Set 0|katobu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=katobu
    Processing Record 108 of Set 0|saint-philippe
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=saint-philippe
    Processing Record 109 of Set 0|ahipara
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ahipara
    Processing Record 110 of Set 0|hihifo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hihifo
    Processing Record 111 of Set 0|novosibirsk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=novosibirsk
    Processing Record 112 of Set 0|bethel
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bethel
    Processing Record 113 of Set 0|tocopilla
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tocopilla
    Processing Record 114 of Set 0|bairiki
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bairiki
    Processing Record 115 of Set 0|basco
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=basco
    Processing Record 116 of Set 0|homer
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=homer
    Processing Record 117 of Set 0|sinnamary
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sinnamary
    Processing Record 118 of Set 0|avarua
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=avarua
    Processing Record 119 of Set 0|kalmunai
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kalmunai
    Processing Record 120 of Set 0|kununurra
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kununurra
    Processing Record 121 of Set 0|iquique
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=iquique
    Processing Record 122 of Set 0|balkanabat
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=balkanabat
    Processing Record 123 of Set 0|tasiilaq
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tasiilaq
    Processing Record 124 of Set 0|andenes
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=andenes
    Processing Record 125 of Set 0|caravelas
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=caravelas
    Processing Record 126 of Set 0|bluff
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bluff
    Processing Record 127 of Set 0|bargal
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bargal
    Processing Record 128 of Set 0|shiyan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=shiyan
    Processing Record 129 of Set 0|byron bay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=byron bay
    Processing Record 130 of Set 0|chuy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=chuy
    Processing Record 131 of Set 0|vestmannaeyjar
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=vestmannaeyjar
    Processing Record 132 of Set 0|bacuit
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bacuit
    Processing Record 133 of Set 0|helong
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=helong
    Processing Record 134 of Set 0|leningradskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=leningradskiy
    Processing Record 135 of Set 0|alofi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=alofi
    Processing Record 136 of Set 0|kahului
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kahului
    Processing Record 137 of Set 0|palana
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=palana
    Processing Record 138 of Set 0|henties bay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=henties bay
    Processing Record 139 of Set 0|samalaeulu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=samalaeulu
    Processing Record 140 of Set 0|marhaura
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=marhaura
    Processing Record 141 of Set 0|carballo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=carballo
    Processing Record 142 of Set 0|puerto penasco
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=puerto penasco
    Processing Record 143 of Set 0|cottonwood
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cottonwood
    Processing Record 144 of Set 0|kangaatsiaq
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kangaatsiaq
    Processing Record 145 of Set 0|victor harbor
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=victor harbor
    Processing Record 146 of Set 0|rodrigues alves
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=rodrigues alves
    Processing Record 147 of Set 0|sistranda
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sistranda
    Processing Record 148 of Set 0|maniitsoq
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=maniitsoq
    Processing Record 149 of Set 0|chokurdakh
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=chokurdakh
    Processing Record 150 of Set 0|qasigiannguit
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=qasigiannguit
    Processing Record 151 of Set 0|koster
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=koster
    Processing Record 152 of Set 0|paragominas
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=paragominas
    Processing Record 153 of Set 0|bachaquero
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bachaquero
    Processing Record 154 of Set 0|cherskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cherskiy
    Processing Record 155 of Set 0|duz
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=duz
    Processing Record 156 of Set 0|neuruppin
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=neuruppin
    Processing Record 157 of Set 0|saposoa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=saposoa
    Processing Record 158 of Set 0|ponta do sol
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ponta do sol
    Processing Record 159 of Set 0|upernavik
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=upernavik
    Processing Record 160 of Set 0|victoria
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=victoria
    Processing Record 161 of Set 0|salalah
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=salalah
    Processing Record 162 of Set 0|sur
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sur
    Processing Record 163 of Set 0|mildura
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mildura
    Processing Record 164 of Set 0|palmer
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=palmer
    Processing Record 165 of Set 0|gwadar
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=gwadar
    Processing Record 166 of Set 0|batagay-alyta
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=batagay-alyta
    Processing Record 167 of Set 0|ribeira grande
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ribeira grande
    Processing Record 168 of Set 0|cabo san lucas
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cabo san lucas
    Processing Record 169 of Set 0|gazni
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=gazni
    Processing Record 170 of Set 0|bredasdorp
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bredasdorp
    Processing Record 171 of Set 0|pisco
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=pisco
    Processing Record 172 of Set 0|afmadu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=afmadu
    Processing Record 173 of Set 0|priiskovyy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=priiskovyy
    Processing Record 174 of Set 0|eyl
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=eyl
    Processing Record 175 of Set 0|mys shmidta
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mys shmidta
    Processing Record 176 of Set 0|wattegama
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=wattegama
    Processing Record 177 of Set 0|balkhash
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=balkhash
    Processing Record 178 of Set 0|manturovo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=manturovo
    Processing Record 179 of Set 0|cap malheureux
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cap malheureux
    Processing Record 180 of Set 0|katsuura
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=katsuura
    Processing Record 181 of Set 0|sao joao da barra
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sao joao da barra
    Processing Record 182 of Set 0|domna
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=domna
    Processing Record 183 of Set 0|longyearbyen
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=longyearbyen
    Processing Record 184 of Set 0|cervo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cervo
    Processing Record 185 of Set 0|murdochville
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=murdochville
    Processing Record 186 of Set 0|cabadiangan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cabadiangan
    Processing Record 187 of Set 0|codrington
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=codrington
    Processing Record 188 of Set 0|rapid valley
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=rapid valley
    Processing Record 189 of Set 0|luderitz
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=luderitz
    Processing Record 190 of Set 0|copacabana
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=copacabana
    Processing Record 191 of Set 0|certeju de sus
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=certeju de sus
    Processing Record 192 of Set 0|kodiak
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kodiak
    Processing Record 193 of Set 0|bakchar
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bakchar
    Processing Record 194 of Set 0|haywards heath
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=haywards heath
    Processing Record 195 of Set 0|road town
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=road town
    Processing Record 196 of Set 0|klyuchi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=klyuchi
    Processing Record 197 of Set 0|lincoln
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lincoln
    Processing Record 198 of Set 0|tucuma
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tucuma
    Processing Record 199 of Set 0|vardo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=vardo
    Processing Record 200 of Set 0|bodmin
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bodmin
    Processing Record 201 of Set 0|praia
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=praia
    Processing Record 202 of Set 0|bellary
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bellary
    Processing Record 203 of Set 0|novobirilyussy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=novobirilyussy
    Processing Record 204 of Set 0|chicama
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=chicama
    Processing Record 205 of Set 0|port hedland
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=port hedland
    Processing Record 206 of Set 0|avrameni
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=avrameni
    Processing Record 207 of Set 0|rumphi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=rumphi
    Processing Record 208 of Set 0|axim
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=axim
    Processing Record 209 of Set 0|mackenzie
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mackenzie
    Processing Record 210 of Set 0|shahreza
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=shahreza
    Processing Record 211 of Set 0|saskylakh
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=saskylakh
    Processing Record 212 of Set 0|sambava
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sambava
    Processing Record 213 of Set 0|hilo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hilo
    Processing Record 214 of Set 0|trairi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=trairi
    Processing Record 215 of Set 0|saint george
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=saint george
    Processing Record 216 of Set 0|el carrizo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=el carrizo
    Processing Record 217 of Set 0|lompoc
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lompoc
    Processing Record 218 of Set 0|fortuna
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=fortuna
    Processing Record 219 of Set 0|aykhal
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=aykhal
    Processing Record 220 of Set 0|havoysund
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=havoysund
    Processing Record 221 of Set 0|liwale
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=liwale
    Processing Record 222 of Set 0|camapua
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=camapua
    Processing Record 223 of Set 0|kidal
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kidal
    Processing Record 224 of Set 0|gizo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=gizo
    Processing Record 225 of Set 0|marcona
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=marcona
    Processing Record 226 of Set 0|juneau
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=juneau
    Processing Record 227 of Set 0|chegdomyn
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=chegdomyn
    Processing Record 228 of Set 0|moyale
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=moyale
    Processing Record 229 of Set 0|vila franca do campo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=vila franca do campo
    Processing Record 230 of Set 0|marawi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=marawi
    Processing Record 231 of Set 0|laguna
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=laguna
    Processing Record 232 of Set 0|fort frances
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=fort frances
    Processing Record 233 of Set 0|hamadan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hamadan
    Processing Record 234 of Set 0|kaiu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kaiu
    Processing Record 235 of Set 0|kamaishi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kamaishi
    Processing Record 236 of Set 0|portobelo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=portobelo
    Processing Record 237 of Set 0|belushya guba
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=belushya guba
    Processing Record 238 of Set 0|tongzi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tongzi
    Processing Record 239 of Set 0|riyadh
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=riyadh
    Processing Record 240 of Set 0|lydenburg
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lydenburg
    Processing Record 241 of Set 0|shahrud
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=shahrud
    Processing Record 242 of Set 0|solnechnyy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=solnechnyy
    Processing Record 243 of Set 0|thompson
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=thompson
    Processing Record 244 of Set 0|tommot
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tommot
    Processing Record 245 of Set 0|azimur
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=azimur
    Processing Record 246 of Set 0|harper
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=harper
    Processing Record 247 of Set 0|tiznit
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tiznit
    Processing Record 248 of Set 0|portland
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=portland
    Processing Record 249 of Set 0|ixtapa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ixtapa
    Processing Record 250 of Set 0|marystown
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=marystown
    Processing Record 251 of Set 0|bengkulu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bengkulu
    Processing Record 252 of Set 0|beira
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=beira
    Processing Record 253 of Set 0|ambon
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ambon
    Processing Record 254 of Set 0|erzin
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=erzin
    Processing Record 255 of Set 0|norman wells
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=norman wells
    Processing Record 256 of Set 0|roald
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=roald
    Processing Record 257 of Set 0|tumaco
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tumaco
    Processing Record 258 of Set 0|hudson bay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hudson bay
    Processing Record 259 of Set 0|iqaluit
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=iqaluit
    Processing Record 260 of Set 0|hualmay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hualmay
    Processing Record 261 of Set 0|teluknaga
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=teluknaga
    Processing Record 262 of Set 0|ahero
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ahero
    Processing Record 263 of Set 0|komsomolskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=komsomolskiy
    Processing Record 264 of Set 0|yoichi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=yoichi
    Processing Record 265 of Set 0|pevek
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=pevek
    Processing Record 266 of Set 0|khani
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=khani
    Processing Record 267 of Set 0|koutsouras
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=koutsouras
    Processing Record 268 of Set 0|ormara
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ormara
    Processing Record 269 of Set 0|muscat
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=muscat
    Processing Record 270 of Set 0|manadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=manadhoo
    Processing Record 271 of Set 0|badulla
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=badulla
    Processing Record 272 of Set 0|micheweni
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=micheweni
    Processing Record 273 of Set 0|geraldton
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=geraldton
    Processing Record 274 of Set 0|brae
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=brae
    Processing Record 275 of Set 0|teluk nibung
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=teluk nibung
    Processing Record 276 of Set 0|nemuro
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nemuro
    Processing Record 277 of Set 0|ksenyevka
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ksenyevka
    Processing Record 278 of Set 0|sungaipenuh
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sungaipenuh
    Processing Record 279 of Set 0|lumut
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lumut
    Processing Record 280 of Set 0|paamiut
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=paamiut
    Processing Record 281 of Set 0|severo-kurilsk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=severo-kurilsk
    Processing Record 282 of Set 0|chimore
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=chimore
    Processing Record 283 of Set 0|yulara
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=yulara
    Processing Record 284 of Set 0|strathmore
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=strathmore
    Processing Record 285 of Set 0|lagoa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lagoa
    Processing Record 286 of Set 0|ambilobe
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ambilobe
    Processing Record 287 of Set 0|kaeo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kaeo
    Processing Record 288 of Set 0|lolua
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lolua
    Processing Record 289 of Set 0|rawannawi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=rawannawi
    Processing Record 290 of Set 0|mahbubabad
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mahbubabad
    Processing Record 291 of Set 0|wewak
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=wewak
    Processing Record 292 of Set 0|olafsvik
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=olafsvik
    Processing Record 293 of Set 0|tahta
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tahta
    Processing Record 294 of Set 0|senno
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=senno
    Processing Record 295 of Set 0|rawson
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=rawson
    Processing Record 296 of Set 0|denizli
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=denizli
    Processing Record 297 of Set 0|jamestown
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=jamestown
    Processing Record 298 of Set 0|berlevag
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=berlevag
    Processing Record 299 of Set 0|bandarbeyla
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bandarbeyla
    Processing Record 300 of Set 0|oktyabrskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=oktyabrskiy
    Processing Record 301 of Set 0|necochea
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=necochea
    Processing Record 302 of Set 0|dukat
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=dukat
    Processing Record 303 of Set 0|la palma
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=la palma
    Processing Record 304 of Set 0|cunha
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cunha
    Processing Record 305 of Set 0|louis trichardt
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=louis trichardt
    Processing Record 306 of Set 0|sao filipe
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sao filipe
    Processing Record 307 of Set 0|maku
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=maku
    Processing Record 308 of Set 0|rocha
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=rocha
    Processing Record 309 of Set 0|faanui
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=faanui
    Processing Record 310 of Set 0|clarence town
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=clarence town
    Processing Record 311 of Set 0|tabiauea
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tabiauea
    Processing Record 312 of Set 0|zhezkazgan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=zhezkazgan
    Processing Record 313 of Set 0|plettenberg bay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=plettenberg bay
    Processing Record 314 of Set 0|lithgow
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lithgow
    Processing Record 315 of Set 0|urumqi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=urumqi
    Processing Record 316 of Set 0|toliary
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=toliary
    Processing Record 317 of Set 0|narsaq
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=narsaq
    Processing Record 318 of Set 0|valparaiso
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=valparaiso
    Processing Record 319 of Set 0|port hardy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=port hardy
    Processing Record 320 of Set 0|zhigansk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=zhigansk
    Processing Record 321 of Set 0|bela
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bela
    Processing Record 322 of Set 0|jutai
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=jutai
    Processing Record 323 of Set 0|constantine
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=constantine
    Processing Record 324 of Set 0|sola
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sola
    Processing Record 325 of Set 0|morro bay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=morro bay
    Processing Record 326 of Set 0|odweyne
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=odweyne
    Processing Record 327 of Set 0|touros
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=touros
    Processing Record 328 of Set 0|bubaque
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bubaque
    Processing Record 329 of Set 0|obo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=obo
    Processing Record 330 of Set 0|dawei
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=dawei
    Processing Record 331 of Set 0|el alto
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=el alto
    Processing Record 332 of Set 0|malwan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=malwan
    Processing Record 333 of Set 0|zhanatas
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=zhanatas
    Processing Record 334 of Set 0|tianpeng
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tianpeng
    Processing Record 335 of Set 0|korla
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=korla
    Processing Record 336 of Set 0|amazar
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=amazar
    Processing Record 337 of Set 0|moyo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=moyo
    Processing Record 338 of Set 0|los llanos de aridane
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=los llanos de aridane
    Processing Record 339 of Set 0|ponta do sol
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ponta do sol
    Processing Record 340 of Set 0|sfantu gheorghe
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sfantu gheorghe
    Processing Record 341 of Set 0|muisne
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=muisne
    Processing Record 342 of Set 0|san cristobal
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=san cristobal
    Processing Record 343 of Set 0|aksarayskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=aksarayskiy
    Processing Record 344 of Set 0|marfino
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=marfino
    Processing Record 345 of Set 0|waipawa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=waipawa
    Processing Record 346 of Set 0|beringovskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=beringovskiy
    Processing Record 347 of Set 0|mahibadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mahibadhoo
    Processing Record 348 of Set 0|kysyl-syr
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kysyl-syr
    Processing Record 349 of Set 0|vaitupu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=vaitupu
    Processing Record 350 of Set 0|point pleasant
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=point pleasant
    Processing Record 351 of Set 0|high level
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=high level
    Processing Record 352 of Set 0|kaitangata
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kaitangata
    Processing Record 353 of Set 0|tuktoyaktuk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tuktoyaktuk
    Processing Record 354 of Set 0|mahebourg
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mahebourg
    Processing Record 355 of Set 0|walvis bay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=walvis bay
    Processing Record 356 of Set 0|carutapera
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=carutapera
    Processing Record 357 of Set 0|tarauaca
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tarauaca
    Processing Record 358 of Set 0|terrace
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=terrace
    Processing Record 359 of Set 0|kondratovo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kondratovo
    Processing Record 360 of Set 0|amderma
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=amderma
    Processing Record 361 of Set 0|hunza
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hunza
    Processing Record 362 of Set 0|bria
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bria
    Processing Record 363 of Set 0|faya
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=faya
    Processing Record 364 of Set 0|tuggurt
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tuggurt
    Processing Record 365 of Set 0|bintulu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bintulu
    Processing Record 366 of Set 0|itoman
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=itoman
    Processing Record 367 of Set 0|mookane
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mookane
    Processing Record 368 of Set 0|shingu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=shingu
    Processing Record 369 of Set 0|port-gentil
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=port-gentil
    Processing Record 370 of Set 0|langsa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=langsa
    Processing Record 371 of Set 0|sangar
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sangar
    Processing Record 372 of Set 0|chkalovskoye
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=chkalovskoye
    Processing Record 373 of Set 0|maldonado
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=maldonado
    Processing Record 374 of Set 0|college
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=college
    Processing Record 375 of Set 0|videira
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=videira
    Processing Record 376 of Set 0|zyryanka
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=zyryanka
    Processing Record 377 of Set 0|pochutla
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=pochutla
    Processing Record 378 of Set 0|thinadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=thinadhoo
    Processing Record 379 of Set 0|srednekolymsk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=srednekolymsk
    Processing Record 380 of Set 0|tres picos
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tres picos
    Processing Record 381 of Set 0|millau
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=millau
    Processing Record 382 of Set 0|sao felix do xingu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sao felix do xingu
    Processing Record 383 of Set 0|polonnaruwa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=polonnaruwa
    Processing Record 384 of Set 0|havelock
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=havelock
    Processing Record 385 of Set 0|sept-iles
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sept-iles
    Processing Record 386 of Set 0|buchanan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=buchanan
    Processing Record 387 of Set 0|aktau
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=aktau
    Processing Record 388 of Set 0|srivardhan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=srivardhan
    Processing Record 389 of Set 0|samarai
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=samarai
    Processing Record 390 of Set 0|naryan-mar
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=naryan-mar
    Processing Record 391 of Set 0|alyangula
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=alyangula
    Processing Record 392 of Set 0|copiapo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=copiapo
    Processing Record 393 of Set 0|andujar
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=andujar
    Processing Record 394 of Set 0|pahrump
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=pahrump
    Processing Record 395 of Set 0|ostrovnoy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ostrovnoy
    Processing Record 396 of Set 0|castro
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=castro
    Processing Record 397 of Set 0|nantucket
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nantucket
    Processing Record 398 of Set 0|tessalit
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tessalit
    Processing Record 399 of Set 0|namtsy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=namtsy
    Processing Record 400 of Set 0|exeter
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=exeter
    Processing Record 401 of Set 0|dunedin
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=dunedin
    Processing Record 402 of Set 0|okhotsk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=okhotsk
    Processing Record 403 of Set 0|nguiu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nguiu
    Processing Record 404 of Set 0|cayenne
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cayenne
    Processing Record 405 of Set 0|southbridge
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=southbridge
    Processing Record 406 of Set 0|mabaruma
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mabaruma
    Processing Record 407 of Set 0|jinchang
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=jinchang
    Processing Record 408 of Set 0|tura
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tura
    Processing Record 409 of Set 0|jiddah
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=jiddah
    Processing Record 410 of Set 0|cordoba
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cordoba
    Processing Record 411 of Set 0|jalu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=jalu
    Processing Record 412 of Set 0|camacha
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=camacha
    Processing Record 413 of Set 0|kudahuvadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kudahuvadhoo
    Processing Record 414 of Set 0|chiang klang
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=chiang klang
    Processing Record 415 of Set 0|sainte-adele
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sainte-adele
    Processing Record 416 of Set 0|tzaneen
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tzaneen
    Processing Record 417 of Set 0|bossangoa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bossangoa
    Processing Record 418 of Set 0|polis
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=polis
    Processing Record 419 of Set 0|port blair
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=port blair
    Processing Record 420 of Set 0|mehamn
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mehamn
    Processing Record 421 of Set 0|nizwa
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nizwa
    Processing Record 422 of Set 0|bulaevo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bulaevo
    Processing Record 423 of Set 0|asayita
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=asayita
    Processing Record 424 of Set 0|makakilo city
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=makakilo city
    Processing Record 425 of Set 0|udachnyy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=udachnyy
    Processing Record 426 of Set 0|manokwari
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=manokwari
    Processing Record 427 of Set 0|zhucheng
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=zhucheng
    Processing Record 428 of Set 0|oistins
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=oistins
    Processing Record 429 of Set 0|sterling
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sterling
    Processing Record 430 of Set 0|flinders
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=flinders
    Processing Record 431 of Set 0|malacacheta
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=malacacheta
    Processing Record 432 of Set 0|manado
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=manado
    Processing Record 433 of Set 0|north myrtle beach
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=north myrtle beach
    Processing Record 434 of Set 0|kisangani
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kisangani
    Processing Record 435 of Set 0|cockburn town
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cockburn town
    Processing Record 436 of Set 0|kirakira
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kirakira
    Processing Record 437 of Set 0|puerto colombia
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=puerto colombia
    Processing Record 438 of Set 0|coihaique
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=coihaique
    Processing Record 439 of Set 0|sibu
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sibu
    Processing Record 440 of Set 0|acarau
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=acarau
    Processing Record 441 of Set 0|haines junction
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=haines junction
    Processing Record 442 of Set 0|lima
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lima
    Processing Record 443 of Set 0|tuatapere
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=tuatapere
    Processing Record 444 of Set 0|alcaniz
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=alcaniz
    Processing Record 445 of Set 0|desbiens
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=desbiens
    Processing Record 446 of Set 0|kijang
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kijang
    Processing Record 447 of Set 0|jacala
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=jacala
    Processing Record 448 of Set 0|mikhaylovka
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mikhaylovka
    Processing Record 449 of Set 0|kieta
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kieta
    Processing Record 450 of Set 0|ullapool
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ullapool
    Processing Record 451 of Set 0|nyrob
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nyrob
    Processing Record 452 of Set 0|marsa matruh
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=marsa matruh
    Processing Record 453 of Set 0|oleksandrivka
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=oleksandrivka
    Processing Record 454 of Set 0|fairbanks
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=fairbanks
    Processing Record 455 of Set 0|izhmorskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=izhmorskiy
    Processing Record 456 of Set 0|malakal
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=malakal
    Processing Record 457 of Set 0|blackfoot
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=blackfoot
    Processing Record 458 of Set 0|dzilam gonzalez
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=dzilam gonzalez
    Processing Record 459 of Set 0|itacoatiara
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=itacoatiara
    Processing Record 460 of Set 0|padang
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=padang
    Processing Record 461 of Set 0|noumea
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=noumea
    Processing Record 462 of Set 0|eydhafushi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=eydhafushi
    Processing Record 463 of Set 0|westport
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=westport
    Processing Record 464 of Set 0|monrovia
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=monrovia
    Processing Record 465 of Set 0|te anau
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=te anau
    Processing Record 466 of Set 0|lumberton
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lumberton
    Processing Record 467 of Set 0|asfi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=asfi
    Processing Record 468 of Set 0|karratha
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=karratha
    Processing Record 469 of Set 0|mezen
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mezen
    Processing Record 470 of Set 0|san luis
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=san luis
    Processing Record 471 of Set 0|demmin
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=demmin
    Processing Record 472 of Set 0|yatou
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=yatou
    Processing Record 473 of Set 0|torit
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=torit
    Processing Record 474 of Set 0|barbar
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=barbar
    Processing Record 475 of Set 0|batemans bay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=batemans bay
    Processing Record 476 of Set 0|loding
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=loding
    Processing Record 477 of Set 0|fujin
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=fujin
    Processing Record 478 of Set 0|luena
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=luena
    Processing Record 479 of Set 0|marang
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=marang
    Processing Record 480 of Set 0|susanville
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=susanville
    Processing Record 481 of Set 0|kremenki
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kremenki
    Processing Record 482 of Set 0|cuauhtemoc
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cuauhtemoc
    Processing Record 483 of Set 0|comodoro rivadavia
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=comodoro rivadavia
    Processing Record 484 of Set 0|ifakara
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=ifakara
    Processing Record 485 of Set 0|kumphawapi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kumphawapi
    Processing Record 486 of Set 0|odienne
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=odienne
    Processing Record 487 of Set 0|loudi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=loudi
    Processing Record 488 of Set 0|muros
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=muros
    Processing Record 489 of Set 0|roblin
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=roblin
    Processing Record 490 of Set 0|roma
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=roma
    Processing Record 491 of Set 0|bathsheba
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bathsheba
    Processing Record 492 of Set 0|opuwo
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=opuwo
    Processing Record 493 of Set 0|iquitos
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=iquitos
    Processing Record 494 of Set 0|butajira
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=butajira
    Processing Record 495 of Set 0|nuuk
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nuuk
    Processing Record 496 of Set 0|hvide sande
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=hvide sande
    Processing Record 497 of Set 0|broken hill
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=broken hill
    Processing Record 498 of Set 0|kendari
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=kendari
    Processing Record 499 of Set 0|klaksvik
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=klaksvik
    Processing Record 500 of Set 0|achisay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=achisay
    Processing Record 501 of Set 0|azul
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=azul
    Processing Record 502 of Set 0|morris
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=morris
    Processing Record 503 of Set 0|havre-saint-pierre
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=havre-saint-pierre
    Processing Record 504 of Set 0|coroico
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=coroico
    Processing Record 505 of Set 0|lavrentiya
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lavrentiya
    Processing Record 506 of Set 0|sakata
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sakata
    Processing Record 507 of Set 0|arman
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=arman
    Processing Record 508 of Set 0|mwense
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=mwense
    Processing Record 509 of Set 0|caucaia
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=caucaia
    Processing Record 510 of Set 0|petropavlovsk-kamchatskiy
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=petropavlovsk-kamchatskiy
    Processing Record 511 of Set 0|puksoozero
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=puksoozero
    Processing Record 512 of Set 0|huarmey
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=huarmey
    Processing Record 513 of Set 0|osakarovka
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=osakarovka
    Processing Record 514 of Set 0|coahuayana
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=coahuayana
    Processing Record 515 of Set 0|uyuni
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=uyuni
    Processing Record 516 of Set 0|lorengau
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=lorengau
    Processing Record 517 of Set 0|naze
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=naze
    Processing Record 518 of Set 0|novopokrovka
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=novopokrovka
    Processing Record 519 of Set 0|vostok
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=vostok
    Processing Record 520 of Set 0|shubarshi
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=shubarshi
    Processing Record 521 of Set 0|sulangan
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sulangan
    Processing Record 522 of Set 0|houma
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=houma
    Processing Record 523 of Set 0|bilma
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=bilma
    Processing Record 524 of Set 0|teya
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=teya
    Processing Record 525 of Set 0|taoudenni
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=taoudenni
    Processing Record 526 of Set 0|viedma
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=viedma
    Processing Record 527 of Set 0|sorland
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=sorland
    Processing Record 528 of Set 0|russell
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=russell
    Processing Record 529 of Set 0|nelson bay
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=nelson bay
    Processing Record 530 of Set 0|andros town
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=andros town
    Processing Record 531 of Set 0|cap-haitien
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=cap-haitien
    Processing Record 532 of Set 0|jiblah
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=jiblah
    Processing Record 533 of Set 0|presidencia roque saenz pena
    http://api.openweathermap.org/data/2.5/weather?appid=96b392d27de5ad004a079b28fe040981&unitsImperial&q=presidencia roque saenz pena
    


```python
# Generate new Dataframe
df = pd.DataFrame(Weather)
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>base</th>
      <th>clouds</th>
      <th>cod</th>
      <th>coord</th>
      <th>dt</th>
      <th>id</th>
      <th>main</th>
      <th>name</th>
      <th>rain</th>
      <th>sys</th>
      <th>visibility</th>
      <th>weather</th>
      <th>wind</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': -97.07, 'lat': 15.85}</td>
      <td>1505414700</td>
      <td>3520994</td>
      <td>{'temp': 302.15, 'pressure': 1016, 'humidity':...</td>
      <td>Puerto Escondido</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4010, 'message': 0.0033, 'co...</td>
      <td>16093.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 4.1, 'deg': 250}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>stations</td>
      <td>{'all': 20}</td>
      <td>200</td>
      <td>{'lon': 30.67, 'lat': 59.68}</td>
      <td>1505417400</td>
      <td>541826</td>
      <td>{'temp': 286.15, 'pressure': 990, 'humidity': ...</td>
      <td>Krasnyy Bor</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 7267, 'message': 0.0051, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 6, 'deg': 200}</td>
    </tr>
    <tr>
      <th>2</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': -42.03, 'lat': -22.97}</td>
      <td>1505419200</td>
      <td>3471451</td>
      <td>{'temp': 298.15, 'pressure': 1017, 'humidity':...</td>
      <td>Arraial do Cabo</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4469, 'message': 0.004, 'cou...</td>
      <td>10000.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 10.3, 'deg': 80}</td>
    </tr>
    <tr>
      <th>3</th>
      <td>stations</td>
      <td>{'all': 100}</td>
      <td>200</td>
      <td>{'lon': -45.24, 'lat': 60.14}</td>
      <td>1505419682</td>
      <td>3421765</td>
      <td>{'temp': 278.36, 'pressure': 1003.78, 'humidit...</td>
      <td>Nanortalik</td>
      <td>{'3h': 17.015}</td>
      <td>{'message': 0.0038, 'country': 'GL', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 502, 'main': 'Rain', 'description': 'h...</td>
      <td>{'speed': 10.75, 'deg': 74.5008}</td>
    </tr>
    <tr>
      <th>4</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 18.42, 'lat': -33.93}</td>
      <td>1505415600</td>
      <td>3369157</td>
      <td>{'temp': 288.15, 'pressure': 1020, 'humidity':...</td>
      <td>Cape Town</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 6529, 'message': 0.0088, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 7.2, 'deg': 190}</td>
    </tr>
    <tr>
      <th>5</th>
      <td>stations</td>
      <td>{'all': 1}</td>
      <td>200</td>
      <td>{'lon': -159.32, 'lat': 22.08}</td>
      <td>1505415360</td>
      <td>5848280</td>
      <td>{'temp': 301.04, 'pressure': 1014, 'humidity':...</td>
      <td>Kapaa</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 833, 'message': 0.0032, 'cou...</td>
      <td>16093.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 1.5}</td>
    </tr>
    <tr>
      <th>6</th>
      <td>stations</td>
      <td>{'all': 40}</td>
      <td>200</td>
      <td>{'lon': -52.73, 'lat': 47.67}</td>
      <td>1505415600</td>
      <td>6167817</td>
      <td>{'temp': 295.15, 'pressure': 1005, 'humidity':...</td>
      <td>Torbay</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 3467, 'message': 0.0044, 'co...</td>
      <td>24140.0</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 8.2, 'deg': 270, 'gust': 12.9}</td>
    </tr>
    <tr>
      <th>7</th>
      <td>stations</td>
      <td>{'all': 64}</td>
      <td>200</td>
      <td>{'lon': -134.97, 'lat': -23.12}</td>
      <td>1505419682</td>
      <td>4030556</td>
      <td>{'temp': 294.56, 'pressure': 1032.47, 'humidit...</td>
      <td>Rikitea</td>
      <td>NaN</td>
      <td>{'message': 0.0039, 'country': 'PF', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 4, 'deg': 96.5008}</td>
    </tr>
    <tr>
      <th>8</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': -73.76, 'lat': 42.65}</td>
      <td>1505418840</td>
      <td>5106834</td>
      <td>{'temp': 298.12, 'pressure': 1011, 'humidity':...</td>
      <td>Albany</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 2088, 'message': 0.0052, 'co...</td>
      <td>16093.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.6, 'deg': 170}</td>
    </tr>
    <tr>
      <th>9</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': 21.1, 'lat': 54.86}</td>
      <td>1505417400</td>
      <td>507291</td>
      <td>{'temp': 286.15, 'pressure': 997, 'humidity': ...</td>
      <td>Polessk</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 7275, 'message': 0.0042, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 6, 'deg': 210, 'gust': 11}</td>
    </tr>
    <tr>
      <th>10</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': 26.83, 'lat': 55.12}</td>
      <td>1505419682</td>
      <td>623760</td>
      <td>{'temp': 285.91, 'pressure': 995.51, 'humidity...</td>
      <td>Pastavy</td>
      <td>NaN</td>
      <td>{'message': 0.0084, 'country': 'BY', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 7.15, 'deg': 231.001}</td>
    </tr>
    <tr>
      <th>11</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': -73.65, 'lat': -37.62}</td>
      <td>1505419682</td>
      <td>3883457</td>
      <td>{'temp': 283.21, 'pressure': 1042.77, 'humidit...</td>
      <td>Lebu</td>
      <td>NaN</td>
      <td>{'message': 0.0033, 'country': 'CL', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 9.75, 'deg': 179.001}</td>
    </tr>
    <tr>
      <th>12</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': 93.3, 'lat': 54.17}</td>
      <td>1505419683</td>
      <td>1502389</td>
      <td>{'temp': 278.91, 'pressure': 973.14, 'humidity...</td>
      <td>Koshurnikovo</td>
      <td>NaN</td>
      <td>{'message': 0.0051, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 1.1, 'deg': 177.001}</td>
    </tr>
    <tr>
      <th>13</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 113.63, 'lat': -24.87}</td>
      <td>1505419683</td>
      <td>2074865</td>
      <td>{'temp': 290.96, 'pressure': 1027.69, 'humidit...</td>
      <td>Carnarvon</td>
      <td>NaN</td>
      <td>{'message': 0.0038, 'country': 'AU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 1.65, 'deg': 100.501}</td>
    </tr>
    <tr>
      <th>14</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': 115.33, 'lat': -33.65}</td>
      <td>1505419683</td>
      <td>2075265</td>
      <td>{'temp': 287.46, 'pressure': 1030.36, 'humidit...</td>
      <td>Busselton</td>
      <td>NaN</td>
      <td>{'message': 0.0031, 'country': 'AU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 9.45, 'deg': 131.001}</td>
    </tr>
    <tr>
      <th>15</th>
      <td>stations</td>
      <td>{'all': 44}</td>
      <td>200</td>
      <td>{'lon': 106.61, 'lat': 23.9}</td>
      <td>1505419683</td>
      <td>1816269</td>
      <td>{'temp': 296.06, 'pressure': 968.92, 'humidity...</td>
      <td>Baicheng</td>
      <td>{'3h': 0.1075}</td>
      <td>{'message': 0.0036, 'country': 'CN', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 1.75, 'deg': 28.5008}</td>
    </tr>
    <tr>
      <th>16</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 46.97, 'lat': -25.02}</td>
      <td>1505415600</td>
      <td>1078317</td>
      <td>{'temp': 292.15, 'pressure': 1014, 'humidity':...</td>
      <td>Amparihy</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 6809, 'message': 0.0038, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 2.1, 'deg': 280}</td>
    </tr>
    <tr>
      <th>17</th>
      <td>stations</td>
      <td>{'all': 48}</td>
      <td>200</td>
      <td>{'lon': 9.96, 'lat': 57.59}</td>
      <td>1505419683</td>
      <td>2620279</td>
      <td>{'temp': 286.11, 'pressure': 1007.43, 'humidit...</td>
      <td>Hirtshals</td>
      <td>NaN</td>
      <td>{'message': 0.0057, 'country': 'DK', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 3.55, 'deg': 291.001}</td>
    </tr>
    <tr>
      <th>18</th>
      <td>stations</td>
      <td>{'all': 8}</td>
      <td>200</td>
      <td>{'lon': 102.5, 'lat': 71.97}</td>
      <td>1505419683</td>
      <td>2022572</td>
      <td>{'temp': 275.76, 'pressure': 1019.99, 'humidit...</td>
      <td>Khatanga</td>
      <td>NaN</td>
      <td>{'message': 0.0035, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 4.9, 'deg': 115.501}</td>
    </tr>
    <tr>
      <th>19</th>
      <td>stations</td>
      <td>{'all': 48}</td>
      <td>200</td>
      <td>{'lon': 131.25, 'lat': -0.88}</td>
      <td>1505419683</td>
      <td>1626542</td>
      <td>{'temp': 299.76, 'pressure': 1020.72, 'humidit...</td>
      <td>Sorong</td>
      <td>NaN</td>
      <td>{'message': 0.0054, 'country': 'ID', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.7, 'deg': 180.501}</td>
    </tr>
    <tr>
      <th>20</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': 90.39, 'lat': 56.01}</td>
      <td>1505419684</td>
      <td>1497951</td>
      <td>{'temp': 277.91, 'pressure': 992.59, 'humidity...</td>
      <td>Nazarovo</td>
      <td>{'3h': 0.375}</td>
      <td>{'message': 0.0067, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 3.4, 'deg': 218.501}</td>
    </tr>
    <tr>
      <th>21</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': 25.51, 'lat': 69.47}</td>
      <td>1505418600</td>
      <td>779350</td>
      <td>{'temp': 279.15, 'pressure': 1000, 'humidity':...</td>
      <td>Karasjok</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 5310, 'message': 0.0038, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 6.2, 'deg': 10}</td>
    </tr>
    <tr>
      <th>22</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 150.8, 'lat': -2.57}</td>
      <td>1505419684</td>
      <td>2094342</td>
      <td>{'temp': 301.66, 'pressure': 1021.77, 'humidit...</td>
      <td>Kavieng</td>
      <td>NaN</td>
      <td>{'message': 0.0178, 'country': 'PG', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 3.35, 'deg': 172.001}</td>
    </tr>
    <tr>
      <th>23</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': -114.35, 'lat': 62.46}</td>
      <td>1505415600</td>
      <td>6185377</td>
      <td>{'temp': 282.15, 'pressure': 1022, 'humidity':...</td>
      <td>Yellowknife</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 3558, 'message': 0.0029, 'co...</td>
      <td>24140.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 1.5, 'deg': 180}</td>
    </tr>
    <tr>
      <th>24</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': 27.91, 'lat': -33.02}</td>
      <td>1505419684</td>
      <td>1006984</td>
      <td>{'temp': 290.71, 'pressure': 1032.15, 'humidit...</td>
      <td>East London</td>
      <td>{'3h': 0.17}</td>
      <td>{'message': 0.0031, 'country': 'ZA', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 3.7, 'deg': 76.0008}</td>
    </tr>
    <tr>
      <th>25</th>
      <td>stations</td>
      <td>{'all': 68}</td>
      <td>200</td>
      <td>{'lon': 80.55, 'lat': 73.51}</td>
      <td>1505419684</td>
      <td>1507390</td>
      <td>{'temp': 277.31, 'pressure': 1022.34, 'humidit...</td>
      <td>Dikson</td>
      <td>NaN</td>
      <td>{'message': 0.0042, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 7.05, 'deg': 47.0008}</td>
    </tr>
    <tr>
      <th>26</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': -70.92, 'lat': -53.15}</td>
      <td>1505415600</td>
      <td>3874787</td>
      <td>{'temp': 277.15, 'pressure': 998, 'humidity': ...</td>
      <td>Punta Arenas</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4642, 'message': 0.0056, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 520, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 9.8, 'deg': 280}</td>
    </tr>
    <tr>
      <th>27</th>
      <td>stations</td>
      <td>{'all': 80}</td>
      <td>200</td>
      <td>{'lon': 121.9, 'lat': -33.87}</td>
      <td>1505419684</td>
      <td>2071860</td>
      <td>{'temp': 283.86, 'pressure': 1020.56, 'humidit...</td>
      <td>Esperance</td>
      <td>NaN</td>
      <td>{'message': 0.0033, 'country': 'AU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.75, 'deg': 141.501}</td>
    </tr>
    <tr>
      <th>28</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': -50.21, 'lat': -30.18}</td>
      <td>1505419685</td>
      <td>3466165</td>
      <td>{'temp': 292.51, 'pressure': 1019.99, 'humidit...</td>
      <td>Cidreira</td>
      <td>{'3h': 4.12}</td>
      <td>{'message': 0.003, 'country': 'BR', 'sunrise':...</td>
      <td>NaN</td>
      <td>[{'id': 501, 'main': 'Rain', 'description': 'm...</td>
      <td>{'speed': 5.9, 'deg': 272.501}</td>
    </tr>
    <tr>
      <th>29</th>
      <td>stations</td>
      <td>{'all': 76}</td>
      <td>200</td>
      <td>{'lon': -81.62, 'lat': 52.3}</td>
      <td>1505419666</td>
      <td>5989520</td>
      <td>{'temp': 284.46, 'pressure': 1029.31, 'humidit...</td>
      <td>Kashechewan</td>
      <td>NaN</td>
      <td>{'message': 0.0031, 'country': 'CA', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 1.95, 'deg': 4.50082}</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>503</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': -67.73, 'lat': -16.19}</td>
      <td>1505415600</td>
      <td>3919085</td>
      <td>{'temp': 284.15, 'pressure': 1036, 'humidity':...</td>
      <td>Coroico</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4426, 'message': 0.0028, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 5.1, 'deg': 90}</td>
    </tr>
    <tr>
      <th>504</th>
      <td>stations</td>
      <td>{'all': 80}</td>
      <td>200</td>
      <td>{'lon': -171, 'lat': 65.58}</td>
      <td>1505419738</td>
      <td>4031637</td>
      <td>{'temp': 277.96, 'pressure': 1014.23, 'humidit...</td>
      <td>Lavrentiya</td>
      <td>{'3h': 0.16}</td>
      <td>{'message': 0.0033, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 6.5, 'deg': 151.001}</td>
    </tr>
    <tr>
      <th>505</th>
      <td>stations</td>
      <td>{'all': 76}</td>
      <td>200</td>
      <td>{'lon': 139.85, 'lat': 38.92}</td>
      <td>1505419739</td>
      <td>1853140</td>
      <td>{'temp': 291.61, 'pressure': 1016.91, 'humidit...</td>
      <td>Sakata</td>
      <td>NaN</td>
      <td>{'message': 0.004, 'country': 'JP', 'sunrise':...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 6.9, 'deg': 307.501}</td>
    </tr>
    <tr>
      <th>506</th>
      <td>stations</td>
      <td>{'all': 12}</td>
      <td>200</td>
      <td>{'lon': 150.17, 'lat': 59.7}</td>
      <td>1505415600</td>
      <td>2127060</td>
      <td>{'temp': 267.15, 'pressure': 1014, 'humidity':...</td>
      <td>Arman</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 7243, 'message': 0.0041, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 741, 'main': 'Fog', 'description': 'fo...</td>
      <td>{'speed': 2.05, 'deg': 52.0008}</td>
    </tr>
    <tr>
      <th>507</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 28.7, 'lat': -10.38}</td>
      <td>1505419739</td>
      <td>902721</td>
      <td>{'temp': 291.16, 'pressure': 900.02, 'humidity...</td>
      <td>Mwense</td>
      <td>NaN</td>
      <td>{'message': 0.0033, 'country': 'ZM', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 2, 'deg': 143.501}</td>
    </tr>
    <tr>
      <th>508</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': -38.65, 'lat': -3.74}</td>
      <td>1505419200</td>
      <td>3402429</td>
      <td>{'temp': 300.15, 'pressure': 1012, 'humidity':...</td>
      <td>Caucaia</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4498, 'message': 0.0034, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 6.7, 'deg': 80}</td>
    </tr>
    <tr>
      <th>509</th>
      <td>stations</td>
      <td>{'all': 40}</td>
      <td>200</td>
      <td>{'lon': 158.65, 'lat': 53.05}</td>
      <td>1505417400</td>
      <td>2122104</td>
      <td>{'temp': 277.15, 'pressure': 1013, 'humidity':...</td>
      <td>Petropavlovsk-Kamchatskiy</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 7248, 'message': 0.003, 'cou...</td>
      <td>10000.0</td>
      <td>[{'id': 802, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 3, 'deg': 30}</td>
    </tr>
    <tr>
      <th>510</th>
      <td>stations</td>
      <td>{'all': 92}</td>
      <td>200</td>
      <td>{'lon': 40.61, 'lat': 62.59}</td>
      <td>1505419739</td>
      <td>504187</td>
      <td>{'temp': 284.76, 'pressure': 988.3, 'humidity'...</td>
      <td>Puksoozero</td>
      <td>{'3h': 0.365}</td>
      <td>{'message': 0.0031, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 4.45, 'deg': 228.501}</td>
    </tr>
    <tr>
      <th>511</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': -78.15, 'lat': -10.07}</td>
      <td>1505419739</td>
      <td>3939168</td>
      <td>{'temp': 293.81, 'pressure': 955.14, 'humidity...</td>
      <td>Huarmey</td>
      <td>NaN</td>
      <td>{'message': 0.0035, 'country': 'PE', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 2.1, 'deg': 203.001}</td>
    </tr>
    <tr>
      <th>512</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 72.57, 'lat': 50.56}</td>
      <td>1505419739</td>
      <td>1520327</td>
      <td>{'temp': 277.86, 'pressure': 973.22, 'humidity...</td>
      <td>Osakarovka</td>
      <td>NaN</td>
      <td>{'message': 0.0027, 'country': 'KZ', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 2.2, 'deg': 220.001}</td>
    </tr>
    <tr>
      <th>513</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': -103.68, 'lat': 18.73}</td>
      <td>1505414400</td>
      <td>4013679</td>
      <td>{'temp': 299.15, 'pressure': 1018, 'humidity':...</td>
      <td>Coahuayana</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 3977, 'message': 0.0033, 'co...</td>
      <td>9656.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 5.1, 'deg': 240}</td>
    </tr>
    <tr>
      <th>514</th>
      <td>stations</td>
      <td>{'all': 56}</td>
      <td>200</td>
      <td>{'lon': -66.83, 'lat': -20.46}</td>
      <td>1505419740</td>
      <td>3901903</td>
      <td>{'temp': 286.86, 'pressure': 647.2, 'humidity'...</td>
      <td>Uyuni</td>
      <td>NaN</td>
      <td>{'message': 0.0032, 'country': 'BO', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 6.9, 'deg': 297.501}</td>
    </tr>
    <tr>
      <th>515</th>
      <td>stations</td>
      <td>{'all': 80}</td>
      <td>200</td>
      <td>{'lon': 147.27, 'lat': -2.02}</td>
      <td>1505419740</td>
      <td>2092164</td>
      <td>{'temp': 299.66, 'pressure': 1021.2, 'humidity...</td>
      <td>Lorengau</td>
      <td>{'3h': 1.595}</td>
      <td>{'message': 0.0033, 'country': 'PG', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 2.7, 'deg': 297.001}</td>
    </tr>
    <tr>
      <th>516</th>
      <td>stations</td>
      <td>{'all': 88}</td>
      <td>200</td>
      <td>{'lon': 129.48, 'lat': 28.37}</td>
      <td>1505419740</td>
      <td>1855540</td>
      <td>{'temp': 301.71, 'pressure': 1016.42, 'humidit...</td>
      <td>Naze</td>
      <td>{'3h': 0.99}</td>
      <td>{'message': 0.0035, 'country': 'JP', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 10.15, 'deg': 143.001}</td>
    </tr>
    <tr>
      <th>517</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 36.55, 'lat': 49.84}</td>
      <td>1505417400</td>
      <td>699328</td>
      <td>{'temp': 287.15, 'pressure': 1014, 'humidity':...</td>
      <td>Novopokrovka</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 7355, 'message': 0.003, 'cou...</td>
      <td>10000.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 2.25, 'deg': 161.501}</td>
    </tr>
    <tr>
      <th>518</th>
      <td>stations</td>
      <td>{'all': 88}</td>
      <td>200</td>
      <td>{'lon': 135.88, 'lat': 46.49}</td>
      <td>1505419740</td>
      <td>2013279</td>
      <td>{'temp': 281.91, 'pressure': 971.19, 'humidity...</td>
      <td>Vostok</td>
      <td>{'3h': 0.125}</td>
      <td>{'message': 0.0035, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 500, 'main': 'Rain', 'description': 'l...</td>
      <td>{'speed': 0.95, 'deg': 272.001}</td>
    </tr>
    <tr>
      <th>519</th>
      <td>stations</td>
      <td>{'all': 8}</td>
      <td>200</td>
      <td>{'lon': 57.19, 'lat': 48.59}</td>
      <td>1505419740</td>
      <td>608270</td>
      <td>{'temp': 287.21, 'pressure': 1006.7, 'humidity...</td>
      <td>Shubarshi</td>
      <td>NaN</td>
      <td>{'message': 0.0032, 'country': 'KZ', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 5.25, 'deg': 171.001}</td>
    </tr>
    <tr>
      <th>520</th>
      <td>stations</td>
      <td>{'all': 76}</td>
      <td>200</td>
      <td>{'lon': 123.72, 'lat': 11.14}</td>
      <td>1505419740</td>
      <td>1685422</td>
      <td>{'temp': 299.96, 'pressure': 1022.74, 'humidit...</td>
      <td>Sulangan</td>
      <td>NaN</td>
      <td>{'message': 0.0027, 'country': 'PH', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 3, 'deg': 215.501}</td>
    </tr>
    <tr>
      <th>521</th>
      <td>stations</td>
      <td>{'all': 75}</td>
      <td>200</td>
      <td>{'lon': -90.72, 'lat': 29.6}</td>
      <td>1505417700</td>
      <td>4328010</td>
      <td>{'temp': 302.61, 'pressure': 1013, 'humidity':...</td>
      <td>Houma</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 1178, 'message': 0.004, 'cou...</td>
      <td>16093.0</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.6, 'deg': 120}</td>
    </tr>
    <tr>
      <th>522</th>
      <td>stations</td>
      <td>{'all': 88}</td>
      <td>200</td>
      <td>{'lon': 12.92, 'lat': 18.69}</td>
      <td>1505419741</td>
      <td>2446796</td>
      <td>{'temp': 304.76, 'pressure': 964.38, 'humidity...</td>
      <td>Bilma</td>
      <td>NaN</td>
      <td>{'message': 0.0032, 'country': 'NE', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 804, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 3.15, 'deg': 90.5008}</td>
    </tr>
    <tr>
      <th>523</th>
      <td>stations</td>
      <td>{'all': 64}</td>
      <td>200</td>
      <td>{'lon': 92.63, 'lat': 60.38}</td>
      <td>1505419741</td>
      <td>1489656</td>
      <td>{'temp': 274.86, 'pressure': 980.92, 'humidity...</td>
      <td>Teya</td>
      <td>NaN</td>
      <td>{'message': 0.0038, 'country': 'RU', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 803, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 2.35, 'deg': 231.001}</td>
    </tr>
    <tr>
      <th>524</th>
      <td>stations</td>
      <td>{'all': 8}</td>
      <td>200</td>
      <td>{'lon': -3.98, 'lat': 22.68}</td>
      <td>1505419741</td>
      <td>2450173</td>
      <td>{'temp': 309.11, 'pressure': 989.59, 'humidity...</td>
      <td>Taoudenni</td>
      <td>NaN</td>
      <td>{'message': 0.0029, 'country': 'ML', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 5.8, 'deg': 38.0008}</td>
    </tr>
    <tr>
      <th>525</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': -63, 'lat': -40.81}</td>
      <td>1505419521</td>
      <td>3832899</td>
      <td>{'temp': 283.81, 'pressure': 1031.01, 'humidit...</td>
      <td>Viedma</td>
      <td>NaN</td>
      <td>{'message': 0.0043, 'country': 'AR', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 7.5, 'deg': 218.001}</td>
    </tr>
    <tr>
      <th>526</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 12.69, 'lat': 67.67}</td>
      <td>1505418600</td>
      <td>3137469</td>
      <td>{'temp': 282.15, 'pressure': 995, 'humidity': ...</td>
      <td>Sorland</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 5306, 'message': 0.0035, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 1.5, 'deg': 10}</td>
    </tr>
    <tr>
      <th>527</th>
      <td>stations</td>
      <td>{'all': 1}</td>
      <td>200</td>
      <td>{'lon': -98.86, 'lat': 38.9}</td>
      <td>1505415360</td>
      <td>4278471</td>
      <td>{'temp': 308.82, 'pressure': 1007, 'humidity':...</td>
      <td>Russell</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 1092, 'message': 0.0036, 'co...</td>
      <td>16093.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 9.8, 'deg': 200, 'gust': 13.4}</td>
    </tr>
    <tr>
      <th>528</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 152.15, 'lat': -32.72}</td>
      <td>1505417400</td>
      <td>2155562</td>
      <td>{'temp': 282.15, 'pressure': 1018, 'humidity':...</td>
      <td>Nelson Bay</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 8242, 'message': 0.0036, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 4.6, 'deg': 290}</td>
    </tr>
    <tr>
      <th>529</th>
      <td>stations</td>
      <td>{'all': 20}</td>
      <td>200</td>
      <td>{'lon': -77.77, 'lat': 24.7}</td>
      <td>1505415600</td>
      <td>3572906</td>
      <td>{'temp': 307.15, 'pressure': 1015, 'humidity':...</td>
      <td>Andros Town</td>
      <td>NaN</td>
      <td>{'type': 1, 'id': 4081, 'message': 0.0035, 'co...</td>
      <td>10000.0</td>
      <td>[{'id': 801, 'main': 'Clouds', 'description': ...</td>
      <td>{'speed': 4.6, 'deg': 350}</td>
    </tr>
    <tr>
      <th>530</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': -72.2, 'lat': 19.76}</td>
      <td>1505419742</td>
      <td>3728474</td>
      <td>{'temp': 302.06, 'pressure': 1017.96, 'humidit...</td>
      <td>Cap-Haitien</td>
      <td>NaN</td>
      <td>{'message': 0.0032, 'country': 'HT', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 3.35, 'deg': 342.501}</td>
    </tr>
    <tr>
      <th>531</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': 44.15, 'lat': 13.92}</td>
      <td>1505419742</td>
      <td>74185</td>
      <td>{'temp': 288.61, 'pressure': 839.39, 'humidity...</td>
      <td>Jiblah</td>
      <td>NaN</td>
      <td>{'message': 0.0038, 'country': 'YE', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 0.6, 'deg': 94.5008}</td>
    </tr>
    <tr>
      <th>532</th>
      <td>stations</td>
      <td>{'all': 0}</td>
      <td>200</td>
      <td>{'lon': -60.44, 'lat': -26.79}</td>
      <td>1505419742</td>
      <td>3840300</td>
      <td>{'temp': 294.76, 'pressure': 1018.04, 'humidit...</td>
      <td>Presidencia Roque Saenz Pena</td>
      <td>NaN</td>
      <td>{'message': 0.0035, 'country': 'AR', 'sunrise'...</td>
      <td>NaN</td>
      <td>[{'id': 800, 'main': 'Clear', 'description': '...</td>
      <td>{'speed': 3.75, 'deg': 104.501}</td>
    </tr>
  </tbody>
</table>
<p>533 rows × 13 columns</p>
</div>




```python
# Extract Data
lat = [df.column("coord")("lat")]
lng = [df.get("coord")("lon")]
Date = [df.get("dt")]
City_Name = [df.get("name")]
CountryCode = [df.get("sys")("country")]
Cloudiness = [df.get("clouds")("all")]
Humidity = [df.get("main")("humidity")]
MaxTemp = [df.get("main")("temp_max")]
WindSpeed = [df.get("wind")("speed")]

#Generate Dataframe
Cities = pd.dataframe({"Lat":[lat],
                      "Lng":[lng],
                      "Date":[Date],
                      "City Name":[City_Name],
                      "CountryCode":[CountryCode],
                      "Cloudiness":[Cloudiness],
                      "Humidity":[Humidity],
                      "MaxTemp":[MaxTemp],    
                      "Wind Speed":[WindSpeed]}

Cities()
```


      File "<ipython-input-223-2c61d2b00a3c>", line 23
        Cities()
             ^
    SyntaxError: invalid syntax
    



```python
Weather[0]
```




    {'base': 'stations',
     'clouds': {'all': 75},
     'cod': 200,
     'coord': {'lat': 15.85, 'lon': -97.07},
     'dt': 1505414700,
     'id': 3520994,
     'main': {'humidity': 70,
      'pressure': 1016,
      'temp': 302.15,
      'temp_max': 302.15,
      'temp_min': 302.15},
     'name': 'Puerto Escondido',
     'sys': {'country': 'MX',
      'id': 4010,
      'message': 0.0033,
      'sunrise': 1505391403,
      'sunset': 1505435391,
      'type': 1},
     'visibility': 16093,
     'weather': [{'description': 'broken clouds',
       'icon': '04d',
       'id': 803,
       'main': 'Clouds'}],
     'wind': {'deg': 250, 'speed': 4.1}}



## City Latitude vs. Max Temperature Plot


```python
Cities.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 533 entries, 0 to 532
    Data columns (total 13 columns):
    base          533 non-null object
    clouds        533 non-null object
    cod           533 non-null int64
    coord         533 non-null object
    dt            533 non-null int64
    id            533 non-null int64
    main          533 non-null object
    name          533 non-null object
    rain          63 non-null object
    sys           533 non-null object
    visibility    227 non-null float64
    weather       533 non-null object
    wind          533 non-null object
    dtypes: float64(1), int64(3), object(9)
    memory usage: 54.2+ KB
    


```python
# Generate Scatter Plot
#pandas.to_datetime('today')
plt.scatter(["Lng"],["Max. Temp"],color="red",  edgecolor="black", linewidths=1, marker="o", alpha = 0.8)

# Format Plot
plt.title("City Latitude Vs. Temperature Plot" + to_datetime('today'))
plt.ylabel("Max Temperature (F)")
plt.xlabel("City Latitude")
plt.grid(True)

# Save Plot
plt.savefig("fig1.png")

# Show Plot
plt.tight_layout()
plt.show()
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-157-896f9cf1fe96> in <module>()
          1 # Generate Scatter Plot
          2 #pandas.to_datetime('today')
    ----> 3 plt.scatter(["Lng"],["Max. Temp"],color="red",  edgecolor="black", linewidths=1, marker="o", alpha = 0.8)
          4 
          5 # Format Plot
    

    C:\Users\Abe\Anaconda2\envs\PythonData\lib\site-packages\matplotlib\pyplot.py in scatter(x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, verts, edgecolors, hold, data, **kwargs)
       3432                          vmin=vmin, vmax=vmax, alpha=alpha,
       3433                          linewidths=linewidths, verts=verts,
    -> 3434                          edgecolors=edgecolors, data=data, **kwargs)
       3435     finally:
       3436         ax._hold = washold
    

    C:\Users\Abe\Anaconda2\envs\PythonData\lib\site-packages\matplotlib\__init__.py in inner(ax, *args, **kwargs)
       1895                     warnings.warn(msg % (label_namer, func.__name__),
       1896                                   RuntimeWarning, stacklevel=2)
    -> 1897             return func(ax, *args, **kwargs)
       1898         pre_doc = inner.__doc__
       1899         if pre_doc is None:
    

    C:\Users\Abe\Anaconda2\envs\PythonData\lib\site-packages\matplotlib\axes\_axes.py in scatter(self, x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, verts, edgecolors, **kwargs)
       4061                 self.set_ymargin(0.05)
       4062 
    -> 4063         self.add_collection(collection)
       4064         self.autoscale_view()
       4065 
    

    C:\Users\Abe\Anaconda2\envs\PythonData\lib\site-packages\matplotlib\axes\_base.py in add_collection(self, collection, autolim)
       1760 
       1761         if autolim:
    -> 1762             self.update_datalim(collection.get_datalim(self.transData))
       1763 
       1764         collection._remove_method = lambda h: self.collections.remove(h)
    

    C:\Users\Abe\Anaconda2\envs\PythonData\lib\site-packages\matplotlib\collections.py in get_datalim(self, transData)
        218             transOffset = transOffset.get_affine()
        219 
    --> 220         offsets = np.asanyarray(offsets, np.float_)
        221         if np.ma.isMaskedArray(offsets):
        222             offsets = offsets.filled(np.nan)
    

    C:\Users\Abe\Anaconda2\envs\PythonData\lib\site-packages\numpy\core\numeric.py in asanyarray(a, dtype, order)
        581 
        582     """
    --> 583     return array(a, dtype, copy=False, order=order, subok=True)
        584 
        585 
    

    ValueError: could not convert string to float: 'Lng'


## City Latitude vs. Humidity Plot


```python
#Generate Scatter Plot
#plt.scatter(["Lng"],
#            ["Humidity"],color="blue", edgecolor="black", linewidths=1, marker="o", alpha = 0.8)

#Format Plot
#plt.title("City Latitude Vs. Humidity Plot")
#plt.ylabel("Humidity (%)")
#plt.xlabel("City Latitude")
#plt.grid(True)

#Save Plot
#plt.savefig("fig2.png")

#Show Plot
#plt.tight_layout()
#plt.show()
```

# City Latitude vs. Cloudiness Plot


```python
#Generate Scatter Plot
#plt.scatter(["Lng"],
#            ["Cloudiness"],color="yellow", edgecolor="black", linewidths=1, marker="o", alpha = 0.8)

#Format Plot
#plt.title("City Latitude vs. Cloudiness Plot")
#plt.ylabel("Cloudiness (%)")
#plt.xlabel("City Latitude")
#plt.grid(True)
#plt.xlim()
#plt.ylim()

#Save
#plt.savefig("fig3.png")

#Show Plot
#plt.tight_layout()
#plt.show()
```

## City Latitude vs. Wind Speed Plot


```python
#Generate Scatter Plot
#plt.scatter(["Lng"],
#            ["Humidity"],color="green", edgecolor="black", linewidths=1, marker="o", alpha=0.8)

#Format Plot
#plt.title("Latitude Vs. Wind Speed Plot")
#plt.ylabel("City Latitude")
#plt.xlabel("Wind Speed(mph)")
#plt.grid(True)
#plt.xlim()
#plt.ylim()

#Save
#plt.savefig("fig4.png")

#Show Plot
#plt.tight_layout()
#plt.show()
```


```python
# Convert Dataframe to CSV
# Cities.to_csv("WeatherPy.csv")
```
