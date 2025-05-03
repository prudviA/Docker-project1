#Base Image
FROM python:3.10-slim

#Set working directory
WORKDIR /app

#Copy application and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app .

# Expose port and run app
EXPOSE 5000
CMD ["python", "app.py"]