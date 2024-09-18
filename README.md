# Production Engineering Portfolio Site

# Portfolio Site

This is a portfolio website that showcases an individual's interests, experience, projects, and education. The site is powered by a **Flask** backend and styled with **HTML** and **CSS** for the frontend. It also includes **bash scripts** for automating the redeployment process using **Docker** for containerized services like **Nginx** and **MySQL**.

## Features

- **Flask Backend**: Handles dynamic content and routing.
- **HTML & CSS Frontend**: Provides a responsive and visually appealing user interface.
- **Bash Automation**: Automates deployment and testing tasks.
- **Docker-Compose**: Manages containers for Nginx, MySQL, and the Flask site.
- **System Monitoring**: Set up Prometheus and Grafana to monitor Docker containers, visualize metrics, and alert on potential issues.
- **Unit and Integration Testing**: Ensures stability before deploying updates.

## Requirements

Ensure the following are installed on your system:

- **Python 3.x**
- **Flask**
- **Docker**
- **Docker Compose**
- **Git**
- **MySQL**

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/k890m/portfoliosite
   cd porfoliosite
   ```

2. **Set Up Virtual Environment**:
   Create a Python virtual environment and install the required packages:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Access the Application**:
   Once the containers are up and running, the site will be available at `http://localhost`.

## Bash Scripts

The project includes several bash scripts for managing deployment and testing.

### Redeployment Script

To redeploy the site after pulling the latest changes from GitHub, use:

```bash
./redeploy.sh
```

This script pulls changes, runs unit and integration tests, and restarts the Docker containers. NOTE: If you choose to use Github actions you will be able to skip having to manually run this script.

### Testing

Unit and integration tests are automatically run as part of the redeployment process. You can also manually run the run_test.sh script.

```bash
./tests/run_test.sh
```

Ensure all tests pass before moving on.

## Docker Containers

The application uses Docker to manage services. The `docker-compose.yml` file defines the following containers:

- **Nginx**: Acts as a reverse proxy to handle web traffic.
- **MySQL**: Database service for storing site data.
- **Flask Application**: Serves the portfolio content.

You can stop the containers with:

```bash
docker-compose down
```

## Troubleshooting

If you encounter any issues, check the logs for the specific service:

```bash
docker logs <container_name>
```

Make sure all services are running properly by checking the Docker containers:

```bash
docker ps
```

If you have other issues try writing tests or debugging.

