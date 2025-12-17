# Databricks notebook source
# MAGIC %md
# MAGIC ### Data LakeHouse
# MAGIC - A Data Lakehouse is a modern data architecture that combines the scalability and low cost of a data lake with the performance, governance, and transactional capabilities of a data warehouse.
# MAGIC - It provides a unified platform for structured, semi-structured, and unstructured data, enabling BI, analytics, and machine learning on a single system.
# MAGIC
# MAGIC #### Key Features of a Data Lakehouse
# MAGIC
# MAGIC 1. Open Data Formats (Parquet, Delta, Iceberg, Hudi)
# MAGIC 2. ACID Transactions (Delta Lake, Iceberg, Hudi)(Atomicity, Consistency, Isolation, Durability)
# MAGIC 3. Schema Evolution & Governance (Unity Catalog)
# MAGIC 4. Unified Storage & Compute
# MAGIC 5. Lakehouse Storage is decoupled with compute so both can scale independently.
# MAGIC     - Storage (where data is stored) is independent of Compute (where data is processed, queried, or transformed).
# MAGIC
# MAGIC 1. **Transaction support:** In an enterprise lakehouse many data pipelines will often be reading and writing data concurrently. Support for ACID transactions ensures consistency as multiple parties concurrently read or write data, typically using SQL.
# MAGIC
# MAGIC 1. **Schema enforcement and governance:** The Lakehouse should have a way to support schema enforcement and evolution, supporting DW schema architectures such as star/snowflake-schemas. The system should be able to reason about data integrity, and it should have robust governance and auditing mechanisms.
# MAGIC
# MAGIC 1. **BI support:** Lakehouses enable using BI tools directly on the source data. This reduces staleness and improves recency, reduces latency, and lowers the cost of having to operationalize two copies of the data in both a data lake and a warehouse.
# MAGIC
# MAGIC 1. **Storage is decoupled from compute:** In practice this means storage and compute use separate clusters, thus these systems are able to scale to many more concurrent users and larger data sizes. Some modern data warehouses also have this property.
# MAGIC
# MAGIC 1. **Openness:** The storage formats they use are open and standardized, such as Parquet, and they provide an API so a variety of tools and engines, including machine learning and Python/R libraries, can efficiently access the data directly.
# MAGIC
# MAGIC 1. **Support for diverse data types ranging from unstructured to structured data:** The lakehouse can be used to store, refine, analyze, and access data types needed for many new data applications, including images, video, audio, semi-structured data, and text.
# MAGIC
# MAGIC 1. **Support for diverse workloads:** including data science, machine learning, and SQL and analytics. Multiple tools might be needed to support all these workloads but they all rely on the same data repository.
# MAGIC
# MAGIC 1. **End-to-end streaming:** Real-time reports are the norm in many enterprises. Support for streaming eliminates the need for separate systems dedicated to serving real-time data applications.

# COMMAND ----------

