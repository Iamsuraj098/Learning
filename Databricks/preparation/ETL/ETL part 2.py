# Databricks notebook source
# MAGIC %md
# MAGIC Databricks Lakehouse primarily consists of:
# MAGIC
# MAGIC - Tables: Managed and external tables stored in Delta Lake.
# MAGIC - Views: Logical representations of query results, similar to SQL views.
# MAGIC - Databases/Schemas: Organizational containers for tables and views.
# MAGIC - Catalog: The highest-level namespace in Unity Catalog, organizing schemas and tables.
# MAGIC - Functions: User-defined functions (UDFs) and built-in functions for data transformations.

# COMMAND ----------

# MAGIC %md
# MAGIC Types of Tables: 
# MAGIC   1. Managed Table
# MAGIC       - **Databricks manage both data and metadata.**
# MAGIC       - Stored in DBFS (Databricks File System)
# MAGIC       - **When drop both data and metadata drops.**
# MAGIC       - `CREATE TABLE table_name (col1 TYPE, col2 TYPE);`
# MAGIC   2. External Table
# MAGIC       - **Only metadata managed by Databricks**
# MAGIC       - Data reside in an external location
# MAGIC       - **When droped only metadata is deleted, but data remain intact.**
# MAGIC       - `CREATE TABLE table_name (col1 TYPE, col2 TYPE) LOCATION 's3://bucket-name/path/';`
# MAGIC   3. Delta Table
# MAGIC       - Support time travel and optimised performance with indexing and caching.
# MAGIC       - Can be either managed or external, depends on how they cerated.
# MAGIC       - It provide ACID transaction, versioning and schema enforcement.
# MAGIC       - `CREATE TABLE table_name USING DELTA LOCATION 's3://bucket-name/path/';`
# MAGIC       - In Databricks, if you do not explicitly specify a storage format when creating a table, it defaults to a Delta table.
# MAGIC
# MAGIC Note: If you want to create a non-Delta table (like Parquet, CSV, etc.), you must explicitly specify the format:
# MAGIC   - `CREATE TABLE employees ( id INT, name STRING, department STRING )USING PARQUET;`

# COMMAND ----------

