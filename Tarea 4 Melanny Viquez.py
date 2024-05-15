#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd


df=pd.read_csv(r"C:\Users\fiore\Downloads\nba (1).csv")


#Limpieza de datos

df['Height']=df['Height'].str.replace('-', '.').astype(float)

#Análisis Edad:

df[['Salary','Age']].groupby(['Age']).agg(['min', 'max', 'mean', 'count']).round(2).sort_values(('Age'),ascending=False)

#Se ordeno por edad descendiente y no se noto ningun patron ya que el promedio de salarios comparado con la edad
#sube o baja sin ninguna tendencia especifica.


# In[54]:


import pandas as pd


df=pd.read_csv(r"C:\Users\fiore\Downloads\nba (1).csv")


#Limpieza de datos

df['Height']=df['Height'].str.replace('-', '.').astype(float)

#Análisis Peso:

df[['Salary','Weight']].groupby(['Weight']).agg(['min', 'max', 'mean', 'count']).round(2).sort_values(('Weight'),ascending=False).head(60) 

#Acá ordenamos por peso descendiente y notamos que en realidad no existe ningun patron ya que las diferencias 
#de peso son muy pequeñas y el promedio de salario muy diferente. Ejemplo una persona de la fila 2 pesa 290 lbs y 
#gana 1200000 mientras que una persona en la fila 3 que pesa 289 lbs gana 13500000. El jugador que pesa 289 lbs
#gana un salario 10 veces mayor que el jugardor de 290 lbs. Lo cual hace que el peso no sea determinante ya que 
#una libra no es una diferencia de peso significativa.


# In[55]:


import pandas as pd


df=pd.read_csv(r"C:\Users\fiore\Downloads\nba (1).csv")


#Limpieza de datos

df['Height']=df['Height'].str.replace('-', '.').astype(float)


#Análisis Altura:

df[['Salary','Height','Team']].groupby(['Team', 'Height']).agg('mean').round (2).head(50)

#Analizando la altura por equipos podemos ver que el salario fluctua mucho, pero esto definitivamente no se debe a la 
#altura ya que no hay ninguna tendencia a la alta o baja.


# In[56]:


import pandas as pd


df=pd.read_csv(r"C:\Users\fiore\Downloads\nba (1).csv")


#Limpieza de datos

df['Height']=df['Height'].str.replace('-', '.').astype(float)


#Análisis Posicion:

df[['Salary','Position']].groupby(['Position']).agg(['mean', 'max', 'min']).round(2)

#Aqui vemos que el salario si depende de la posicion que vaya a ocupar un jugador, la posicion C (Center) y 
#PG (Point Guard) son las que pagan mas.  Esto quiere decir que la posición de juego de un jugador en la cancha 
#y la demanda de esa posición en la nba pueden influir en su salario.


# In[57]:


import pandas as pd


df=pd.read_csv(r"C:\Users\fiore\Downloads\nba (1).csv")


#Limpieza de datos

df['Height']=df['Height'].str.replace('-', '.').astype(float)


#Analisis College:

df[['Salary','College']].groupby(['College']).agg(['mean', 'max', 'min']).round(2).head(50).fillna(0)


#El College donde provienen los jugadores al parecer si influye en su salario. Colleges donde se destaque mas este 
#deporte se le dara mas importancia por lo que los jugadores pueden generar una base de fanáticos y seguidores leales 
#además hay colleges mas exigentes academicamente que otros y si un jugador tiene un rendimiento destacado en la 
#universidad, puede aumentar su perfil y su valor en el draft de la nba.

