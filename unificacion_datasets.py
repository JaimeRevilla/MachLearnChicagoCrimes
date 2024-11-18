import pandas as pd

# Carga los dos datasets
df1 = pd.read_csv('datasets/Mercadona_Intervalo_1_Dataset.csv')  # Reemplaza con la ruta de tu archivo
df2 = pd.read_csv('datasets/Mercadona_Intervalo_2_Dataset.csv')  # Reemplaza con la ruta de tu archivo

# Verifica que las columnas sean las mismas
if list(df1.columns) == list(df2.columns):
    # Combina los datasets (unión de filas)
    df_combined = pd.concat([df1, df2], ignore_index=True)
    
    # Elimina duplicados si es necesario
    df_combined = df_combined.drop_duplicates()

    # Guarda el resultado en un nuevo archivo CSV
    df_combined.to_csv('datasets/dataset_unificado_mercadona.csv', index=False)

    print("Datasets unificados y guardados como 'dataset_unificado.csv'")
else:
    print("Los datasets tienen columnas diferentes. No se pueden unificar directamente.")