# MAGIC %md
# MAGIC ### Deleting the table: 
# MAGIC   - Managed Table: 
# MAGIC     - `Drop table table_name`
# MAGIC     - In Databricks, dropping a managed Delta table using DROP TABLE table_name removes both the table metadata and underlying data files automatically.
# MAGIC     - Databricks manages both metadata and storage for managed tables, no additional steps are needed.
# MAGIC   - External Table:
# MAGIC     - `DROP TABLE external_table_name;`
# MAGIC     - External tables store metadata in Databricks' metastore, but their data is stored in an external storage location (e.g., AWS S3, Azure Data Lake, GCS).
# MAGIC     - Dropping the table only removes its reference from Databricks, but does not delete the actual data files.
# MAGIC
# MAGIC ### Deleting Schema/Catalog:
# MAGIC - Other keyword when used with drop command: 
# MAGIC   - Schema Deletion: 
# MAGIC     - `DROP SCHEMA schema_name CASCADE`
# MAGIC     - Deletes the schema and all tables, views, and objects inside it.
# MAGIC     - Effect:
# MAGIC       - Deletes my_schema and all its objects (tables, views, functions, etc.).
# MAGIC       - Both metadata and managed table data (if any) are deleted.
# MAGIC       - External table data is not deleted—only metadata is removed.
# MAGIC     - `DROP SCHEMA schema_name;` (Without CASCADE)
# MAGIC     - If the schema is empty → The schema is dropped successfully.
# MAGIC     - If the schema contains tables, views, or functions → It will throw an error
# MAGIC   - Catalog Deletion:
# MAGIC     - `DROP CATALOG catalog_name CASCADE`
# MAGIC     - Removes the entire catalog along with all schemas, tables, and views inside it.
# MAGIC     - Effect:
# MAGIC       - Deletes my_catalog and all schemas, tables, and views inside it.
# MAGIC       - Managed table data is also deleted, but external table data remains.
# MAGIC     - `DROP CATALOG catalog_name;` (Without CASCADE)
# MAGIC     - If the catalog is empty → It is dropped successfully.
# MAGIC     - If it contains schemas, tables, or views → It throws an error.
# MAGIC
# MAGIC **Note: Cascade: The CASCADE option in Databricks SQL is used when dropping a schema or catalog to ensure that all dependent objects (like tables, views, and functions) inside them are also removed.**
# MAGIC
# MAGIC |Command	|Without CASCADE|	With CASCADE|
# MAGIC |---------|--------------|---------------|
# MAGIC |DROP SCHEMA sales;|	Fails if schema is not empty|	Deletes schema & all objects inside|
# MAGIC |DROP CATALOG my_catalog;|	Fails if catalog has schemas/tables|	Deletes catalog & all contents|
# MAGIC |DROP TABLE employees;|	Deletes table (no CASCADE needed)	|Not supported|
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### VACUUM Commands:
# MAGIC - These commands are used to permanently delete the old, unrefreshed delta table files from storage.
# MAGIC - It help manage storage cleanup and optimize performance.
# MAGIC - `VACUUM table_name RETAIN <retention_hours>;`
# MAGIC   - `<retention_hours>` Specifies how long to keep older data versions before deleting them
# MAGIC - How Does VACUUM Work?
# MAGIC   - Delta Lake uses a transaction log (_delta_log/) to track all table changes.
# MAGIC   - When you update, delete, or merge data, old files are not immediately deleted.
# MAGIC   - Running VACUUM removes files that are no longer referenced in the transaction log.
# MAGIC - Basic VACUUM Command: `VACUUM my_table;`
# MAGIC   - Deletes all files older than 7 days (default setting).
# MAGIC - VACUUM with Custom Retention Period: `VACUUM my_table RETAIN 48 HOURS;`
# MAGIC   - Deletes old files older than 48 hours.
# MAGIC   - Keeps the last 2 days of history.
# MAGIC - Force Delete All Old Data: `SET spark.databricks.delta.retentionDurationCheck.enabled = false; VACUUM my_table RETAIN 0 HOURS;`
# MAGIC   -  Warning:
# MAGIC     - This immediately deletes all unreferenced data.
# MAGIC     - You cannot time-travel to old versions after this!
# MAGIC
# MAGIC - Key benifits of Vacuum: 
# MAGIC   - Reduces Storage Cost
# MAGIC   - Improves Performance
# MAGIC   - Optimize delta table
# MAGIC   - Prevents Overhead
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exceptional Handling
# MAGIC - Python try-except block to handle the exception while other language used the try-catch.
# MAGIC - `try:`
# MAGIC
# MAGIC     `spark.read.table("table_name").select("column").write.mode("append").saveAsTable("new_table_name")`
# MAGIC
# MAGIC   `except Exception as e:`
# MAGIC
# MAGIC     `print(f"Query failed: {e}")`
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Checkpointing, Watermarking, and Idempotent Sinks in the context of Spark Structured Streaming
# MAGIC 1. Checkpointing:
# MAGIC     - Ensure fault Trolerance and Recovery
# MAGIC     - Store metadata to persist metadata
# MAGIC     - Used with stateful operations (aggregations, joins, mapGroupsWithState, etc.).
# MAGIC     - Allows stateful streaming queries to resume from where they left off after failure.
# MAGIC 2. Watermarking
# MAGIC     - Manages late-arriving data in event-time processing
# MAGIC     - Helps remove old statge to optimize tha memory usages.
# MAGIC     - Work with event time aggregation
# MAGIC     - Defines a threshold beyond which late data is discarded.
# MAGIC
# MAGIC 3. Idempotent Sinks 
# MAGIC     - Prevents duplicate writes
# MAGIC     - Ensures that if a streaming query retries, it does not cause duplicate writes.
# MAGIC     - Example sinks: Delta Lake, Kafka (Exactly-Once), File Sink (Append Mode).
# MAGIC
# MAGIC #### Write-Ahead Logging and Read-Ahead Logging
# MAGIC Write-Ahead Logging
# MAGIC   - Used in Spark Streaming (DStreams) for fault tolerance.
# MAGIC   - Logs received data before processing to avoid data loss.
# MAGIC   - Not used in Structured Streaming, as it relies on Checkpointing instead.
# MAGIC   
# MAGIC Read-Ahead Logging (RAL)
# MAGIC   - Read-Ahead Logging (RAL) is a technique used to preload or prefetch data into memory before it is actually needed.
# MAGIC   - This approach helps improve performance by reducing I/O latency and ensuring that subsequent read operations are faster.