# MAGIC %md
# MAGIC ### What is Compute Resources?
# MAGIC Compute resources refer to the hardware and software components that provide processing power and memory to run workloads, such as data processing, analytics, machine learning, and other computational tasks
# MAGIC
# MAGIC ###How Compute Resources Are Used in Azure Databricks?
# MAGIC - In the Databricks Computer resources are sees as Clusters. 
# MAGIC - A Cluster is the group of VMs that work together to process data.
# MAGIC - There are Two types of node in Cluster
# MAGIC   - Driver Node:
# MAGIC       - This is **Control Node** that coordinate the task and manage cluster.
# MAGIC       - Runs the apache spark driver programe and handles the job cluster.
# MAGIC   - Worker Node:
# MAGIC       - This is **Compute Node** that perform the actual data processing
# MAGIC       - Execute task in parallel to distribute workload.
# MAGIC ### Types of Compute Resources in Azure Databricks
# MAGIC 1. All purpose Cluster
# MAGIC     - Used for interactive data analysis and development.
# MAGIC     - Users can attach notebooks to these clusters and run ad-hoc queries.
# MAGIC 2. Job Cluster
# MAGIC     - Created specifically to run automated jobs (e.g., ETL pipelines, scheduled tasks).
# MAGIC     - Automatically terminated after the job completes.
# MAGIC 3. Single Node Cluster
# MAGIC     - Consist of only a driver node (no worker nodes).
# MAGIC     - Used for lightweight tasks or testing.
# MAGIC 4. High Concurrency Cluster
# MAGIC     - Optimized for multiple users running interactive workloads simultaneously.
# MAGIC     - Provide fine-grained access control and resource sharing.
# MAGIC
# MAGIC #### Differ b/w Compute and cluster
# MAGIC | Feature       | Compute | Cluster |
# MAGIC |--------------|---------|---------|
# MAGIC | **Definition** | The overall processing power (CPU, memory, GPU) used for computation. | A group of virtual machines (nodes) working together to process data. |
# MAGIC | **Scope** | Broad term that includes clusters, virtual machines, containers, and more. | A specific arrangement of compute resources for distributed computing. |
# MAGIC | **Components** | Includes CPUs, memory, GPUs, and storage used for computing. | Consists of a **driver node** and multiple **worker nodes**. |
# MAGIC | **Purpose** | Provides the raw computational resources to run workloads. | Organizes and manages compute resources efficiently for tasks. |
# MAGIC | **Example** | Virtual Machines (VMs), Kubernetes Pods, EC2 Instances. | Databricks Cluster, Spark Cluster, Hadoop Cluster. |
# MAGIC | **Relationship** | Compute is the foundational resource used in clusters. | A cluster is a structured way to utilize compute resources. |
# MAGIC
# MAGIC **Key Takeaway:**  
# MAGIC A **cluster** is a part of **compute**, but **compute** is a broader concept that includes various ways to use processing power, including clusters. 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Describe the relationship between the data lakehouse and the data warehouse.
# MAGIC - A Data Lakehouse is a modern architecture that combines the best features of a Data Lake and a Data Warehouse into a single platform.
# MAGIC - While Data Warehouses are optimized for structured data and high-speed analytics, Data Lakehouses extend this by supporting structured, semi-structured, and unstructured data with ACID transactions and governance.
# MAGIC
# MAGIC #### Key Differences Between a Data Warehouse and a Data Lakehouse
# MAGIC - Storage & Cost
# MAGIC     - Data Warehouse: Uses proprietary storage (Snowflake, Redshift, BigQuery). Expensive at scale.
# MAGIC     - Data Lakehouse: Uses low-cost cloud storage (S3, ADLS, GCS) with open formats (Delta, Iceberg, Hudi).
# MAGIC - Data Processing & Schema
# MAGIC     - Data Warehouse: Schema-on-write → Requires predefined schema before data ingestion.
# MAGIC     - Data Lakehouse: Schema evolution → Supports schema flexibility and late binding.
# MAGIC - Machine Learning & AI
# MAGIC     - Data Warehouse: Optimized for SQL-based analytics but not for ML & AI.
# MAGIC     - Data Lakehouse: Optimized for BI, Machine Learning, and real-time analytics.
# MAGIC - Performance Optimization
# MAGIC     - Data Warehouse: Uses indexing & materialized views for fast queries.
# MAGIC     - Data Lakehouse: Uses Z-Ordering, Caching, Data Skipping, and Indexing for faster queries.
# MAGIC     

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify the improvement in data quality in the data lakehouse over the data lake.
# MAGIC A Data Lakehouse improves data quality over a traditional Data Lake by introducing ACID transactions, schema enforcement, data governance, and indexing while still maintaining the flexibility of a data lake.
# MAGIC
# MAGIC How a Data Lakehouse Enhances Data Quality ?
# MAGIC 1. ACID Transactions Prevent Corrupt or Inconsistent Data
# MAGIC     - In a Data Lake, concurrent writes can cause data corruption.
# MAGIC     - A Lakehouse (via Delta Lake, Iceberg, Hudi) ensures transaction safety.
# MAGIC 2. Schema Enforcement Reduces Errors
# MAGIC     - A Data Lake allows inconsistent data formats, leading to dirty data.
# MAGIC     - A Lakehouse enforces schema rules at write time.
# MAGIC 3. Data Governance
# MAGIC     - A Data Lake lacks fine-grained access controls.
# MAGIC     - A Lakehouse uses RBAC, ABAC, and Unity Catalog for secure access.
# MAGIC 4. Data duplication and Compaction Improves Cleaness
# MAGIC     - A data lake store duplicate, redundent data.
# MAGIC     - A Lakehouse automatically compacts and deduplicates data.

# COMMAND ----------

