# Use the latest Alpine Linux image as the base image
FROM alpine:latest

# Install Node.js and npm using apk
RUN apk add --no-cache nodejs npm

# Set the working directory to /code
WORKDIR /code

# Copy the Pipfile and Pipfile.lock to the working directory
COPY ./package.json .
COPY ./package-lock.json .

# Install the dependencies using npm
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Set the default command to run the application using Node.js
CMD ["npm", "run", "dev"]