# escribir en la terminal: python -m pip install matplotlib
import matplotlib.pyplot as plt

#Función para la gráfica de barras
def generate_bar_chart(labels,values):

    """#Crea los labels yvalues
    labels=['a','b','c']
    values=[100,200,50]"""

    #figura y ax es coordenadas
    fig,ax= plt.subplots()
    #diagrama de barras
    ax.bar(labels,values)
    #muestre la gráfica
    plt.show()


#Función para la gráfica de pastel
def generate_pie_chart(labels,values):
    fig,ax= plt.subplots()
    #diagrama de pastel, ojo con las reglas de la libreria
    ax.pie(values, labels=labels)
    #para que acomode la gáfica en el centro
    ax.axis('equal')
    #muestre la gráfica
    plt.show()

#ejecutarlo como script
if __name__ == '__main__':
    labels=['a','b','c']
    values=[500,200,50]
    generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)