# COMMAND ----------

df.writeStream \
  .format("delta") \
  .option("checkpointLocation", "/path/to/checkpoint") \
  .start()


# COMMAND ----------

# MAGIC %md
# MAGIC ### what is directory listing, file notification, file hashing and dynamic file lookup
# MAGIC 1. Directory Listing:
# MAGIC     - Process of retreiving a list of files and subdirectory in given directory.
# MAGIC     - Used for file discovery, batch processing and metadata
# MAGIC
# MAGIC 2. File Notification
# MAGIC     - A mechanism to detect changes (creation, modification, deletion) in files.
# MAGIC     - Helps in event-driven processing and incremental data ingestion.
# MAGIC
# MAGIC 3. File Hashing
# MAGIC     - A technique to compute a unique fingerprint for a file.
# MAGIC     - Used to check file integrity, detect duplicates, and verify authenticity.
# MAGIC
# MAGIC 4. Dynamic File Lookup
# MAGIC     - The ability to dynamically search and access files based on patterns, metadata, or queries.
# MAGIC     - Used in real-time data pipelines to load files dynamically.

# COMMAND ----------

# MAGIC %md
# MAGIC Medalion Architecture:
# MAGIC 1. Bronze Table
# MAGIC     - Raw copy of ingested data
# MAGIC     - Replaces traditional data lake
# MAGIC     - Provides efficient storage and querying of full, unprocessed history of data
# MAGIC     - No schema is applied at this layer
# MAGIC     - Bronze Tables store raw, unprocessed data from various sources.
# MAGIC     - They serve as the landing zone for data before any transformations or cleaning.
# MAGIC     - Typically, ingestion jobs write data to Bronze tables.
# MAGIC     - Data can come from streaming sources (Kafka, IoT, event logs) or batch sources (JSON, CSV, Parquet, etc.).
# MAGIC
# MAGIC 2. Silver Table:
# MAGIC     - Stores cleaned & transformed data
# MAGIC     - Reduces data storage complexity, latency, and redundency
# MAGIC     - Optimizes ETL throughput and analytic query performance
# MAGIC     - Preserves grain of original data (without aggregation)
# MAGIC     - Eliminates duplicate records
# MAGIC     - production schema enforced
# MAGIC     - Data quality checks, quarantine corrupt data
# MAGIC
# MAGIC 3. Gold Layer:
# MAGIC     - Stores aggregated & curated data
# MAGIC     - Powers ML applications, reporting, dashboards, ad hoc analytics
# MAGIC     - Refined views of data, typically with aggregations
# MAGIC     - Reduces strain on production systems
# MAGIC     - Optimizes query performance for business-critical data

# COMMAND ----------

# MAGIC %md
# MAGIC ### What happen when we drop a delta table: 
# MAGIC 1. In context of Managed Table: 
# MAGIC     - Metadata is deleted from the metastore.
# MAGIC     - Data is permanently deleted from storage (Databricks deletes the actual files).
# MAGIC     - Schema information is lost.
# MAGIC     - Irreversible: You cannot recover the data unless you have backups or use versioning features.
# MAGIC 2. In context of External Table:
# MAGIC     -  Metadata is deleted from the metastore.
# MAGIC     - Data is NOT deleted (because it's stored in an external location, e.g., S3, ADLS, DBFS).
# MAGIC     - Schema information is lost in Databricks, but data files remain intact.
# MAGIC     - Reversible: You can recreate the table by pointing to the same location using:

# COMMAND ----------