# MAGIC %md
# MAGIC ###Melladion Architecture
# MAGIC |**Layer**|**Purpose**|**Data Processing**|**Users**|
# MAGIC |---------|-----------|-------------------|---------|
# MAGIC |Bronze 🥉|	Raw data ingestion|	No schema enforcement, duplicates allowed|	Data Engineers|
# MAGIC |Silver 🥈|	Cleaned & structured data|	Deduplication, type casting, joins|	Analysts, Data Scientists|
# MAGIC |Gold 🥇|	Business-ready data|	Aggregation, KPIs, precomputed reports|	BI Users, Executives|
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Compare and contrast silver and gold tables, which workloads will use a bronze table as a source, which workloads will use a gold table as a source.
# MAGIC
# MAGIC #### Comparison of Silver and Gold Tables  
# MAGIC
# MAGIC | **Feature**          | **Silver Table (Cleaned & Enriched Data)** | **Gold Table (Business-Ready Data)** |
# MAGIC |----------------------|--------------------------------------------|--------------------------------------|
# MAGIC | **Purpose**         | Cleansed, validated, and enriched data      | Aggregated, business-ready data for BI |
# MAGIC | **Data Processing** | Deduplicated, standardized, and transformed | Pre-aggregated and modeled for reporting |
# MAGIC | **Data Format**     | Still detailed, but structured              | Summarized and optimized for BI |
# MAGIC | **Schema Complexity** | Moderate                                  | Simple, with KPIs & metrics |
# MAGIC | **Storage Size**    | Larger                                      | Smaller (Aggregations reduce data size) |
# MAGIC | **Used By**        | Data Engineers, Analysts                    | Business Analysts, Executives, BI tools |
# MAGIC | **Example Use Case** | Preparing structured data for further modeling | Power BI, Tableau, or Looker dashboards |
# MAGIC
# MAGIC
# MAGIC #### Which Workloads Use a Bronze Table as a Source?
# MAGIC A Bronze Table contains raw, unprocessed data ingested from different sources (logs, IoT, transactional systems).
# MAGIC - Workloads that Use Bronze Tables:
# MAGIC   - Data Cleansing & Transformation → ETL pipelines to create Silver Tables
# MAGIC   - Data Exploration & Debugging → Data Engineers validate raw logs
# MAGIC   - Streaming & Batch Processing → Real-time ingestion from Kafka or IoT
# MAGIC   - Machine Learning Feature Engineering → Extracting raw features
# MAGIC
# MAGIC #### Which Workloads Use a Gold Table as a Source?
# MAGIC A Gold Table contains business-ready, aggregated data, often used in BI & reporting.
# MAGIC - Workloads that Use Gold Tables:
# MAGIC   - Business Intelligence & Dashboards → Power BI, Tableau, Looker
# MAGIC   - Executive Reports → Revenue, Sales, Customer Insights
# MAGIC   - Machine Learning Model Training → Using curated data for predictive models

# COMMAND ----------

# MAGIC %md
# MAGIC ###Identify elements of the Databricks Platform Architecture, such as what is located in the data plane versus the control plane and what resides in the customer’s cloud account
# MAGIC
# MAGIC #### The Databricks Platform Architecture is divided into two main components:
# MAGIC 1. Control Plane (Managed by Databricks)
# MAGIC 2. Data Plane (Located in the Customer’s Cloud Account)
# MAGIC
# MAGIC #### Control Plane (Managed by Databricks)
# MAGIC The control plane is responsible for managing and orchestrating workloads. It resides in the Databricks-managed cloud account and includes:
# MAGIC 1. **Databricks Web Application**: UI for managing jobs, clusters, and notebooks.
# MAGIC 2. REST API: Allows programmatic interaction with Databricks resources.
# MAGIC 3. **Cluster Manager**: Controls cluster lifecycle (start, stop, resize).
# MAGIC 4. Notebook and Job Scheduler: Manages job execution and **workflow automation**.
# MAGIC 5. Databricks Workspace Metastore: Stores metadata about **notebooks**, jobs, and queries.
# MAGIC 6. **IAM Authentication and Access Control**: Manages users, roles, and permissions.
# MAGIC
# MAGIC ### Data Plane (Located in Customer’s Cloud Account)
# MAGIC The data plane is where data processing occurs and is fully within the customer’s cloud environment (AWS, Azure, or GCP). It includes:
# MAGIC 1. **Clusters (Compute Resources)**: Virtual machines (VMs) running Spark jobs.
# MAGIC 1. Databricks Runtime: Optimized Spark-based engine for running workloads.
# MAGIC 1. **Storage (Customer's Cloud Storage)**: Data resides in AWS S3, Azure Data Lake Storage (ADLS), or Google Cloud Storage (GCS).
# MAGIC 1. Network and Security Controls: Managed in the customer’s environment to restrict access and secure data.
# MAGIC
# MAGIC #### Key Separation of Responsibilities
# MAGIC
# MAGIC | **Component**           | **Control Plane (Databricks-Managed)** | **Data Plane (Customer's Cloud Account)** |
# MAGIC |-------------------------|------------------------------------|------------------------------------|
# MAGIC | Cluster Management      | Yes                                | No                                 |
# MAGIC | Job Scheduling         | Yes                                | No                                 |
# MAGIC | Notebooks & UI         | Yes                                | No                                 |
# MAGIC | Data Storage           | No                                 | Yes                                |
# MAGIC | Spark Compute         | No                                 | Yes                                |
# MAGIC | Security Controls     | Partially (IAM)                    | Yes (Networking, Storage Access)  |
# MAGIC
# MAGIC
# MAGIC Note: A Customer Cloud Account refers to a cloud environment owned and managed by an organization (the customer) within a public cloud provider, such as AWS, Azure, or Google Cloud. This account allows the customer to provision and manage cloud resources like virtual machines, storage, databases, and networking components.

