import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline

dataset = pd.read_csv("Catalogo_de_Plantas_Potabilizadoras_Municipales_en_Operacion_Format.csv")

dataset

estado = dataset[dataset.Estado == "JALISCO"]

estado

municipio = estado[estado.Municipio == "Puerto Vallarta"]

municipio

df = pd.DataFrame(data=estado, columns = ['Nombre de la Planta','Proceso Potabilización'])

df_group = df.groupby("Proceso Potabilización").count()

df_group

df2 = pd.DataFrame(data = dataset, columns = ['Nombre de la Planta','Proceso Potabilización'])

df2_group = df2.groupby("Proceso Potabilización").count()

df2_group

df_group.plot()

df2_group.plot()

plt.figure(figsize = (15,3))
plt.plot(df_group)
plt.ylabel('Cantidad')
plt.xlabel('Proceso')
plt.title('Distribución en el estado de Jalisco')
plt.show()

plt.figure(figsize = (25,7))
plt.plot(df2_group)
plt.ylabel('Cantidad')
plt.xlabel('Proceso')
plt.title('Distribución en el Pais')
plt.show()

