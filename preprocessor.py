import pandas as pd
import numpy as np

def preprocess(lap_price):
    # Let's replace the empty strings with NaN values
    lap_price = lap_price.replace(' ', np.nan)
    # Let's replace the question marks (?) with NaN values
    lap_price = lap_price.replace('?', np.nan)
    # Let's replace the question marks (.) with NaN values
    lap_price = lap_price.replace('.', np.nan)
    
    return lap_price