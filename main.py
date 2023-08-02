#Importar los módulos a utilizar
import utils
import read_csv
import charts

#Función para correr el archivo main
def run():
    #Ubicación de la data através del módulo para leer csv --> read_csv
    data = read_csv.read_csv('D:\pyapp/data.csv')

 #### DIAGRAMA DE PASTEL 

    #Filtrar southamerica porque el pastel se veía muy lleno
    data = list(filter(lambda item : item['Continent'] == 'South America',data))

    #Seleccionar la columna de los paises
    countries = list(map(lambda x: x['Country/Territory'],data))
    #Seleccionar la columna de los porcentajes
    percentages = list(map(lambda x: x['World Population Percentage'],data))
    #Generar diagrama de pastel
    charts.generate_pie_chart(countries, percentages)
    
#####


#####  DIAGRAMA DE BARRAS

    #Ingresar el país
    country = input('Type Country => ')

    #Llamar la función creada en utils que filtra el país
    result=utils.population_by_country(data,country)

    #Si el país seleccionado no existe la longitud de result sería vacía
    if len(result)>0:
        country=result[0]
        labels,values=utils.get_population(country)
        charts.generate_bar_chart(labels,values)
#####
 
    #print(result)


if __name__ == '__main__':
  run()