#!/bin/bash

echo "Создать директорию ./log и заполнить ее архивами типа smbp_DATE_TIME_appNUM.log.gz? (y/n)"
read answer

if [[ $answer =~ ^[Yy]$ ]]; then
    if [ -d "log" ]; then
        echo "Директория log уже существует!"
        exit
    fi

    mkdir -p ./log
    cd ./log

    # Генерация архивов
    for i in {0..100}; do
        date=$(date -d "${i} days ago" +%Y%m%d)
        time=$(date -d "$((i*15)) sec ago" +%H%M%S)

        file_name="smbp_${date}_${time}_app${i}.log"

        # Добавление строки c "Error" или "Success"
        if [[ $((i%2)) -eq 0 ]]; then
            content="This is a test log${i} file. Success!"
        else
            content="This is a test log${i} file. Error!"
        fi

        # Запись в файл
        echo "$content" > "$file_name"

        # Архивация и удаление файла
        gzip  $file_name

    done

echo "Папка log с архивами успешно создана!"

else
    exit
fi
