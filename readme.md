# Proyecto de Machine Learning: Predicción de Crímenes en Chicago

## 📌 Descripción
Este proyecto tiene como objetivo desarrollar un modelo de Machine Learning capaz de predecir el tipo de crimen más probable en una determinada ubicación y hora en la ciudad de Chicago. Utilizando datos históricos de crímenes reportados, el modelo busca optimizar la asignación de recursos policiales y mejorar estrategias de prevención.

📊 **Dataset utilizado:** [Crimes in Chicago - Kaggle](https://www.kaggle.com/datasets/currie32/crimes-in-chicago)

## 📁 Estructura del Repositorio
```
📂 crime_prediction_project
 ├── 📜 README.md  # Este archivo
 ├── 📜 documentacion_proyecto.pdf  # Documentación completa del proyecto
 ├── 📂 notebooks  # Jupyter Notebooks con el análisis y modelos
 │   ├── eda.ipynb  # Análisis exploratorio de datos (EDA)
 │   ├── preprocesamiento.ipynb  # Limpieza y transformación de datos
 │   ├── modelos.ipynb  # Entrenamiento y evaluación de modelos
 │   ├── mejora_modelos.ipynb  # Optimización de modelos
 ├── 📂 data  # Datos utilizados en el proyecto
 │   ├── crimes.csv  # Dataset original de Kaggle
 │   ├── crimes_clean.csv  # Dataset preprocesado
 ├── 📂 src  # Código fuente del proyecto
 │   ├── data_preprocessing.py  # Script para preprocesar datos
 │   ├── model_training.py  # Script para entrenar modelos
 │   ├── model_evaluation.py  # Evaluación de modelos
 ├── 📂 results  # Resultados obtenidos
 │   ├── confusion_matrix.png  # Matriz de confusión del mejor modelo
 │   ├── feature_importance.png  # Importancia de características
```

## ⚙️ Instalación y Configuración
Para ejecutar este proyecto en tu entorno local, sigue los siguientes pasos:

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/crime_prediction_project.git
cd crime_prediction_project
```

### 2️⃣ Crear un entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Descargar y preparar los datos
1. Descarga el dataset desde [Kaggle](https://www.kaggle.com/datasets/currie32/crimes-in-chicago) y guárdalo en la carpeta `data/`.
2. Ejecuta el script de preprocesamiento:
```bash
python src/data_preprocessing.py
```

### 4️⃣ Entrenar los modelos
```bash
python src/model_training.py
```

### 5️⃣ Evaluar los modelos
```bash
python src/model_evaluation.py
```

## 🔬 Modelos Implementados
Se entrenaron varios modelos supervisados y no supervisados para la predicción de crímenes:

### Modelos Supervisados:
- **Árboles de Decisión (Gini y Entropy)** 📊
- **Random Forest** 🌳
- **Gradient Boosting** 🔥 (mejor desempeño con 60% de precisión)
- **K-Nearest Neighbors (KNN)** 🔎
- **Redes Neuronales** 🧠 (mejorada hasta 60% de precisión)

### Modelos No Supervisados:
- **K-Means Clustering** 📌 (Índice de Silhouette: 0.19)

## 📊 Resultados Claves
- **Los crímenes más comunes**: Robo y daño a la propiedad.
- **Mayor incidencia**: Entre las 15:00 y 21:00 horas.
- **Días más peligrosos**: Viernes y sábados, con picos en verano.
- **Zonas con más delitos**: Distritos 11, 8 y 6.
- **Mejor modelo**: **Gradient Boosting** con 60% de precisión.

## 🚀 Mejoras Futuras
- Recolectar más datos externos (factores socioeconómicos, densidad poblacional, etc.).
- Implementar técnicas avanzadas para manejar el desbalance de clases (SMOTE, oversampling).
- Ajuste de hiperparámetros con técnicas más sofisticadas (Optuna, Grid Search).
- Uso de modelos más avanzados como Transformers o modelos de Series Temporales (LSTM, Prophet).

## 👨‍💻 Autores
- Ismael Alcaide
- Jaime Revilla
- Enrique Puente

📧 Para consultas, contáctanos en [tu_email@example.com](mailto:tu_email@example.com)

📝 **Licencia**: MIT License

