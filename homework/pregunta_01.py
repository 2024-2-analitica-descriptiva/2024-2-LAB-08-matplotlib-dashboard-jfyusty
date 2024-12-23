# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

# Importa las librerías necesarias para el manejo de datos y la creación de gráficos.
import pandas as pd # Importa la biblioteca pandas para manejo de datos.
import matplotlib.pyplot as plt # Importa la biblioteca matplotlib para crear gráficos.
import os # Importa la biblioteca os para manejo de rutas y directorios.

# Función para cargar datos desde un archivo CSV.
def load_data():
    df = pd.read_csv("files/input/shipping-data.csv") # Lee el archivo CSV y lo almacena en un DataFrame.
    return df # Devuelve el DataFrame.

# Función para crear un gráfico de barras de envíos por almacén.
def create_visual_for_shipping_per_warehouse(df):
    df = df.copy() # Crea una copia del DataFrame para evitar modificar el original.
    plt.figure() # Inicia una nueva figura
    counts = df.Warehouse_block.value_counts() # Cuenta la frecuencia de cada bloque de almacén.
    counts.plot.bar( # Crea un gráfico de barras.
        title = "Shipping per Warehouse", # Título del gráfico.
        xlabel = "Warehouse block", # Etiqueta del eje x.
        ylabel = "Record count", # Etiqueta del eje y.
        color = "tab:blue", # Color de las barras.
        fontsize = 8, # Tamaño de la fuente.
    )
    plt.gca().spines['top'].set_visible(False) # Oculta el borde superior del gráfico.
    plt.gca().spines['left'].set_visible(False) # Oculta el borde izquierdo del gráfico.
    plt.savefig('docs/shipping_per_warehouse.png') # Guarda el gráfico en un archivo.

# Función para crear un gráfico circular del modo de envío.
def create_visual_for_mode_of_shipment(df):
    df = df.copy() # Crea una copia del DataFrame para evitar modificar el original.
    plt.figure() # Inicia una nueva figura.
    counts = df.Mode_of_Shipment.value_counts() # Cuenta la frecuencia de cada modo de envío.
    counts.plot.pie( # Crea un gráfico circular.
        title = "Mode of shipment", # Título del gráfico.
        wedgeprops = dict(width=0.35), # Establece el ancho de los segmentos del gráfico circular
        ylabel = "", # Sin etiqueta para el eje y.
        colors = ["tab:blue", "tab:orange", "tab:green"], # Colores de los segmentos.
    )
    plt.savefig('docs/mode_of_shipment.png') # Guarda el gráfico en un archivo.

# Función para crear un gráfico de barras horizontales de la calificación promedio de los clientes.
def create_visual_for_average_customer_rating(df):
    df = df.copy() # Crea una copia del DataFrame para evitar modificar el original
    plt.figure() # Inicia una nueva figura.
    df = (
        df[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe() # Agrupa por modo de envío y calcula estadísticas descriptivas para las calificaciones de los clientes.
    )
    df.columns = df.columns.droplevel() # Elimina el nivel superior de las columnas del DataFrame.
    df = df[["mean", "min", "max"]] # Selecciona solo las columnas de media, mínima y máxima.
    plt.barh( # Crea un gráfico de barras horizontales.
        y = df.index.values, # Índice como etiquetas del eje y.
        width = df["max"].values - 1, # Anchura de las barras, ajustadas para representar el rango.
        left = df["min"].values, # Establece el valor mínimo como el inicio de las barras.
        height = 0.9, # Altura de las barras.
        color = "lightgray", # Color de las barras.
        alpha = 0.8, # Transparencia de las barras
    )
    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values # Colorea las barras según la media de las calificaciones.
    ]
    plt.barh( # Crea un segundo conjunto de barras para las calificaciones medias
        y = df.index.values,
        width = df["mean"].values - 1,
        left = df["min"].values,
        color = colors,
        height = 0.5,
        alpha = 1.0,
    )
    plt.title("Average Customer Rating") # Título del gráfico.
    plt.gca().spines['top'].set_visible(False) # Oculta el borde superior del gráfico.
    plt.gca().spines['left'].set_color("gray") # pinta el borde izquierdo de color gris del gráfico.
    plt.gca().spines['right'].set_visible(False) # Oculta el borde derecho del gráfico.
    plt.gca().spines['bottom'].set_color("gray") # pinta el borde inferior de color gris del gráfico.
    plt.savefig('docs/average_customer_rating.png') # Guarda el gráfico en un archivo.

# Función para crear un histograma de la distribución del peso de los envíos.
def create_visual_for_weight_distribution(df):
    df = df.copy() # Crea una copia del DataFrame para evitar modificar el original.
    plt.figure() # Inicia una nueva figura.
    df.Weight_in_gms.plot.hist( # Crea un histograma.
        title = "Shipped Weight Distribution",  # Título del gráfico.
        color = "tab:orange", # Color de las barras del histograma.
        edgecolor = "white", # Color del borde de las barras.
    )
    plt.gca().spines['top'].set_visible(False) # Oculta el borde superior del gráfico.
    plt.gca().spines['right'].set_visible(False) # Oculta el borde derecho del gráfico.
    plt.savefig('docs/weight_distribution.png') # Guarda el gráfico en un archivo.



def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    """
    Este código genera un gráfico que muestra cómo las personas obtienen sus noticias
     a lo largo del tiempo, usando diferentes colores y estilos de línea para 
     representar distintos medios de comunicación.
    
    Dependencias:
        - pandas
        - matplotlib.pyplot
        - os
    """

    if not os.path.exists("docs/"): # Verifica si el directorio 'docs' existe.
        os.makedirs("docs/") # Crea el directorio si no existe.

    df = load_data()
    create_visual_for_shipping_per_warehouse(df) # Crea y guarda el gráfico de envíos por almacén.
    create_visual_for_mode_of_shipment(df) # Crea y guarda el gráfico del modo de envío.
    create_visual_for_average_customer_rating(df) # Crea y guarda el gráfico de la calificación promedio de los clientes
    create_visual_for_weight_distribution(df) # Crea y guarda el histograma de la distribución del peso.

    # Crea contenido HTML para un dashboard simple.
    html_content = """
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Shipping Dashboard Example</h1>
            <div style="width:45%;float:left">
                <img src="shipping_per_warehouse.png" alt="Fig 1">
                <img src="mode_of_shipment.png" alt="Fig 2">
            </div>
            <div style="width:45%;float:left">
                <img src="average_customer_rating.png" alt="Fig 3">
                <img src="weight_distribution.png" alt="Fig 4">
            </div>
        </body>
    </html>
    """

    # Guarda el contenido HTML en un archivo.
    with open("docs/index.html", "w") as file:
        file.write(html_content) # Escribe el contenido HTML en el archivo.

# Llamar a la función para generar el dashboard
pregunta_01()
