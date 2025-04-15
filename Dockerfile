#Use an official Python runtime
FROM python:3.10-slim

#Set working directory
WORKDIR /app

#Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy the app
COPY . .

#Run the app
CMD ["python", "app.py"]
