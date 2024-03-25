# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /webapp

# Copy the current directory contents into the container at /app
COPY . /webapp

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=django_blog.settings

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
