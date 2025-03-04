#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es
import avl_tree as a
import cursos as cursos
import pandas as pd
from linked_queue import *
#Creamos los arboles

arbol_A = a.AVL()
arbol_B = a.AVL()
arbol_mezcla = a.AVL()
arbol_diferencias = a.AVL()

info_comun = []
info_agregada = []
info_a = []
info_b = []

#Extracción de datos

with open('ejA.txt','r',encoding='utf-8') as contenido1:
    datos_cursos_a = contenido1.read()

with open('ejB.txt','r',encoding='utf-8') as contenido2:
    datos_cursos_b = contenido2.read()



#Separamos los datos por líneas
datos_cursos_a = datos_cursos_a.split('\n') 
datos_cursos_b = datos_cursos_b.split('\n')

#Extraemos la información y vamos creando los obejetos de la clase curso
for line in datos_cursos_a:
    if len(line)>0:
        line = line.split(',')
        if len(line) == 6:
            name, dur, participantes, level, lang, precio = line
            curso = cursos.Curso(name, lang, dur, participantes, level, precio)
            print(curso)

            #Creamos un identificafdor para filtrar dentro del arbol y lo insertamos
            identificador = f'{curso.curso_name}_{curso.level}_{curso.lang}'
            arbol_A[identificador] = curso
            info_a.append(arbol_A[identificador].info_curso)


for line in datos_cursos_b:
    if len(line)>0:
        line = line.split(',')
        if len(line) == 6:
            name, dur, participantes, level, lang, precio = line
            curso = cursos.Curso(name, lang, dur, participantes, level, precio)
            
            #Creamos un identificafdor para filtrar dentro del arbol y lo insertamos
            identificador = f'{curso.curso_name}_{curso.level}_{curso.lang}'
            arbol_B[identificador] = curso
            info_b.append(arbol_B[identificador].info_curso)


a.preorder_indent_BST(arbol_A,arbol_A.root(),0)
print(len(arbol_A))
#print(arbol_A.dequeue())
#a.preorder_indent_BST(arbol_B,arbol_B.root(),0)

#Ahora para la oferta agregada y la común
for i in arbol_A:
    curso_actual = arbol_A[i]
    if i in arbol_B:
        curso_actual2 = arbol_B[i]
        if curso_actual2>curso_actual:
            curso = cursos.Curso(curso_actual.curso_name + '__B', curso_actual.lang, curso_actual.durac, curso_actual.participantes + curso_actual2.participantes, curso_actual.level, curso_actual.precio)
            #print(curso)
            identificador = f"{curso.curso_name}"
            arbol_mezcla[identificador] = curso
            arbol_diferencias[i] = curso
            info_agregada.append(arbol_diferencias[i].info_curso)
            info_comun.append(arbol_mezcla[identificador].info_curso)
        else:
            curso = cursos.Curso(curso_actual.curso_name  +'__A', curso_actual.lang, curso_actual.durac, curso_actual.participantes + curso_actual2.participantes, curso_actual.level, curso_actual.precio)
            #print(curso.curso_name)
            identificador = f"{curso.curso_name}"
            arbol_mezcla[identificador] = curso
            arbol_diferencias[i] = curso
            info_agregada.append(arbol_diferencias[i].info_curso)
            info_comun.append(arbol_mezcla[identificador].info_curso)
    else:
        identificador1 = f"{curso_actual.curso_name}_{curso_actual.level}_{curso_actual.lang + '__A'}"
        arbol_diferencias[i] = curso_actual
        info_agregada.append(arbol_diferencias[i].info_curso)
    for j in arbol_B:
        curso_actual2 = arbol_B[j]
        if (j not in arbol_A) and (j not in arbol_diferencias):
            identificador2 = f"{curso_actual2.curso_name}_{curso_actual2.level}_{curso_actual2.lang + '__B'}"
            arbol_diferencias[j] = curso_actual2
            info_agregada.append(arbol_diferencias[j].info_curso)


'''
for i in arbol_A:
    curso_actual = arbol_A[i]
    if i in arbol_B:
        curso_actual2 = arbol_B[i]
        identificador1 = f"{curso_actual.curso_name}_{curso_actual.level}_{curso_actual.lang +'_A' }"
        identificador2 = f"{curso_actual2.curso_name}_{curso_actual2.level}_{curso_actual2.lang +'_B'}"
        arbol_mezcla[identificador1] = curso_actual
        arbol_mezcla[identificador2] = curso_actual2
        '''


print(info_agregada)
print(info_comun)


columnas = ['Nombre', 'Idioma', 'Nivel', 'Duracion', 'Participantes', 'Precio','Beneficio', 'Ingresos']

df_a = pd.DataFrame(info_a, columns = columnas)
df_b = pd.DataFrame(info_b, columns = columnas)
df_u = pd.DataFrame(info_comun, columns = columnas)
df_i = pd.DataFrame(info_agregada, columns = columnas)
#a.preorder_indent_BST(arbol_mezcla,arbol_mezcla.root(),0)


#a.preorder_indent_BST(arbol_diferencias,arbol_diferencias.root(),0)


print(df_a,'\n')
print(df_b,'\n')
print(df_u,'\n')
print(df_i,'\n')


group_col = 'Idioma'
target_col = 'Participantes'
puntuation_per_director = df_a.groupby(group_col).agg({target_col :["mean"]})
print(puntuation_per_director, '\n')


group_col = 'Nivel'
target_col = 'Participantes'
puntuation_per_director = df_a.groupby(group_col).agg({target_col :["mean"]})
print(puntuation_per_director, '\n')


puntuation_per_director = df_a['Ingresos'].sum()
print(puntuation_per_director, '\n')


