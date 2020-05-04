# Python script in QGIS
# Last update: 2020-05-03 18:41
# Develped by N.S.

import datetime
import pandas as pd
import os
import shutil
from shutil import move

zona = 'Florida Norte (FN-4)'
FILE_NAME_DATA_BASE = 'c:\\NS\\INET\\Survey\\Database\\'+zona+'.csv'

df_general = pd.DataFrame(columns=['URA','Zona','Fecha','Relevadores','Entidades','Postes','Edificaciones','Demanda'])
new_row = pd.DataFrame([[""] * df.shape[1]], columns=df.columns)
new_row.at[0, 'URA'] = 'qwe'
df_general = pd.concat([df_general, new_row], ignore_index=True)
df_general.to_csv(zona, index=False)
shutil.move(zona,FILE_NAME_DATA_BASE)
os.startfile(FILE_NAME_DATA_BASE, 'open')

fechas = ['2020-03-13','2020-04-29','2020-04-30','2020-05-04']

al=iface.activeLayer()
print('\nEn la zona "{}":'.format(zona))

s=[0,0,0]
for fecha in fechas:
    c=[0,0,0] # cantidad de: postes, edificaciones, demanda
    aux = datetime.datetime.strptime(fecha, '%Y-%m-%d')
    print('** El día {} se registraron:'.format(aux.strftime("%d/%m/%Y (%A)")))
    for feature in al.getFeatures():
        if fecha==feature['__created'].toString('yyyy-MM-dd'):
            if feature['entidad']=='Poste': c[0] += 1
            if feature['entidad']=='Edificacion': c[1] += 1
            if feature['demanda']!=NULL:
                c[2] += int(feature['demanda'])
    s[0] += c[0]
    s[1] += c[1]
    s[2] += c[2]
    print('   {} postes, {} edificaciones, total demanda: {}.'.format(c[0],c[1],c[2]))

print('En total se registraron {} entidades, de las cuales:'.format(al.featureCount()))
print('   {} postes, {} edificaciones, {} demanda.'.format(s[0],s[1],s[2]))
