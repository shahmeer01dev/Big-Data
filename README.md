# Hadoop HDFS CRUD Operations with Docker

This project demonstrates how to set up a **multi-node Hadoop Distributed File System (HDFS)** cluster using **Docker Compose**.
It includes a **Python script** that runs within a Docker container to perform basic **Create, Read, Update, and Delete (CRUD)** operations on the HDFS cluster — showcasing a complete, containerized big data workflow.

This setup is designed to solve common Docker networking challenges between a client application and a Hadoop cluster by running all components on the same Docker network.

---

## Technologies Used

* **Docker & Docker Compose** – For containerizing and orchestrating the Hadoop cluster and the Python client.
* **Hadoop (HDFS)** – The distributed file system for storing data.
* **Python** – Used for the client application to interact with HDFS.
* **`hdfs` Python Library** – A Python client for WebHDFS that allows communication with the HDFS REST API.

---

## Structure

```
/
├── docker-compose.yml   # Defines the Hadoop and Python client services
├── Dockerfile           # Builds the Python client container
├── main.py              # Python script with HDFS CRUD operations
└── .gitignore           # Specifies files for Git to ignore
```

---

## How to Run This Project

### Prerequisites

* Docker Desktop installed and running on your system.

---

### Step-by-Step Instructions

#### Clone the Repository (or Set Up the Files)

If you have this project in a Git repository, clone it.
Otherwise, ensure the `docker-compose.yml`, `Dockerfile`, and `main.py` files are in the same directory.

#### Clean Up Previous Containers

Open a terminal in the project's root directory and run the following command to stop and remove any old containers and networks. This ensures a clean start:

```bash
docker-compose down --remove-orphans
```

#### Build and Start the Hadoop Cluster

This command will build your Python image and start the **namenode** and **datanode** services in the background:

```bash
docker-compose up --build -d namenode datanode
```

#### Wait for Hadoop to Initialize (Important!)

Wait for about **30–60 seconds** to give the Hadoop services time to fully boot up.
You can check the status by opening the NameNode's web UI in your browser:

* **HDFS Dashboard:** [http://localhost:9870](http://localhost:9870)

You should see **“Started”** at the top of the page.
Under the **“Datanodes”** tab, you should see **1 live node**.

#### 5️Run the Python Client Script

Once the Hadoop cluster is ready, run the Python client manually with the following command.
The `--rm` flag automatically cleans up the client container after it finishes:

```bash
docker-compose run --rm client python main.py
```

---

## Expected Outcome

If successful, you will see the following output in your terminal, confirming that the Python script connected to HDFS and performed all file operations:

```
Successfully connected to HDFS from within the Docker network.

--- Performing CREATE operations ---
Directory '/user/final_test' created.
File '/user/final_test/final_file.txt' created.

--- Performing READ operation ---
Reading content from '/user/final_test/final_file.txt':
---
This connection works perfectly!
---

--- Performing UPDATE operation (Append) ---
Appended content to '/user/final_test/final_file.txt'.
Verifying updated content:
---
This connection works perfectly!
The networking issue is solved.
---

--- Performing DELETE operations ---
Directory '/user/final_test' and its contents deleted.

All operations completed successfully!

