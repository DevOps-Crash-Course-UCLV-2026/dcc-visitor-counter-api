# Project: Visitor Counter API

## Overview
You are provided with a Python Flask application that interacts with a Redis database to track visitor counts. Your goal is to move away from local development patterns and transition into a production-ready cloud workflow. 

You will containerize the API, build a **GitHub Actions CI/CD pipeline** to automatically test and push your image to the **GitHub Container Registry (GHCR)**, and finally use **Docker Compose** to pull your remote image and orchestrate the full multi-container architecture.

---

## Requirements

### Phase 1: Dockerizing the Flask API
Create a `Dockerfile` for the provided `main.py`. The python version used is 3.7

### Phase 2: Orchestration with Docker Compose
Create a `docker-compose.yml` file in the root directory to define the following architecture:

1.  **Service: `web`**
    * Ensure it **depends on** the redis service.
2.  **Service: `redis`**

### Phase 3: CI/CD Pipeline (GitHub Actions)
Create your custom workflow file (`.github/workflows/visitor-pipeline-YOUR_USERNAME.yml`). This pipeline will automatically trigger on every `push` or `pull_request` to the `main` branch to validate your code and ship your image.

### Naming Convention Rule:
To prevent your pipeline from overriding or mixing up with your classmates workflows in the central repository, you **MUST** uniquely identify your pipeline:
1. Name your workflow file exactly: `.github/workflows/visitor-pipeline-YOUR_USERNAME.yml`
2. Set the internal YAML name property to: `name: Visitor Counter API - YOUR_USERNAME`
3. Tag your image using your username.

### Pipeline Stages & Rules:
* **Stage 1: Linting (CI)**
* **Stage 2: Security Scan (DevSecOps)**
* **Stage 3: Build & Publish (CD):** If stages 1 and 2 pass, the pipeline must automatically build your Docker image and push it to the **GitHub Container Registry (GHCR)**.

---

## How to Submit Your Work

1.  **Fork this Repository**
2.  **Clone Your Fork**
3.  **Develop a solution**
4.  **Commit & Push**
5.  **Submit a Pull Request (PR)**
