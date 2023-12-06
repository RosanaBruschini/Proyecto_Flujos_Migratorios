import streamlit as st
import requests
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Ruta de la imagen (usando una ruta relativa)
image_path = "latam.jpg"

import streamlit as st


# Ahora, crea el menú de radio
menu_option = st.sidebar.radio(
    "Menú", ["Home", "Acerca de nosotros", "Nuestro equipo", "Investigaciones destacadas", "Dashboard", "API", "Contactanos"]
)

# Agregar espacio entre el título y la imagen
st.write(" ")

# Crear una fila para el título y la imagen
title_col, image_col = st.columns([2, 1])

# Mostrar el título en la columna del título
#title_col.title("LATAMTIC | Data Science")
title_lines = ["**LATAMTIC** |", "**DATA SCIENCE**"]
# Mostrar el título en la columna del título con dos líneas
title_col.markdown(f"# {title_lines[0]}  \n{title_lines[1]}")

# Mostrar la imagen en la columna de la imagen
image_col.image(image_path, caption=" ", width=90)

# Contenido principal
if menu_option == "Home":
    st.markdown("<h1 style='color: blue;'>Portal de Análisis Migratorios de América Latina</h1>", unsafe_allow_html=True)
    st.write(""" Este portal se presenta como un producto que facilita de manera interactiva los datos recopilados, 
             sumado a la integración de un modelo predictivo desarrollado para proporcionar insights futuros. El 
             análisis revela desafíos significativos, como el aumento en la tasa de emigración y la disminución 
             del Producto Interno Bruto (PIB) per cápita. Estos resultados informan sobre la situación actual, como
             también sobre posibles tendencias futuras. 
             El enfoque de integración estratégica, contempla un Dashboard interactivo que a través del análisis de 
             indicadores clave de rendimiento (KPIs), se pretende generar una visión detallada de los factores 
             socioeconómicos que impulsan los patrones migratorios.
             El mantenimiento post-implementación garantiza la actualización continua de datos, permitiendo una 
             adaptación ágil a cambios en la dinámica migratoria.""")
    
    # Ruta del archivo GIF (usando una ruta relativa)
    gif_path = "DATAIMAGE.gif"
    # Mostrar el GIF
    st.image(gif_path, caption=" ")
    
elif menu_option == "Acerca de nosotros":
    st.markdown("<h1 style='color: blue;'>Acerca de nosotros</h1>", unsafe_allow_html=True)
    st.write(""" Somos una consultora especializada en Data Science, con una fuerte vocación por el análisis
             socioeconómico y geopolítico a nivel mundial. Durante diez años, hemos estado liderando el 
             mercado con soluciones innovadoras que trascienden las fronteras de la información y generan un
             impacto real en la toma de decisiones.  """)
    
    st.write("""En LATAM TIC, creemos en la transformación a través de los datos, y nuestro compromiso es 
             brindar la más alta calidad en investigación y análisis para impulsar el cambio y el desarrollo. 
             Nos enorgullece decir que hemos establecido una amplia trayectoria de éxito en el apasionante 
             campo de la analítica y la ciencia de datos, especialmente en el contexto latinoamericano.""")
    st.markdown("**Misión y Visión:**")
             
    st.write("""Nuestra Misión: Generar conocimiento basado en datos que empodere a las organizaciones y gobiernos
             para tomar decisiones informadas y efectivas.""")
             
    st.write("""Nuestra Visión: Ser un referente global en la generación de estudios socioeconómicos y geopolíticos, 
             impulsando un mundo más conectado y equitativo.""")
     # Ruta del archivo GIF (usando una ruta relativa)
    gif_path = "nosotros.gif"
    # Mostrar el GIF
    st.image(gif_path, caption=" ")
elif menu_option == "Nuestro equipo":
    st.markdown("<h1 style='color: blue;'>Nuestro Equipo</h1>", unsafe_allow_html=True)
    gif_path = "roles.jpg"
    # Mostrar el GIF
    st.image(gif_path, caption=" ")
    st.write("""En LATAM TIC, contamos con un equipo de expertos en datos y análisis de datos que lideran 
             la vanguardia en el campo de la ciencia de datos. Nuestros profesionales altamente calificados
             provienen de diversas disciplinas y aportan una amplia gama de habilidades y experiencias, lo 
             que nos permite abordar desafíos complejos desde múltiples perspectivas.
             Nuestra pasión por los datos y el compromiso con la excelencia nos impulsan a seguir innovando
             y ofreciendo soluciones impactantes. En LATAM TIC, creemos que los datos son la clave para un
             mundo mejor y más informado.""")
    # Ruta del archivo GIF (usando una ruta relativa)
    gif_path = "equipo.gif"
    # Mostrar el GIF
    st.image(gif_path, caption=" ")

