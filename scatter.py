import pandas as pd
import matplotlib.pyplot as plt
import sys
#create dataframe
df=pd.read_csv(sys.argv[1], header=None, names=['col1', 'col2'])

#plot scatter with first column as x values and second column as y values
plt.scatter(df['col1'],df['col2'],color='#000000',label="All India level Recorded Forest Area ")

#specifying labels
plt.xlabel("Year")
plt.ylabel("Total Forest Area")

#enable legend
plt.legend()
plt.show()