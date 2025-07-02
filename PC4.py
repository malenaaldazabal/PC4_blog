# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>¡Hola mundo! Esta es mi bitácora en programación 📝💻</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("foto_perfil.jpg", caption='¡Esta es una de mis fotos favoritas! Ese día visité TVPerú y aprendí sobre su programación cultural en lenguas originarias.', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = """
<p>¡Hola! Soy <strong>Malena Aldazabal</strong>, tengo <strong>19 años</strong> y soy de <strong>Lima, Perú</strong>.</p>

<p>Estudio <strong>Periodismo</strong> y actualmente voy en <strong>quinto ciclo</strong>. Elegí esta especialidad pues me permite seguir <strong>aprendiendo todo el tiempo</strong>, <strong>investigar</strong> y <strong>conocer nuevas cosas</strong>.</p>

<p>Lo que más me gusta de esta carrera es que es muy <strong>dinámica y adaptable</strong>. Me encanta <strong>escribir</strong>, <strong>tomar fotos</strong> y la <strong>comunicación oral</strong>, pero más allá de las herramientas, lo que realmente me motiva es poder <strong>dar visibilidad a historias</strong> que muchas veces no se cuentan; además de <strong>construir identidad y comunidad</strong>.</p>

<p>En el futuro, me gustaría hacer <strong>periodismo cultural</strong>, ya que me interesa cómo el <strong>arte</strong> y la <strong>cultura</strong> reflejan quiénes somos. También me atrae la <strong>gestión cultural</strong> y la <strong>comunicación corporativa</strong>.</p>

<p>En mi tiempo libre me gusta <strong>bailar marinera norteña</strong>, ver <strong>documentales históricos</strong> y <strong>escuchar música</strong>.</p>
"""

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Experiencia':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2 = """
    <p>Aprender a programar ha sido una experiencia <strong>desafiante</strong> pero muy <strong>enriquecedora</strong>. Al principio me daba <strong>miedo</strong>, porque nunca había hecho algo parecido. Pensaba que la programación era un mundo <strong>rígido</strong> y muy <strong>técnico</strong>, pero con el tiempo descubrí que no todo es tan cuadriculado en <strong>Python</strong>, un lenguaje que me ha sorprendido por su <strong>flexibilidad</strong> y sus <strong>posibilidades creativas</strong>.</p>
    <p>Programar me ha enseñado a <strong>pensar con más lógica</strong>, a ser <strong>paciente</strong> y a desarrollar formas de <strong>resolver problemas</strong>: dividirlos, probar, equivocarme y volver a intentar. Me ha hecho más <strong>perseverante</strong> y me ha demostrado que, aunque algo parezca difícil, siempre hay una forma de entenderlo si lo abordas <strong>paso a paso</strong>.</p>
    <p>Lo que más me gusta de programar es la <strong>sensación de transformar una idea en algo funcional</strong>. Disfruto mucho ese momento en que, después de varios intentos, todo encaja y el <strong>código finalmente corre bien</strong>. Además, me motiva saber que puedo usar la programación como una herramienta dentro de mi carrera: <strong>adaptar códigos</strong> según mis necesidades, <strong>automatizar procesos</strong> o <strong>desarrollar recursos propios</strong> me da más independencia, un plus como profesional y mayor <strong>autonomía</strong> para afrontar distintos proyectos.</p>
    <p>En el futuro, me gustaría usar la programación para <strong>enriquecer proyectos comunicacionales</strong> con <strong>datos</strong>, <strong>visualizaciones de gráficos</strong> y <strong>mapas</strong> o <strong>análisis automatizados</strong>, especialmente, en el ámbito de la <strong>comunicación digital</strong>. Creo que la tecnología puede ayudarnos a <strong>contar historias de forma más clara, atractiva y significativa</strong>, y me entusiasma seguir <strong>aprendiendo</strong> en ese camino.</p>
