import pandas as pd
import matplotlib.pyplot as plt
import sys


#reading data frame from a csv file
df=pd.read_csv(sys.argv[1], header=None, names=['col1'])
    
#plot bar plot with xticks which is position of bars as first argument and height of bars as second argument
plt.bar([1,2,3,4,5,6],df['col1'],color='#ddbb55',label="Cash Transaction Reports (CRTS) received in 2011-12 under Prevention of Money Laundering Act")

#specify labels on xticks
plt.xticks([1,2,3,4,5,6],["2007-08","2008-09","2009-10","2010-11","2011-12","Till 31/3/12"])
plt.xlabel("Year")
plt.ylabel("CRTs received from Cooperative Banks & Others")

#enabling legend
plt.legend()
plt.show()