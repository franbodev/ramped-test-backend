# Python FastAPI MongoDB Auth Project

This project is a Python-based test implementation that uses FastAPI, MongoDB. It's containerized with Docker Compose for easy deployment.

## Description

This project employs the following technologies:

1. **FastAPI Backend:**

    - FastAPI is a modern, high-performance web framework for building APIs with Python.
    - The backend handles HTTP requests, data processing, and communicates with MongoDB.

2. **MongoDB:**
    - MongoDB is a NoSQL database that stores data in a flexible, JSON-like format.
    - It's used to persist and manage the application's data, supporting structured and unstructured data storage.

## Software Requirements

To run this project, you need the following software:

1. **Operating System:** Windows, Linux, macOS
2. **Docker and Docker Compose**

## How to Run this Project

1. Clone the Git repository:

    ```bash
    git clone gitlink
    ```

2. Create a `.env` file with the following content:

    ```ini
    ENV="dev"
    DB_URL="mongodb://root:example@mongo:27017/"
    DB_USERNAME=root
    DB_PASSWORD=example
    DB_NAME=test
    BACKEND_URL="http://api:8080"
    ACCESS_TOKEN_EXPIRES_IN=15
    REFRESH_TOKEN_EXPIRES_IN=1440
    JWT_ALGORITHM=RS256
    CLIENT_ORIGIN=http://localhost:3000
    JWT_PRIVATE_KEY=<Your JWT Private Key Here>
    JWT_PUBLIC_KEY=<Your JWT Public Key Here>
    ```

    Replace `<Your JWT Private Key Here>` and `<Your JWT Public Key Here>` with your actual JWT keys.

3. Run the Docker Compose file:

    ```bash
    docker-compose up -d --build
    ```

    This command will build and run Docker images for the services defined in the `docker-compose.yaml` file.

    - Access the Streamlit UI at: [http://localhost:8501](http://localhost:8501) on your local machine.

    - If you want to view the database, you can install [MongoDB Compass](https://www.mongodb.com/products/tools/compass) and use the following connection string:

        ```ini
        mongodb://root:example@<Your local IPv4 address>:27017/
        ```

4. Import Data into MongoDB:

    Download CSV file from https://docs.google.com/spreadsheets/d/1b0c1fbBuq4WNejtBi6IdPodOx74BG2-VwI1nGbyPHck/edit?usp=sharing.

    And import the csv into Jobs collection in MongoDb

That's it! You can now explore and customize this boilerplate code to add your own logic and features. Enjoy working with this project!
