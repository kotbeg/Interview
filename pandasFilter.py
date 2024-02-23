import pandas as pd

dataInit = pd.read_csv('Spotify Million Song Dataset_exported.csv')
a = dataInit.loc[dataInit.artist == 'ABBA']

print(a)
