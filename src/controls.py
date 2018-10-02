# flake8: noqa

# In[]:
# Controls for webapp
COUNTIES = {
    '001': 'Albany',
    '003': 'Allegany',
    '005': 'Bronx',
    '007': 'Broome',
    '009': 'Cattaraugus',
    '011': 'Cayuga',
    '013': 'Chautauqua',
    '015': 'Chemung',
    '017': 'Chenango',
    '019': 'Clinton',
    '021': 'Columbia',
    '023': 'Cortland',
    '025': 'Delaware',
    '027': 'Dutchess',
    '029': 'Erie',
    '031': 'Essex',
    '033': 'Franklin',
    '035': 'Fulton',
    '037': 'Genesee',
    '039': 'Greene',
    '041': 'Hamilton',
    '043': 'Herkimer',
    '045': 'Jefferson',
    '047': 'Kings',
    '049': 'Lewis',
    '051': 'Livingston',
    '053': 'Madison',
    '055': 'Monroe',
    '057': 'Montgomery',
    '059': 'Nassau',
    '061': 'New York',
    '063': 'Niagara',
    '065': 'Oneida',
    '067': 'Onondaga',
    '069': 'Ontario',
    '071': 'Orange',
    '073': 'Orleans',
    '075': 'Oswego',
    '077': 'Otsego',
    '079': 'Putnam',
    '081': 'Queens',
    '083': 'Rensselaer',
    '085': 'Richmond',
    '087': 'Rockland',
    '089': 'St. Lawrence',
    '091': 'Saratoga',
    '093': 'Schenectady',
    '095': 'Schoharie',
    '097': 'Schuyler',
    '099': 'Seneca',
    '101': 'Steuben',
    '103': 'Suffolk',
    '105': 'Sullivan',
    '107': 'Tioga',
    '109': 'Tompkins',
    '111': 'Ulster',
    '113': 'Warren',
    '115': 'Washington',
    '117': 'Wayne',
    '119': 'Westchester',
    '121': 'Wyoming',
    '123': 'Yates'
 }

CATEGORY_NAME = {'Amiibo': 'amiibo', 'AmiiboCards': 'amiibo-cards', 'Berbrick': 'berbrick', 'Covetly': 'covetly-store', \
                 'DcC': 'dc-comics', 'DisneyI': 'disney-infinity-figures', 'Dorbz': 'dorbz', 'Funko':'funko', \
                 'FunkoO': 'funko-other', 'Garbage': 'garbage-pail-kids', 'GiJoe': 'gi-joe', 'Hikari': 'hikari', \
                 'Kaws': 'kaws', 'KidRobot': 'kid-robot', 'KidRobotB': 'kid-robot-blind-boxes', 'MarvelC': 'marvel-comics',\
                 'MastersU': 'masters-of-the-universe', 'MightyJ': 'mighty-jaxx', 'MyLittlePony': 'my-little-pony',\
                 'MysteryM': 'mystery-minis', 'Pokemon': 'pokemon-cards', 'PrintHeroes': 'pint-sized-heroes', \
                 'RockC': 'rock-candy', 'Sideshow': 'sideshow-collectibles', 'Skylanders': 'skylanders', \
                 'StarWar': 'star-wars-kenner', 'Superplastic': 'superplastic', 'Tokidoki': 'tokidoki', \
                 'Transformers': 'transformers', 'Vynl': 'vynl'}


WELL_TYPES = dict(
     BR = 'Brine',
     Confidential = 'Confidential',
     DH = 'Dry Hole',
     DS = 'Disposal',
     DW = 'Dry Wildcat',
     GD = 'Gas Development',
     GE = 'Gas Extension',
     GW = 'Gas Wildcat',
     IG = 'Gas Injection',
     IW = 'Oil Injection',
     LP = 'Liquefied Petroleum Gas Storage',
     MB = 'Monitoring Brine',
     MM = 'Monitoring Miscellaneous',
     MS = 'Monitoring Storage',
     NL = 'Not Listed',
     OB = 'Observation Well',
     OD = 'Oil Development',
     OE = 'Oil Extension',
     OW = 'Oil Wildcat',
     SG = 'Stratigraphic',
     ST = 'Storage',
     TH = 'Geothermal',
     UN = 'Unknown',
)

CATEGORY_COLORS = ['#FFEDA0', '#FA9FB5','#A1D99B','#67BD65','#BFD3E6','#B3DE69','#FDBF6F','#FC9272',\
    '#D0D1E6','#ABD9E9','#3690C0','#F87A72','#CA6BCC','#DD3497','#4EB3D3','#FFFF33','#FB9A99','#A6D853','#D4B9DA',\
    '#AEB0B8','#CCCCCC','#EAE5D9','#C29A84','#FA9FB5','#A1D99B','#67BD65','#BFD3E6','#B3DE69','#FDBF6F','#FC9272']

WELL_COLORS = dict(
     GD = '#FFEDA0',
     GE = '#FA9FB5',
     GW = '#A1D99B',
     IG = '#67BD65',
     OD = '#BFD3E6',
     OE = '#B3DE69',
     OW = '#FDBF6F',
     ST = '#FC9272',
     BR = '#D0D1E6',
     MB = '#ABD9E9',
     IW = '#3690C0',
     LP = '#F87A72',
     MS = '#CA6BCC',
     Confidential = '#DD3497',
     DH = '#4EB3D3',
     DS = '#FFFF33',
     DW = '#FB9A99',
     MM = '#A6D853',
     NL = '#D4B9DA',
     OB = '#AEB0B8',
     SG = '#CCCCCC',
     TH = '#EAE5D9',
     UN = '#C29A84',
)