# COMMAND ----------

# MAGIC %md
# MAGIC #### Difference Between All-Purpose Clusters and Job Clusters
# MAGIC
# MAGIC Databricks provides two types of clusters for different workloads:  
# MAGIC
# MAGIC 1. **All-Purpose Clusters**  
# MAGIC 2. **Job Clusters**  
# MAGIC
# MAGIC ##### 1. All-Purpose Clusters
# MAGIC All-purpose clusters are designed for interactive and collaborative workloads, such as running notebooks, ad-hoc queries, and development tasks.
# MAGIC
# MAGIC ##### **Key Features**
# MAGIC - **Shared and Persistent**: These clusters remain active until manually terminated, making them suitable for multiple users.  
# MAGIC - **Supports Multiple Workloads**: Users can run notebooks, SQL queries, and ML models simultaneously.  
# MAGIC - **Interactive Development**: Ideal for exploratory analysis and debugging.  
# MAGIC - **Higher Cost**: Since they run continuously, they may incur higher costs if not properly managed.  
# MAGIC - **Auto-Termination (Optional)**: Can be configured to shut down after inactivity to save costs.  
# MAGIC
# MAGIC ##### **Use Cases**
# MAGIC - Data exploration and analysis  
# MAGIC - Collaborative development  
# MAGIC - Running interactive notebooks  
# MAGIC - Running ML model training experiments  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ##### 2. Job Clusters
# MAGIC Job clusters are ephemeral and created specifically for running a single job, such as a batch ETL process or scheduled task. They are terminated automatically after execution.
# MAGIC
# MAGIC ##### **Key Features**
# MAGIC - **Ephemeral and Dedicated**: Created when a job starts and automatically terminates after job completion.  
# MAGIC - **Single-Job Execution**: Optimized for running a specific job, ensuring resource isolation.  
# MAGIC - **Cost-Efficient**: Eliminates idle cluster time, reducing costs.  
# MAGIC - **Automated Management**: Fully managed by Databricks with minimal manual intervention.  
# MAGIC
# MAGIC ##### **Use Cases**
# MAGIC - Running scheduled ETL pipelines  
# MAGIC - Batch data processing  
# MAGIC - Automated data ingestion and transformation  
# MAGIC - Executing scheduled ML model inference tasks  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### Key Differences Summary
# MAGIC
# MAGIC | **Feature**            | **All-Purpose Cluster** | **Job Cluster** |
# MAGIC |------------------------|----------------------|----------------|
# MAGIC | **Persistence**        | Persistent (until manually terminated) | Ephemeral (terminates after job completion) |
# MAGIC | **User Access**        | Shared among multiple users | Dedicated to a single job execution |
# MAGIC | **Cost Efficiency**    | Higher cost (runs continuously) | Cost-efficient (shuts down after execution) |
# MAGIC | **Use Case**          | Interactive analysis, development, ML training | Batch jobs, ETL, scheduled data processing |
# MAGIC | **Cluster Creation**   | Manually created by users | Created automatically for job execution |
# MAGIC
# MAGIC By choosing the right cluster type, organizations can optimize costs and improve efficiency based on workload requirements.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify how cluster software is versioned using the Databricks Runtime.
# MAGIC #### Databricks Runtime (DBR) Versioning
# MAGIC
# MAGIC Databricks Runtime (DBR) is the core software environment that runs on Databricks clusters. It includes **Apache Spark**, **libraries**, **ML frameworks**, and **optimizations** for performance and compatibility.
# MAGIC
# MAGIC ##### 1. Databricks Runtime Versioning
# MAGIC
# MAGIC Each **Databricks Runtime** version follows a structured format:  
# MAGIC
# MAGIC **`Databricks Runtime X.Y`**, where:  
# MAGIC - **X** = Major version (significant changes, upgrades, and feature additions).  
# MAGIC - **Y** = Minor version (bug fixes, performance improvements, and small enhancements).  
# MAGIC - **LTS (Long-Term Support)**: Some versions are designated as **LTS**, meaning they receive extended support and stability updates.
# MAGIC
# MAGIC ###### **Example Versions**
# MAGIC - `Databricks Runtime 13.3 LTS` (Long-Term Support version)  
# MAGIC - `Databricks Runtime 14.1` (Latest short-term release)  
# MAGIC - `Databricks Runtime 12.2 LTS` (Older LTS version with stability updates)  
# MAGIC
# MAGIC ##### 2. Types of Databricks Runtime
# MAGIC
# MAGIC | **Runtime Type**       | **Purpose** |
# MAGIC |------------------------|------------|
# MAGIC | **Databricks Runtime** | Standard runtime with Apache Spark, optimized for general workloads. |
# MAGIC | **Databricks Runtime for ML** | Preinstalled ML libraries (TensorFlow, PyTorch, MLflow) for machine learning. |
# MAGIC | **Databricks Runtime for GenAI** | Specialized runtime optimized for Generative AI workloads. |
# MAGIC | **Databricks Runtime for SQL** | Optimized for SQL workloads with Photon acceleration. |
# MAGIC | **Photon Runtime** | High-performance query execution engine for analytics and BI workloads. |
# MAGIC
# MAGIC ##### 3. How to Check and Select Databricks Runtime Version
# MAGIC
# MAGIC - When **creating a cluster**, users can **select** the desired DBR version from the Databricks UI.
# MAGIC - Using the **REST API**, runtime versions can be retrieved programmatically.
# MAGIC - The **cluster configuration page** provides information on the current DBR version.
# MAGIC
# MAGIC ##### 4. Databricks Runtime Lifecycle
# MAGIC
# MAGIC Databricks releases **new DBR versions** frequently, and older versions **reach end-of-support (EoS)** over time.  
# MAGIC - **LTS versions** have extended stability support.  
# MAGIC - **Short-term releases** provide the latest features but may deprecate faster.  
# MAGIC - Users should **upgrade regularly** to benefit from performance improvements and security patches.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ##### **Summary**
# MAGIC - Databricks Runtime is versioned as **X.Y**, where X is the major version, and Y is the minor version.
# MAGIC - Different types of DBR exist for **general workloads, ML, SQL, and GenAI**.
# MAGIC - Users can select the DBR version **when creating clusters** or update existing clusters.
# MAGIC - **LTS versions** offer long-term stability, while **short-term releases** provide the latest features.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify how clusters can be filtered to view those that are accessible by the user
# MAGIC Filtering clusters to view those accessible by a user involves leveraging Azure's identity and access management (IAM) and Databricks' workspace-level permissions.
# MAGIC
# MAGIC 1. Check Azure IAM Permissions
# MAGIC
# MAGIC Azure IAM controls access to Azure resources, including Databricks workspaces. To filter clusters accessible by a user:
# MAGIC - Verify the user's role assignments in the Azure portal:
# MAGIC   - Navigate to the Azure portal.
# MAGIC   - Go to the Databricks workspace resource.
# MAGIC   - Select Access control (IAM).
# MAGIC   - Check the user's role (e.g., Contributor, Reader, or custom roles).
# MAGIC - Ensure the user has at least Reader access to the Databricks workspace to view clusters.
# MAGIC
# MAGIC 2. Databricks Workspace Permissions
# MAGIC
# MAGIC Databricks has its own permission model for clusters within a workspace. To filter clusters accessible by a user:
# MAGIC - Log in to the Databricks workspace as an admin or user with appropriate permissions.
# MAGIC - Navigate to the Clusters page:
# MAGIC     - In the Databricks UI, go to Compute > Clusters.
# MAGIC - Use the filter option to view clusters:
# MAGIC     - By default, users can see clusters they have created or have been granted access to.
# MAGIC     - Admins can see all clusters in the workspace.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Describe how clusters are terminated and the impact of terminating a cluster.
# MAGIC In Azure Databricks terminating a cluster is a come operation that stops the compute resource associated with the cluster.
# MAGIC
# MAGIC ---
# MAGIC #### How to terminate the cluster?
# MAGIC 1. Via the Databricks UI
# MAGIC     - Navigate to the Compute section in the Databricks workspace.
# MAGIC     - Find the cluster you want to terminate.
# MAGIC     - Click the three vertical dots (⋮) next to the cluster name.
# MAGIC     - Select Terminate
# MAGIC     - Confirm the termination.
# MAGIC 2. Via Databricks CLI
# MAGIC   - `databricks clusters delete --cluster-id <cluster-id>`
# MAGIC ---
# MAGIC #### Impact of Terminating a cluster: 
# MAGIC 1. Compute Resources
# MAGIC   - Stopped Resources: Terminating a cluster stops all associated compute resources (virtual machines, memory, CPU, etc.).
# MAGIC   - Cost Savings: Since you are no longer using these resources, you stop incurring costs for compute. However, storage costs (e.g., DBFS, attached cloud storage) may still apply.
# MAGIC 2. Running jobs and Notebooks: 
# MAGIC   - Active Job: If the cluster is running jobs, terminating it will interrupt those jobs. The jobs will fail unless they are configured to restart on a new cluster.
# MAGIC   - Notebooks Session: Any active notebook sessions attached to the cluster will be disconnected, and unsaved work may be lost.
# MAGIC 3. Data and Storage
# MAGIC   - Attached Storage: Data stored in attached cloud storage (e.g., Azure Blob Storage, ADLS) or DBFS (Databricks File System) is not affected by cluster termination.
# MAGIC   - Local Disk Data: Any data stored on the cluster's local disks (e.g., temporary files, cached data) is lost when the cluster is terminated.
# MAGIC 4. Cluster Configuration:
# MAGIC   - Persistent Configurataion: The cluster configuration (e.g., instance type, libraries, init scripts) is retained even after termination. You can restart the cluster with the same configuration.
# MAGIC   - Epheremal Cluster: For clusters created for specific jobs or tasks, termination removes the cluster entirely, and it cannot be restarted.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify a scenario in which restarting the cluster will be useful.
# MAGIC - Restarting a cluster in Azure Databricks can be useful in several scenarios, particularly when you want to preserve the cluster configuration and avoid the overhead of recreating the cluster from scratch.
# MAGIC - Restarting a cluster is particularly useful in interactive development and debugging scenarios, where preserving the cluster configuration and applying changes (e.g., library installations, configuration updates) is essential. It helps resolve resource issues, clear the cluster state, and avoid the overhead of recreating the cluster.
# MAGIC
# MAGIC ---
# MAGIC #### Scenario where we have required to restart the cluster:
# MAGIC 1. Library Installation and Upgradation
# MAGIC 2. Configuration Changes
# MAGIC 3. Memory or Resource Issues
# MAGIC 4. Debugging
# MAGIC
# MAGIC ---
# MAGIC #### Steps to Restart a Cluster
# MAGIC 1. Via Databricks UI:
# MAGIC     1. Go to the Compute section in the Databricks workspace.
# MAGIC     1. Find the cluster you want to restart.
# MAGIC     1. Click the three vertical dots (⋮) next to the cluster name.
# MAGIC     1. Select Restart.
# MAGIC 2. Via Databricks CLI:
# MAGIC     `databricks clusters restart --cluster-id <cluster-id>`

