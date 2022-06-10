lista1 =["codigo", 1123, "abril"]

lista2 = ["codigo", 1231, "abril"]

lista3 = ["otrocodigo", 1236, "febrero"]


#este objeto tendrías ya armado aunque funciona con lista o con lista de lista

lista=[lista1,lista2,lista3]
#acá va a ir a parar lo que queres sumar
agrupacion = []
def agrupar(lista):
    for i in lista:        
        if "abril" in i:
            #acá detectas lo referente a la lista que te va a indicar que tenes que capturar un valor para posteriormente agruparlo en base a eso
            agrupacion.append(i[1])
    
agrupar(lista)
#aca tendría la columna agrupada mediante el metodo sum()

valor_agrupado=(sum(agrupacion))
#armas una nueva lista en base a los items repetidos que ya conoces pero en la "columna" que querias que se agrupe le pones la variable que tiene guardado la suma de esa agrupación
lista_agrupada=[lista[0][0], valor_agrupado, lista[0][2]]

print(lista_agrupada)



