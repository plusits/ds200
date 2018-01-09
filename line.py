import pandas as pd
import matplotlib.pyplot as plt
import sys
#create dataframe
df=pd.read_csv(sys.argv[1], header=None, names=['col1', 'col2'])

#plot line plot with first column of dataframe as x values and second column as y values
plt.plot(df['col1'],df['col2'],color='#dd12dd',label="Infant Mortality Rate (IMR)")
# plt.scatter(Mem['col3'],Mem['col4'],color='#caabdd',label="Hop6")

#specifying labels
plt.xlabel("Year")
plt.ylabel("All India IMR")

#enable legend
plt.legend()
plt.show()