# MAGIC %md
# MAGIC ### Can a Single Cluster Have Multiple Sessions?
# MAGIC Yes, a single Databricks or Spark cluster can have multiple sessions running simultaneously.
# MAGIC #### Understanding Cluster, Session, and Jobs in Databricks
# MAGIC   - Cluster: The underlying compute engine (set of nodes) that processes Spark workloads.
# MAGIC   - Session: A Spark application (or interactive notebook session) that runs within a cluster.
# MAGIC   - Job: A specific task or script executed within a session.
# MAGIC
# MAGIC **Note: Each user or notebook can create a separate session, even if they are using the same cluster.**
# MAGIC
# MAGIC #### How Multiple Sessions Work in a Single Cluster
# MAGIC   - In Databricks, multiple users can attach different notebooks to the same cluster.
# MAGIC   - Each notebook operates in its own session, meaning temporary views or variables are not shared between notebooks.
# MAGIC   - Global temporary views (GLOBAL TEMP VIEW) can be shared across sessions but require the global_temp namespace.
# MAGIC
# MAGIC **Note: Thats why global temp view can be access all over any session(but require the global_temp namespace.) while session scoped/temp view are not access accross all session they can access within same session.**

# COMMAND ----------

# MAGIC %md
# MAGIC ### Terms Explanation
# MAGIC 1. Uncache: 
# MAGIC   - `UNCACHE TABLE table_name`
# MAGIC   - Removes the table from the cache.
# MAGIC   - Used when you explicitly want to remove cached data (useful for in-memory caching).
# MAGIC
# MAGIC 2. Cache:
# MAGIC   - `Cache Table table_name`
# MAGIC   - Forces the table to be fully cached in memory for faster queries.
# MAGIC
# MAGIC 3. Broadcast:
# MAGIC   - BROADCAST in Spark is used to optimize joins by broadcasting (copying) a small table to all worker nodes, reducing shuffling during a join operation.
# MAGIC   - However, there is no BROADCAST TABLE command in Spark SQL. Instead, the broadcast hint is applied in PySpark or SQL queries.
# MAGIC   - Used for broadcast joins (small tables)
# MAGIC vg
# MAGIC 3. Refresh Table:
# MAGIC   - When using external tables with formats like CSV, JSON, TEXT, or BINARY, Spark caches metadata and file locations after the first query. This means:
# MAGIC       - New files added to the external storage won’t be detected in the same session unless explicitly refreshed.
# MAGIC   - `Refesh Table table_name`

# COMMAND ----------

# MAGIC %md
# MAGIC #### Constraints Supported by Delta Tables
# MAGIC Delta Lake supports constraints to enforce data integrity. The main types of constraints in Delta tables are:
# MAGIC
# MAGIC |Constraint Type|	Supported?	|Description|
# MAGIC |-----------------|---------|-----------|
# MAGIC |Primary Key (PK)|	 No|	Delta does not enforce primary keys but can be simulated using constraints.|
# MAGIC |Foreign Key (FK)	| No|	Delta does not support foreign keys natively.|
# MAGIC |Unique Constraint|	 No	|No native UNIQUE constraint, but can be enforced using a Merge or Dedupe strategy.|
# MAGIC |NOT NULL|	 Yes|	Ensures a column cannot have NULL values.|
# MAGIC |CHECK Constraint|	Yes	|Ensures column values meet specific conditions.|

# COMMAND ----------

# MAGIC %md
# MAGIC ### Terms Explanation:
# MAGIC 1. SHALLOW CLONE: 
# MAGIC   - If you wish to create a copy of a table quickly to test out applying changes without the risk of modifying the current table, SHALLOW CLONE can be a good option. Shallow clones just copy the Delta transaction logs, meaning that the data doesn't move so it can be very quick.
# MAGIC   - `CREATE OR REPLACE TABLE {new_table_name} SHALLOW CLONE {source_table_name}|[LOCATION path]`
# MAGIC
# MAGIC 2. DEEP CLONE: 
# MAGIC   - fully copies data and metadata from a source table to a target. This copy occurs incrementally, so executing this command again can sync changes from the source to the target location. It copies all of the data and transaction logs this can take a long time based on the size of the table.
# MAGIC   - `CREATE OR REPLACE TABLE {new_table_name} DEEP CLONE {source_table_name}|[LOCATION path]`