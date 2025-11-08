# 📨 Celery + RabbitMQ + Redis (Dockerized Message Queue Demo)

A practical **DevOps mini-project** demonstrating how to build an **asynchronous task processing system** using **Celery**, **RabbitMQ**, and **Redis**, all running in **Docker containers**.

This setup helps you understand how distributed systems handle background jobs, message queues, and decoupled workloads in production environments.

---

## 🚀 Overview

This project demonstrates how backend services can:
- Queue background jobs instead of executing them synchronously.
- Decouple task submission from execution.
- Use **Celery** as a task queue framework.
- Use **RabbitMQ** as the **message broker**.
- Use **Redis** as the **result backend** to store task outcomes.

---

## 🧠 Architecture

```
Python App (Producer)
        ↓
   RabbitMQ (Broker)
        ↓
Celery Worker (Consumer)
        ↓
   Redis (Result Backend)
```

| Component | Role |
|------------|------|
| 🐇 **RabbitMQ** | Acts as the **message broker** that queues and routes tasks. |
| ⚙️ **Celery Worker** | Processes background tasks asynchronously. |
| 🧰 **Redis** | Stores task results and states. |
| 🐍 **Python App** | Sends tasks to the queue and retrieves results. |

---

## 🧱 Project Structure

```
mq-demo/
│
├── docker-compose.yml        # Container orchestration
└── app/
    ├── Dockerfile            # Python app container
    ├── requirements.txt      # Python dependencies
    ├── tasks.py              # Celery config & tasks
    └── producer.py           # Example producer script
```

---

## ⚙️ Setup Instructions

### 1️⃣ Start the environment
```bash
docker compose up --build
```

This will start the following containers:

| Service | Description | Port |
|----------|--------------|------|
| `rabbitmq` | Message broker with web UI | **15672** |
| `redis` | Stores Celery task results | **6379** |
| `celery_worker` | Background task processor | — |
| `python_app` | Interactive container for sending tasks | — |

---

### 2️⃣ Access RabbitMQ Dashboard

- URL → [http://localhost:15672](http://localhost:15672)  
- Username → `guest`  
- Password → `guest`  

Go to **Queues → celery** to see tasks being queued and consumed in real time.

---

### 3️⃣ Run a Task Manually

Once all containers are up:
```bash
docker exec -it python_app bash
```

Then inside the container:
```bash
python producer.py
```

Expected output:
```
Sending task...
Task ID: 0fdcfdbf...
Waiting for result...
Result: 30
```

---

## 🧠 Understanding the Flow

| Step | Description |
|------|--------------|
| 1️⃣ | The Python app sends a Celery task to RabbitMQ. |
| 2️⃣ | RabbitMQ queues the task safely until a worker is ready. |
| 3️⃣ | Celery worker consumes the task and executes it asynchronously. |
| 4️⃣ | The worker stores the result in Redis. |
| 5️⃣ | The app retrieves the result using the task ID. |

---

## 📊 Observability

### 🪶 RabbitMQ Management UI
- Visualize queues, message rates, and acknowledgments.
- Monitor message flow between producers and consumers.

### 🧱 Redis (Check Task Results)
Inspect stored results directly from Redis:
```bash
docker exec -it redis redis-cli
keys *
get celery-task-meta-<task_id>
```

You’ll see something like:
```json
{"status": "SUCCESS", "result": 30, "traceback": null}
```

### 🧾 Celery Worker Logs
Tail the worker logs to view task execution in real time:
```bash
docker logs -f celery_worker
```

---

## 🧰 Tools & Technologies

- **Python 3.10**
- **Celery**
- **RabbitMQ** (Message Broker)
- **Redis** (Result Backend)
- **Docker & Docker Compose**

---

## 🧹 Cleanup

To stop and remove all containers, networks, and volumes:
```bash
docker compose down -v
```

---

## 🧩 Learning Objectives

✅ Understand how message queues decouple services.  
✅ Learn asynchronous task handling with Celery.  
✅ Observe message flow between producers and consumers.  
✅ Practice containerized orchestration with Docker Compose.  
✅ Explore result storage using Redis.

---

## 💡 Optional Enhancements

- Add a **Flask API** to trigger tasks via REST (`/run-task`, `/status/<id>`).  
- Integrate **Flower** for real-time Celery monitoring (`http://localhost:5555`).  
- Deploy to **Kubernetes** or **AWS ECS**.  
- Add **Prometheus + Grafana** for metrics and queue insights.  

---

## 🧠 Real-World Use Cases

- Asynchronous email or notification sending  
- Image/video processing pipelines  
- Report generation and scheduled jobs  
- ETL (Extract, Transform, Load) data workflows  
- Microservice communication patterns  

---

## 👨‍💻 Author

**Jayant Danech**  
Senior Cloud, DevOps & SysOps Engineer  

> A practical demonstration of asynchronous message queuing and distributed task processing using Celery, RabbitMQ, and Redis — for learning and DevOps practice.

