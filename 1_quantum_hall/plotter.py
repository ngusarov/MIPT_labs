from matplotlib import font_manager


def unpack_data(filename):
    f = open(filename, 'r')
    x = []
    y = []
    for ind, line in enumerate(f):
        if ind >= 2:
            line = line.split()
            x.append(float(line[0]))
            y.append(float(line[1]))
    return x, y

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axvline(752.5, linestyle='--', c='grey', linewidth='2')
ax.axvline(802.5, linestyle='--', c='grey', linewidth='2')
ax.axvline(789, linestyle='--', c='grey', linewidth='2')
ax.axvline(745.5, linestyle='--', c='grey', linewidth='2')

x, y = unpack_data('A579.txt')
ax.plot(x, y, c='green', label='A579')

x, y = unpack_data('A579_no_filter.txt')
ax.plot(x, y, c='red', label='A579, no filter')

x, y = unpack_data('A580.txt')
ax.plot(x, y, c='blue', label='A580')

font = {'fontname': 'Times New Roman'}
#ax.set_title("Sample A579", **font, fontsize=25)

# Подписи:
ax.set_xlabel("Wavelength $\lambda$, [$nm$]", **font, fontsize=25)
ax.set_ylabel("Power, [a.u.]", **font, fontsize=25)

# Сетка:
ax.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=20)
#ax.grid(which='major', axis='both')
#ax.grid(which='minor', axis='both', linestyle=':')

fig.set_figheight(7)
fig.set_figwidth(10)

font_2 = font_manager.FontProperties(family='Times New Roman', size=25)
plt.legend(loc='upper left', prop=font_2)
fig.savefig("A579.pdf", dpi=500)
plt.close()

fig, ax = plt.subplots()

ax.axvline(802.5, linestyle='--', c='grey', linewidth='2')
ax.axvline(789, linestyle='--', c='grey', linewidth='2')
ax.axvline(752.5, linestyle='--', c='grey', linewidth='2')
ax.axvline(745.5, linestyle='--', c='grey', linewidth='2')

x, y = unpack_data('A579.txt')
ax.plot([each for each in x if 700 < each < 830], [each for ind, each in enumerate(y) if 700 < x[ind] < 830], c='green')

x, y = unpack_data('A579_no_filter.txt')
ax.plot([each for each in x if 700 < each < 830], [each for ind, each in enumerate(y) if 700 < x[ind] < 830], c='red')

x, y = unpack_data('A580.txt')
ax.plot([each for each in x if 700 < each < 830], [each for ind, each in enumerate(y) if 700 < x[ind] < 830], c='blue')

font = {'fontname': 'Times New Roman'}

# Сетка:
ax.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=25)
#ax.grid(which='major', axis='both')
#ax.grid(which='minor', axis='both', linestyle=':')

fig.set_figheight(7)
fig.set_figwidth(10)

fig.savefig("A579_enl.pdf", dpi=500)
plt.close()

