nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def generar_estructura_alumnos (nombres, notas1, notas2):
    nombres = nombres.strip().split(",")
    noms=[nombre.replace("'","").replace("\n","").strip()for nombre in nombres]
    return zip(noms, notas1,notas2)

def notas_promedio_alumnos (alumnos):
    promedio= lambda x,y: (x+y)/2
    promedio_alumnos = {}
    for alumno, nota1, nota2 in alumnos:
        promedio_alumnos[alumno]=promedio(nota1, nota2)
    return promedio_alumnos

import functools
def promedio_general_del_curso (promedio_alumnos):
    sumar = lambda x,y: x+y
    return (functools.reduce(sumar, promedio_alumnos.values()))/len(promedio_alumnos)

def alumno_promedio_mayor (promedio_alumnos):
    return (sorted(promedio_alumnos.items(), key = lambda item:item[1], reverse=True)[:1])[0][0]

def alumno_nota_mas_baja (alumnos):
    alumnos_notas_mas_bajas = {}
    for alumno, nota1, nota2 in alumnos:
        alumnos_notas_mas_bajas[alumno]=nota1 if (nota1<nota2) else nota2
    return (sorted(alumnos_notas_mas_bajas.items(), key = lambda item:item[1])[:1])[0][0]

if __name__ == "__main__":
    alumnos = list(generar_estructura_alumnos(nombres, notas_1,notas_2))
    promedio_alumnos = notas_promedio_alumnos(alumnos)
    print(f"El promedio general del curso es de: {promedio_general_del_curso(promedio_alumnos):.2f}")
    print(f"El alumno que mayor nota promedio tiene es {alumno_promedio_mayor(promedio_alumnos)}")
    print(f"El alumno que tiene la nota más baja es {alumno_nota_mas_baja(alumnos)}")