from api.tags import *
from api.config import settings

db = [
    {
        "code": "MAD",
        "description": "Madrid is a charming city. It is famous for both beautiful architecture and excellent museums. Their offer includes works by Pablo Picasso and Salvador Dalí. The Spanish capital loves fiesta, and every day the bars and clubs are full of music.",
        "pf": 1.2,
        "name": "Madrid",
        "country": "Spain",
        "lat": "40.471926",
        "long": "-3.56264",
        "img": f'{settings["base_url"]}/static/img/MAD.jpg',
        "tags": {EXPERIENCE, SEA, CULTURE, NIGHT_LIFE, HOTEL, ARCHITECTURE},
    },
    {
        "code": "ZAD",
        "description": "Zadar, a city on Croatia’s Dalmatian coast, is known for the Roman and Venetian ruins of its peninsular Old Town. There are several Venetian gates in the city walls. Surrounding the Roman-era Forum is 11th-century St. Mary’s Convent, with religious art dating to the 8th century. There’s also the grand, 12th-century St. Anastasia’s Cathedral and the round, 9th-century pre-Romanesque Church of St. Donatus.",
        "pf": 1.4,
        "name": "Zadar",
        "country": "Croatia",
        "lat": "44.108299",
        "long": "15.3467",
        "img": f'{settings["base_url"]}/static/img/ZAD.png',
        "tags": {EXPERIENCE, CULTURE, SPORT, HOT, FOOD, ARCHITECTURE, TENT},
    },
    {
        "code": "GVA",
        "description": "Geneva, as well as the whole Switzerland, is associated with chocolate and watches, but these are not the only products worth buying there. In Geneva, it is worth going for fashion shopping. Although the city center is full of boutiques of the best world brands, the flea market Plaine de Plainpalais, where you can find fashion retro things, is also interesting.",
        "pf": 1.6,
        "name": "Geneva",
        "country": "Switzerland",
        "adds": [ANC_SKI, ANC_SEAT],
        "lat": "46.23809814453125",
        "long": "6.108950138092041",
        "img": f'{settings["base_url"]}/static/img/GVA.png',
        "tags": {MOUNTAIN, HOTEL, LAKE, COLD, SKI},
    },
    {
        "code": "ARN",
        "description": "Stockholm, known as the Venice of the North, would have no trouble winning rivalry for the European capital city to be the most originally located – the old town is located on an island occupying a strip of land between the Baltic Sea and the great Mälaren Lake. The vicinities of Stockholm are a mosaic of pine forests, lakes and rocks.",
        "pf": 1.6,
        "name": "Stockholm",
        "country": "Sweden",
        "lat": "59.651901245116996",
        "long": "17.918600082397",
        "img": f'{settings["base_url"]}/static/img/ARN.jpg',
        "tags": {CITY, LANDSCAPE, LAKE, HOTEL, COLD, ARCHITECTURE},
    },
    {
        "code": "SOF",
        "description": "Sofia, the capital of Bulgaria and the largest city in the country, is one of the oldest cities of Europe. Since antiquity, the place has been influenced by both eastern and western traditions; and, as a result, Sofia is an extremely diverse city with rich tradition and culture. You can see the miraculous stone Orthodox churches, huge socialist-realist buildings, vibrant streets, and dark housing estates on the outskirts.",
        "pf": 0.9,
        "name": "Sofia",
        "country": "Bulgaria",
        "lat": "42.696693420410156",
        "long": "23.411436080932614",
        "img": f'{settings["base_url"]}/static/img/SOF.png',
        "tags": {HOTEL, CULTURE, ARCHITECTURE, SEA, COLD},
    },
    {
        "code": "PEK",
        "description": "Beijing is famous for its unusual diversity and contradictions. Contrasts can be seen in the city from the first sight - old temples from the imperial times are mixed with modern, glass skyscrapers. The size of the metropolis and the crowds in it are also dazzling. Beijing is more than 30 times bigger than Warsaw and it is inhabited by almost 20 million people. The biggest attraction is the Forbidden City - the seat of the Emperors of the Ming and Qing dynasties from the fifteenth century.",
        "pf": 1.0,
        "name": "Beijing",
        "country": "China",
        "lat": "40.0801010131836",
        "long": "116.58499908447266",
        "img": f'{settings["base_url"]}/static/img/PEK.jpg',
        "adds": [ANC_SEAT, ANC_BAG],
        "tags": {FOOD, CULTURE, ARCHITECTURE, CITY, HOTEL, EXPERIENCE, UNIQUE},
    },
    {
        "code": "KUL",
        "description": "A visit to the capital of Malaysia is a feast for all the senses. The city landscape is decorated with skyscrapers, minarets and lush parks. The walks are accompanied by amazing aromas of freshly prepared dishes and drinks. Kuala Lumpur is characterized by multiculturalism which is perfectly reflected in the colorful Chinatown and fragrant Little India. This is one of our many connections to Asia, Australia and New Zealand, prepared with partner airlines with a convenient transfer in Singapore.",
        "pf": 1.1,
        "name": "Kuala Lumpur",
        "country": "Malaysia",
        "lat": "2.7455799579619997",
        "long": "101.70999908446998",
        "adds": [ANC_SEAT, ANC_BAG],
        "img": f'{settings["base_url"]}/static/img/KUL.jpg',
        "tags": {FOOD, NIGHT_LIFE, HOTEL, CULTURE, SEA, HOT, UNIQUE},
    },
    {
        "code": "LWO",
        "description": "A walk along the streets of Lviv is a treat for enthusiasts of modernism. Next to numerous monuments there are many pearls of modernist architecture. Lviv is also famous for its majestic memorials. One of the most popular is Adam Mickiewicz’s statue.",
        "pf": 0.8,
        "name": "Lvov",
        "country": "Ukraine",
        "lat": "49.8125",
        "long": "23.95610046386719",
        "img": f'{settings["base_url"]}/static/img/LWO.jpg',
        "tags": {ARCHITECTURE, NIGHT_LIFE, SPORT, CITY, HOTEL},
    },
    {
        "code": "DEL",
        "description": "A journey through Delhi is like using a time machine. On the one hand, it is a modern city full of spectacular office buildings, sumptuous shopping centers, and centers that excel in futuristic information and telecommunications technologies. On the other hand, Delhi has three monuments, which were inscribed on the UNESCO List. Visit in Delhi is a great opportunity to taste local delicacies: curry, samosa or naan.",
        "pf": 0.9,
        "name": "Delhi",
        "country": "India",
        "lat": "28.5665",
        "long": "77.103104",
        "img": f'{settings["base_url"]}/static/img/DEL.jpg',
        "adds": [ANC_SEAT, ANC_BAG],
        "tags": {HOT, CULTURE, HOTEL, FOOD, UNIQUE},
    },
    {
        "code": "LAX",
        "description": "Los Angeles is a city connected with nature, where bustling neighborhoods combine with golden beaches and hills densely woven by plants. It is also a global center of creativity and entertainment. It attracts courageous dreamers and creators to realize their visions on stages and film studios.",
        "pf": 1.5,
        "name": "Los Angeles",
        "country": "United States",
        "lat": "33.94250107",
        "long": "-118.40799709999999",
        "img": f'{settings["base_url"]}/static/img/LAX.jpg',
        "adds": [ANC_SEAT],
        "tags": {EXPERIENCE, NIGHT_LIFE, HOT, SEA, CITY, HOTEL, SPORT},
    },
    {
        "code": "DBV",
        "description": 'Dubrovnik is vibrant city that never sleeps. There are many museums and monuments - its old town was inscribed on the UNESCO World Heritage List. An interesting fact is that in the city you can see places known from the "Game of Thrones" series, including St. Dominic Street and Bokar or Minceta Fortress.',
        "pf": 1.1,
        "name": "Dubrovnik",
        "country": "Croatia",
        "lat": "42.38",
        "long": "18.06",
        "img": f'{settings["base_url"]}/static/img/DBV.jpg',
        "tags": {HOT, LANDSCAPE, SEA, CITY, HOTEL},
    },
    {
        "code": "EVN",
        "description": "When planning a trip to the Caucasus, you should consider Yerevan, the energetic capital of Armenia. The Republic Square is surrounded by monumental office buildings built of yellow and pink tuff — volcanic ash. When being in the city center you can go to the Museum of Armenian History and learn about the oldest Christian state. You also might be interested in a walk through the Cascades to see Ararat over pink tuff buildings.",
        "pf": 1.1,
        "name": "Yervan",
        "country": "Armenia",
        "lat": "40.11",
        "long": "44.31",
        "img": f'{settings["base_url"]}/static/img/EVN.jpg',
        "tags": {EXPERIENCE, TENT, MOUNTAIN, LANDSCAPE},
    },
    {
        "code": "NRT",
        "description": "Fans of urban hustle and exotic flavors will definitely enjoy Tokyo. The city is full of life by day and by night. During a travel to the capital of the Land of the Rising Sun visit one of the most crowded crossings in the world - Shibuya Crossing. Later go to one of the most expensive districts of Tokyo - Ginza, and try local sushi at one of famous fish markets.",
        "pf": 2.1,
        "name": "Tokyo",
        "country": "Japan",
        "lat": "35.41",
        "long": "139.41",
        "img": f'{settings["base_url"]}/static/img/NRT.jpg',
        "adds": [ANC_SEAT, ANC_FOOD],
        "tags": {FOOD, CITY, HOTEL, MOUNTAIN, LANDSCAPE, NIGHT_LIFE, UNIQUE},
    },
    {
        "code": "YYZ",
        "description": "Toronto is a multicultural city. Almost every day there are extraordinary festivals, shows, exhibitions and sports competitions. It's worth to remember, that Canadians especially love hockey.",
        "pf": 0.8,
        "name": "Toronto",
        "country": "Canada",
        "lat": "43.44",
        "long": "-79.22",
        "img": f'{settings["base_url"]}/static/img/YYZ.jpg',
        "adds": [ANC_BAG, ANC_SKI],
        "tags": {TENT, WILDERNESS, COLD, SKI, MOUNTAIN, LANDSCAPE, LAKE},
    },
    {
        "code": "SYD",
        "description": "Sydney is surrounded by national parks. Their greenery penetrates into the city's space, and surrounds skyscrapers and houses. The seaside scenery is charming: the harbor and the golden beaches encourage to rest. This city never sleeps because there is always something new to discover - bars, restaurants, pubs, concerts and festivals. This is one of our many connections to Asia, Australia and New Zealand, prepared with partner airlines with a convenient transfer in Singapore.   ",
        "pf": 0.8,
        "name": "Sydney",
        "country": "Australia",
        "lat": "-33.86",
        "long": "151.20",
        "img": f'{settings["base_url"]}/static/img/SYD.jpg',
        "adds": [ANC_FOOD, ANC_SEAT],
        "tags": {SEA, WILDERNESS, NIGHT_LIFE, HOT, UNIQUE},
    },
    {
        "code": "SIN",
        "description": "Fly to Singapore - one of the most friendly places in the world. It is really popular among travelers because it is a gateway to other exotic destinations. However, it is worth considering a longer stay in the City of Lion. Exotic districts drawing from diverse cultures make it possible to move to another Asian region - India, China or Arab countries - with every meal.",
        "pf": 0.8,
        "name": "Singapore",
        "country": "Singapore",
        "lat": "1.35",
        "long": "103.81",
        "img": f'{settings["base_url"]}/static/img/SIN.jpg',
        "adds": [ANC_BAG, ANC_SEAT],
        "tags": {CITY, HOT, HOTEL, NIGHT_LIFE},
    },
    {
        "code": "ICN",
        "description": "Seoul is a fashionable and technologically advanced city, and at the same time very traditional. The capital of South Korea dynamically grows and develops, captivating its heritage at the same time. In the city you can see Bukchon, traditional Korean houses, which contrast with the skyscrapers. It is also worth going to Changdeokgung and Gyeongbokgung, places with rich histories.",
        "pf": 0.8,
        "name": "Seoul",
        "country": "South Korea",
        "lat": "37.56",
        "long": "126.97",
        "img": f'{settings["base_url"]}/static/img/SEL.jpg',
        "adds": [ANC_BAG, ANC_FOOD],
        "tags": {CITY, LAKE, EXPERIENCE, CULTURE, FOOD, UNIQUE},
    },
    {
        "code": "BKK",
        "description": "Bangkok belongs to those Asian metropolises that never fall asleep. Around the clock you can see speeding tuk-tuks, eat aromatic street food delicacies and enjoy the bustle of this amazing city. During your stay, you can go to the Temple of the Wat Phra Kaew and the Grand Palace, the flagship attractions of the Thai capital. This is one of our many connections to Asia, Australia and New Zealand, prepared with partner airlines with a convenient transfer in Singapore.",
        "pf": 0.8,
        "name": "Bangkok",
        "country": "Thailand",
        "lat": "13.75",
        "long": "100.50",
        "img": f'{settings["base_url"]}/static/img/BKK.jpg',
        "adds": [ANC_SEAT, ANC_FOOD],
        "tags": {WILDERNESS, HOT, SEA, CULTURE, LANDSCAPE},
    },
]
