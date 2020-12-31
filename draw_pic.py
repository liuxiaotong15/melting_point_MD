import numpy as np
import matplotlib.pyplot as plt
import time


V = [[1487.1294816307504, 1496.689710468552, 1485.2348130876842, 1491.6775270384796, 1493.1748505968078, 1491.0940755081344, 1497.2814811164299, 1495.9253869503618, 1494.6189983935774, 1499.9806055475285],
[1476.7691398629286, 1498.9902853261808, 1498.9701827306787, 1508.5077383183022, 1509.9040096663462, 1514.7505588917572, 1510.1797563347893, 1505.9626211328318, 1512.2075771585044, 1515.404478895561],
[577.2332271392992, 585.5033073484458, 587.0264730876763, 577.3520371662271, 577.3175523403233, 583.4246080772227, 578.7900946929485, 580.7002775827224, 592.5904406767482, 581.6872304718746]
]

T = list(range(300, 1300, 100))

f = ['Li2SbZn_ICSD_1243',  'Li2SbZn_ICSD_199259',  'LiSbZn_ICSD_42064',  'LiSbZn_ICSD_642350']

font_axis = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}
font_legend = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}

for i in range(3):
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
    
    ax.legend(loc='best', prop=font_legend)
    ax.grid(True)
    
    ax.set_ylabel(r'$Volume, \AA^3$', font_axis)
    # ax1.set_ylabel(r'$Pair\ Distance/\AA$', font_axis)
    ax.set_xlabel(r'$Temperature/K$', font_axis)
    ax.tick_params(labelsize=15)
    # ax1.tick_params(labelsize=15)
    
    plt.subplots_adjust(bottom=0.13, right=0.99, left=0.15, top=0.97)
    plt.show() 
