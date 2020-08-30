import pandas as pd

cities_df = pd.read_csv('cities.csv')

cities_df.to_html('cities.html', index=False)