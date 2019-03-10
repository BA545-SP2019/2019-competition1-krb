# Imports and things
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.options.display.max_columns = None


#bin I3 columns by sector
def assign_sector(sector):
    
    if sector < 999:
        return "Agriculture/Forestry/Fishing"
    elif sector >= 1000 and sector <= 1499:
        return "Mining"
    elif sector >= 1500 and sector <= 1799:
        return "Construction"
    elif sector >= 2000 and sector <= 3999:
        return "Manufacturing"
    elif sector >= 4000 and sector <= 4999:
        return "Transportation/Communications/Utulities"
    elif sector >= 5000 and sector <= 5199:
        return "Wholesale Trade"
    elif sector >= 5200 and sector <= 5999:
        return "Retail Trade"
    elif sector >= 6000 and sector <= 6799:
        return "Finance/Insurance/Realestate"
    elif sector >= 7000 and sector <= 8999:
        return "Services"
    elif sector >= 9100 and sector <= 9799:
        return 'Public Administration'
    elif sector >= 9800:
        return "Non Classafiable Establishments"
    
