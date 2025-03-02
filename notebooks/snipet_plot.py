import matplotlib.pyplot as plt



fig, ax = plt.subplots(figsize=(12,8))

ax.scatter(x=acquisition_year.index, y=acquisition_year, s=5, c='yellow')
ax.set_yscale('log')

ax.set_title('Tate Gallery Acquisition')
ax.set_xlabel('Acquisition Year')
ax.set_ylabel('Artwork Count')

ticks = [year for year in acquisition_year.index if year % 10 == 0]

ax.set_xticks(ticks)
ax.set_xticklabels(ticks, rotation=45)

ax.grid(True)
ax.set_axisbelow(True)


fig.tight_layout()
plt.show()