# Databricks notebook source
# MAGIC %md
# MAGIC ### Identify where Delta Lake provides ACID transactions
# MAGIC 1. **Data writes and updates**: Data Lake esures these process are atomic and isolated. This means that partial writes are not visible until the transaction is complete, and conflicts are managed to maintain consistency.
# MAGIC 2. **Data Versioning and Time Travel**: Delta Lake uses a transaction log (also known as the Delta Log) to track all changes made to the data. This log ensures that every operation is recorded as a transaction, enabling ACID guarantees. It also allows for time travel, where users can query previous versions of the data.
# MAGIC 3. **Merge, Update and Delete Operation**: Delta Lake supports complex operations like MERGE, UPDATE, and DELETE on large datasets. These operations are executed as ACID transactions, ensuring that changes are applied atomically and consistently.
# MAGIC 4. **Streaming and Batch Processing**:  In streaming scenarios, it ensures that data is ingested in an ACID-compliant manner, even when multiple streams are writing to the same table simultaneously.
# MAGIC 5. **Schema enforcement and evolution**: When schema changes are applied to a Delta Lake table, these changes are handled as ACID transactions. This ensures that schema updates do not corrupt the data or leave it in an inconsistent state.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify the benefits of ACID transaction
# MAGIC 1. Atomicity: 
# MAGIC     - Ensures that a transaction is treated as a single, indivisible unit of work.
# MAGIC     - Impact: If any part of the transaction fails, the entire transaction is rolled back, leaving the system in its original state. This prevents partial updates or corrupt data, which is crucial for maintaining data integrity.
# MAGIC 2. Consistency: 
# MAGIC     - Guarantees that a transaction brings the system from one valid state to another, adhering to all defined rules (e.g., constraints, schemas, and business logic).
# MAGIC     - Impact: Ensures that data remains accurate and valid after every transaction, reducing the risk of errors or inconsistencies in the dataset.
# MAGIC 3. Isolation: 
# MAGIC     - Ensures that once a transaction is committed, its changes are permanent and will survive
# MAGIC     - Impact: Provides reliability and trust in the system, as users can be confident that their data will not be lost after a successful transaction.
# MAGIC 4. Durability: 
# MAGIC     - Ensures that once a transaction is committed, its changes are permanent and will survive system failures (e.g., crashes, power outages).
# MAGIC     - Impact: Provides reliability and trust in the system, as users can be confident that their data will not be lost after a successful transaction.
# MAGIC
# MAGIC Additional benifit of ACID property:  Data Integrity, Error Recovery, Time Travel, Auditing, Concurrency Supports.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify whether a transaction is ACID-compliant
# MAGIC 1. Atomicity: 

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data:
# MAGIC - Data refers to the raw, unprocessed facts, numbers, or observations that represent information. It can be structured (e.g., databases), semi-structured (e.g., JSON, XML), or unstructured (e.g., text, images).
# MAGIC - Example: A customer's name, age, and purchase history in a sales database.
# MAGIC ### Metadata: 
# MAGIC - Metadata is **data about data**. It provides context, description, or additional information about the data, such as its source, format, creation date, or purpose.
# MAGIC - Example: The file size, creation date, and author of a document.
# MAGIC - Types: 
# MAGIC     - Descriptive ->  Describes the content (e.g., title, author, keywords)
# MAGIC     - Structural -> Describes the organization of data (e.g., file format, relationships between tables)
# MAGIC     - Administrative Metadata ->  Provides management information (e.g., access rights, creation date).
# MAGIC ### Comparision of Data and Metadata: 
# MAGIC
# MAGIC |Aspect	|Data|	Metadata|
# MAGIC |-------|----|---------|
# MAGIC |Definition|	Raw facts or observations.	|Information about the data.|
# MAGIC |Purpose	|Used for analysis and decision-making.	|Used to organize, manage, and understand data.|
# MAGIC |Examples	|Sales figures, customer names.	|File size, creation date, author.|
# MAGIC |Storage	|Stored in databases or files.	|Stored in headers, catalogs, or repositories.|
# MAGIC |Dependency	|Can exist without metadata.	|Cannot exist without data.|
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Managed Tables
# MAGIC Managed tables are fully controlled by the data management system (e.g., Spark, Delta Lake). The system manages both the metadata (table definition) and the data (actual files) for these tables.
# MAGIC
# MAGIC Storage: The data for managed tables is stored in a location controlled by the system, typically within a predefined directory (e.g., the spark-warehouse directory in Spark).
# MAGIC
# MAGIC Lifecycle: When a managed table is dropped, both the metadata (table schema) and the underlying data files are deleted. This ensures no orphaned data remains.
# MAGIC
# MAGIC Use Case: Ideal for scenarios where the data is exclusively managed by the system and does not need to be shared outside of it.
# MAGIC
# MAGIC Code: `CREATE TABLE managed_table (id INT, name STRING);`
# MAGIC
# MAGIC ### External Tables
# MAGIC External tables are tables where the data is stored in an external location (e.g., cloud storage like AWS S3, Azure Data Lake, or HDFS), and the system only manages the metadata (table definition).
# MAGIC
# MAGIC Storage: The data for external tables resides in a user-specified location outside the system's control. The system only maintains the metadata (e.g., schema, table properties).
# MAGIC
# MAGIC Lifecycle: When an external table is dropped, only the metadata is deleted. The underlying data files remain intact in the external location.
# MAGIC
# MAGIC Use Case: Ideal for scenarios where the data is shared across multiple systems or applications, or when the data needs to persist independently of the table definition.
# MAGIC
# MAGIC Code: `CREATE TABLE external_table (id INT, name STRING) LOCATION 's3://my-bucket/external-table';`
# MAGIC
# MAGIC ### Compare: 
# MAGIC
# MAGIC |Aspect	|Managed Tables| 	External Tables|
# MAGIC |-------|--------------|-----------------|
# MAGIC |Data Storage	|Stored in a system-controlled location.|	Stored in an external, user-specified location.|
# MAGIC |Lifecycle Management	|Both metadata and data are managed by the system.|	Only metadata is managed by the system; data is managed externally.|
# MAGIC |Dropping the Table|	Deletes both metadata and data.|	Deletes only metadata; data remains intact.|
# MAGIC |Use Case|	Data is exclusive to the system.|	Data is shared across systems or applications.|
# MAGIC |Example Location|	spark-warehouse directory.|	AWS S3, Azure Data Lake, HDFS, etc.|

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify scenario to use an external tables
# MAGIC A common scenario to use an external table is when you need to share data across multiple systems or applications while maintaining control over the data's storage location and lifecycle.
# MAGIC -  Sharing Inventory Data Across Multiple Workloads
# MAGIC - No Accidental Data deletion
# MAGIC - Easy Data Updates
# MAGIC - Multiple work load can access the data

