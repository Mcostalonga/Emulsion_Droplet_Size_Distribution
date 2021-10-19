# Importing modules

import numpy as np

# Used to create a char array and replace "," for "." in this script

import numpy.core.defchararray as np_f

# Used to create graphs

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)

# Used to save a file in .XLSX format

import xlsxwriter

# Name and location of the data file

file_d = 'data/001.txt'
path_f = 'results/'

# Getting the test name

name = file_d.split('/')
name_split = name[len(name) - 1].split('.')
test_name = name_split[0]

# Reading data file

diameter_data = []
with open(file_d, 'r') as f:
    f = f.readlines()
    f = np_f.replace(f, ',', '.')
    for line in f:
        diameter_data.append(float(line.strip()))

# Creating an fixed interval to make future comparisons easier

interval = list(np.arange(0, 250, 5))

# Calculating the relative and cumulative frequency for data

hist, edges = np.histogram(diameter_data, interval)
rel_freq = (hist / float(hist.sum()))
rel_freq = rel_freq * 100
cumulative_freq = np.zeros(len(rel_freq))
cumulative_freq[0] = 0
for i in range(len(rel_freq) - 1):
    cumulative_freq[i + 1] = cumulative_freq[i] + rel_freq[i]

# Calculating the d90_a

d90_a = 0
i1 = 0
while cumulative_freq[i1] <= 90:
    i1 += 1
i2 = len(cumulative_freq) - 1
while cumulative_freq[i2] > cumulative_freq[i1]:
    i2 -= 1
if cumulative_freq[i1] != 90:
    d90_a = ((cumulative_freq[i2 + 1] - 90) / (cumulative_freq[i2 + 1] - cumulative_freq[i1 - 1])) * (
            interval[i2 + 1] - interval[i1 - 1]) + interval[i1 - 1]
else:
    d90_a = interval[i1]

yd90 = [0, 100]
d90 = [d90_a, d90_a]

info = ('Column info', '1st - Droplet Diameter', '2nd - Interval', '3rd - Relative Frequency',
        '4th - Cumulative Frequency', '5th - Y to plot d 90', '6th - Value of d90')
# Saving data into .xlsx file

workbook = xlsxwriter.Workbook(path_f + test_name + '.xlsx')
worksheet = workbook.add_worksheet()
Line = 0
Column = 0
ProcData = [diameter_data, interval, rel_freq, cumulative_freq, yd90, d90, info]
while Column < len(ProcData):
    for item in ProcData[Column]:
        worksheet.write(Line, Column, item)
        Line += 1
    Column += 1
    Line = 0
workbook.close()

# Plotting results

fig, ax = plt.subplots(figsize=(8, 6))
barchart = plt.bar(interval[:-1], rel_freq, width=5.0, align='edge', ec='k', alpha=0.7,
                   color=(0, 0, 1), label='Droplet size distribution')

ax2 = plt.twinx()
linechart, = plt.plot(interval[:-1], cumulative_freq, color=(0, 0, 0), label='Cumulative Frequency')
d90chart, = plt.plot(d90, yd90, '--', color=(0.4, 0.4, 0.4), label='d\u2089\u2080')
color_d90chart = d90chart.get_color()

# Legend

legends = barchart, linechart
labels = [item.get_label() for item in legends]
ax.legend(legends, labels, loc='center right')

d90_a = d90[0]
d90_a = '{0:.3f}'.format(d90_a)
ax2.text(d90[0] + 0.5, 80, '\u2190d\u2089\u2080 = ' + d90_a
         + ' \u03BCm', color=color_d90chart, font='Times New Roman', fontsize=12)

# Title

ax.set_title('Droplet Size Distribution and d\u2089\u2080', font='Times New Roman', fontsize=14, fontweight='bold')

# Formatting axes, labels, lines, tickmarks, gridlines

# X axis

ax.set_xlabel('Droplet Diameter [\u03BCm]', font='Times New Roman', fontsize=12, fontweight='bold')
ax.set_xlim([0, 250])

# Y axis - left
ax.set_ylabel('Relative Frequency [%]', font='Times New Roman', fontsize=12, fontweight='bold')
ax.set_ylim(0, max(rel_freq))

# Y axis - right

ax2.set_ylabel('Cumulative Frequency [%]', font='Times New Roman', fontsize=12, fontweight='bold')
ax2.set_ylim(0, 100)

# Tickmarks positioning

ax.xaxis.set_ticks_position('both')
ax.tick_params(which='major', width=1.50, length=5, direction='in')
ax.tick_params(which='minor', width=1.5, length=3, labelsize=10, direction='in')
ax2.tick_params(which='major', width=1.50, length=5, direction='in')
ax2.tick_params(which='minor', width=1.5, length=3, labelsize=10, direction='in')

# Adding minor tickmarks

# X axis

ax.xaxis.set_minor_locator(MultipleLocator(5))

# Y axis - left

ax.yaxis.set_minor_locator(MultipleLocator(0.5))

# Y axis - right

ax2.yaxis.set_minor_locator(MultipleLocator(5))

# Label font and size

plt.setp(ax.get_xticklabels(), font='Times New Roman', fontsize=12)
plt.setp(ax.get_yticklabels(), font='Times New Roman', fontsize=12)
plt.yticks(font='Times New Roman', fontsize=12)

# Setting the line width to axes

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(1.5)

# Saving the figure at path informed

plt.savefig(path_f + test_name + '.png', format='png', dpi=200)

# Showing the figure for "t" seconds
t = 3
plt.show(block=False)
plt.pause(t)
plt.close()
