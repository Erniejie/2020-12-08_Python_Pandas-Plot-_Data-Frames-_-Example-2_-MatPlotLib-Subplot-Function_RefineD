#Pandas Plot - How to Use the MatPlotLib Subplot function-6th Nov 2018 Tutorial

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#pd.__version__
df = pd.DataFrame({"key":[193,196,203,205,200,206,204]})
print(df)
#% matplotlib inline :NOTE:this inbuilt function I think is available on jupyternotebook
df["Deflection"] =10
print(df)


fig,axes =plt.subplots(nrows=1,ncols=2,figsize=(17,8))
fig.subplots_adjust(hspace=0.9) # this lines is useful to keep the spacing bettwen rows if chose option \
                                #"nrows=2", "ncols 1"

print(df["key"].plot(ax=axes[0]))
print(df["Deflection"].plot(ax=axes[1]))

# Graph for DataFrame 1: df["key"]
axes[0].set_title("Case 1: Simply Supported Beam")
axes[0].set_xlabel("Span in [m]",fontsize=18,color ="r")
axes[0].set_ylabel("Settlement in [mm]",fontsize=16,color ="b")
axes[0].legend(["Case 1:Simply Supported"])

# Graph for Inserted DataFrame 2: df["Deflection"]
axes[1].set_title("Case 2: Cantilever Beam")
axes[1].set_xlabel("Span in [m]",fontsize=17,color ="g")
axes[1].set_ylabel("Settlement in [mm]",fontsize=15,color ="y")
axes[1].legend(["Case 2:Cantilever"])



plt.show()