# COMMAND ----------

# MAGIC %md
# MAGIC ### Describe how to use multiple languages within the same notebook.
# MAGIC In Azure Databricks, you can use multiple programming languages within the same notebook, which is particularly useful for data engineering, data science, and machine learning workflows. Databricks notebooks support Python, SQL, Scala, and R, and you can switch between these languages seamlessly within a single notebook.
# MAGIC
# MAGIC how to use multiple languages in the same notebook: 
# MAGIC 1. During creating the cluster we give it a default language(python, scala, Sql, R).
# MAGIC 2. Using Multiple Languages in the Same Notebook:
# MAGIC     - **_Magic Commands_** : Magic commands are special commands that start with % and allow you to specify the language for a specific cell.
# MAGIC         - %python: Switch to Python.
# MAGIC         - %sql: Switch to SQL.
# MAGIC         - %scala: Switch to Scala.
# MAGIC         - %r: Switch to R
# MAGIC 3. Sharing Variables Across Languages: Databricks allows you to share variables and data across languages using the spark object and temporary views.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify how to run one notebook from within another notebook.
# MAGIC - In Azure Databricks, you can run one notebook from within another notebook using the %run magic command or the dbutils.notebook.run() function. 
# MAGIC - This is useful for modularizing your code, reusing common logic, or orchestrating complex workflows.
# MAGIC Two Methods of Run one notebook into another notebooks: 
# MAGIC 1. Use **_%run_** command:
# MAGIC   - The %run command allows you to run another notebook in the same context as the current notebook. This means that all variables, functions, and dataframes defined in the called notebook become available in the calling notebook.
# MAGIC 2. Using the **_dbutils.notebook.run()_** Function
# MAGIC   - The dbutils.notebook.run() function allows you to run another notebook as a separate job. Unlike %run, this method does not share the execution context, and the called notebook runs in an isolated environment.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC Comparision
# MAGIC choosing Between %run and dbutils.notebook.run()
# MAGIC |Feature|	%run	|dbutils.notebook.run()|
# MAGIC |-------|-------|----------------------|
# MAGIC |Execution Context|	Shared context|	Isolated context|
# MAGIC |Variable Sharing|	Variables are shared|	Variables are not shared|
# MAGIC |Use Case|	Modularizing code, reusing logic|	Orchestrating workflows, job-like execution|
# MAGIC |Parameters	|Not supported	|Supported via arguments|
# MAGIC |Return Value|	Not applicable	|Supported via dbutils.notebook.exit()|
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC
# MAGIC
# MAGIC %md
# MAGIC ### Identify how notebooks can be shared with others
# MAGIC Different ways to share the notebooks:
# MAGIC 1. Share Notebook within databricks:
# MAGIC     - You can share notebooks with specific users or groups:
# MAGIC         - Open the notebook in Databricks.
# MAGIC         - Click on "Share" (top-right corner).
# MAGIC         - Enter the user’s email or group name.
# MAGIC         - Set permissions:
# MAGIC           - Can View (Read-only access)
# MAGIC           - Can Run (Execute but not edit)
# MAGIC           - Can Edit (Full editing rights)
# MAGIC         - Click Share.
# MAGIC     - **Best for: Teams working within the same Databricks workspace**
# MAGIC 2. Export and Import Notebooks
# MAGIC     - Export as HTML, Source Code, or IPython Notebook and the simple send to the target user, by simple importing it he can used it.
# MAGIC     - **Best for: External collaboration or saving versions.**
# MAGIC 3. Use Git Integration:
# MAGIC     - Steps:
# MAGIC       - Enable Git Integration in Databricks settings.
# MAGIC       - Connect to a GitHub, GitLab, Bitbucket, or Azure DevOps repo.
# MAGIC       - Use "Repos" in Databricks to manage shared notebooks.
# MAGIC       - Team members can push, pull, and merge changes.
# MAGIC     - **Best for: Collaboration across teams with version control.**
# MAGIC 4. Share via Databricks workflow:
# MAGIC     - Steps:
# MAGIC       - Convert a notebook into a Databricks Job.
# MAGIC       - Schedule it and share job run results.
# MAGIC       - Publish dashboards for non-technical users to view insights.
# MAGIC     - **Best for: Automating & sharing analysis results with business teams.**

