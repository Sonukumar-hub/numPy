#  seaborn - is a library that uses matplotlib underneath to ploat graph i.e pyplot
# matplotlib(pyplot)-seaborn

# Distplot - distribution plot(curve plot - histogram)

import matplotlib.pyplot as plt
import seaborn as sns 

sns.distplot([0,1,2,3,4,5])
plt.show()

# plotting a distplot without the histogram
import matplotlib.pyplot as plt
import seaborn as sns 

sns.distplot([0,1,2,3,4,5],hist=False)
plt.show()

