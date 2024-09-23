# Pull base image
FROM python:3.11

# Create work directory
WORKDIR /app

# Install poetry env, project dependency and model files
COPY poetry.lock pyproject.toml ./

COPY requirements.txt ./

RUN pip install --no-cache-dir poetry==1.7.1 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

RUN pip install -r requirements.txt

# Copy application files
COPY ./ ./

# Expose port and run application
EXPOSE 8000

# Define the command to run FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]