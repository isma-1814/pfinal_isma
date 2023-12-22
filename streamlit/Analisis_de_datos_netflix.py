
import streamlit as st
import time

st.set_page_config(page_title='Análisis de datos Netflix', layout='wide',     page_icon="📈")
st.image('Netflix.png')

placeholder = st.empty()
with placeholder:
    #from PIL import Image
    #image = Image.open('mired.png')
    #placeholder.image(image, caption='MiRed semantic engine',use_column_width = 'always') 
    for seconds in range(5):
        placeholder.write(f"⏳ {seconds} Cargando sistema...")
        time.sleep(1)
placeholder.empty()


st.write("# Bienvenido al análisis de datos de películas y programas en Netflix 👋")

st.sidebar.success("Selecciona una página. Visualiza el dashboard interactivo o infórmate acerca del dataset de Netflix.")

st.markdown(
    """
    El conjunto de datos de Netflix TV Shows y Movies proporciona información completa sobre varios títulos disponibles en la popular plataforma de streaming.
    El conjunto de datos incluye detalles como el nombre del título, su tipo (ya sea un programa de televisión o una película), una breve descripción del contenido,
    el año en que se lanzó, calificación de certificación de edad, plazo de ejecución, puntuación IMDb y votos de IMDb.
    Al analizar este conjunto de datos, podemos obtener información sobre la distribución de las puntuaciones y calificaciones de IMDb tanto para programas de televisión como para películas disponibles en Netflix.
    Esta información puede ayudarnos a entender la popularidad y recepción de títulos basados en las calificaciones de los usuarios.
    
    Variables del dataset:
    
    Título: El nombre del programa de televisión o película. Esta columna contiene los títulos de varios programas de televisión y películas disponibles en Netflix.
    Puede utilizar esta información para identificar títulos específicos dentro del conjunto de datos.
    
    Tipo: Indica si la entrada es un programa de televisión o una película.La columna de tipo categoriza cada entrada como un programa de televisión o una película.
    Puedes filtrar tu análisis en base a estas categorías para centrarte en programas de televisión o películas específicamente.
    
    descripción: Una breve descripción del programa de televisión o película. La columna de descripción proporciona un resumen de la trama o historia de cada programa de televisión o película.
    Esta información puede ayudarle a obtener una visión general de lo que trata cada título antes de sumergirte en un análisis posterior más profundo.
    
    release-year: El año en que se estrenó el programa de televisión o la película. Esta columna indica el año de lanzamiento de cada título en formato numérico.
    Puede utilizar este punto de datos para examinar las tendencias a lo largo del tiempo agrupando y agregando títulos en función de sus años de lanzamiento.
    
    age-certificación: La calificación de certificación de edad para el programa de televisión o película.La columna de certificación de edad especifica las calificaciones de edad asignadas a cada título, indicando si son adecuados para audiencias generales (por ejemplo, todas las edades) o
    restringidas debido a contenidos para adultos (por ejemplo, R).
    El análisis de este atributo permite entender qué tipo de contenido ofrece Netflix a diferentes niveles de edad.
    
    runtime : La duración de los episodios para programas de televisión o duración para películas. La columna de tiempo de ejecución proporciona la duración de los episodios para programas de televisión o la duración de las películas en formato numérico.
    Esta información puede ayudarle a identificar títulos más cortos o más largos en función de su tiempo de ejecución y compararlos dentro de su análisis.
    
    Imdb.score: La partición del programa de televisión o película en IMDB. Esta columna muestra la puntuación IMDB asignada a cada título, representando su calidad y popularidad general en IMDB.
    Se puede usar esta métrica para evaluar y clasificar diferentes títulos basados en sus calificaciones, potencialmente descubriendo patrones o percepciones interesantes.
    
    Imdb.votes: El número de votos recibidos por programa de televisión o película.
    
    Gráficos:
    
    Analizar la distribución de las puntuales y calificaciones de IMDB para programas de televisión y películas en Netflix puede ayudar a identificar tendencias y patrones en las preferencias de audiencia.
    Esta información puede ser valiosa para los creadores de contenido y productores a la hora de decidir en qué tipos de espectáculos o películas invertir.
    
    Al examinar las calificaciones de certificación de edad, es posible analizar la audiencia objetivo para diferentes programas de televisión y películas en Netflix.
    Esta información puede ser útil para los anunciantes que quieren llegar a grupos demográficos específicos o para los padres que quieran tomar decisiones informadas sobre lo que sus hijos ven.
    
    Comparar las puntuales y los votos de IMDB a través de diferentes años de lanzamiento puede proporcionar información sobre cómo la calidad del contenido en Netflix ha evolucionado con el tiempo.
    Este análisis puede revelar cualquier cambio en las preferencias de audiencia o cambios en los estándares de la industria que han influido en las percepciones y opiniones de los espectadores.




"""
)
