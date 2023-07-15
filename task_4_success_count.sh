#!/bin/bash

# Определяем сегодняшний день
today=$(date +%Y%m%d)

# Счетчик "Success"
total=0

# Подсчет количества "Success" в архивах
for file in ./log/smbp_${today}*.log.gz; do
    lines=$(zcat "$file" | grep -c "Success")
    total=$((total + lines))
done

echo "Количество успешных записей за сегодня($today): ${total}"
