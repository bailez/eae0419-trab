import pandas as pd

path = r'/home/bailez/data/Projetos/repos/eae0419-trab/'

old_df = pd.read_excel(path + '95-11.xlsx').iloc[1:,18:]
def clear_old_data(x):
    return str(x[:4])
old_df.columns = old_df.iloc[0,:].apply(clear_old_data)
old_df.index = old_df.iloc[:,0]
old_df = old_df.iloc[2:,3:].T
old_df.index = pd.to_datetime(old_df.index, format="%Y")
old_df = old_df.apply(pd.to_numeric, errors="coerce")*10
old_df = old_df.sort_index()