# COMMAND ----------

# MAGIC %md
# MAGIC ### Describe how Databricks Repos enables CI/CD workflows in Databrick
# MAGIC - Databricks Repos integrates with Git-based version control systems, enabling teams to implement CI/CD (Continuous Integration & Continuous Deployment) workflows. 
# MAGIC - This allows collaborative development, automated testing, and deployment of notebooks, workflows, and ML models.
# MAGIC <img src="https://docs.databricks.com/en/_images/repos-cicd-techniques.png" width="50%" height="50%">
# MAGIC ---
# MAGIC #### Key Features of Databricks Repos for CI/CD
# MAGIC | **Feature**|**Purpose**|
# MAGIC |------------|-----------|
# MAGIC |Git Integration|	Connects with GitHub, GitLab, Azure DevOps, Bitbucket|
# MAGIC |Branching & Merging|	Enables feature branches, pull requests, and merges|
# MAGIC |Version Control|	Tracks changes to notebooks, scripts, and workflows|
# MAGIC |Automation via Jobs & Pipelines|	Schedules tests, deployments, and workflows|
# MAGIC |CI/CD Integration|	Works with Jenkins, GitHub Actions, Azure DevOps Pipelines|
# MAGIC
# MAGIC ---
# MAGIC #### How Databricks Repos Supports CI/CD Workflows ?
# MAGIC 1. Version Control and Collaboration
# MAGIC     - Developers work on feature branches in Repos.
# MAGIC     - Changes are committed & pushed to GitHub/GitLab.
# MAGIC     - Teams can review code via pull requests (PRs) before merging.
# MAGIC 2. Automated testing with CI/CD pipelines
# MAGIC     - CI tools (Jenkins, GitHub Actions, Azure Pipelines) trigger tests when code is pushed.
# MAGIC     - PyTest, dbx, or Databricks Jobs validate notebook execution.
# MAGIC 3. Deployment and Promotion Across Environment
# MAGIC     - Databricks CI/CD Pipelines promote code from dev → staging → production.
# MAGIC     - Automated Jobs & Workflows deploy and test notebooks.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify Git operations available via Databricks Repos.
# MAGIC Databricks Repos integrates Git functionality directly into the Databricks workspace, enabling seamless version control and collaboration for notebooks and other code files.
# MAGIC
# MAGIC ---
# MAGIC #### Git operations available via Databricks Repos:
# MAGIC
# MAGIC | **Git Operation**             | **Description** |
# MAGIC |--------------------------------|----------------|
# MAGIC | **Clone a Repository**         | Clone a remote Git repository into Databricks Repos. |
# MAGIC | **Pull Changes**               | Fetch and merge updates from the remote Git repository. |
# MAGIC | **Commit Changes**             | Save changes locally in Databricks before pushing to Git. |
# MAGIC | **Push Changes**               | Upload local commits to the remote Git repository. |
# MAGIC | **Create Branch**              | Create a new branch for feature development. |
# MAGIC | **Switch Branches**            | Change between different branches in the repository. |
# MAGIC | **Merge Branches**             | Merge changes from one branch to another. |
# MAGIC | **Resolve Merge Conflicts**    | Handle conflicts when merging branches. |
# MAGIC | **Revert Changes**             | Undo changes before committing them. |
# MAGIC | **View Commit History**        | See past commits and changes made in the repository. |
# MAGIC | **Sync with Remote Repository** | Keep Databricks Repos up to date with the remote repository. |
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify limitations in Databricks Notebooks version control functionality relative to Repos
# MAGIC Databricks **Notebooks** offer basic version control, but they have several **limitations** compared to **Databricks Repos**, which provides full **Git integration**.  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### **🔹 Key Limitations of Databricks Notebooks Version Control**  
# MAGIC
# MAGIC | **Limitation**              | **Databricks Notebooks** | **Databricks Repos (Git-Enabled)** |
# MAGIC |-----------------------------|-------------------------|------------------------------------|
# MAGIC | **Full Git Support**        | No direct Git operations (commit, push, pull, merge) | Fully integrated with GitHub, GitLab, Azure DevOps, Bitbucket |
# MAGIC | **Branching & Merging**     | Cannot create, switch, or merge branches |  Supports feature branching & merging |
# MAGIC | **Pull Requests (PRs)**     | No support for PRs or code review workflows |  Git-based collaboration with PRs & code reviews |
# MAGIC | **Conflict Resolution**     | No version conflict handling |  Can resolve Git merge conflicts |
# MAGIC | **Commit History**          | Limited to basic notebook revisions |  Full Git commit history available |
# MAGIC | **Multi-File Versioning**   | Only tracks individual notebooks |  Tracks multiple notebooks, scripts, and configs in a repo |
# MAGIC | **CI/CD Integration**       | No automation for deployments |  Supports GitHub Actions, Jenkins, Azure Pipelines for CI/CD |
# MAGIC | **External Collaboration**  | Cannot sync directly with external Git repos |  Can sync and push changes to remote Git repositories |
# MAGIC | **Tracking Changes Across Workflows** |  No dependency tracking across multiple notebooks |  Tracks all repo files together for consistency |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### Summary: Why Use Databricks Repos Instead?
# MAGIC - **Repos provide full Git capabilities**, enabling advanced version control.  
# MAGIC - **Notebooks only support limited checkpointing** and lack branching, merging, or CI/CD integration.  
# MAGIC - **For teams working collaboratively**, **Databricks Repos** is the preferred choice.  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Databricks Cluster Pools: Optimizing Cluster Startup Time & Cost
# MAGIC
# MAGIC A Databricks Cluster Pool is a pre-allocated set of virtual machines (VMs) that helps reduce cluster startup time and optimize costs by maintaining a pool of ready-to-use instances. When a cluster is created from a pool, it skips VM provisioning time, significantly speeding up the process.
# MAGIC
# MAGIC #### How Do Databricks Cluster Pools Work?
# MAGIC 1. Pre-allocated Work: 
# MAGIC     - A pool consists of a set of pre-warmed instances, reducing the need to provision new VMs from scratch.
# MAGIC     - These instances sit idle, ready for clusters to use them instantly.
# MAGIC 2. Cluster Creating from Pool:
# MAGIC     - When a job or interactive workload needs a cluster, it acquires instances from the pool instead of requesting fresh ones from the cloud provider.
# MAGIC     - This minimizes startup time from several minutes to seconds.
# MAGIC 3. Instance Reuse and Auto-Scalling:
# MAGIC     - After a cluster finishes its job, the instances return to the pool for reuse, reducing provisioning delays.
# MAGIC     - The pool can scale dynamically, adding or removing instances based on demand.
# MAGIC
# MAGIC #### When Should You Use Cluster Pools?
# MAGIC * When Databricks job clusters take too long to start (e.g., 5-10 minutes).
# MAGIC * For frequent or scheduled jobs where minimizing startup time is crucial.
# MAGIC * To reduce cloud costs by reusing VMs instead of provisioning new ones.
# MAGIC * When using auto-scaling clusters that need fast scaling capabilities.
# MAGIC
# MAGIC #### How to Create and Use a Cluster Pool in Databricks
# MAGIC 1. Go to the Databricks UI → Compute → Pools
# MAGIC 1. Click "Create Pool"
# MAGIC 1. Configure the following:
# MAGIC     - Choose a cloud provider (AWS, Azure, GCP).
# MAGIC     - Select VM instance types.
# MAGIC     - Set Min & Max capacity.
# MAGIC     - Enable Auto-Termination if needed.
# MAGIC       - Save and Create the Pool
# MAGIC       - Attach clusters to the Pool in cluster settings.