elif menu_option == "Investigaciones destacadas":
    st.markdown("<h1 style='color: blue;'>Investigaciones Destacadas</h1>", unsafe_allow_html=True)
    # Ruta del archivo GIF (usando una ruta relativa)
    gif_path = "investigacion.gif"
    # Mostrar el GIF
    st.image(gif_path, caption=" ")
    st.markdown("**Proyecto:** Flujos migratorios  -  **Cliente:** Migrantes Unidos  - **Tipo de Empresa:** ONG")
    st.markdown("**[GitHub](https://github.com/LatamTIC/Proyecto_Flujos_Migratorios)**")

    
    gif_path = "Migrantes_unidos.png"
    # Mostrar el GIF
    st.image(gif_path, caption=" ", width=150)
    
    st.write("""
             El presente proyecto se centra en analizar y comprender los movimientos migratorios en la región de 
             América Latina, considerando el periodo desde el 2015 hasta el 2022. Nuestra labor de investigación 
             se enfoca en los países de Argentina, Venezuela, Colombia, Perú y El Salvador, con el propósito de 
             explicar este fenómeno a través de diversos indicadores.

             Para llevar a cabo esta tarea, hemos sido contratados por la renombrada organización no gubernamental 
             "Migrantes Unidos," que trabaja incansablemente en la defensa de los derechos de los migrantes en toda
             América Latina. Su misión es luchar por la justicia y la igualdad para todos los migrantes, y su 
             compromiso con el apoyo directo, la defensa de los derechos y la investigación profunda ha tenido un 
             impacto significativo en la región.

             En colaboración con "Migrantes Unidos," nuestro equipo de expertos se enfocará en comprender los procesos 
             migratorios desde múltiples perspectivas, contemplando factores económicos, sociales, culturales y otros
             indicadores clave. 

             Este proyecto no solo es un ejercicio de investigación, sino un paso hacia un mundo más inclusivo y 
             comprensivo, donde la migración sea segura y respetada. Buscamos aportar valiosos conocimientos que 
             beneficien a la región y a todas las personas que buscan una vida mejor lejos de sus lugares de origen. """)

    st.write("""**Objetivo Principal:**""") 
    st.write(""" Generar un análisis de los datos, de forma exhaustiva, con el fin de obtener hallazgos con información 
             clave, que permita generar un mejor estudio y entendimiento sobre los procesos migratorios, contemplando
             el nivel de influencia e impacto que generan los aspectos sociales y económicos en los 5 países 
             seleccionados de América Latina en el período 2015 - 2020, con el fin de brindar una comprensión completa
             sobre el fenómeno.
             """)
       
    
#  espacio 
    st.write(" ")
        
    st.markdown("**Diagrama de Flujos**")
    st.write("""Grafica la forma en la que los datos son procesados y transformados a medida que fluyen a través del sistema. 
             Facilitando el entendimiento de la lógica de procesamiento e identificación de los puntos de entrada y salida.""")
    # Ruta del archivo GIF (usando una ruta relativa)
    gif_path = "flujo_dato.jpg"
    # Mostrar el GIF
    st.image(gif_path, caption=" ")
    #  espacio 
    st.write(" ")
  
    
