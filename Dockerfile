# Use official Python image
FROM python:3.10

WORKDIR /opt

# Install Flask
RUN pip install --no-cache-dir flask

# Copy the application file
COPY app.py /opt/app.py

EXPOSE 5000

CMD ["python", "app.py"]
