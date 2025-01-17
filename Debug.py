import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Games data
#game_df_test = game_df_1[['x','y','endX','endY','type','outcomeType']]
#game_df_test.to_csv("game_df_test.csv")

#Adding xT to data
xT_grid = pd.read_csv("https://raw.githubusercontent.com/mckayjohns/xT/main/xT_Grid.csv",header=None)
xT=np.array(xT_grid)
xT_rows, xT_cols = xT.shape

# Create bins based on xT np array
game_df_test['x1_bin'] = pd.cut(game_df_test['x'], bins=xT_cols, labels=False)
game_df_test['y1_bin'] = pd.cut(game_df_test['y'], bins=xT_rows, labels=False)
game_df_test['x2_bin'] = pd.cut(game_df_test['endX'], bins=xT_cols, labels=False)
game_df_test['y2_bin'] = pd.cut(game_df_test['endY'], bins=xT_rows, labels=False)

# Calculate xT for only successful passes

if game_df_test['outcomeType']=='Successful' and game_df_test['type']=='Pass':
	game_df_test['start_zone_value'] = game_df_test[['x1_bin', 'y1_bin']].apply(lambda x: xT[x[1]][x[0]], axis=1)
	game_df_test['end_zone_value'] = game_df_test[['x2_bin', 'y2_bin']].apply(lambda x: xT[x[1]][x[0]], axis=1)
	game_df_test['xT'] = game_df_test['end_zone_value'] - game_df_test['start_zone_value']
else:
	game_df_test['start_zone_value'] = np.nan
	game_df_test['end_zone_value'] = np.nan
	game_df_test['xT'] = np.nan
