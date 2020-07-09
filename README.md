# Urban Sounds Identification v1.0

Se presentan 3 Jupyter Notebooks diferentes.

0) Data Analysis: Se analizan los parámetros fundamentales referidos al formato de cada archivo de audio wav.
    - Número de canales.
    - Frecuencia de sampleo.
    - Profundidad de bits.

1) Preprocesamiento: Se seleccionan los valores únicos para el dataset de frecuencia de sampleo, profundidad de bits y número de canales. En esta versión, se utilizará un resampleo a 22050 Hz a partir de una ventana de Kaiser con B=15 y una frecuencia de cutoff de 0.95 de la frecuencia de Nyquist correspondiente.

- Se trabaja con los Coeficientes Cepstrales de las Frecuencias de Mel como feature principal a extraer de los archivos de audio. Se elige un número de Mels de salida para analizar los primeros resultados, quedando sujeto a modificaciones futuras.

- Se divide el dataset en train y test sets, usando el 20% para test.

2) Entrenamiento y Evaluación inicial del modelo:

- Se elige trabajar en primer lugar con un modelo sencillo (MLP), que contiene una capa de inputs, una de outputs y una capa oculta.
- Para las primeras 2 capas se utiliza una ReLU como función de activación, mientras que para la última capa se trabaja con Softmax, para lograr una representación de las distribuciones de probabilidad; entonces, el modelo hará sus predicciones basado en qué opción tiene mayor probabilidad.
- Se entrena el modelo utilizando 100 Epochs.
- Se realiza un testeo del modelo en función de su Accuracy (tanto para training-set como para test-set).
- Se valida el mismo a partir de predecir en sample data utilizada en el primer notebook, y en audios externos a los datasets presentados.
- El modelo MLP parece ser satisfactorio en general, generalizando de manera correcta ante nuevos datos que se le ingresan.

3) Evaluación final del modelo (CNN):

- En lugar de trabajar con un modelo MLP, se utiliza una red neuronal convolucional (CNN).
- Se trabaja con zero padding para ingresar datos de longitud fija a la red.
- Se entrena el modelo utilizando 70 epochs.
- Se obtiene un valor final de Accuracy de 94% para el training set y 89% para el test set (esto significa una mejora respecto del modelo anterior).
- El modelo generaliza correctamente y predice bien contra datos nuevos que se le ingresan.

Se propone mejorar el modelo para la versión 1.1, cambiando ciertos parámetros de preprocesamiento (frecuencia de sampleo, profundidad de bits, tipo de ventana) y también parámetros de la red neuronal (cantidad de nodos, dropout, funciones de activación, etc.).

