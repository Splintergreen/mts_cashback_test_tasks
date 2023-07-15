#!/bin/bash

# Определяем текущий месяц
current_month=$(date +"%Y%m")

# Перебираем все архивы в директории ./log и заполняем Error.log
for file in ./log/smbp_${current_month}*.log.gz; do
  zcat "$file" | grep "Error" >> Error.log
done

echo "Файл Error.log успешно создан."
