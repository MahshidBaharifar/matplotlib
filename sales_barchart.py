import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [5000, 8000, 3000, 6000]

plt.bar(products, sales)
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Performance of Different Products')
plt.show()