"""

# Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)


    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Videos explicativos que desarrollé en mis PC's 🎥</h2>", unsafe_allow_html=True)
    
    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://www.youtube.com/watch?v=X_Z7d04x9-E".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.

    # O creamos un botón para ir al enlace del video con button
    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1_0WoWoUvaCFNfnTEJhXfdF4A6Hjhyd5b/view?usp=drive_link' target='_blank'><button>Video de mi PC1</button></a></div>", unsafe_allow_html=True) 
    
    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1y3sntggeM69n7oglQA--pRDXj_U5vt6u/view?usp=drive_link' target='_blank'><button>Video de mi PC2</button></a></div>", unsafe_allow_html=True) 
    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Mi debut visual en Python</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Nube hashtags de la campaña #PiscoSpiritOfPeru', 'Gráfico de barras de películas y series estrenadas por año', 'Mapa interactivo de lenguas en Perú']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
        # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Nube hashtags de la campaña #PiscoSpiritOfPeru':
        st.image("grafico1.JPG", caption='Nube hashtags de la campaña #PiscoSpiritOfPeru', width=700)
        st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
        Este gráfico revela que los términos "marcaperu", "peru" y "piscospiritofperu" son los más grandes, lo que indica que fueron los más utilizados en los 14 videos analizados. Su tamaño refleja una estrategia centrada en vincular el producto con la identidad nacional y con la marca país, reforzando así el carácter patriótico de la campaña. También aparecen con un tamaño mediano hashtags como "piscosour" y "orgulloperuano", que fortalecen la asociación del pisco con el orgullo cultural peruano y con celebraciones reconocidas.
        <br><br>
        En contraste, otros hashtags aparecen con tamaño más pequeño, como "shakira", "bizarrap", "tumbo" o "diadelpiscosour", lo que indica un uso menos frecuente. Sin embargo, su inclusión sugiere una búsqueda de conexión con tendencias virales o elementos llamativos que puedan atraer a una audiencia más joven. La combinación de hashtags grandes, centrados en la identidad nacional, con otros más pequeños y actuales, apunta a una campaña que comienza a tratar de equilibrar lo cultural con lo popular para ampliar su alcance en TikTok.
    </div>
    """, unsafe_allow_html=True)
        pass
    elif grafico_seleccionado == 'Gráfico de barras de películas y series estrenadas por año':
        st.image("grafico2.JPG", caption='Gráfico de barras de películas y series estrenadas por año', width=700)
        st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
        El gráfico de barras muestra la cantidad de películas y series estrenadas por año, diferenciadas por color (verde para películas y naranja para series). Desde la década de 1980 se observa un crecimiento progresivo en la producción, que se acelera fuertemente a partir del año 2000, alcanzando su punto máximo entre 2017 y 2019, con más de 1000 estrenos anuales. Este aumento responde al auge de las plataformas de streaming, que han ampliado considerablemente la creación y distribución de contenido audiovisual a nivel global. Durante ese pico, las películas siguen siendo más numerosas, pero las series muestran un crecimiento cada vez más sostenido, lo que sugiere una transformación en los patrones de consumo.
        <br><br>
        En las primeras décadas del gráfico, la producción estuvo dominada casi exclusivamente por películas, mientras que las series eran escasas. Sin embargo, a partir de la segunda década del siglo XXI, las series aumentan visiblemente su presencia, acercándose cada vez más al volumen de películas estrenadas. Esta tendencia refleja el creciente interés del público por los contenidos seriados, impulsado por plataformas que privilegian este formato. Finalmente, entre 2020 y 2021 se observa una caída significativa en el número de estrenos para ambos tipos, atribuible a la pandemia de COVID-19. Aun así, la cantidad de producciones se mantiene muy por encima de los niveles históricos, consolidando un nuevo panorama en la industria audiovisual.
    </div>
    """, unsafe_allow_html=True)
        pass
    elif grafico_seleccionado == 'Mapa interactivo de lenguas en Perú':
    
        # Mostrar el HTML del mapa
        import streamlit.components.v1 as components
        with open("mapa_lenguas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        
        # Mostrar la interpretación del gráfico
        st.markdown("""
        <div style='text-align: justify; font-size: 16px;'>
            El mapa interactivo muestra la diversidad geográfica de lenguas originarias en el Perú, con marcadores distribuidos principalmente en la Amazonía, la región andina y algunas zonas costeras. Cada punto azul representa una lengua distinta, y al hacer clic o pasar el cursor sobre ellos se despliega el nombre de la lengua junto a su familia lingüística, como Quechuan, Arawakan, Zaparoan, entre otras. Esta representación permite visualizar la riqueza lingüística del país y destaca que muchas de estas lenguas se concentran en zonas rurales o de difícil acceso, lo cual refleja su fuerte vínculo con territorios ancestrales.
            <br><br>
            Además, el uso de clústeres de marcadores ayuda a comprender la densidad de lenguas en ciertas regiones, especialmente en la selva norte y centro del Perú. También se observa la coexistencia de lenguas en áreas específicas, lo que sugiere espacios de contacto e intercambio cultural. Este mapa no solo evidencia la variedad idiomática, sino también la necesidad de políticas públicas que protejan y revitalicen estas lenguas, muchas de las cuales están en peligro de desaparecer.
        </div>
        """, unsafe_allow_html=True)

        pass


    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)
    
