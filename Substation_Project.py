import pandas as pd
import simplekml

# Substation Coordinates
substation_data = [
    ('ORCHARD', -120.124309, 36.146461),
    ('GATES', -120.1248911, 36.13979872),
    ('TMPLTN', -120.6803, 35.55503),
    ('DIABLO', -120.854896, 35.211724),
    ('MIDWAY', -119.4531,  35.40411),
    ('ARCO', -119.9142634, 35.77542921), 
    ('MSTANS', -119.919373, 36.232212),
    ('KTTLEM', -120.112696, 36.04407493),
    ('CALFSS', -120.322536, 35.870004),
    ('COLNG2', -120.3148064, 36.23728825),
    ('FIFTHS',  -120.13009, 36.14256),
    ('JAYNE', -120.344012, 36.136583),
    ('HURON', -120.1045354, 36.18579717),
    ('PNOCHE', -120.58168, 36.65361),
    ('LOSBNS', -121.021419, 37.053151),
    
    ('TBLMTN', -121.6443541, 39.55563977),
    ('FERNRD', -121.5615, 40.3842),
    ('THERMA', -121.632458, 39.514145),
    ('MCNEJT', -121.57109,  39.69847998), 
    ('RIOOSO', -121.4664694, 38.93644279),
    ('TESLA',  -121.5640,   37.7147), 
    ('VACADX', -121.9199288, 38.40164418),
    ('BELDEN', -120.844348, 39.466564),
    ('HYATT', -121.486236, 39.531996),
    ('TRESVS', -121.687993, 39.48670654),
    ('NOTRDM', -121.7959489, 39.73042313),
    ('ESQUON', -121.7684448, 39.60787615),
    ('BUTTE', -121.8133103, 39.71181326),
    ('MALIN', -121.317387, 42.006722),
    ('INDNSP', -121.5209022, 41.36399539),
    ('CTTNWD', -122.26421, 40.39779),
    ('RNDMTN', -121.9378918, 40.7911693),
    ('PIT7', -121.8692007, 38.03076087),
    ('CARRBY', -121.752919, 40.859128),
    ('PIT4', -121.8492575, 40.98633148),
    ('PALRMO', -121.51764,  39.45426),
    ('WYNDOT', -121.5411609, 39.4916287),
   
]

# Create a DataFrame from the CAISO Coordinates
df = pd.DataFrame(substation_data, columns=['Substation', 'Longitude', 'Latitude'])

# Create a new KML object
kml = simplekml.Kml()

# Add points for each substation
for _, row in df.iterrows():
    kml.newpoint(name=row['Substation'], coords=[(row['Longitude'], row['Latitude'])])

# Draw lines between the substations
for i in range(len(df) - 1):
    line = kml.newlinestring(
        name=f"{df.iloc[i]['Substation']} to {df.iloc[i+1]['Substation']}",
        coords=[
            (df.iloc[i]['Longitude'], df.iloc[i]['Latitude']),
            (df.iloc[i+1]['Longitude'], df.iloc[i+1]['Latitude'])
        ]
    )
    line.style.linestyle.width = 2
    line.style.linestyle.color = simplekml.Color.lightblue

# Save the KML file with the desired name
kml.save("California_Substations.kml")
