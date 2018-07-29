
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


dfLaser = pd.read_csv("nis_laser.txt", header=None)
dfRadar = pd.read_csv("nis_radar.txt", header=None)

df = pd.concat([dfLaser, dfRadar], axis=1, join='inner', keys=["NIS_laser", "NIS_radar"])


# In[15]:


fig = plt.figure()
ax = plt.subplot(111)
ax.plot(dfRadar)
plt.title("NIS_radar")
ax.legend()

fig.savefig("NIS_radar.png")


# In[14]:


fig = plt.figure()
ax = plt.subplot(111)
ax.plot(dfLaser)
plt.title("NIS_laser")
ax.legend()

fig.savefig("NIS_laser.png")

