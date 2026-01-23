<h2 align="center";">NoCountry H12-25-Equipo27-DataScience</h2>
<h2 align="center";">Proyecto de Predicción de Atrasos en Vuelos con Machine Learning</h2>

# Descripción
Este repositorio documenta el desarrollo de un proyecto colaborativo de ciencia de datos enfocado en la predicción de retrasos en vuelos, realizado por el equipo H12-25-L-Equipo 27 en el marco de la plataforma de simulación NoCountry.
El objetivo del proyecto es simular un entorno laboral real mediante el análisis y modelado de datos de vuelos, aplicando técnicas de machine learning para la predicción de retrasos y el estudio de los factores que los influyen.
El desarrollo se llevó a cabo principalmente utilizando Python y diversas librerías orientadas a la ciencia de datos y la extracción de información, como Pandas, NumPy, Scikit-learn, Requests, entre otras.

# Objetivo General
Desarrollar un producto mínimo viable (MVP) que permita predecir si un vuelo será puntual o sufrirá un retraso, a través del uso de técnicas de ciencia de datos y machine learning.

# Objetivos específicos
-	Analizar y comprender un conjunto de datos históricos de vuelos, identificando patrones y variables relevantes asociadas a los retrasos.
-	Realizar tareas de limpieza y preprocesamiento de datos, incluyendo el tratamiento de valores faltantes y la transformación de variables.
-	Diseñar y construir features relevantes
-	Entrenar y comparar modelos de clasificación supervisada para la predicción de retrasos de vuelos.
-	Evaluar el desempeño de los modelos utilizando métricas como Accuracy, Precision, Recall y F1-score.
-	Seleccionar el modelo con mejor desempeño y serializarlo para su posterior utilización.
-	Documentar el proceso de análisis, modelado y evaluación del modelo.

# Alcance del proyecto
-	El proyecto se limita al desarrollo de un modelo de clasificación binaria (Puntual / Retrasado).
-	El trabajo tiene un enfoque educativo y experimental, realizado en el contexto de una simulación de entorno laboral.

# Datos utilizados
Los datos fueron extraídos desde “kaggle”, tomando un dataset con alrededor de 540.000 registros y 9 columnas, tales como id, aerolínea, vuelo, origen, destino, día de la semana, tiempo, duración y retraso.

# Tecnología y herramientas
Para el desarrollo del proyecto se utilizó Google Colab como entorno de trabajo, empleando notebooks Jupyter y el lenguaje de programación Python.
Asimismo, se hizo uso de diversas librerías orientadas a la extracción, procesamiento y modelado de datos:
- Manipulación y análisis de datos:
  - Pandas
  - Numpy

- Machine Learning (scikit-learn):
Se utilizaron varios submódulos y funciones de scikit-learn para cubrir todo el flujo de modelado:
  - sklearn.model_selection: División de datos (Entrenamiento/prueba) y validación cruzada.
  - sklearn.preprocessing: Transformación y escalado de variables.
  - sklearn.impute: manejo de valores faltantes.
  - sklearn.calibration: calibración de probabilidades.
  - sklearn.ensemble: Modelo de clasificación Gradient Boosting.
  - sklearn.metrics: Metricas de evaluación del modelo:
    - accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report

- Serialización del modelo:
  - joblib

- Consumo de datos y manejo de solicitudes HTTP:
  - requests
  - requests.adapters
  - urllib3.util.retry

- Utilidades y manejo del sistema:
  - datetime
  - os
  - shutil
  - logging

# Metodología
Del dataset anteriormente mencionado, durante la limpieza de datos se eliminaron las columnas "id" y  "flight", además de crear ciertas variables como "hora de vuelo" y "día de la semana", para luego crear una nueva variable denominada "fecha_hora_clima", con el fin de obtener datos desde una API de clima (open-meteo) que nos brinden datos como son "temperatura", "velocidad del viento" y "visibilidad".

Para el entrenamiento del modelo se emplearon tanto variables numéricas como categóricas:

- Variables numéricas:
  - distancia_km
  - hora_decimal
  - temperatura
  - velocidad_viento
  - visibilidad

- Variables categóricas:
  - aerolinea
  - origen
  - destino
  - dia_semana
 
Las variables categóricas fueron transformadas utilizando One-Hot Encoding para permitir su uso en el modelo de machine learning. El dataset fue dividido en conjuntos de entrenamiento y prueba utilizando una proporción 80/20, garantizando una evaluación adecuada del desempeño del modelo sobre datos no vistos.

Se entrenó un modelo de Gradient Boosting utilizando la implementación GradientBoostingClassifier de scikit-learn. Durante esta etapa se realizó ajuste de hiperparámetros con el objetivo de mejorar el rendimiento predictivo del modelo.

El desempeño del modelo fue evaluado utilizando diversas métricas de clasificación, entre ellas:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- 
Asimismo, se generó un "classification report" para analizar de forma detallada los resultados obtenidos. Finalmente, el modelo entrenado fue serializado utilizando joblib, permitiendo su posterior carga y utilización en otros entornos o aplicaciones.

# Resultados



# Estructura del Repositorio
- `/data`: Datasets utilizados
- `/notebooks`: Notebooks de Jupyter/Colab (ej: análisis exploratorio).
- `/src`: Scripts Python reutilizables (ej: funciones de modelado).
- `/docs`: Documentación adicional (ej: planes, reportes).
- `/models`: Modelos guardados (ej: archivos .joblib).
- `/tests`: Pruebas unitarias.
- `/flight-delay-api`: Carpeta para el despliegue de la API Rest.

## Requisitos
- Python 3.11+
- Librerías: `pip install pandas scikit-learn joblib`

# Miembros del Equipo y Roles
- **NS** - Nicolas Serge Wolgan Staffelbach Henao - Machine Learning Operations
- **IC** - Ismael Cerda - Data Engineer
- **LJ** - Luis Jácome - Machine Learning Engineer
- **DA** - Degenhardt David Aragon Hueck - Data Analyst
- **EA** - Eduardo Ayala - Feature Architect

# Cómo Contribuir
1. Clona el repositorio: `git clone https://github.com/TuUsuario/nocountry-h12-25-equipo27-datascience.git`
2. Crea una branch: `git checkout -b feature/tu-tarea`
3. Trabaja y commitea: `git add .` y `git commit -m "Descripción"`
4. Push: `git push origin feature/tu-tarea`
5. Crea un Pull Request en GitHub para revisión.
6. Usa Issues para tareas pendientes.

# Integración con Google Colab
- Guarda notebooks en `/notebooks`.
- Exporta desde Colab directamente a GitHub.

Si tienes preguntas, usa el chat del equipo o crea un Issue.

¡Vamos equipo! 🚀
