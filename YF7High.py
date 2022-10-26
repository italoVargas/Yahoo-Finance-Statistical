
import yfinance as yf
import numpy as np 
import pandas as pd
#from scipy.stats import *
import scipy as sp
from datetime import date
import datetime as dt
import matplotlib.pyplot as plt
import time 
import matplotlib

#matplotlib.use('Agg')

def YHF(T,Ai,Af):


	
	Ticker=yf.Ticker(T) 
	INFO=Ticker.history(period='max')
	print(Ticker)
	print(INFO)
	
	#Ai=1950
	#Af=2022
	
	dias=np.arange(1,32,1)
	meses=np.arange(1,13,1)
	años=np.arange(int(Ai),int(Af),1)
	
	DIAS=[]
	MESES=[]
	AÑOS=[]
	
	M1=[]
	M2=[]
	M3=[]
	M4=[]
	M5=[]
	M6=[]
	M7=[]
	M8=[]
	M9=[]
	M10=[]
	M11=[]
	M12=[]
	
	
	T1=[]
	T2=[]
	T3=[]
	T4=[]
	
	df = INFO.copy()
	df['Año'],df['Mes'], df['Dia'] = INFO.index.year, INFO.index.month, INFO.index.day
	
	NombresCol=df.columns.values
	
	Añomin=df.Año.min()
	Añomax=df.Año.max()
	
	Omin=df.Open.min()
	Omax=df.Open.max()
	Omean=df.Open.mean()
	
	Hmean=df.High.mean()
	Hmin=df.High.min()
	Hmax=df.High.max()
	
	Lmean=df.Low.mean()
	Lmin=df.Low.min()
	Lmax=df.Low.max()
	
	Cmean=df.Close.mean()
	Cmin=df.Close.min()
	Cmax=df.Close.max()
	
	Dmean=df.Dividends.mean()
	Dmax=df.Dividends.max()
	Dmin=df.Dividends.min()
	
	
	Sp=df['Stock Splits'].mean()
	
	for a in años:
		try:
			ia=df[df.Año==a]
			AÑOS.append(ia.High.mean())
			#print(ia)
		except:
			pass
	
	for k in meses:
		try:
			
			ms=df[df.Mes==k]
			MESES.append(ms.High.mean())
	
		except:
			pass
	
	
	for i in dias:	
		try:
			i=df[df.Dia==i]
		
			DIAS.append(i.High.mean())
	
	
			for m in meses:
				j=i[i.Mes==m]
	
				if m==1:
					M1.append(j.High.mean())
				if m==2:
					M2.append(j.High.mean())
	
				if m==3:
					M3.append(j.High.mean())
				if m==4:
					M4.append(j.High.mean())
	
				if m==5:
					M5.append(j.High.mean())
				if m==6:
					M6.append(j.High.mean())
	
				if m==7:
					M7.append(j.High.mean())
				if m==8:
					M8.append(j.High.mean())
		
				if m==9:
					M9.append(j.High.mean())
				if m==10:
					M10.append(j.High.mean())
	
				if m==11:
					M11.append(j.High.mean())
				if m==12:
					M12.append(j.High.mean())
	
		except:
			pass
	
	
	
	print(NombresCol)
	print(AÑOS)
	print('Open max',Omax,'Open Min ',Omin)
	print('Low max',Lmax,'Low min',Lmin)
	print('High max',Hmax,'high min ',Hmin)
	print('Close max',Cmax,'Close min ',Cmin)
	print('Dividends max',Dmax,'Dividends min ',Dmin,'Dividends mean =',Dmean)
	print('Stock Splits=',Sp)
	
	#plt.style.use('seaborn-ticks')
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,1)
	plt.title('AÑO')
	
	plt.xlabel('Año')
	plt.ylabel('Valor')
	plt.plot(AÑOS)
	plt.grid(True)
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	#ticks_x=ticker.FuncFormatter(lambda x,)
	#plt.ylim(dmin,dmax)
	plt.tight_layout()
	
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,2)
	plt.title('MES')
	
	plt.xlabel('MES')
	plt.ylabel('Valor')
	plt.plot(MESES)
	plt.grid(True)
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)




	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,3)
	plt.title('Por   DIA ')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(DIAS)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	#plt.xlim(dmin,dmax)
	




	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,4)
	
	plt.title('ENERO')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M1)
	plt.grid(True)
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,5)
	plt.title(' FEBRERO')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M2)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,6)
	plt.title(' MARZo')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M3)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,7)
	
	
	plt.title(' ABRIL')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M4)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,8)
	plt.title(' MAYO')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M5)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,9)
	plt.title(' JUNIO')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M6)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,10)
	plt.title(' JULIO')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M7)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,11)
	plt.title(' AGOSTO')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M8)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,12)
	plt.title(' Septiembre')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M9)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,13)
	plt.title(' OCTUBRE')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M10)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,14)
	plt.title(' NOVIEMBRE')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M11)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,15)
	plt.title(' DICIEMBRE')
	
	plt.xlabel('Dia')
	plt.ylabel('Valor')
	plt.plot(M12)
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()
	#plt.ylim(dmin,dmax)
	
	plt.figure('Gráfico de promedios '+' - '+ str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax),figsize=(20, 10)).add_subplot(4,4,16)
	plt.title('Open-min-max-mean  C---  L---  H---  C---  Div  SP ')
	
	plt.xlabel(Omin)
	plt.ylabel(Omax)
	plt.scatter(0,Omin)
	plt.scatter(1,Omax)
	plt.scatter(2,Omean)
	plt.scatter(6,Lmin)
	plt.scatter(7,Lmax)
	plt.scatter(8,Lmean)
	plt.scatter(3,Hmin)
	plt.scatter(4,Hmax)
	plt.scatter(5,Hmean)
	plt.scatter(9,Cmin)
	plt.scatter(10,Cmax)
	plt.scatter(11,Cmean)
	plt.scatter(12,Dmin)
	plt.scatter(13,Dmax)
	plt.scatter(14,Dmean)
	plt.scatter(15,Sp)
	
	plt.legend()
	plt.legend(loc='best')
	plt.grid()
	plt.minorticks_on()
	plt.grid(  which='minor', color='green', linestyle='--', alpha=0.3)
	plt.tight_layout()	
	#plt.savefig(str( T )+' Desde: '+str(Añomin)+' Hasta: '+str(Añomax)+'.png')
	plt.savefig(str( T )+' Desde: '+str(Ai)+' Hasta: '+str(Af)+ 'High' +'.png')
#	plt.show(block=False)
#	time.sleep(1)
#	plt.close()
	
	#print(AÑOS)





	#T='GMEXICOB.MX'
	
	#'VOO'
	#T='GENIUS21.MX'
	#T='IVVPESOISHRS.MX'#
	#'^GSPC'#
	#'SPY'#
	#T='WALMEX.MX'#
	#'VNQ'#
	#'GMEXICOB.MX'
	#T='BABA'
	#T='SPY'


while True:
	YHF('BTC-USD','2015','2022')
	YHF('GENIUS21.MX','2015','2022')
	YHF('ICLN','2015','2022')
	YHF('FB','2015','2022')
	YHF('VMEX19.MX','2015','2022')
	YHF('IVVPESOISHRS.MX','2015','2022')
	YHF('SPLG','2015','2022')
	YHF('^GSPC','2015','2022')
	YHF('VT','2015','2022')
	YHF('WALMEX.MX','2015','2022')
	YHF('SPY','2015','2022')
	YHF('VNQ','2015','2022')
	YHF('VOO','2015','2022')
	YHF('GMEXICOB.MX','2015','2022')
	YHF('BABA','2015','2022')


