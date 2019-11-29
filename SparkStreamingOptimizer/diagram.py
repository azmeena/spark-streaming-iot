#!/usr/bin/env python3

import matplotlib.pyplot as plot
from matplotlib import colors
import pandas as pd
import sys

n_bins = 50

df1 = pd.read_csv(sys.argv[1])
df1 = df1[(df1.time < 3) & (df1.time > 0.25)]
df2 = pd.read_csv(sys.argv[2])
df2 = df2[(df2.time < 3) & (df2.time > 0.25)]

fig, axs = plot.subplots(1,2, sharey=True, tight_layout=True)

N1, bins1, patches1 = axs[0].hist(df1['time'], bins=n_bins)
N2, bins2, patches2 = axs[1].hist(df2['time'], bins=n_bins)

fracs1 = N1/N1.max()
fracs2 = N2/N2.max()

norm1 = colors.Normalize(fracs1.min(), fracs1.max())
norm2 = colors.Normalize(fracs2.min(), fracs2.max())

for thisfrac, thispatch in zip(fracs1, patches1):
    color = plot.cm.viridis(norm1(thisfrac))
    thispatch.set_facecolor(color)

for thisfrac, thispatch in zip(fracs2, patches2):
    color = plot.cm.viridis(norm2(thisfrac))
    thispatch.set_facecolor(color)

plot.show()