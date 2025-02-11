# Use Python Base Image
FROM python:3.9
# Set working directory
WORKDIR /app 
COPY . /app
# Install Flask
RUN pip install flask
# Expose port
EXPOSE 5001
# Run the application
CMD ["python", "app.py"]