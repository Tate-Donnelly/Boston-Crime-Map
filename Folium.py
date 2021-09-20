import folium
import numpy as np
from folium import FeatureGroup, LayerControl, Map, Marker

crime= np.loadtxt('Sheet1.csv', delimiter=',', skiprows=1, dtype=None, usecols = range(0,3))
features = crime[:,1:3]
code = crime[:,0]
m = folium.Map( location=[42.3601, -71.0589], zoom_start=10, tiles='Stamen Toner')
m.save(outfile='map.html')

Larceny=[]
Larcenycodes=[616, 626, 636, 618, 628, 638, 617, 627, 637, 614, 624, 634, 619, 629, 639, 621, 611, 631, 612, 622, 632, 613, 623, 633, 615, 625, 635, 649]
Larceny_group = FeatureGroup(name='Larceny')
Liquor=[]
Liquorcodes=[2646, 2202, 2201, 2204]
Liquor_group = FeatureGroup(name='Liquor')
MV=[]
MVcodes=[2908 , 3830 , 2907 , 3831 , 3709 , 3810 , 3811 , 3821 , 3712 , 3801 , 3807 , 3702 , 3803 , 3704 , 3805 , 3701 , 3802 , 3820 , 3706 , 3205 , 3205 , 3206]
MV_group = FeatureGroup(name='MV')
Manslaughter=[]
Maslaughtercodes=[121, 122, 123, 124, 125]
Manslaughter_group = FeatureGroup(name='Manslaughter')
Drugs=[]
Drugscodes=[1815, 1846, 1830, 1832, 1831, 1806, 1844, 1805, 1810, 1870, 2609, 1874, 1842, 1841, 1849, 1848, 1858, 1855, 1864, 1863, 1866, 1868, 1843, 3023, 3021, 1875, 3022, 1847, 1840, 1873]
Drugs_group = FeatureGroup(name='Drugs')
Prostitution=[]
Prostitutioncodes=[1605, 1603, 1601, 1607]
Prostitution_group = FeatureGroup(name='Prostitution')
Rape=[]
Rapecodes=[222, 230, 236, 211, 232, 233, 224, 213, 231, 237, 212, 234, 235]
Rape_group = FeatureGroup(name='Rape')
RobberyBurglary=[]
Robberycodes=[381, 301, 302, 304, 303, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 373, 374, 375, 376, 377, 378, 379, 380, 541, 540, 562, 561, 542, 521, 520, 522, 560]
Robbery_group = FeatureGroup(name='Robbery')
B_E=[]
B_Ecodes=[541, 540, 542, 543, 547, 531, 530, 532, 537, 521, 520, 522, 527, 511, 510, 512, 517]
B_E_group = FeatureGroup(name='Breaking and Entering')
Vandalism=[]
Vandalism_group = FeatureGroup(name='Vandalism')
Assault=[]
Assaultcodes=[801, 802, 401, 402, 403, 404, 411, 412, 413, 421, 422, 423, 424, 431, 432, 433]
Ass_group = FeatureGroup(name='Assault')
Auto_Theft=[]
Auto_Theftcodes=[706, 723, 724, 727, 735, 770, 780, 790]
Auto_Theft_group = FeatureGroup(name='Auto Theft')
Bomb_Threat=[]
Bomb_Threat_group = FeatureGroup(name='Bomb Threat')
Arson=[]
Arsoncodes=[900, 901, 902, 905, 906, 907, 920, 930]
Arson_group = FeatureGroup(name='Arson')
sick_injured=[]
sick_injuredcodes=[3006, 3018]
sick_injured_group = FeatureGroup(name='Sick/injured')
Harassment=[]
Harassmentcodes=[3151,2629]
Harassment_group = FeatureGroup(name='Harassment')
Demonstrations=[]
Demonstrations_group = FeatureGroup(name='Demonstration')
Trespassing=[]
Trespassing_group = FeatureGroup(name='Trespassing')
dontcare=[]
other=[]
Other_group = FeatureGroup(name='Other Crimes')

