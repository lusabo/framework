# Escolha uma imagem base do Python
FROM python:3.12

# Ajustes de ambiente (opcional para não gerar bytecode, logs, etc.)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Cria diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos para dentro do container
COPY pyproject.toml /app/

# Instala dependências
RUN pip install --no-cache-dir -r pyproject.toml

# Copia todo o código do projeto para a pasta /app do container
COPY . /app/

# Exemplo de comando final (caso use Gunicorn ou outro server, ajuste aqui)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
