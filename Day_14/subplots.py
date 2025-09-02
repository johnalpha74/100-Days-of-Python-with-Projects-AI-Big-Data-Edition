import matplotlib.pyplot as plt

# 1x2 layout: two separate axes in a single figure
fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.plot(x, y, marker='o')
ax1.set_title('Line')

ax2.bar(categories, values)
ax2.set_title('Bar')

fig.suptitle('Subplots Example')
plt.tight_layout()
plt.show()
