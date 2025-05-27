#!/bin/bash

# Configuración de la base de datos
DB_NAME="gestion_porcina"
DB_USER="porcina_admin"
DB_HOST="localhost"
DB_PORT="5432"

# Configuración de backup
BACKUP_DIR="/home/$(whoami)/backups/postgres"
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/backup_${DB_NAME}_$DATE.sql"

# Crear directorio de backup si no existe
mkdir -p $BACKUP_DIR

# Realizar backup
echo "Iniciando backup de la base de datos $DB_NAME..."
pg_dump -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME > $BACKUP_FILE

# Comprimir el archivo
gzip $BACKUP_FILE

# Verificar si el backup se realizó correctamente
if [ $? -eq 0 ]; then
    echo "Backup realizado exitosamente: $BACKUP_FILE.gz"

    # Eliminar backups antiguos (mantener solo los últimos 7 días)
    find $BACKUP_DIR -name "backup_${DB_NAME}_*.sql.gz" -mtime +7 -delete
    echo "Backups antiguos eliminados"
else
    echo "Error al realizar el backup"
    exit 1
fi

# Opcional: Subir a almacenamiento en la nube (ejemplo con AWS S3)
# aws s3 cp $BACKUP_FILE.gz s3://mi-bucket-backups/postgres/