# COMMAND ----------

# MAGIC %md
# MAGIC #### Create a managed table
# MAGIC A managed table means that Databricks / Hive manages both the metadata and the underlying data. If you drop the table, the data is also deleted.
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE osa_inventory (
# MAGIC     date DATE,
# MAGIC     store_id INT,
# MAGIC     sku INT,
# MAGIC     product_category STRING,
# MAGIC     total_sales_units INT,
# MAGIC     on_hand_inventory_units INT,
# MAGIC     replenishment_units INT,
# MAGIC     inventory_pipeline INT,
# MAGIC     units_in_transit INT,
# MAGIC     units_in_dc INT,
# MAGIC     units_on_order INT,
# MAGIC     units_under_promotion INT,
# MAGIC     shelf_capacity INT
# MAGIC )
# MAGIC USING DELTA;
# MAGIC
# MAGIC df.write.format("delta") \
# MAGIC     .mode("overwrite") \
# MAGIC     .saveAsTable("osa_inventory")
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify the location of a table
# MAGIC - `DESCRIBE EXTENDED osa_inventory;`
# MAGIC - `DESCRIBE FORMATTED osa_inventory;`
# MAGIC - `DESCRIBE DETAIL osa_inventory`
# MAGIC - `table_location = spark.sql("DESCRIBE DETAIL osa_inventory").select("location").collect()[0][0] print(f"Table Location: {table_location}")`

# COMMAND ----------

# MAGIC %md
# MAGIC ### Inspect the directory structure of Delta Lake file
# MAGIC
# MAGIC Delta Lake stores data in Parquet files with a transaction log (_delta_log/) for ACID compliance. You can inspect the directory structure to understand how Delta Lake manages data.
# MAGIC
# MAGIC osa_inventory/                         # Root Delta table directory
# MAGIC
# MAGIC - part-00000-xyz.snappy.parquet      # Parquet data file (partitioned)
# MAGIC
# MAGIC - part-00001-abc.snappy.parquet      # Another Parquet data file
# MAGIC
# MAGIC - _delta_log/                        # Transaction log directory
# MAGIC
# MAGIC     - 00000000000000000001.json       # JSON log of first transaction
# MAGIC
# MAGIC     -  00000000000000000002.json       # JSON log of second transaction
# MAGIC     
# MAGIC     - 00000000000000000004.checkpoint.parquet  # Checkpoint file
# MAGIC

# COMMAND ----------

# Replace <path> with the actual table location from DESCRIBE DETAIL
dbutils.fs.ls("dbfs:/user/hive/warehouse/osa_inventory")

dbutils.fs.ls("dbfs:/user/hive/warehouse/osa_inventory/_delta_log/")


# COMMAND ----------

df = spark.read.json("dbfs:/user/hive/warehouse/osa_inventory/_delta_log/00000000000000000000.json")
df.show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify who has written previous versions of a table.
# MAGIC Delta lake maintain the transaction logs inside the _delta_log/ directory which contain metadata about every change to a table. You can inspect these logs to find out who modified the table, when, and how.

# COMMAND ----------

# MAGIC %sql
# MAGIC Describe history delta.`dbfs:/user/hive/warehouse/osa_inventory`

# COMMAND ----------

# MAGIC %md
# MAGIC ### Roll back a table to a previous version.
# MAGIC Delta Lake allows you to restore a table to a previous version using Time Travel. You can roll back your table by specifying a timestamp or version number.

# COMMAND ----------

# Load previous version
df = spark.read.format("delta").option("versionAsOf", 3).load("dbfs:/user/hive/warehouse/osa_inventory")

# Overwrite current table
df.write.format("delta").mode("overwrite").save("dbfs:/user/hive/warehouse/osa_inventory")


# COMMAND ----------

# MAGIC %sql
# MAGIC RESTORE TABLE osa_inventory TO VERSION AS OF 3;
# MAGIC
# MAGIC -- another way
# MAGIC
# MAGIC CREATE OR REPLACE TABLE osa_inventory AS 
# MAGIC SELECT * FROM osa_inventory VERSION AS OF 3;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Query a specific version of a table
# MAGIC Delta Lake supports Time Travel, which allows you to query a table at a specific version or as of a certain timestamp.

# COMMAND ----------

# query using version
df = spark.read.format("delta").option("versionAsOf", 3).load("dbfs:/user/hive/warehouse/osa_inventory")
df.show()

# query using timestamp
df = spark.read.format("delta").option("timestampAsOf", "2025-01-30 10:15:00").load("dbfs:/user/hive/warehouse/osa_inventory")
df.show()


# COMMAND ----------

# MAGIC %sql
# MAGIC -- query using version
# MAGIC SELECT * FROM osa_inventory VERSION AS OF 3;
# MAGIC
# MAGIC -- query using time stamp
# MAGIC SELECT * FROM osa_inventory TIMESTAMP AS OF '2025-01-30 10:15:00';
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify why Zordering is beneficial to Delta Lake table
# MAGIC
# MAGIC Z-Ordering (or Z-Order Clustering) is an optimization technique in Delta Lake that improves query performance by reducing the amount of data scanned. It is particularly beneficial when querying large datasets with filter conditions on specific columns.
# MAGIC
# MAGIC Z-Ordering reorders data within files based on specific columns to keep similar values physically close. This helps Databricks optimize queries by reducing the number of files read.
# MAGIC
# MAGIC When to Use Z-Ordering?
# MAGIC
# MAGIC Apply Z-Ordering when:
# MAGIC   - Queries frequently filter on specific columns
# MAGIC   - The table has large datasets (TB-scale)
# MAGIC   - You use multiple partition columns (avoids small files issue)
# MAGIC
# MAGIC When NOT to Use:
# MAGIC   - When the table is small (Z-Ordering benefits large tables)
# MAGIC   - When updates/deletes are frequent (Reclustering can be costly)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sales WHERE region = 'California';
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC How to Apply Z-Ordering
# MAGIC
# MAGIC You can optimize a Delta table using Z-Ordering with the OPTIMIZE command:

# COMMAND ----------

OPTIMIZE osa_inventory ZORDER BY (store_id, sku);

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify the kind of files Optimize compacts
# MAGIC The OPTIMIZE command in Delta Lake compacts small files into fewer but larger Parquet files to improve query performance and storage efficiency.
# MAGIC What Files does OPTIMIZE Compact?
# MAGIC
# MAGIC 1. Small Parquet Files
# MAGIC     - Delta Lake writes many small Parquet files due to frequent updates, inserts, and deletes.
# MAGIC     - OPTIMIZE merges these small files into larger ones, reducing file fragmentation.
# MAGIC 2. Files Within the Same Partition
# MAGIC     - Delta Lake compacts files inside each partition to ensure efficient scanning.
# MAGIC     - Example: If osa_inventory is partitioned by date, only files in the same date partition are merged together.
# MAGIC 3.  Stale Files That Increase Read Costs
# MAGIC     - If your Delta table has many small files, Spark has to scan more files to execute a query, leading to high read costs.
# MAGIC     - OPTIMIZE helps reduce the number of files, making queries faster and more efficient.
# MAGIC
# MAGIC What Files OPTIMIZE Does NOT Compact?
# MAGIC
# MAGIC Already Optimized Large Files
# MAGIC   - If a file is already large (default ~1GB), OPTIMIZE does not merge it further.
# MAGIC   
# MAGIC Deleted Files (Until VACUUM Runs)
# MAGIC   - OPTIMIZE does not remove deleted files—it just compacts existing ones.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify CTAS as a solution
# MAGIC CTAS (CREATE TABLE AS SELECT) is a powerful solution in Delta Lake and Databricks for creating new tables based on query results. It is useful for data transformations, schema changes, and performance improvements.
# MAGIC
# MAGIC CTAS creates a new table by selecting data from an existing table using a SQL query.
# MAGIC
# MAGIC When to Use the CTAS(create table as select): 
# MAGIC - Schema Transformation
# MAGIC - Performance Optimization
# MAGIC - Data Archival and Backup
# MAGIC - Filtering and Duplication

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE new_table
# MAGIC AS
# MAGIC SELECT * FROM existing_table WHERE condition;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a generated column
# MAGIC A generated column is a virtual column in a Delta table whose values are calculated based on expressions or other columns. This column is not physically stored in the table but is computed at query time.
# MAGIC
# MAGIC Types of generated column
# MAGIC 1. Virtual Column: Values are computed when queried and are not stored physically.
# MAGIC 2. Persisted Column: Values are computed when inserted or updated and are physically stored

# COMMAND ----------

# MAGIC %sql
# MAGIC --  Virtual Generated Column
# MAGIC CREATE TABLE osa_inventory_with_generated AS
# MAGIC SELECT *,
# MAGIC   (on_hand_inventory_units + units_in_transit + units_on_order) AS total_inventory
# MAGIC FROM osa_inventory;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Persisted Generated Column
# MAGIC CREATE TABLE osa_inventory_with_persisted_generated (
# MAGIC   store_id INT,
# MAGIC   sku INT,
# MAGIC   on_hand_inventory_units INT,
# MAGIC   units_in_transit INT,
# MAGIC   units_on_order INT,
# MAGIC   total_inventory INT GENERATED ALWAYS AS (on_hand_inventory_units + units_in_transit + units_on_order) STORED
# MAGIC )
# MAGIC USING DELTA;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Benefits of Generated Columns
# MAGIC - Reduced Redundancy: Automatically calculate values instead of storing them.
# MAGIC - Improved Performance: Prevents recalculation and reduces storage overhead for derived data.
# MAGIC - Data Integrity: Ensures calculated values are always in sync with the base columns.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Add a table comment.
# MAGIC Adding a table comment in Delta Lake helps provide metadata about the purpose, structure, or other important details of the table. It can be helpful for data documentation and understanding the context of the table when querying or managing it.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE osa_inventory (
# MAGIC     store_id INT,
# MAGIC     sku INT,
# MAGIC     total_sales_units INT,
# MAGIC     units_in_transit INT,
# MAGIC     units_on_order INT
# MAGIC ) COMMENT 'This table tracks store inventory levels, sales, and promotions'
# MAGIC USING DELTA;
# MAGIC
# MAGIC -- using the alter command to add the comments
# MAGIC ALTER TABLE table_name
# MAGIC SET TBLPROPERTIES ('comment' = 'This table tracks store inventory levels, sales, and promotions.');

# COMMAND ----------

# MAGIC %md
# MAGIC ### IMP: Databricks notebooks support automatic change tracking and versioning.
# MAGIC
# MAGIC When you are editing the notebook on the right side check version history to view all the changes, every change you are making is captured and saved.

# COMMAND ----------

# MAGIC %md
# MAGIC #### Increasing cluster size of SQL Endpoint: 
# MAGIC
# MAGIC It refers to scaling up the computational resources of a SQL Endpoint by increasing the number of nodes (or the power of existing nodes) in the cluster that runs the SQL queries.
# MAGIC
# MAGIC Why Increase the Cluster Size?
# MAGIC   -  To improve performance for complex queries.
# MAGIC   -  To handle larger datasets efficiently.
# MAGIC   -  To reduce query execution time for real-time analytics.
# MAGIC   -  To support more concurrent users running queries simultaneously.