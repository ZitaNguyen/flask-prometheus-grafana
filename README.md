# Project Name: **Flask App with Prometheus & Grafana**

This project demonstrates how to set up a **Flask web application** with **Prometheus** for monitoring and **Grafana** for visualization. It uses **Docker** for containerization.

## **Table of Contents**

- [Project Name: **Flask App with Prometheus \& Grafana**](#project-name-flask-app-with-prometheus--grafana)
  - [**Table of Contents**](#table-of-contents)
  - [**Project Overview**](#project-overview)
  - [**Setup \& Installation**](#setup--installation)
    - [**Clone the Repository**](#clone-the-repository)
    - [**Docker Setup**](#docker-setup)
    - [**Environment Configuration**](#environment-configuration)
  - [**Running the Application**](#running-the-application)
  - [**Accessing the Application**](#accessing-the-application)
    - [**Prometheus**](#prometheus)
    - [**Grafana**](#grafana)
  - [**Testing**](#testing)

## **Project Overview**

This project provides a simple **Flask** web application that exposes **Prometheus metrics** (such as HTTP request count and request duration) through the `/metrics` endpoint. Prometheus scrapes this endpoint to collect data, and Grafana is used to visualize these metrics.

The setup uses **Docker** for easy deployment and management of containers.

---

## **Setup & Installation**

### **Clone the Repository**

First, clone this repository to your local machine:

```sh
git clone https://github.com/yourusername/flask-prometheus-grafana.git
cd flask-prometheus-grafana
```

### **Docker Setup**

Ensure Docker and Docker Compose are installed on your machine. If Docker is installed correctly, you should be able to run:

```sh
docker --version
docker-compose --version
```

---

### **Environment Configuration**

You may want to update certain configurations, such as the **Prometheus scraping interval**. These configurations are located in the following files:

- **`prometheus.yml`** - Prometheus scraping configuration.
- **`docker-compose.yml`** - Docker Compose service configuration (Flask app, Prometheus, and Grafana).
- **`flask-app/`** - Your Flask application directory (for code updates).

---

## **Running the Application**

Once you've cloned the repository and set up the environment, run the following commands to start the entire stack:

```sh
docker-compose up -d
```

This will:

- Build the containers for the Flask app, Prometheus, and Grafana.
- Start the containers in detached mode (`-d`).

---

## **Accessing the Application**

### **Prometheus**

Once everything is up and running, you can access the Prometheus UI at:

```sh
http://localhost:9090
```

Prometheus will scrape the Flask app's `/metrics` endpoint for data.

### **Grafana**

Grafana's web interface will be available at:

```sh
http://localhost:3000
```

- **Login**: The default admin username is `admin` and the password is `admin`.
- **Prometheus Data Source**: Add it manually by going to **Connections** > **Data Sources** > **Add new data source** and setting the URL to `http://prometheus:9090`.

---

## **Testing**

To verify that everything is working as expected, follow these steps:

1. **Check Flask App Metrics**:  
   Open a browser and navigate to:

   ```sh
   http://localhost:5000/metrics
   ```

   You should see a list of metrics in the Prometheus format, such as:

   ```plaintext
   http_requests_total{method="GET",endpoint="/"} 3.0
   http_request_duration_seconds_count{endpoint="/"} 3.0
   ```

2. **Verify Prometheus Data**:  
   In the Prometheus UI at `http://localhost:9090`, run a query like:

   ```promql
   prometheus_http_requests_total
   ```

   You should see the data collected from your Flask app.

3. **Verify Grafana Dashboard**:  
   In Grafana at `http://localhost:3000`, navigate to **Explore** and choose Prometheus as the data source. You can choose to run a query like:

   ```promql
   prometheus_http_requests_total
   ```

   in **Metric** dropdown menu, and then visualize your metric!



