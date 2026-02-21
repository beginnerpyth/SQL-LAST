import pandas as pd
bios=pd.read_csv('bios.csv')
#print(bios)
#print(bios.columns)
#print(bios[(bios['height_cm']>100)&(bios['born_country']=="USA"),])
#print(bios.loc[0:5,("name","height_cm")])
#print(bios['born_country'].str.contains("USA|GBR",case=False))
#print(bios['name'].str.contains('keith|henry|patrick',case=False))#| patrick
#print(bios['born_city'].str.contains("bhaktapur|tokyo",case=False,regex=False))#exact match nikalxa regex ley
print(bios[bios['born_country'].isin(['USA',"FRA","GBR"])&(bios['name'].str.startswith("Bob"))])#isin ma jaile[] chainxa rey
#print(bios.query('born_country=="USA" and born_city=="Washington"'))sab data bahiraa nikalxa jun chahi usa ma janmekorw washington ma janmeko
jand=pd.read_csv("pand.csv")
#print(jand.columns)
#add remove columns
jand['ranking']=1

#print(jand.columns)
#print(jand.head())
#import numpy as np
#jand['NEWPULSE']=np.where(jand['Pulse']>=110,220,240)#jun 110 vanda small value chai 220 and all other data should be 240
#print(jand.head())
#print(jand.drop(0))#just temporary we can dropm the index
#jand.drop(columns=['Calories'],inplace=True)#dropping the columns with inplace deletesthe column permanently and without it removes temporarily
#print(jand)
#band['ranking']=2
#print(band)
#print(jand)#so basically what happens here is that when we do band it creates permanently on jand too
#band=jand.copy()
#band['ranking']=3 
#print(jand)#now it doesnot change because we used copy in band
#jand['totalpulse']=jand['Pulse']*jand['Maxpulse']
#print(jand)
#jand.rename(columns={"totalpulse":"nothing"},inplace=True)#if i dont do inplace is true then itss not permanent and for tempo we use print
#print(jand.head())
bios_new=bios.copy()
#bios_new['hahaha']=bios_new['name'].str.split(" ").str[0]##column bana tesma name lai split gareara first ko part matra leu

print(bios_new.columns)
bios_new['born_date2']=pd.to_datetime(bios_new['born_date'])#we do this o make pandas understand to take out the dates as we wanrs
bios_new["born_year"]=bios_new['born_date2'].dt.year
print(bios_new)