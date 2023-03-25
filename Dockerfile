# Use Python 3.9 base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy required files
COPY requirements.txt .
COPY PavankumarAmazonScraper.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for web access
EXPOSE 80

# Run the program
CMD [ "python", "./PavankumarAmazonScraper.py" ]