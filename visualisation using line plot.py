import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# July birth rate data
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
july_births = [12,15,11,9,1,9,21]
df_july = pd.DataFrame({'Day':days,'Births':july_births})

# Line plot for July
plt.plot(df_july['Day'],df_july['Births'],marker='o',linestyle='--',linewidth=2,color='blue')
plt.title("Birth Rate - July")
plt.xlabel("Day")
plt.ylabel("New Births")
plt.show()

# August birth rate data
aug_births = [17,5,2,11,1,8,29]
df_aug = pd.DataFrame({'Day':days,'Births':aug_births})

# Line plot for August
plt.plot(df_aug['Day'],df_aug['Births'],marker='s',linestyle='-.',linewidth=2,color='green')
plt.title("Birth Rate - August")
plt.xlabel("Day")
plt.ylabel("New Births")
plt.show()

# Comparison of July and August
plt.plot(days,july_births,marker='o',linestyle='--',linewidth=2,label='July')
plt.plot(days,aug_births,marker='s',linestyle='-.',linewidth=2,label='August')
plt.title("Birth Rate Comparison")
plt.xlabel("Day")
plt.ylabel("New Births")
plt.legend()
plt.show()

# Plot equation y = 6x^2 + x + 1
x = np.arange(1,11)
y = 6*x**2 + x + 1
plt.plot(x,y,marker='o')
plt.title("Plot of y = 6x^2 + x + 1")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()