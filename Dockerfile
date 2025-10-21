FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
COPY main.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application
CMD ["python3", "-m", "main"]
