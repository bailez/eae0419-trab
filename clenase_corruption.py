import io
import pandas as pd
import numpy as np

path = r'/home/bailez/data/Projetos/repos/eae0419-trab/'

# %% old data
old_df = pd.read_excel(path + '95-11.xlsx').iloc[1:,18:]
def clear_old_data(x):
    return str(x[:4])
old_df.columns = old_df.iloc[0,:].apply(clear_old_data)
old_df.index = old_df.iloc[:,0]
old_df = old_df.iloc[2:,3:].T
old_df.index = pd.to_datetime(old_df.index, format="%Y")
old_df = old_df.apply(pd.to_numeric, errors="coerce")*10
old_df = old_df.sort_index()

# %% new data

new_df = pd.read_excel(path + '12-18.xlsx', sheet_name='CPI Timeseries 2012 - 2018').iloc[1:,:]
new_df.columns = new_df.iloc[0,:]
new_df.index = new_df.iloc[:,0]

scores = ['CPI Score 2012','CPI Score 2013',
          'CPI score 2014','CPI score 2015',
          'CPI score 2016','CPI score 2017',
          'CPI score 2018',
    ]
new_df = new_df.iloc[1:,3:]
new_df = new_df[scores].T
new_df.index = [2012,2013,2014,2015,2016,2017,2018]
new_df.index = pd.to_datetime(new_df.index, format="%Y")
new_df = new_df.apply(pd.to_numeric, errors="coerce")
new_df = new_df.sort_index()
new_df = new_df.reindex(sorted(new_df.columns), axis=1)
# %% concat all data

df = old_df.append(new_df)
# %% Emerging Markets
countries = ['Brazil', 'Argentina', 'Turkey', 
             'South Africa', 'China', 'Chile', 
             'Iran', 'Mexico', 'Russia', 'Venezuela',
             'Colombia', 'India', 'Indonesia']
em = df[countries]
# %%
exports = pd.read_excel(path + 'imf.xlsx').iloc[1:-2,:]
exports.index = exports.iloc[:,0]
exports = exports.iloc[:,1:].apply(pd.to_numeric,errors='coerce').T
exports.index = pd.to_datetime(exports.index,format='%Y')
texports = exports['1995':]
texdf = df['1995':'2010']
texdf = texdf.T.dropna().T
texdf = texdf.drop(['Taiwan'],axis=1)
texports = texports.T.dropna().T
countries = ['Argentina', 'Australia', 'Austria', 'Brazil', 'Canada',
       'Chile', "China, People's Republic of", 'Colombia', 'Denmark', 'Finland', 'France', 'Germany',
       'Greece', 'Hong Kong SAR', 'Hungary', 'India', 'Indonesia', 'Ireland',
       'Italy', 'Japan', 'Korea, Republic of', 'Malaysia', 'Mexico', 'Netherlands',
       'New Zealand', 'Norway', 'Philippines', 'Portugal', 'Singapore',
       'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Thailand',
       'Turkey', 'United Kingdom', 'United States', 'Venezuela']
texports = texports[countries]

texdf.columns = ['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada',
       'Chile', 'China', 'Colombia', 'Denmark', 'Finland', 'France', 'Germany',
       'Greece', 'Hong Kong', 'Hungary', 'India', 'Indonesia', 'Ireland',
       'Italy', 'Japan', 'South Korea', 'Malaysia', 'Mexico', 'Netherlands',
       'New Zealand', 'Norway', 'Philippines', 'Portugal', 'Singapore',
       'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey',
       'United Kingdom', 'United States', 'Venezuela']
texports.columns = ['Argentina', 'Australia', 'Austria', 'Brazil', 'Canada', 'Chile',
       'China', 'Colombia', 'Denmark', 'Finland',
       'France', 'Germany', 'Greece', 'Hong Kong', 'Hungary', 'India',
       'Indonesia', 'Ireland', 'Italy', 'Japan', 'South Korea',
       'Malaysia', 'Mexico', 'Netherlands', 'New Zealand', 'Norway',
       'Philippines', 'Portugal', 'Singapore', 'South Africa', 'Spain',
       'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom',
       'United States', 'Venezuela']

texports = texports.reindex(sorted(texports.columns), axis=1)
texdf = texdf.reindex(sorted(texdf.columns), axis=1)
logdf = np.log(texdf)
logex = np.log(texports)
logdf.T.corrwith(logex.T,axis=1)
