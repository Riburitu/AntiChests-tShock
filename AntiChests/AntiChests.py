# SPANISH

# Esté código limpia los cofres duplicados desde la base de datos InfChests3.sqlite el cual se provoca por un bug al crear las IDs de los cofres.
# El cual los reposiciona en una misma posición y esto se duplica así exponencialmente. Asimismo, se reasigna la secuencia de IDs para que no se repitan al final.
# Si estas utilizando esté programa, asegúrate de crear una copia de seguridad de tu base de datos antes de ejecutarlo, ya que podrías remplazar y perder datos permanentemente.

# ENGLISH

# This code cleans the duplicated chests in the InfChests3.sqlite database, which is caused by a bug when creating the chest IDs.
# It repositions them in the same position, and this duplicates exponentially. Additionally, it reassigns the ID sequence to prevent future duplicates.
# If you are using this program, make sure to create a backup of your database before running it, as you may overwrite and lose data permanently.

import sqlite3
import pandas as pd
import os

INPUT_DB = "InfChests3.sqlite"
OUTPUT_DB = "InfChests3_clean.sqlite"
TABLE_NAME = "InfChests3"
SECUENCIA_DESEADA = 22265

def limpiar_cofres_y_fijar_sequence(input_db, output_db):
    if not os.path.exists(input_db):
        print(f"File no found: {input_db}")
        return

    print("Open SQL...")
    conn = sqlite3.connect(input_db)
    df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME}", conn)

    print(f"Input originals: {len(df)}")
    df = df.sort_values(by="ID", ascending=False)
    df_clean = df.drop_duplicates(subset=["X", "Y"], keep="first")

    print(f"Inputs post clean: {len(df_clean)}")

    # Reasigna los IDs secuenciales.
    df_clean = df_clean.sort_values(by=["X", "Y"]).reset_index(drop=True)
    df_clean["ID"] = df_clean.index

    print("Save SQL...")
    conn_clean = sqlite3.connect(output_db)
    df_clean.to_sql(TABLE_NAME, conn_clean, if_exists="replace", index=False)

    cursor = conn_clean.cursor()
    try:
        cursor.execute("SELECT seq FROM sqlite_sequence WHERE name = ?", (TABLE_NAME,))
        result = cursor.fetchone()
        if result:
            cursor.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ?", (SECUENCIA_DESEADA, TABLE_NAME))
        else:
            cursor.execute("INSERT INTO sqlite_sequence (name, seq) VALUES (?, ?)", (TABLE_NAME, SECUENCIA_DESEADA))
        conn_clean.commit()
        print(f"Sequence follow: following ID is {SECUENCIA_DESEADA + 1}")
    except sqlite3.OperationalError:
        print("⚠️ The board 'sqlite_sequence' not exists. It's possible not found the AUTOINCREMENT.")

    conn.close()
    conn_clean.close()
    print(f"SQL cleaned. Saved as '{output_db}'.")

if __name__ == "__main__":
    limpiar_cofres_y_fijar_sequence(INPUT_DB, OUTPUT_DB)
