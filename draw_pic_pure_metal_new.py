import numpy as np
import matplotlib.pyplot as plt
import time


V = [
[1426.7934476540183, 1426.1700702147828, 1426.975752525524, 1427.7760656076573, 1428.5834880422658, 1429.4195513361071, 1430.2039452514425, 1431.0424600455976, 1431.8514980438865, 1432.699737545002, 1433.533396331994, 1434.3748525335548, 1435.1927886610622, 1436.034841310566, 1436.8939681933412, 1437.714267354007, 1438.5741195831952, 1439.4430257569807, 1440.2619313500009, 1441.1780474293118, 1442.0122953011826],
[5607.859116663954, 5529.15127659144, 5605.021543901501, 5605.292724731683, 5567.30623796226, 5526.6160533825805, 5664.791619719889, 5539.605563489037, 5586.345799855347, 5569.097913729348, 5689.550999858577, 5613.796902178572, 5611.976007869808, 5532.95724447225, 5680.123583723915, 5548.217973720745, 5668.372174406047, 5707.757203718594, 5557.378142990648, 5652.862349097407, 5610.109426361656],
[1221.5068508747756, 1225.3763335255007, 1229.6001646873174, 1233.4667010709222, 1237.0454344946675, 1241.6034555635604, 1245.283110690229, 1249.1496270838302, 1253.9102915992064, 1258.2135808418623, 1262.8509029044233, 1268.0451186997764, 1271.857056596255, 1276.223116652283, 1283.2370083373514, 1287.2201695944439, 1292.3422334124728, 1340.4672230067647, 1304.3370457629487, 1311.9395035670548, 1354.7871113582198],
[2758.098369532976, 2731.360170045986, 2722.8097295476045, 2721.5389261369114, 2721.043328274479, 2739.935191703807, 2734.874121968799, 2745.715570910779, 2754.806145170721, 2769.8022526567, 2795.21948461862, 2820.8995105696645, 2842.499574915164, 2877.127134731254, 2904.1842177438803, 2924.0112424311837, 2977.0601114663436, 3014.2128041114297, 3062.8025599575035, 3092.314409768532, 3158.9425663214906]
]

T = list(range(1, 1002, 50))

f = ['Li', 'Sb', 'Zn', 'Li_SNAP_ZuoChenLi_2019']

font_axis = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}
font_legend = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}

for i in range(5):
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    x = T
    y = V[i]
    ax.scatter(x, y, c='tab:blue', label=f[i], s=100,
              alpha=1.0, edgecolors='none')
    # ax1 = ax.twinx()
    
    valid_reward = 0
    
    
    ax.spines['left'].set_color('blue')
    ax.tick_params(axis='y', colors='blue')
    ax.yaxis.label.set_color('blue')
    # ax1.spines['right'].set_color('blue')
    # ax1.tick_params(axis='y', colors='blue')
    # ax1.yaxis.label.set_color('blue')
    y_high = ax.get_ylim()[0]*0.1 + ax.get_ylim()[1]*0.9
    
    ax.text(5, y_high, f[i], fontsize=16)
    # ax.legend(loc='best', prop=font_legend, scatterpoints=0)
    ax.grid(True)
    
    ax.set_ylabel(r'$Volume, \AA^3$', font_axis)
    # ax1.set_ylabel(r'$Pair\ Distance/\AA$', font_axis)
    ax.set_xlabel(r'$Temperature/K$', font_axis)
    ax.tick_params(labelsize=15)
    # ax1.tick_params(labelsize=15)
    
    plt.subplots_adjust(bottom=0.13, right=0.99, left=0.15, top=0.97)
    plt.show() 
