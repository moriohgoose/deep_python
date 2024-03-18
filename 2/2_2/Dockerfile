# Используем официальный образ Python 3.11
FROM python:3.11-slim

# Устанавливаем LaTeX и необходимые пакеты для работы с изображениями
RUN apt-get update && apt-get install -y \
    texlive \
    texlive-latex-extra \
    texlive-fonts-recommended \
    imagemagick \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir --index-url https://test.pypi.org/simple/ hamster-latex-gen

# Копируем код в контейнер
COPY . /app
WORKDIR /app

# Запускаем скрипт для генерации LaTeX и компиляции в PDF
CMD ["python", "pdf_generator.py"]