FROM python:3.10-slim-buster

# Create a non-root user
RUN useradd -ms /bin/bash movieverse

# Update and install dependencies
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y git build-essential

WORKDIR /bot
# Copy requirements file separately and install dependencies
COPY requirements.txt /bot/requirements.txt
RUN pip install --upgrade pip && pip install -U -r requirements.txt

COPY . .

# Set ownership of the application directory to the non-root user
RUN chown -R movieverse:movieverse /bot

# Switch to the non-root user
USER movieverse

CMD ["python3", "bot.py"]
