import pandas as pd
import numpy as np
def load_data(raw_data_path):
    return pd.read_csv(raw_data_path, sep=';')

def load_and_wrangle_data(raw_data_path):
    """
    This function loads the data from the specified raw_data_path and does some wrangling by dropping unnecessary columns, 
    creating a binary column for high GDP per capita, replacing 0 values with NaNs in non-beer consumption columns, 
    dropping rows with NaNs and renaming the high_gdp column.
    """
    df = (load_data(raw_data_path)
          .drop(['Year', 'Population', 'Military expenditure', 'People practicing open defecation'], axis=1)
          .assign(high_gdp=lambda x: x['GDP per capita'] > 17246.112996855245) #the value of mean GDP per capita
          .apply(lambda x: x.replace(0, np.nan) if x.name != 'Beer consumption per capita' else x, axis=0)
          .dropna()
          .rename(columns={'high_gdp': 'High GDP per capita'})
         )
    return df
