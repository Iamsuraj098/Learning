# Databricks notebook source
# MAGIC %md
# MAGIC ### Use CREATE OR REPLACE TABLE and INSERT OVERWRITE
# MAGIC CREATE OR REPLACE TABLE and INSERT OVERWRITE are commonly used in SQL-based environments like Databricks, Snowflake, and Hive for managing tables and updating data efficiently.
# MAGIC - This statement creates a new table or replaces an existing one.
# MAGIC - It drops the old table (if it exists) and creates a new one with the defined schema.
# MAGIC
# MAGIC Using INSERT OVERWRITE
# MAGIC - This statement replaces the existing data in a table with new data.
# MAGIC - Unlike CREATE OR REPLACE TABLE, it does not drop the table structure.
# MAGIC
# MAGIC DIfference: 
# MAGIC |Scenario	|Use CREATE OR REPLACE TABLE|	Use INSERT OVERWRITE|
# MAGIC |---------|----------------------------|--------------------|
# MAGIC |Changing table schema|	✅|	❌|
# MAGIC |Keeping table schema but replacing data	|❌	|✅|
# MAGIC |Completely resetting a table	|✅	|✅ (If schema remains same)|
# MAGIC | **Purpose**       | Replaces the entire table (schema + data) | Overwrites only the data in the table |
# MAGIC | **Schema Impact** | Drops and recreates the table, allowing schema changes | Preserves the existing schema |
# MAGIC | **Effect on Data** | Completely removes existing table and creates a new one | Replaces only the data, keeping structure intact |
# MAGIC | **Performance**   | Can be expensive since it recreates the table | More efficient if only replacing data |
# MAGIC | **Use Case**      | When modifying schema or fully resetting a table | When replacing data but keeping schema unchanged |
# MAGIC | **Transactionality** | Non-atomic (drops the table first, then recreates) | Atomic (overwrites data in a single operation) |
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE sales_data (
# MAGIC     sale_id INT,
# MAGIC     customer_name STRING,
# MAGIC     amount DECIMAL(10,2),
# MAGIC     sale_date DATE
# MAGIC ) USING DELTA;
# MAGIC
# MAGIC INSERT OVERWRITE sales_data
# MAGIC SELECT * FROM updated_sales_data;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify a scenario in which MERGE should be used
# MAGIC Merge should be used when you need to insert, update, or delete records in a table based on a matching condition. This is especially useful for incremental updates, such as updating a table with new or changed records from another dataset.
# MAGIC
# MAGIC Use Case for MERGE
# MAGIC   - If a customer exists → Update their details.
# MAGIC   - If a customer is new → Insert them into the table.
# MAGIC   - If a customer is marked as inactive → Set their status to "inactive"
# MAGIC
# MAGIC ### Describe the benefits of the MERGE command
# MAGIC The MERGE command is highly efficient for handling incremental data updates, making it a powerful tool in databases like Databricks (Delta Lake), Snowflake, and SQL-based systems. 
# MAGIC 1. Improves performances and reduce data processing overhead
# MAGIC 2. Ensures data accuracy and consistency
# MAGIC 3. Ideal for Incremental Data Loads & Slowly Changing Dimensions (SCD)

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO customers AS c
# MAGIC USING new_customers AS nc
# MAGIC ON c.customer_id = nc.customer_id
# MAGIC WHEN MATCHED AND nc.is_active = FALSE THEN 
# MAGIC     UPDATE SET c.status = 'inactive'
# MAGIC WHEN MATCHED THEN 
# MAGIC     UPDATE SET c.name = nc.name, c.email = nc.email
# MAGIC WHEN NOT MATCHED THEN 
# MAGIC     INSERT (customer_id, name, email, status) 
# MAGIC     VALUES (nc.customer_id, nc.name, nc.email, 'active');
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify why a `COPY INTO` statement is not duplicating data in the target table.
# MAGIC `COPY INTO` statement used to **load data efficiently** into the table but it **does not inherently check for duplicates unless specific constraints or logic** are applied. If `COPY INTO` is not duplicating data, here are the possible reasons:
# MAGIC 1. File Tracking mechanism
# MAGIC     - `COPY INTO` tracks loaded files and prevents reloading the same file unless forced.
# MAGIC     - If you run `COPY INTO` twice on the same file, it won’t reload duplicate records unless you use **FORCE = TRUE**
# MAGIC 2. Primary Keys or Unique Constraints in the Target Table
# MAGIC     - If the target table has a primary key or a unique constraint, duplicate records are automatically rejected.
# MAGIC 3. File Already Processed
# MAGIC     - `COPY INTO` command track the metadata, to see is table is already processed or not.
# MAGIC     - If the table already processsed then `COPY INTO` command ingore it.

# COMMAND ----------

COPY INTO sales_transactions
FROM 'abfss://sales-data@storageaccount.dfs.core.windows.net/daily/'
FILEFORMAT = CSV
FORMAT_OPTIONS ('header' = 'true', 'inferSchema' = 'true')
COPY_OPTIONS ('mergeSchema' = 'true');

# COMMAND ----------

# MAGIC %md
# MAGIC ### Use COPY INTO to insert data.
# MAGIC The COPY INTO statement is used to load data from an external source (e.g., cloud storage, local files, or stages) into a table. It is optimized for bulk inserts and incremental data ingestion while preventing duplicates.
# MAGIC
# MAGIC

# COMMAND ----------

COPY INTO sales_data
FROM ''
FILEFORMAT = CSV
FORMAT_OPTIONS ('header' = 'true', 'inferSchema' = 'true')
COPY_OPTIONS ('mergeSchema' = 'true');

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify the components necessary to create a new DLT pipeline.
# MAGIC A Delta Live Tables (DLT) pipeline automates the ETL (Extract, Transform, Load) process using structured, declarative processing in Databricks. To create a new DLT pipeline, you need the following components:
# MAGIC 1. Target Table
# MAGIC 2. Transformation Logic
# MAGIC 3. Source Data
# MAGIC 4. Pipeline Configuration
# MAGIC 5. Compute Resource - cluster for execution
# MAGIC 6. Storage Location - Target for Processed Data
# MAGIC
# MAGIC |Component|	Purpose|
# MAGIC |----------|-------|
# MAGIC |Target Table (Delta Table)	|Stores transformed data|
# MAGIC |Source Data|	Raw data from cloud storage, tables, or streams|
# MAGIC |Transformation Logic (ETL)|	SQL/Python logic to clean and process data|
# MAGIC |Storage Location|	Specifies where DLT tables are written|
# MAGIC |Pipeline Configuration|	Defines execution mode, schedule, and settings|
# MAGIC |Compute Resources|	Databricks-managed cluster to process data|

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify the purpose of the target and of the notebook libraries in creating a pipeline.
# MAGIC Both target table and notebook libraries play a crucial role in creating pipeline due to these resons:
# MAGIC 1. **Target Table:** Stores the final, processed data in Delta tables, ensuring data persistence, schema management, and ACID transactions.
# MAGIC     - Traget table is the destination where the processed data is stored.
# MAGIC     - It referes to the Delta table that holds the data which comes after data pipeline complete its execution
# MAGIC     - Key purpose of target table: 
# MAGIC         - Stored transformed data
# MAGIC         - Defines data schema and structure
# MAGIC         - Optimizes Data Storages
# MAGIC         - Ensures data quality and expectation
# MAGIC 2. **Notebook Libraries:** Contains the ETL logic and data quality rules to transform the source data and process it according to business requirements.
# MAGIC     - These provide the programming logics and functions thats needed to define and run the bussiness logics of the pipelines.
# MAGIC     - These libraries include the SQL or Python code that processes the source data and writes it to the target.
# MAGIC     - Key purpose of notebook libraries:
# MAGIC         - Define transformation logics
# MAGIC         - Define data logic and expectation
# MAGIC         - Modularize data pipeline logic

# COMMAND ----------

# MAGIC %md
# MAGIC ### Compare and contrast triggered and continuous pipelines in terms of cost and latency
# MAGIC Triggre and Continuous are two modes of Pipelines.
# MAGIC - Triggered Pipelines (Batch Mode):
# MAGIC     - Triggered pipelines run based on a schedule or when manually triggered.
# MAGIC     - They process data in batches, typically at fixed intervals(hourly, daily, weekly)
# MAGIC     - **Cost:**
# MAGIC         - Low Cost
# MAGIC         - Cost control is easier because the pipeline runs at predefined intervals and does not require continuous resources.
# MAGIC         - Cluster usage is active only during pipeline execution.
# MAGIC     - **Latency:**
# MAGIC         - High Latency
# MAGIC         - Triggered pipelines introduce higher latency because data is processed only when the batch job runs.
# MAGIC         - There is typically a delay between data ingestion and when it’s actually processed and available.
# MAGIC         - For instance, if you set your pipeline to run hourly, it might take up to an hour to process new data.
# MAGIC
# MAGIC - Continous Pipelines (Stream Mode):
# MAGIC     - Continuous pipelines run continuously and process data in real-time or near real-time as it arrives.
# MAGIC     - They process streaming data from sources like Kafka, Event Hubs, or file streams.
# MAGIC     - **Cost:**
# MAGIC         - High
# MAGIC         - Continuous pipelines consume resources continuously, even when no data is being processed.
# MAGIC         - This leads to higher costs due to constant cluster usage for processing streaming data.
# MAGIC         - Continuous pipelines generally require auto-scaling clusters that need to be on at all times, contributing to more compute and storage costs.
# MAGIC     - **Latency:**
# MAGIC         - Low Latency:
# MAGIC         - Continuous pipelines can process data as soon as it is ingested, achieving near real-time processing with minimal delay.
# MAGIC         - Data is typically available in seconds or a few minutes after it enters the pipeline.
# MAGIC         - This is critical for applications like real-time analytics, monitoring, or fraud detection where latency is a key factor.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify which source location is utilizing Auto Loader
# MAGIC Autoloader is a features of Databricks that allows you to efficiently stream data from cloud storage (e.g., AWS S3, Azure Blob Storage, GCS) into Delta tables. It automatically detects new files and ingests them in a scalable and efficient manner without having to manually manage file discovery.
# MAGIC
# MAGIC Key Component of Autoloader: 
# MAGIC 1. Cloud Storage Path: The source location must be an external cloud storage path (e.g., S3 bucket, Azure Blob Storage container, or GCS path)
# MAGIC 1. Auto Loader Configuration: Auto Loader is used in the code to read files from the cloud storage path. This is typically done using spark.readStream in Python or cloudFiles in SQL. The key feature is the *cloudFiles* source that facilitates Auto Loader.
# MAGIC
# MAGIC Note: Schema location is used to store schema inferred by AUTO LOADER, so the next time AUTO LOADER runs faster as does not need to infer the schema every single time by trying to use the last known schema.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify a scenario in which Auto Loader is beneficial
# MAGIC 1. Real-Time Ingestion of IoT Sensor Data
# MAGIC 2. Stock Market Data Processing
# MAGIC 3. Log File Ingestion

# COMMAND ----------

# MAGIC %md
# MAGIC ###  Identify why Auto Loader has inferred all data to be STRING from a JSON source
# MAGIC |Issue	|Fix|
# MAGIC |-------|----|
# MAGIC |Schema inference fails|	Manually define schema using StructType|
# MAGIC |JSON values stored as strings	|Cast fields to correct data types after reading|
# MAGIC |Schema inferred from first batch|	Enable schema evolution (mergeSchema)|
# MAGIC |Missing schema tracking	|Use schemaLocation to persist schema|

# COMMAND ----------

# MAGIC %md
# MAGIC ###Identify the default behavior of a constraint violation
# MAGIC
# MAGIC | **Constraint Type** | **Description** | **Default Behavior on Violation** |
# MAGIC |----------------------|----------------|-----------------------------------|
# MAGIC | **PRIMARY KEY**      | Ensures each row has a unique identifier. | **Error:** Cannot insert duplicate or NULL values. |
# MAGIC | **FOREIGN KEY**      | Ensures referential integrity between tables. | **Error:** Cannot insert a value that does not exist in the parent table. |
# MAGIC | **UNIQUE**           | Ensures all values in a column are distinct. | **Error:** Cannot insert duplicate values. |
# MAGIC | **NOT NULL**         | Ensures a column cannot have NULL values. | **Error:** Cannot insert NULL values. |
# MAGIC | **CHECK**            | Ensures values meet a specific condition. | **Error:** Cannot insert or update a row that violates the condition. |
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify the impact of ON VIOLATION DROP ROW and ON VIOLATION FAIL UPDATE for a constraint violation
# MAGIC 1. ON VIOLATION DROP ROW
# MAGIC     - `ON VIOLATION DROP`
# MAGIC     - Drops the row that violates the constraint instead of failing the entire operation.
# MAGIC     - Other valid rows continue to be inserted or updated.
# MAGIC     - Helps in data cleansing by silently discarding invalid records.
# MAGIC     - Risk:
# MAGIC         - Data loss without warning, since invalid rows are discarded.
# MAGIC         - Should be used only when data quality is not critical or when handling large, noisy datasets.
# MAGIC 2. ON VIOLATION FAIL UPDATE
# MAGIC     - `ON VIOLATION FAIL`
# MAGIC     - Fails the update operation if any row violates a constraint.
# MAGIC     - Ensures strict data integrity by preventing partial updates.
# MAGIC     - Used when data consistency is more important than ingestion speed.
# MAGIC     - Risk:
# MAGIC         - Can block updates if constraint violations exist.
# MAGIC         - May require manual intervention to resolve conflicts before updates proceed.
# MAGIC     
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- On voilation drop row
# MAGIC CREATE TABLE users (
# MAGIC     user_id INT PRIMARY KEY,
# MAGIC     username STRING UNIQUE
# MAGIC );
# MAGIC
# MAGIC INSERT INTO users 
# MAGIC SELECT * FROM temp_users
# MAGIC ON VIOLATION DROP ROW;
# MAGIC
# MAGIC -- ON VIOLATION FAIL UPDATE
# MAGIC UPDATE users
# MAGIC SET username = 'john_doe'
# MAGIC WHERE user_id = 5
# MAGIC ON VIOLATION FAIL UPDATE;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Explain change data capture and the behavior of _`APPLY CHANGES INTO`_
# MAGIC
# MAGIC Change Data Capture is technique used to track and process the changes(Insert, update and delete) in source table incremently.
# MAGIC It helps keep downstream systems synchronized with the latest data changes, reducing processing overhead by only capturing new and modified records instead of reprocessing the entire dataset.
# MAGIC - Apply Changes Into: 
# MAGIC   - APPLY CHANGES INTO is a CDC mechanism in Delta Live Tables (DLT) that automatically applies changes from a source table to a target table.
# MAGIC   - Behaviour of Apply Changes Into
# MAGIC     -  Uses primary keys and timestamp to determine how to apply updates.
# MAGIC     - Tracks incremental changes(Insert, updates, delete) is a source table.
# MAGIC     - Ensure safe processing without duplication
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC APPLY CHANGES INTO LIVE.order_history
# MAGIC FROM STREAM(LIVE.orders)
# MAGIC KEYS (order_id)
# MAGIC APPLY AS DELETE WHEN order_status = 'CANCELLED'
# MAGIC SEQUENCE BY updated_at;

# COMMAND ----------

# MAGIC %md
# MAGIC ###  Query the events log to get metrics, perform audit loggin, examine lineage.
# MAGIC The event log in Databricks provides detailed metadata on pipeline executions, transformations, and system activities. You can use it for monitoring performance, auditing changes, and tracking lineage.
# MAGIC 1. Querying the Event Log for Metrics: You can analyze execution performance, task duration, and resource usage by querying the event log.
# MAGIC 2. Performing Audit Logging: Audit logging helps track who performed what actions, data modifications, and pipeline failures.
# MAGIC 3. Examining Data Lineage: Tracking data lineage helps understand how data flows through different tables and transformations.

# COMMAND ----------

# MAGIC %md
# MAGIC ### DownStream System
# MAGIC Downstream system refer to system or process that consumed data which produced by earlier process in the pipeline. These systems rely on the output of previous steps for their own operations.
# MAGIC
# MAGIC ### Example in Data Pipelines:
# MAGIC 1. **Upstream System:** A data pipeline that extracts data from a database or data lake and processes it.
# MAGIC 1. **Downstream System:** Another pipeline, application, or service that receives the processed data for further analysis, reporting, or storage.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC `spark.readStream`
# MAGIC
# MAGIC `.format("cloudfiles")`
# MAGIC
# MAGIC `.option("format",”csv)`
# MAGIC
# MAGIC `.option("checkpointlocation", ‘dbfs:/location/checkpoint/’)`
# MAGIC
# MAGIC `.load(data_source)`
# MAGIC
# MAGIC `.writeStream`
# MAGIC
# MAGIC `.option("schemalocation",’ dbfs:/location/checkpoint/’)`
# MAGIC
# MAGIC `.option("overwrite", "true")`
# MAGIC
# MAGIC `.table(table_name))`
# MAGIC
# MAGIC At the place of `overwrite` we can use these also: 
# MAGIC
# MAGIC 1. append (Default Write Mode): When you want to incrementally add new data to an existing table without modifying previous records.
# MAGIC 2. mergeSchema (Handles Schema Evolution): When the schema of incoming data might change over time, and you want to accommodate new columns dynamically.
# MAGIC 3. overwrite (Replaces Existing Data): When you want to replace the entire dataset with new data.
# MAGIC 4. complete mode: is one of the output modes in Spark Structured Streaming. It is mainly used when performing aggregations where you want to update all results instead of just adding new rows.

# COMMAND ----------

# MAGIC %md
# MAGIC `%py dlt.expect("valid Timestamp", "timestamp > '2020-01-02'")`
# MAGIC
# MAGIC `%sql CONSTRAINT valid_timestamp EXPECT (timestamp > '2020-01-01')`: (Retain Invalid Record) Record voilate expactation are add to target table. Flagged in invalid in evants log pipeline continues
# MAGIC
# MAGIC `%py dlt.expect_or_drop("valid Timestamp", "timestamp > '2020-01-02'")`
# MAGIC
# MAGIC `%sql CONSTRAINT valid_timestamp EXPECT (timestamp > '2020-01-01') on voilation drop row`: (Drop Invalid Record) Records voilate expactaion are dropped fromt target table, Flagged invalid event log pipeline continues
# MAGIC
# MAGIC `%py dlt.expect_or_fail("valid Timestamp", "timestamp > '2020-01-02'")`
# MAGIC
# MAGIC `%sql CONSTRAINT valid_timestamp EXPECT (timestamp > '2020-01-01') on voilation fail`: (Fail or Invalid Records) Records voilate expectation Cause fail the job

# COMMAND ----------

# MAGIC %md
# MAGIC #### Comparison: Job Cluster vs. All-Purpose Cluster in Databricks
# MAGIC |Feature	|Job Cluster|	All-Purpose Cluster|
# MAGIC |------------|----------|--------------|
# MAGIC |Startup Time	|⏳ Slower (cold start)	| Faster (warm pools)|
# MAGIC |Lifecycle	|Ephemeral (created for a job & terminates after)|	Persistent (stays alive until manually stopped)|
# MAGIC |Cost	|Lower (only runs for job duration)|	Higher (always running, even when idle)|
# MAGIC |Use Case	|Scheduled jobs, batch processing|	Interactive notebooks, ad-hoc analysis, multiple users|

# COMMAND ----------

# MAGIC %md
# MAGIC ####What Are Tags?
# MAGIC
# MAGIC Tags are key-value pairs that you can assign to Databricks jobs, clusters, and resources to help track and manage costs, ownership, and usage. These tags are then propagated to the cloud provider's billing system (AWS, Azure, GCP), allowing you to filter and analyze costs based on specific tags.