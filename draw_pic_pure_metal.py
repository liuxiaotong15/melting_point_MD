import numpy as np
import matplotlib.pyplot as plt
import time


V = [
[1430.216919880311, 1431.8296548794892, 1433.5293823670609, 1435.2257645063953, 1436.8827445490713, 1438.510648518412, 1440.2699061028238, 1441.9851254470248, 1443.676202938547, 1445.4880065648447],
[2802.4113446829883, 2805.55591173305, 2808.720661094657, 2811.96720978332, 2815.1782504297316, 2818.4113136245733, 2821.7281784752176, 2824.960966828669, 2828.1987942181627, 2831.634928020665],
[5668.202642258165, 5588.992082051917, 5616.51415510874, 5660.871278956602, 5651.421081459449, 5553.473939708946, 5595.9263199967, 5549.299928425414, 5661.747312367729, 5617.356037278511],
[1246.8411550223384, 1257.7251980797903, 1276.3690811600925, 1311.101045057165, 1326.4046468455833, 1344.037935843428, 1352.595314684919, 1356.35662246053, 1378.5538952991817, 1396.9352487718668],
[1247.5279876195616, 1299.0043496208355, 1312.3195545811843, 1325.3500015026514, 1333.9465940145146, 1343.8707259125517, 1353.1385837206183, 1355.224216276449, 1362.255177719808, 1369.1027393269478]
]

T = list(range(300, 1300, 100))

f = ['Li', 'Li', 'Sb', 'Zn', 'Zn']

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
    
    ax.text(300, y_high, f[i], fontsize=16)
    # ax.legend(loc='best', prop=font_legend, scatterpoints=0)
    ax.grid(True)
    
    ax.set_ylabel(r'$Volume, \AA^3$', font_axis)
    # ax1.set_ylabel(r'$Pair\ Distance/\AA$', font_axis)
    ax.set_xlabel(r'$Temperature/K$', font_axis)
    ax.tick_params(labelsize=15)
    # ax1.tick_params(labelsize=15)
    
    plt.subplots_adjust(bottom=0.13, right=0.99, left=0.15, top=0.97)
    plt.show() 
