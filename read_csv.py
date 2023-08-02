#importar para poder manejar csv
import csv


#función para obtener la ubicación del archivo
def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        
        #extraer encabezados
        header=next(reader)
        
        #crear lista para retornar diccionarios
        data=[]


        #leer fila a fila
        for row in reader:
            #Unir encabezado con contenido cada fila en una tupla
            iterable=zip(header,row)

            #Crear diccionario con comprhension
            country_dict={key:value for key,value in iterable}
            #print(country_dict)

            #agregara cada línea de diccionario en la lista de arriba
            data.append(country_dict)
        return data


#Para correrlo como un script desde la terminal
if __name__=='__main__':
    data=read_csv('D:\pyapp/data.csv')
    #print(data)
    print(data[2])