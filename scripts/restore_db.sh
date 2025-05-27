#!/bin/bash

# Verificar que se proporcione el archivo de backup
if [ $# -eq 0 ]; then
    echo "Uso: $0 <archivo_backup.sql.gz>"
    echo "Ejemplo: $0 /home/usuario/backups/postgres/backup_gestion_porcina_20250527_143000.sql.gz"
    exit 1
fi

BACKUP_FILE=$1

# Verificar que el archivo existe
if [ ! -f "$BACKUP_FILE" ]; then
    echo "Error: El archivo $BACKUP_FILE no existe"
    exit 1
fi

# Configuración de la base de datos
DB_NAME="gestion_porcina"
DB_USER="porcina_admin"
DB_HOST="localhost"
DB_PORT="5432"

echo "¿Estás seguro de que quieres restaurar la base de datos $DB_NAME?"
echo "Esto eliminará todos los datos actuales. (y/N)"
read -r response

if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    echo "Restaurando base de datos..."

    # Descomprimir el archivo si está comprimido
    if [[ $BACKUP_FILE == *.gz ]]; then
        echo "Descomprimiendo archivo..."
        gunzip -c $BACKUP_FILE | psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME
    else
        psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME < $BACKUP_FILE
    fi

    if [ $? -eq 0 ]; then
        echo "Restauración completada exitosamente"
    else
        echo "Error durante la restauración"
        exit 1
    fi
else
    echo "Restauración cancelada"
fi