for x in range(0,990):
    if crime[x][0] in Robberycodes:
        RobberyBurglary.append(crime[x])
    elif crime[x][0] in Assaultcodes:
        Assault.append(crime[x])
    elif crime[x][0] in Auto_Theftcodes:
        Auto_Theft.append(crime[x])
    elif crime[x][0] in Arsoncodes:
        Arson.append(crime[x])
    elif crime[x][0] in Rapecodes:
        Rape.append(crime[x])
    elif crime[x][0] in Larcenycodes:
        Larceny.append(crime[x])
    elif crime[x][0] in Drugscodes:
        Drugs.append(crime[x])
    elif crime[x][0] in Liquorcodes:
        Liquor.append(crime[x])
    elif crime[x][0] in Maslaughtercodes:
        Manslaughter.append(crime[x])
    elif crime[x][0] in B_Ecodes:
        B_E.append(crime[x])
    elif crime[x][0] in Assaultcodes:
        Assault.append(crime[x])
    elif crime[x][0] in Auto_Theftcodes:
        Auto_Theft.append(crime[x])
    elif crime[x][0] in Arsoncodes:
        Arson.append(crime[x])
    elif crime[x][0] in Rapecodes:
        Rape.append(crime[x])
    elif crime[x][0] in Larcenycodes:
          Larceny.append(crime[x])
    elif crime[x][0] ==2610:
        Trespassing.append(crime[x])
    elif crime[x][0]==(2648):
        Bomb_Threat.append(crime[x])
    elif crime[x][0] in MVcodes:
        MV.append(crime[x])
    elif crime[x][0] == 3305:
        Demonstrations.append(crime[x])
    elif crime[x][0] in Prostitutioncodes:
        Prostitution.append(crime[x])
    elif crime[x][0]==1402 or crime[x][0] == 1415:
        Vandalism.append(crime[x])
    elif crime[x][0] in sick_injuredcodes:
        dontcare.append(crime[x][0])
    elif crime[x][0] in Harassmentcodes:
        Harassment.append(crime[x][0])
    else:
        other.append(crime[x])



m = folium.Map( location=[42.3601, -71.0589], zoom_start=15, tiles='Stamen Toner')

for x in range(0,len(Larceny)):
    folium.Marker(location=[Larceny[x][1], Larceny[x][2]], popup='Larceny', icon=folium.Icon(color='blue')).add_to(Larceny_group)
for x in range(0, len(Liquor)):
    folium.Marker(location=[Liquor[x][1], Liquor[x][2]], popup='Liquor', icon=folium.Icon(color='lightblue')).add_to(Liquor_group)
for x in range(0, len(MV)):
    folium.Marker(location=[MV[x][1], MV[x][2]], popup='Motor Vehicle', icon=folium.Icon(color='pink')).add_to(MV_group)
for x in range(0, len(Manslaughter)):
    folium.Marker(location=[Manslaughter[x][1], Manslaughter[x][2]], popup='Manslaughter', icon=folium.Icon(color='lightred')).add_to(Manslaughter_group)
for x in range(0, len(Drugs)):
    folium.Marker(location=[Drugs[x][1], Drugs[x][2]], popup='Drugs', icon=folium.Icon(color='green')).add_to(Drugs_group)
for x in range(0, len(Prostitution)):
    folium.Marker(location=[Prostitution[x][1], Prostitution[x][2]], popup='Prostitution', icon=folium.Icon(color='beige')).add_to(Prostitution_group)
for x in range(0, len(Rape)):
    folium.Marker(location=[Rape[x][1], Rape[x][2]], popup='Rape', icon=folium.Icon(color='purple')).add_to(Rape_group)
for x in range(0, len(RobberyBurglary)):
    folium.Marker(location=[RobberyBurglary[x][1], RobberyBurglary[x][2]], popup='Robbery', icon=folium.Icon(color='gray')).add_to(Robbery_group)
for x in range(0, len(B_E)):
    folium.Marker(location=[B_E[x][1], B_E[x][2]], popup='Breaking and Entering', icon=folium.Icon(color='red')).add_to(B_E_group)
for x in range(0, len(Vandalism)):
    folium.Marker(location=[Vandalism[x][1], Vandalism[x][2]], popup='Vandalism', icon=folium.Icon(color='darkpurple')).add_to(Vandalism_group)
for x in range(0, len(Assault)):
    folium.Marker(location=[Assault[x][1], Assault[x][2]], popup='Assault', icon=folium.Icon(color='darkred')).add_to(Ass_group)
for x in range(0, len(Auto_Theft)):
    folium.Marker(location=[Auto_Theft[x][1], Auto_Theft[x][2]], popup='Auto Theft', icon=folium.Icon(color='cadetblue')).add_to(Auto_Theft_group)
for x in range(0, len(Bomb_Threat)):
    folium.Marker(location=[Bomb_Threat[x][1], Bomb_Threat[x][2]], popup='Bomb Threat', icon=folium.Icon(color='black')).add_to(Bomb_Threat_group)
for x in range(0, len(Arson)):
    folium.Marker(location=[Arson[x][1], Arson[x][2]], popup='Arson', icon=folium.Icon(color='orange')).add_to(Arson_group)
for x in range(0, len(other)):
    folium.Marker(location=[other[x][1], other[x][2]], popup='Other', icon=folium.Icon(color='lightgray')).add_to(Other_group)

Larceny_group.add_to(m)
Liquor_group.add_to(m)
MV_group.add_to(m)
Manslaughter_group.add_to(m)
Drugs_group.add_to(m)
Prostitution_group.add_to(m)
Rape_group.add_to(m)
Robbery_group.add_to(m)
B_E_group.add_to(m)
Vandalism_group.add_to(m)
Ass_group.add_to(m)
Auto_Theft_group.add_to(m)
Bomb_Threat_group.add_to(m)
Arson_group.add_to(m)
Other_group.add_to(m)

LayerControl().add_to(m)

m.save(outfile='map.html')