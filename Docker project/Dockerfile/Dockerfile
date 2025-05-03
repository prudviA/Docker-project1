#Base image
FROM python:3.10-slim

#set working directory
WORKDIR /app

#Copy application and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app.

#Expose port and run app
Expose 5000
CMD ["python", "app.py"]