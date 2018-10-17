#!/usr/bin/env python
import matplotlib.pyplot as plt
#%matplotlib inline
import cartopy.crs as ccrs
import cartopy.feature as cfeat

fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(1,1,1,projection=ccrs.LambertConformal())
ax.add_feature(cfeat.LAND)
ax.add_feature(cfeat.OCEAN)
ax.add_feature(cfeat.COASTLINE)
ax.add_feature(cfeat.BORDERS,linestyle=":")
ax.add_feature(cfeat.LAKES,alpha=0.6)
ax.add_feature(cfeat.RIVERS)
ax.set_extent([30,45,30,-30])
fig.show()
