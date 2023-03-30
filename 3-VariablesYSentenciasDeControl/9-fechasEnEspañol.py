# %%
from datetime import datetime
import locale
#locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dt =datetime.strptime('29/04/2022','%d/%m/%Y') #datetime.now()

print(dt)
print('\nDirectívas\n-------------------------------')
print('Día de semana corto       ' + dt.strftime(': %a'))
print('Día de la semana largo    ' + dt.strftime(': %A'))
print('Número de dia de la semana' + dt.strftime(': %w'))
print('Día del mes               ' + dt.strftime(': %d'))
print('Nombre del mes corto      ' + dt.strftime(': %b'))
print('Nombre del mes largo      ' + dt.strftime(': %B'))
print('Numero del mes            ' + dt.strftime(': %m'))
print('Año version corta         ' + dt.strftime(': %y'))
print('Anyo version larga        ' + dt.strftime(': %Y'))
print('Hora formato (00-23)      ' + dt.strftime(': %H'))
print('Hora formato (00-11)      ' + dt.strftime(': %I'))
print('AM/PM                     ' + dt.strftime(': %p'))
print('Minutos                   ' + dt.strftime(': %M'))
print('Segundos                  ' + dt.strftime(': %%'))

print('\nFormato de texto de fechas\n--------------')
print(dt.strftime('%a %d-%m-%Y'))
print(dt.strftime('%a %d/%m/%Y'))
print(dt.strftime('%a %d/%m/%y'))
print(dt.strftime('%A %d-%m-%Y, %H:%M:%S'))
print(dt.strftime('%X %x'))
