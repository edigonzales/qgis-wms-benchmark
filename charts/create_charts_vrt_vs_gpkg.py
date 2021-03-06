# -*- coding: utf-8 -*- 
import matplotlib
matplotlib.use( "agg" )
import matplotlib.pyplot as plt
import pylab


t11 = [1, 2, 3, 4, 5, 6, 7]
t12 = [1, 2, 4, 8, 16, 32, 64]

## AV-WMS (farbig)
#filename = "avwms_bench"
#title = "AV-WMS (farbig)"
#direkt = [5.5, 10.9, 12.8, 21.4, 22.8, 29.9, 31.5]
#embedded = [5.3, 10.4, 15.4, 19.8, 21.6, 30.4, 31.9]
#wms = [4.0, 5.7, 8.6, 9.7, 5.8, 1.9, pylab.nan]

## Plan fuer das Grundbuch
#filename = "grundbuchplan_bench"
#title = "Grundbuchplan"
#direkt = [2.7, 6.1, 12.3, 20.0, 31.1, 32.0, 32.0]
#embedded = [6.2, 11.9, 17.7, 25.0, 30.1, 22.7, 32.9]
#wms = [4.8, 7.3, 8.7, 12.8, 8.1, 1.6, pylab.nan]

## Basisplan
#filename = "basisplan_bench"
#title = "Basisplan"
#direkt = [3.2, 6.1, 9.3, 13.0, 14.2, 15.2, 15.7]
#embedded = [3.2, 5.7, 9.5, 13.8, 14.0, 14.9, 15.2]
#wms = [2.4, 3.6, 5.9, 6.3, 3.2, pylab.nan, pylab.nan]

## Orthofoto
#filename = "orthofoto_bench"
#title = "Orthofoto"
#direkt = [2.9, 5.6, 9.3, 14.0, 13.1, 14.6, 15.0]
#embedded = [3.3, 5.3, 9.4, 14.0, 14.0, 14.6, 14.9]
#wms = [1.8, 3.0, 4.6, 5.2, 2.6, pylab.nan, pylab.nan]

# Kombination
filename = "ortho_vrt_vs_gpkg_bench"
title = "Orthofoto VRT vs. GPKG"
vrt = [1.5, 2.7, 4.1, 5.2, 5.4, 5.9, 6.2]
gpkg = [1.2, 2.3, 4.0, 4.7, 4.9, 5.3, 5.8]
gpkg_single = [1.2, 2.4, 3.7, 4.4, 5.1, 5.4, 5.7]

plt.plot(t11, vrt,  marker='s', color='b', label='VRT', linewidth='2')
plt.plot(t11, gpkg, marker='o', color='y', label='GPKG', linewidth='2')
plt.plot(t11, gpkg_single, marker='^', color='m', label='Single GPKG', linewidth='2')

plt.xlabel('N Requests')
plt.ylabel('Throughput (Req/s)')
plt.title(title)
plt.legend(bbox_to_anchor=(0.02, 0.98), loc=2, borderaxespad=0.)

plt.xticks( [1, 2, 3, 4, 5, 6, 7],  t12 )
plt.ylim([0, 7])

plt.grid(b=True, which='major', linestyle='dotted') 

plt.savefig('./'+filename+'.png', dpi=100)
