areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12,
             "Habitació2", 12.23]
'''Imprimir el sgon elemente'''
print("El segon element es: ", areas_pis[1:2])
'''Imprimir l’últim element'''
print("L'ultim element es: ", areas_pis[13:])
'''Imprimir l’àrea de la terrassa'''
print("L'area de la terrassa es: ", areas_pis[7:8])
'''Imprimir del primer element al tercer element'''
print("Els elements del primer al tercer son: ", areas_pis[0:3])
'''Imprimir del tercer element a l’últim'''
print("Els elemnts del tercer a l'ultim son: ", areas_pis[2:])
'''Imprimir el total de l'àrea de les dues habitacions'''
total = areas_pis[5] + areas_pis[13]
print("L'area dels dues habitacions es: ", total)
'''Modificar l’àrea del lavabo i imprimir la nova list area'''
areas_pis[9] = 8.5
print(areas_pis)
'''Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.'''
areas_pis.append("pati interior")
areas_pis.append(2.78)
print(areas_pis)
'''Imprimir el total de l’àrea del pis.'''
total_area = sum(areas_pis[1::2])
print("L'area del pis es: ", total_area)
print(areas_pis)

