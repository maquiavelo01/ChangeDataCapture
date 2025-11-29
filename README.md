# 🔄 Polyglot Persistence & Data Replication Pipeline

![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Orchestration-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Source-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Target-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

## 📖 Overview
This project implements a **Multi-Database Replication Architecture** designed to simulate real-world data synchronization challenges. It uses **Python** as an orchestration layer to manage the lifecycle of four different containerized databases (MySQL, MongoDB, Redis, Cassandra) and establishes a data pipeline that replicates transactional data (OLTP) to a document store (NoSQL).

The core logic demonstrates a custom **Change Data Capture (CDC)** pattern, where time-series data is ingested into a relational source (MySQL) and synchronized near real-time with a downstream MongoDB instance for analytics.

## 🏗️ Architecture
The system relies on a central scheduler that coordinates data flow between containerized services.

```mermaid
graph TD
    subgraph Infrastructure [Docker Containers]
        MySQL[(MySQL Source)]
        Mongo[(MongoDB Target)]
        Redis[(Redis Cache)]
        Cassandra[(Cassandra Store)]
    end

    subgraph Orchestrator [Python Automation]
        Scheduler[scheduler.py]
        ContainerMgr[container.py]
    end

    ContainerMgr -->|Spins Up| MySQL
    ContainerMgr -->|Spins Up| Mongo
    
    Scheduler -->|Write Timestamp| MySQL
    Scheduler -->|Read Delta| MySQL
    Scheduler -->|Replicate| Mongo
    Scheduler -->|Verify Consistency| Mongo
````

## 🚀 Key Features

  * **Automated Infrastructure:** Python scripts (`my_sql_container.py`, `my_mongo_container.py`) that programmatically spin up, initialize, and tear down Docker containers.
  * **Polyglot Persistence:** Simultaneous management of Relational (MySQL), Document (MongoDB), Key-Value (Redis), and Wide-Column (Cassandra) stores.
  * **Data Replication Loop:** A threaded scheduler (`scheduler.py`) that:
    1.  Generates synthetic data (Time Stamps + UUIDs) in MySQL.
    2.  Reads the latest commits.
    3.  Upserts data into MongoDB to ensure eventual consistency.
  * **Self-Healing/Verification:** Automatic checks to ensure data written to the source appears correctly in the destination.

## 🛠️ Tech Stack

  * **Orchestration:** Python (Threading, Subprocess)
  * **Containers:** Docker API / CLI
  * **Databases:**
      * **MySQL 8.0:** Primary transactional store.
      * **MongoDB 4.4:** Analytical/Document store.
      * **Redis & Cassandra:** Integrated for caching and scaling scenarios.
  * **Libraries:** `pymysql`, `pymongo`, `cassandra-driver`, `redis-py`

## 📂 Project Structure

All files are located in the root directory for ease of execution.

```text
├── container.py            # Master controller: creates/deletes all DB containers
├── scheduler.py            # Main loop: writes, replicates, and verifies data
├── mysqldb.py              # MySQL Data Access Object (DAO) for writes/reads
├── mongodb.py              # MongoDB Data Access Object (DAO) for replication
├── my_sql_container.py     # MySQL container lifecycle management
├── my_mongo_container.py   # MongoDB container lifecycle management
├── my_redis_container.py   # Redis container lifecycle management
├── my_cassandra_container.py # Cassandra container lifecycle management
└── README.md               # Project documentation
```

## 💻 Getting Started

### 1\. Prerequisites

  * **Docker Desktop** running.
  * **Python 3.x** installed.
  * Pip requirements:
    ```bash
    pip install pymysql pymongo cassandra-driver redis
    ```

### 2\. Infrastructure Setup

You can bring up the entire stack using the master controller. This script orchestrates the individual container scripts.

```bash
# Create all containers (MySQL, Mongo, Redis, Cassandra)
python container.py -create

# Initialize schemas (Tables/Collections)
python container.py -init
```

*Note: This command triggers the individual `my_*_container.py` scripts to pull images and bind ports (MySQL: 5600, Mongo: 1800).*

### 3\. Running the Replication Pipeline

Start the main scheduler loop. This will begin writing data to MySQL and replicating it to MongoDB every 5 seconds.

```bash
python scheduler.py
```

**Expected Output:**

```text
--- LOOP: Sat Nov 29 12:00:01 2025 ---
Data in mysql:
2025-11-29 12:00:00
...
Data in mongo:
2025-11-29 12:00:00
```

### 4\. Cleanup

To stop and remove all containers:

```bash
python container.py -delete
```

## 👤 Author

**José Antonio Morfín Guerrero**

  * Digital Transformation Leader | Data Engineer
  * [LinkedIn](https://www.google.com/search?q=https://linkedin.com/in/joseantoniomorfinguerrero)
  * [Portfolio](https://joseantoniomorfin.name)

<!-- end list -->

```
```
