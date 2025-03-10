import pandas as pd
import pandas as pd 

Tabla = {
        "Producto": ["Manzanas", "Naranjas", "Platanos", "Uvas", "Peras"],
        "Precio": [100,80,60,120,90],
        "Stock": [30,50,20,60,40]
}

df = pd.DataFrame(Tabla)
print (df)

precios = df["Precio"]
#print (precios)

producto_naranjas = df.loc [1, "Producto"]
#print (producto_naranjas)

producto_naranjas_1 = df.loc [1]
#print (producto_naranjas_1)

producto_naranjas_2 = df.iloc[1,0]
#print (producto_naranjas_2)

producto_naranjas_3 = df.loc [2]
#print (producto_naranjas_3)

#producto_naranjas_4 = df.loc ["Manzanas"]
#print (producto_naranjas_4)

#Precios altos 

df_preciosaltos= df[df["Precio"] > 80]
print (df_preciosaltos)

df_filtrado = df [(df["Precio"] > 60) & (df["Stock"]>30)]
print (df_filtrado)

df_were = df ["Precio"].where(df["Precio"]>80, other=0)
print (df_were)

print ("Query")
df_query = df.query ("Precio > 80")
print (df_query)