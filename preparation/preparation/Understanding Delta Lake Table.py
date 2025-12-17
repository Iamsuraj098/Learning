# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE Table IF NOT EXISTS employees
# MAGIC (id INT, name String, salary Double);

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS Customers (
# MAGIC   id INT,
# MAGIC   name STRING,
# MAGIC   salary DOUBLE
# MAGIC )
# MAGIC USING DELTA;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC We can dalta table by using the "Using Delta" this code or directly create it, in both cases Delta Table is created automatically.

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE detail default.employees

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog `hive_metastore`; select * from `default`.`customers` limit 100;

# COMMAND ----------

dbutils.fs.ls("dbfs:/user/hive/warehouse/")

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history default.employees

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT into table default.employees
# MAGIC VALUES (1, "Joker", 1222.2);

# COMMAND ----------

# MAGIC %sql
# MAGIC Describe history default.employees;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- selecting the table using the version. This is imp feature of delta table which is Time Stamp.
# MAGIC select * from default.employees version as of 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT into table default.employees
# MAGIC VALUES (2, "Jira", 1222002.2);

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from default.employees;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Now by using time stamp Elena  we can rollback Koshka to our older version.
# MAGIC RESTORE table default.employees version as of 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from default.employees
# MAGIC -- our oler version of this employees table is retrevie.

# COMMAND ----------

# MAGIC %sql
# MAGIC Optimize default.employees
# MAGIC Zorder by id;

# COMMAND ----------

# MAGIC %md
# MAGIC Hive Metastore: it is repository  of database and schemas.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Now we are creating new schema
# MAGIC Create SCHEMA new_default;

# COMMAND ----------

# MAGIC %sql
# MAGIC use new_default;
# MAGIC create table sales
# MAGIC (id int, name string, price double);
# MAGIC insert into sales values(1, "Toy", 123456);

# COMMAND ----------

# MAGIC %md
# MAGIC Creating Delta Lake Table using the CTAS statement.
# MAGIC
# MAGIC CTAS - create table as Select
# MAGIC
# MAGIC CTAS - automaticaly infere the schema from the query result.
# MAGIC
# MAGIC Additional functinality of CTAS statement
# MAGIC
# MAGIC ex: 
# MAGIC
# MAGIC create table new_table_name
# MAGIC
# MAGIC Comment "any_want_to_leave"
# MAGIC
# MAGIC partioned by "column_name_of_table"
# MAGIC
# MAGIC Location "directory_where_this_table_store"
# MAGIC
# MAGIC as
# MAGIC
# MAGIC Select * from any_table
# MAGIC
# MAGIC
# MAGIC #### Partitioning
# MAGIC - Partitioning in Delta Tables is done to optimize data storage and query performance by organizing data based on specific columns.
# MAGIC - Partitioning in Delta Lake (and other data storage systems like Hive or Parquet) is a technique to physically divide the dataset into smaller, organized subsets based on the values in one or more columns. It helps improve query performance, manageability, and scalability for large datasets.
# MAGIC - what partitioning does exactly
# MAGIC   - Organizes Data into Subdirectories
# MAGIC   - Reduces Data Scanning (Partition Pruning)
# MAGIC   - Enables Parallel Processing
# MAGIC   - Optimizes Write Operations
# MAGIC   - Improves File Organization
# MAGIC   

# COMMAND ----------

# MAGIC %md
# MAGIC #### Table Constraint
# MAGIC 1. Not Null Constraint
# MAGIC 2. Check Constraint
# MAGIC
# MAGIC Syntax: ALter Table_name add constraint contraint_name constraint_details
# MAGIC
# MAGIC Ex: Alter Table orderes add constraint valid_date Check(date > '2020-01-01');
# MAGIC
# MAGIC #### Shallow Clone
# MAGIC - Quickly create a copy of table
# MAGIC   - just copy the Delta Transaction Log
# MAGIC - Create Table table_name Shallow Clone source_table. 
# MAGIC
# MAGIC Cloning is a best to test data so parent/original data is remain unchange.
# MAGIC
# MAGIC
# MAGIC #### Views:
# MAGIC Views are three types:
# MAGIC 1. Stored Views - Syntax: Create View view_name AS query
# MAGIC 2. Temporary Views - Syntax: Create Temporary/Temp View view_name AS query
# MAGIC 3. Global Temporary Views - Syntax: Create Global Temp/Temporary View view_name AS query

# COMMAND ----------

# MAGIC %md
# MAGIC # ETL
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Query Filing
# MAGIC -- select * from json.`dbfs:/FileStore/tables/Data/employee_data-1.json`;
# MAGIC Create or Replace table employee as
# MAGIC select * from json.`dbfs:/FileStore/tables/Data/employee_data-1.json`;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from default.employee

# COMMAND ----------

# MAGIC %sql
# MAGIC select *, input_file_name() as source_file from json.`dbfs:/FileStore/tables/Data/employee_data-1.json`;
# MAGIC -- input)file_name() -> it give the details source file.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- another weay of quering files
# MAGIC select * from text.`dbfs:/FileStore/tables/Data/employee_data-1.json`;
# MAGIC
# MAGIC -- text -> can qury ant type of file it may be json, csv, parquet etc.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- way of querying files.
# MAGIC select * from binaryFile.`dbfs:/FileStore/tables/Data/employee_data-1.json`;
# MAGIC
# MAGIC -- it give all details about the file like when it modified, time, lenght etc.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from csv.`dbfs:/FileStore/tables/sf_fire_calls.csv`
# MAGIC
# MAGIC
# MAGIC --we can refresh table also
# MAGIC -- Refresh Tbale table_name

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE EXTENDED book_csv

# COMMAND ----------

# MAGIC %md
# MAGIC # ETL using python

# COMMAND ----------

spark.read.table("book_csv").write.mode("append").format("csv"),option('header', 'true').option('delimiter', ';').save()