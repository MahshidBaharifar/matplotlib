import matplotlib.pyplot as plt
population=[100000,110000,120000,130000,140000]
year=[2018,2019,2020,2021,2022]
plt.xlabel('population')
plt.ylabel('year')
plt.title('population growth')
plt.plot(population,year,marker='o')
plt.show()