# Agrega esta parte para la opción "Dashboard"
elif menu_option == "Dashboard":
    st.markdown("<h1 style='color: blue;'>Dashboard</h1>", unsafe_allow_html=True)
     # Código para mostrar dashboard
    st.subheader("Proyecto: Flujos Migratorios")
    st.write("""Explora los flujos migratorios en América Latina a través del Dashboard interactivo. Visualiza
                tendencias, analiza patrones y mantenete actualizado con una herramienta esencial para 
                comprender y tomar decisiones informadas sobre el fenómeno migratorio en la región.""")
    # Cargar y mostrar el contenido del dashboard de Power BI
    #st.markdown('<iframe title="Report Section" width="800" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiY2IzNjg4NjMtNzVmYS00MDc1LTlkMjktY2Q0MmJhYTEyOTY4IiwidCI6IjFmODEwNTkyLTJiMTAtNGQyZi05ZDFkLWNhMzFiMjY5MTVkZSIsImMiOjR9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
    
    # Cargar y mostrar el contenido del dashboard de Power BI
    st.markdown('<iframe title="Report Section" width="800" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiYzJhYzM5ODctY2M4YS00ODBlLThiNWEtNTZkNDM5OTA3MTk0IiwidCI6IjFmODEwNTkyLTJiMTAtNGQyZi05ZDFkLWNhMzFiMjY5MTVkZSIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
    

# Crear el modelo de árbol de decisión fuera de la función
modelo_arbol = DecisionTreeClassifier(max_depth=4, min_samples_split=2, min_samples_leaf=3, max_features=None)

# Función para realizar la predicción
def predecir_emigracion(pib_anual, pib_per_capita, idh, esperanza_vida, muertes, tasa_mortalidad):
    
    # Cargar tus datos y entrenar el modelo
    df = pd.read_excel("MODELADO.xlsx")

    # 'EMIGRANTES' se convierte en clases 'bajo' y 'alto' según la mediana
    mediana = df['EMIGRANTES'].median()
    df['Clase_EMIGRANTES'] = df['EMIGRANTES'].apply(lambda x: 'alto' if x > mediana else 'bajo')

    # Dividir datos
    X = df[['PIB anual', 'PIB Per Capita', 'IDH', 'Esperanza de vida', 'Muertes', 'Tasa mortalidad']]
    y = df['Clase_EMIGRANTES']

    # Codificar etiquetas de clase
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Dividir los datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=178)

    # Entrenar el modelo
    modelo_arbol.fit(X_train, y_train)

    # Crear un nuevo conjunto de datos con los valores ingresados por el usuario
    nueva_prediccion_dict = {
        'PIB anual': [pib_anual],
        'PIB Per Capita': [pib_per_capita],
        'IDH': [idh],
        'Esperanza de vida': [esperanza_vida],
        'Muertes': [muertes],
        'Tasa mortalidad': [tasa_mortalidad]
    }

    nueva_prediccion = pd.DataFrame(nueva_prediccion_dict)

    # Realizar la predicción para los nuevos datos
    predicciones = modelo_arbol.predict(nueva_prediccion)

    # Mapear el resultado numérico a un texto descriptivo
    resultado_texto = 'Alta emigración' if predicciones[0] == 0 else 'Baja emigración'

    # Devolver la predicción y el texto descriptivo
    return predicciones, resultado_texto

# Contenido de la página API
if menu_option == "API":
    st.markdown("<h1 style='color: blue;'>API</h1>", unsafe_allow_html=True)
    st.write("""En este apartado podrás generar predicciones migratorias del país que se pretenda estimar, a partir de los 
                 datos ingresados. Los cuales, reflejan la situación migratoria expresada en alta o baja probabilidad 
                 (emigración e inmigración) de forma actualizada.""")
    st.image("code.gif", use_column_width=True)
    st.title("Predicción de Emigración") 
    
    # Obtener parámetros de entrada desde el usuario
    pib_anual = st.number_input("PIB Anual:", min_value=0)
    pib_per_capita = st.number_input("PIB Per Capita:", min_value=0)
    idh = st.number_input("IDH:", min_value=0.0, max_value=1.0, step=0.01)
    esperanza_vida = st.number_input("Esperanza de Vida:", min_value=0.0)
    muertes = st.number_input("Muertes:", min_value=0.0)
    tasa_mortalidad = st.number_input("Tasa de Mortalidad:", min_value=0.0)
    
    # Botón para realizar la predicción
    if st.button("**Realizar Predicción**"):
        # Llamar a la función de predicción con los parámetros ingresados
        resultado_prediccion, resultado_texto = predecir_emigracion(pib_anual, pib_per_capita, idh, esperanza_vida, muertes, tasa_mortalidad)
        #st.write("Resultado de la predicción (Numérico):", resultado_prediccion)
        st.write("Resultado de la predicción (Texto):", resultado_texto)

elif menu_option == "Contactanos":
    st.markdown("<h1 style='color: blue;'>Contactanos</h1>", unsafe_allow_html=True)
    # Código para mostrar información de contacto o formulario, según sea el caso
    st.subheader("Hola!. Dejnos tus consultas y comentarios 🚀")
    # Campos de entrada para el formulario
    nombre = st.text_input("**Nombre:**")
    email = st.text_input("**Correo Electrónico:**")
    consulta = st.text_area("**Consulta:**")

# Botón para enviar la consulta
    if st.button("**Enviar Consulta**"):
    # se almacena los datos en una base de datos.
     st.success(f"Consulta enviada:\nNombre: {nombre}\nCorreo Electrónico: {email}\nConsulta: {consulta}")
     st.subheader("**¡Gracias por contactarnos!**")
     st.write("""   """)
    
     


    






       




    

