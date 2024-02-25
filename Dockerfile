# Use the official Python image as the base image
FROM python:3.10.5-slim

# Set the working directory in the container
WORKDIR /wowdrobe-ai

# Copy the poetry files to the container
COPY pyproject.toml poetry.lock /wowdrobe-ai/
# Install poetry and project dependencies
RUN pip install poetry && poetry install

# Copy the rest of the application code to the container
COPY nutrisnap /wowdrobe-ai/

# Expose the port your Flask app will run on
EXPOSE 5000

# Command to run the application
CMD ["poetry", "run", "python", "app.py"]
