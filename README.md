# Urban Sounds Identification v1.0

Se presentan 3 Jupyter Notebooks diferentes.

0) Data Analysis: Se analizan los parámetros fundamentales referidos al formato de cada archivo de audio wav.
    - Número de canales.
    - Frecuencia de sampleo.
    - Profundidad de bits.

1) Preprocesamiento: Se seleccionan los valores únicos para el dataset de frecuencia de sampleo, profundidad de bits y número de canales. En esta versión, se utilizará un resampleo a 22050 Hz a partir de una ventana de Kaiser con B=15 y una frecuencia de cutoff de 0.95 de la frecuencia de Nyquist correspondiente.

- Se trabaja con los Coeficientes Cepstrales de las Frecuencias de Mel como feature principal a extraer de los archivos de audio. Se elige un número de Mels de salida para analizar los primeros resultados, quedando sujeto a modificaciones futuras.

- Se divide el dataset en train y test sets, usando el 20% para test.

2) Entrenamiento del modelo:
