import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#linking and importing files
shape_link = r"C:\Users\HP ENVY\Documents\GIS\nga_adm_osgof_20190417_SHP\nga_admbnda_adm1_osgof_20190417.shp"
shape = gpd.read_file(shape_link)

#setting up dataframe and plotiing shape
ax = shape.boundary.plot(edgecolor='black', linewidth=0.3, figsize=(10,10))
shape.plot(ax=ax, column = 'Shape_Area', legend = True, cmap = 'RdBu', legend_kwds={'shrink':0.3, 'orientation':'horizontal'})

#Removing Border and border text
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

for edge in ['right', 'left', 'top','bottom']:
    ax.spines[edge].set_visible(False)

#labelling edge polygon with the feild name ADM1_EN
for x,y,label in zip(shape.geometry.centroid.x,shape.geometry.centroid.y, shape['ADM1_EN']):
    ax.text(x,y,label, fontsize=8.0, va='center',ha='center')


#give title to the maps
ax.set_title('Map of Nigeria Showing State by Size')

#print
plt.show()