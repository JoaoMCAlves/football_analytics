# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:46:27 2021

@author: Alves
"""
 
from highlight_text import ax_text,fig_text
import mplsoccer
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from Scrape import scrape_data_fbref as fbref

df_fbref = fbref.readfromhtml('https://fbref.com/en/comps/Big5/shooting/players/Big-5-European-Leagues-Stats')

# NOW PLOTTING THE SCATTERPLOT
# SETTING UP THE AXES

title_font = 'Comic Sans'
main_font = 'Open Sans'

fig, ax = plt.subplots(figsize=(12,10))
fig.set_facecolor('white')
ax.set_facecolor('white')
ax.set_title("title", fontfamily = title_font, fontsize = 20, fontweight = 'bold', loc = 'left')
ax.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.4, zorder=1)


#ax.set_ylim(0,1)
#ax.set_xlim(0,1)


#ax.spines['top'].set_visible(False)
#ax.spines['bottom'].set_color('red')

# SETTING UP THE X AND Y OF THE SCATTERPLOT
# SETTING UP THE AXES
no_90s = 5
df_fil = df_fbref[df_fbref['90s']>=no_90s] # select player that have played more than 10 games
df_fil = df_fil[df_fil['Pos'].apply(lambda x: x in ['FW','MF,FW','FW,MF'])] # select only fowards
x,y = (df_fil['xG']/df_fil['90s']).to_list(), (df_fil['Gls']/df_fil['90s']).to_list()
ax.scatter(x,y,alpha=0.3, c='orange', marker='o')

df_player = df_fil[df_fil['Player']=='Erling Haaland']
x_player = df_player['xG']/df_player['90s']
y_player = df_player['Gls']/df_player['90s']
ax.scatter(x_player, y_player, c='blue', zorder=2, marker='x')

ax.set_xlabel("X label", fontdict = {'fontsize':15, 'weight' : 'bold'})
ax.set_ylabel('Y label', fontdict = dict(fontsize = 15, weight = 'bold'))

plt.tight_layout()
plt.savefig("./ok")
plt.show()