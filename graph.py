# import csv
import matplotlib.pyplot as plt
import pandas as pd

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'black', 'orange',
          'purple', 'brown', 'gray', 'cyan', 'magenta']

available_data = [
    "Index",
    "Time (ms)",
    "sed RAM (MB)",
    "Total RAM (MB)",
    "Number of Free RAM Blocks",
    "Size of Free RAM Blocks (MB)",
    "Used SWAP (MB),Total SWAP (MB)",
    "Cached SWAP (MB),CPU Frequency (MHz)",
    "CPU 0 Load (%)",
    "CPU 1 Load (%)",
    "CPU 2 Load (%)",
    "CPU 3 Load (%)",
    "CPU 4 Load (%)",
    "CPU 5 Load (%)",
    "CPU 6 Load (%)",
    "CPU 7 Load (%)",
    "APE frequency (MHz)",
    "Used GR3D (%)",
    "GR3D Frequency (MHz)",
    "Used EMC (%)",
    "AUX Temperature (C)",
    "CPU Temperature (C)",
    "thermal Temperature (C)",
    "Tboard Temperature (C)",
    "AO Temperature (C)",
    "GPU Temperature (C)",
    "Tdiode Temperature (C)",
    "PMIC Temperature (C)",
    "Current GPU Power Consumption (mW)",
    "Current GPU average Power Consumption (mW)",
    "Current CPU Power Consumption (mW)",
    "Current CPU average Power Consumption (mW)",
    "Current SOC Power Consumption (mW)",
    "Current SOC average Power Consumption (mW)",
    "Current CV Power Consumption (mW)",
    "Current CV average Power Consumption (mW)",
    "Current VDDRQ Power Consumption (mW)",
    "Current VDDRQ average Power Consumption (mW)",
    "Current SYS5V Power Consumption (mW)",
    "Current SYS5V average Power Consumption (mW)",
]

pairs = [('Time (ms)', 'Used GR3D (%)'), 
        ('Time (ms)', 'Current CPU Power Consumption (mW)'),
        ('Time (ms)', "CPU 0 Load (%)")]

class Graph:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file, skiprows=1, header=0, index_col=0)

    def scatter_plot(self, x, y):
        plt.figure()
        plt.title(f'{x} vs. {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.scatter(self.df.loc[:, x], self.df.loc[:, y])
        plt.savefig(f'{x} vs. {y}.png')

    def plots(self):
        for pair in pairs:
            self.scatter_plot(pair[0], pair[1])

if __name__ == '__main__':
    csv_file = 'sample_log.csv'

    graph = Graph(csv_file)
    graph.plots()
