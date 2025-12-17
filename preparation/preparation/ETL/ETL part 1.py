# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Extract data from a single file and from a directory of files
# MAGIC   - Here we read the files using both sql and python.

# COMMAND ----------

from pyspark import *

# COMMAND ----------

df = spark.read.csv('dbfs:/FileStore/tables/sf_fire_calls.csv')

# COMMAND ----------

display(df);

# COMMAND ----------

df2 = spark.read.option("header", "true").csv(
    "dbfs:/FileStore/tables/sf_fire_calls.csv"
)

# here header  -> true means first row contains the column names.

# COMMAND ----------

df3 = (
    spark.read.option("header", "true")
    .option("infereSchema", "true")
    .parquet("/FileStore/tables/Data/summary.parquet")
)
df3.show()

# here infereSchema -> true means its automatically infere the scehma.

# COMMAND ----------

df4 = (
    spark.read.format("parquet")
    .option("header", "true")
    .option("infereSchema", "true")
    .load("/FileStore/tables/Data/summary.parquet")
)
df4.show()
# here format() -> define the file type which cluster read the file in future.

# COMMAND ----------

display(spark.read.parquet('dbfs:/FileStore/tables/Data/summary.parquet'))

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from csv.`dbfs:/FileStore/tables/sf_fire_calls.csv`

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from parquet.`dbfs:/FileStore/tables/Data/summary.parquet`

# COMMAND ----------

# MAGIC %md
# MAGIC #### Note: 
# MAGIC 1. read (Batch Processing)
# MAGIC     - Method: Spark.read
# MAGIC     - Purpose: Reads the entire dataset at once (batch mode).
# MAGIC     - Use Case: When working with static datasets or running ad-hoc queries.
# MAGIC     - Behavior: Loads all data into memory at once.
# MAGIC     - Supported Formats: CSV, JSON, Parquet, Delta, etc
# MAGIC 2. write(Batch Processing)
# MAGIC     - Used in batch processing mode.
# MAGIC     - Writes data to a specified sink (e.g., Parquet, CSV, Delta, JDBC).
# MAGIC     - Commonly used for saving static DataFrames.
# MAGIC 2. readStream (Streaming Processing)
# MAGIC     - Method: Spark.readStream
# MAGIC     - Purpose: Reads data continuously as new records arrive (streaming mode).
# MAGIC     - Use Case: When working with real-time data sources such as Kafka, Delta Tables, or File Streams.
# MAGIC     - Behavior: Loads only newly arriving data incrementally.
# MAGIC     - Supported Formats: Kafka, Delta, JSON, Parquet, etc.
# MAGIC 3. readWrite(Streaming Processing)
# MAGIC     - Used in structured streaming to write data continuously as new data arrives.
# MAGIC     - Requires a trigger and a checkpoint location.
# MAGIC     - Supports append, complete, and update output modes.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Identify the prefix included after the FROM keyword as the data type
# MAGIC In Spark SQL, the prefix included after the FROM keyword is used to indicate the data source type. This prefix specifies how Spark should interpret and process the data. 
# MAGIC Common Prefixes and Their Meanings:
# MAGIC - Delta : Refer for the `delta live tables`
# MAGIC - Parquet : refer for `parquet` files
# MAGIC - CSV: refer for the `csv` files
# MAGIC - JSON: refer for `json` file.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from csv.`dbfs:/FileStore/tables/sf_fire_calls.csv`

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Create a view, a temporary view, and a CTE as a reference to a files 

# COMMAND ----------

df2.createTempView("pre_0")

# COMMAND ----------

df2.createOrReplaceTempView("pre_1");

# COMMAND ----------

df2.createGlobalTempView("pre_2");

# COMMAND ----------

df2.createOrReplaceGlobalTempView("pre_3");

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from pre_0;
# MAGIC select * from pre_1;
# MAGIC select * from global_temp.pre_2;
# MAGIC select * from global_temp.pre_3;

# COMMAND ----------

# we can also write sql command inside the spark commant: 
spark.sql("select * from global_temp.pre_2").show()

# COMMAND ----------

# we can also create a sample table using the dataframe crated views
spark.sql("CREATE OR REPLACE temp VIEW my_view AS SELECT * FROM pre_0")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from my_view;

# COMMAND ----------

# MAGIC %md
# MAGIC - Create a Common Table Expression (CTE)
# MAGIC
# MAGIC A CTE is a temporary named result set used within a single SQL query. It is not stored in the catalog and only exists for the query's scope.

# COMMAND ----------

spark.sql("""
WITH my_data2 AS (
  SELECT * FROM pre_0
)
SELECT * FROM my_data2
""");

# we can't use the my_data2 out this sql command.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from my_data2

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Difference between temp view and global temp view: 
# MAGIC temp:
# MAGIC - Accessible only in the session where it was created.
# MAGIC - If the session ends, the view is dropped automatically.
# MAGIC
# MAGIC global temp view: 
# MAGIC - Accessible across all sessions and notebooks running on the same cluster.
# MAGIC - The view name must always be prefixed with global_temp.
# MAGIC
# MAGIC #### Difference between the 
# MAGIC | **Feature**             | **View**                         | **Temporary View/Session Scoped Temp View**               | **CTE**                                  |
# MAGIC |--------------------------|-----------------------------------|-----------------------------------|------------------------------------------|
# MAGIC | **Persistence**          | Persistent across sessions       | Exists only for the current session | Exists only for the current query        |
# MAGIC | **Registration Method**  | `CREATE VIEW`                   | `createOrReplaceTempView`         | `WITH ...` syntax                        |
# MAGIC | **Catalog**              | Stored in Spark's catalog        | Not stored in the catalog         | Not stored anywhere                      |
# MAGIC | **Use Case**             | Reusable across multiple sessions | Session-specific queries          | Query-specific transformations           |
# MAGIC
# MAGIC
# MAGIC Note: 
# MAGIC 1. Both global and local temporary views are deleted when the cluster is restarted, though global views are available to other sessions while the cluster is running.
# MAGIC 2. During notebook deattach or attach then temporary view is disapear but global temporary view remain persistent.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Identify that tables from external sources are not Delta Lake tables.
# MAGIC
# MAGIC To identify whether tables from external sources are not Delta Lake tables, you can check the table's provider or metadata.
# MAGIC To check: 
# MAGIC - Describe Extend command
# MAGIC - Data source prefix (point - 2)
# MAGIC - Check for the _delta_log Directory
# MAGIC
# MAGIC | **Check Method**                  | **Delta Lake Table**            | **Non-Delta Lake Table**                   |
# MAGIC |-----------------------------------|---------------------------------|--------------------------------------------|
# MAGIC | **Provider** (`DESCRIBE EXTENDED`) | `delta`                        | `parquet`, `csv`, `json`, `jdbc`, etc.     |
# MAGIC | **Transaction Log** (`_delta_log`) | Exists                         | Does not exist                             |
# MAGIC | **Data Source Prefix**            | Not required                   | Often includes the file format prefix      |
# MAGIC
# MAGIC
# MAGIC #### Note: 
# MAGIC Delta lake is
# MAGIC - Open source
# MAGIC - Builds up on standard data format
# MAGIC - Optimized for cloud object storage
# MAGIC - Built for scalable metadata handling
# MAGIC
# MAGIC Delta lake is not
# MAGIC - Proprietary technology
# MAGIC - Storage format
# MAGIC - Storage medium
# MAGIC - Database service or data warehouse

# COMMAND ----------

# MAGIC %sql
# MAGIC USE samples;
# MAGIC
# MAGIC DESCRIBE EXTENDED tpch.customer;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Create a table from a JDBC connection and from an external CSV files

# COMMAND ----------

# Create a Table from a JDBC Connection
# JDBC connection parameters
jdbc_url = "jdbc:mysql://hostname:3306/database_name"
table_name = "your_table"
properties = {
    "user": "your_username",
    "password": "your_password",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Load data from the JDBC connection into a DataFrame
df = spark.read.jdbc(url=jdbc_url, table=table_name, properties=properties)

# Create a table in Spark from the DataFrame
df.createOrReplaceTempView("jdbc_table")

# Query the table
spark.sql("SELECT * FROM jdbc_table").show()

# COMMAND ----------

# MAGIC %sql
# MAGIC --external SQL table by connecting to a local instance of an SQLite database using JDBC
# MAGIC CREATE TABLE <jdbcTable>
# MAGIC USING org.apache.spark.sql.jdbc or JDBC
# MAGIC OPTIONS (
# MAGIC     url = "jdbc:<databaseServerType>://<jdbcHostname>:<jdbcPort>",
# MAGIC     dbtable " = <jdbcDatabase>.atable",
# MAGIC     user = "<jdbcUsername>",
# MAGIC     password = "<jdbcPassword>"
# MAGIC )

# COMMAND ----------

#  Create a Table from an External CSV File
# Load data from the CSV file into a DataFrame
df_csv = spark.read.csv("/path/to/external/csv_file.csv", header=True, inferSchema=True)

# Create a table from the DataFrame
df_csv.createOrReplaceTempView("csv_table")

# Query the CSV table
spark.sql("SELECT * FROM csv_table").show()


# COMMAND ----------

# MAGIC %md
# MAGIC ### 6. Identify how the count_if function and the count where x is null can be used
# MAGIC 1. Count_if function: The count_if function counts the number of rows that satisfy a given condition. It is similar to the COUNT function, but it allows you to apply a condition directly.
# MAGIC 2. Count funciton with where x is null

# COMMAND ----------

# MAGIC %sql
# MAGIC -- count_if()
# MAGIC -- select * from tpch.customer;
# MAGIC
# MAGIC select count_if(c_nationkey > 10) from tpch.customer;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- count()
# MAGIC select count(*) from tpch.customer where c_nationkey is null;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 7. Identify how the count(row) skips NULL values.
# MAGIC
# MAGIC - In SQL, the COUNT(row) function counts the number of rows in a result set, but it skips rows where the specified column(s) contain NULL values
# MAGIC - If i pass any argument inside the count(), then it only count the not_null values.
# MAGIC - COUNT(*): Includes all rows, regardless of NULL values in any column.

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(c_nationkey) as number_of_national_key from tpch.customer;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 8. Deduplicate rows from an existing Delta Lake table.
# MAGIC 1. Distinct: Removes all duplicate rows in the table.
# MAGIC 2. DropDuplicate
# MAGIC     - removes duplicate rows based on all columns.
# MAGIC     - You can specify specific columns to drop duplicates based on those columns only.

# COMMAND ----------

# MAGIC %sql
# MAGIC select distinct * from delta.`path`

# COMMAND ----------

df6 = df2.dropDuplicates()
display(df6)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 9. Create a new table from an existing table while removing duplicate rows.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE emergency
# MAGIC as (
# MAGIC   select distinct * from csv.`dbfs:/FileStore/tables/Data/911.csv`
# MAGIC )

# COMMAND ----------

df = (
    spark.read.format("csv")
    .option("header", "true")
    .option("infereSchema", "true")
    .load("/FileStore/tables/Data/911.csv")
)

df2 = df.dropDuplicates()
df2.write.format('csv').mode('overwrite').save('hive_metastore/default')

# COMMAND ----------

# MAGIC %md
# MAGIC ### 10. Deduplicate a row based on specific columns
# MAGIC 1. DISTINCT: If you want to remove duplicate rows while considering only specific columns for deduplication, use DISTINCT with selected columns.
# MAGIC     - This removes duplicate combinations of column1, column2, and column3.
# MAGIC     - Other columns not included in the SELECT clause will not be part of the result.
# MAGIC 2. Use dropDuplicates: The simplest way to deduplicate based on specific columns is by using the dropDuplicates function.
# MAGIC     - dropDuplicates(["column1", "column2"]) ensures that only one row is kept for each unique combination of column1 and column2.
# MAGIC     - Other columns in the DataFrame are retained, but no guarantee is made about which row is kept for the duplicates.

# COMMAND ----------

# MAGIC %sql
# MAGIC select distinct col1, col2, col3 from any_table

# COMMAND ----------

df7 = spark.read.csv('path')
sample_x = df7.dropDuplicates(['col1', 'col2'])
sample_x.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 11. Validate that the primary key is unique across all rows.
# MAGIC - Approach 1: Find Duplicate Primary Key Values
# MAGIC - Approach 2: Validate Uniqueness (No Results Means Unique)

# COMMAND ----------

# MAGIC %sql 
# MAGIC -- Approach 1
# MAGIC use samples;
# MAGIC -- DESCRIBE table tpch.customer;
# MAGIC
# MAGIC select c_custkey, count(*) as `count`
# MAGIC from tpch.customer
# MAGIC group by c_custkey
# MAGIC having count(*) > 1;
# MAGIC
# MAGIC -- if above code dosen't give any result that means their no any dupicate value in primary key column. 

# COMMAND ----------

# Approach 1
df = spark.read.csv('dbfs:/FileStore/tables/sf_fire_calls.csv')
# display(df);
is_duplicate = df.groupby('_c0').count().filter('count > 1');
is_duplicate.show();

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Approach 2
# MAGIC SELECT CASE 
# MAGIC            WHEN COUNT(*) = COUNT(DISTINCT c_custkey) THEN 'Primary Key is Unique'
# MAGIC            ELSE 'Duplicates Exist in Primary Key'
# MAGIC        END AS validation_result
# MAGIC FROM tpch.customer;

# COMMAND ----------

# approach 2, if both count unique and without unique are equal then no duplicy
total_count = df.count()
unique_count = df.select("_c0").distinct().count()
if total_count == unique_count: 
    print("No duplication")
else:
    print("Their is duplication")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 12. Cast a column to a timestamp

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Cast a Column to Timestamp Using SQL
# MAGIC -- select * from hive_metastore.default.emergency;
# MAGIC
# MAGIC -- select cast(_c5 as timestamp) as Time_stamp, *
# MAGIC -- from hive_metastore.default.emergency limit 10;
# MAGIC
# MAGIC -- or
# MAGIC
# MAGIC select cast(_c5 as date) as Time_stmap, *
# MAGIC from hive_metastore.default.emergency limit 10;

# COMMAND ----------

from pyspark.sql.functions import col

# Example DataFrame
data = [("2025-01-28 15:30:00",), ("2025-01-29 12:45:30",)]
df = spark.createDataFrame(data, ["date_string"])

# Cast the string column to a timestamp
df_with_timestamp = df.withColumn("date_timestamp", col("date_string").cast("timestamp"))
df_with_date = df.withColumn("data", col("date_string").cast("date"))
# Show the result
df_with_timestamp.show()
df_with_date.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 13.  Extract a specific pattern from an existing string column
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import *
df = spark.read.option("infereSchema", "true").csv('dbfs:/FileStore/tables/sf_fire_calls.csv')
# display(df)

df_pattern = df.withColumn("pattern", regexp_extract("_c1", r"(\d+)", 1))
df.show(10)
# display(df_pattern)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE or replace table firefighter as
# MAGIC SELECT * from csv.`dbfs:/FileStore/tables/sf_fire_calls.csv`

# COMMAND ----------

# MAGIC %sql
# MAGIC -- select * from default.firefighter limit 10;
# MAGIC
# MAGIC select regexp_extract("_c1", r"(\d{2})") as pattern
# MAGIC from firefighter limit 10;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 14. Utilize the dot syntax to extract nested data fields
# MAGIC
# MAGIC In both PySpark and SQL, you can use dot syntax to access nested fields in structured data such as JSON, structs, or nested columns.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- select * from json.`dbfs:/FileStore/tables/Data/minifigs.json`
# MAGIC
# MAGIC -- Create or replace table mini as
# MAGIC -- select * from json.`dbfs:/FileStore/tables/Data/minifigs.json` limit 10;
# MAGIC
# MAGIC
# MAGIC -- here result is column which store some json format data, by using the dot operator we fetch the last_modified_dt.
# MAGIC select 
# MAGIC   results.last_modified_dt,
# MAGIC   results.name[0], -- at specific index we can also get data.
# MAGIC   results.num_parts
# MAGIC from default.mini;

# COMMAND ----------

df = (
    spark
    .read
    .format("json")
    .option("header", "true")
    .option("infereSchema", "true")
    .load("/FileStore/tables/Data/minifigs.json")
)
df_dot = df.select("results.num_parts", "results.name");
df_dot.show(10);

# COMMAND ----------

# MAGIC %md
# MAGIC ### 15. Identify the benefits of using array function
# MAGIC
# MAGIC Array functions are powerful tools for handling collections of elements within a single column in a dataset. They provide flexibility for working with lists or arrays directly without the need for complex transformations.
# MAGIC - Efficient Storages and access of data
# MAGIC - Reduce Join Complexity
# MAGIC - Perform Set Operation

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import array, array_contains, explode
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType
spark = SparkSession.builder.appName("ArrayFunctions").getOrCreate()

data = [("Alice", [1, 2, 3, 4]), ("Bob", [5, 6, 7, 8])]
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Array", ArrayType(IntegerType()), True)
])

df_dot = spark.createDataFrame(data, schema)

df_dot.show(truncate=False)
df_dot.select("name", array_contains("number", 3)).show()

# COMMAND ----------

# MAGIC %sql
# MAGIC -- select * from default.mini;
# MAGIC
# MAGIC select 
# MAGIC   *,
# MAGIC   explode(results) as new_result
# MAGIC from default.mini limit 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 16. Parse JSON strings into structs
# MAGIC
# MAGIC In PySpark, the `from_json` function is used to parse JSON strings into struct types. This is particularly useful when working with datasets containing JSON strings that need to be processed as structured data.

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
spark = SparkSession.builder.appName("ParseJSON").getOrCreate()
data = [
    ("Alice", '{"city": "San Francisco", "state": "CA", "age": 30}'),
    ("Bob", '{"city": "New York", "state": "NY", "age": 25}')
]

json_schema = StructType([
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("age", IntegerType(), True)
])

df = spark.createDataFrame(data, ["name", "address_json"])
df_parsed = df.withColumn("address", from_json(col("address_json"), json_schema))
df_parsed.select("name", "address.city", "address.state", "address.age").show(truncate=False)

df.createOrReplaceTempView("json_test");

# COMMAND ----------

# MAGIC %sql
# MAGIC select 
# MAGIC   from_json("address_json", 'STRUCT<city: STRING, state: STRING, age: INT>') as Address
# MAGIC from 
# MAGIC   json_test;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 17. Identify which result will be returned based on a join query.
# MAGIC Its all about inner join, outer join, left join, right join, semi join, anti join.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 18. Identify a scenario to use the explode function versus the flatten function
# MAGIC 1. explode Function
# MAGIC     - Purpose: Converts each element in an array (or each key-value pair in a map) into a separate row.
# MAGIC     - When to Use: Use explode when you want to expand an array into multiple rows, with one row for each element in the  array.
# MAGIC
# MAGIC 2. Flatten Function: 
# MAGIC     - Purpose: Merges multiple arrays into a single array.
# MAGIC     - When to Use: Use flatten when you have nested arrays (arrays within arrays) and want to combine them into a single array
# MAGIC     

# COMMAND ----------

data = [("Alice", ["apple", "banana", "cherry"]),
        ("Bob", ["grape", "orange"])]
df = spark.createDataFrame(data, ["name", "items"])
df_exploded = df.withColumn("item", explode(df.items))
df_exploded.show()

from pyspark.sql.functions import flatten
df_flattened = df.withColumn("items", flatten(df.items))
df_flattened.show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 19. Define a SQL UDF
# MAGIC
# MAGIC A SQL UDF (User Defined Function) is a function that allows you to extend the functionality of SQL queries by defining custom logic that is not available in standard SQL functions. SQL UDFs are commonly used when the built-in SQL functions are insufficient for a specific task.
# MAGIC
# MAGIC SQL UDFs can be created in SQL-based databases or distributed data systems (like Spark) to perform complex operations directly within SQL queries. You define a SQL UDF to be used in a query, just like any other SQL function.

# COMMAND ----------

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def to_Upper_case(text):
    if text:
        return text.upper()
    return None

# here we register using spark
udf_toUpper_case = udf(to_Upper_case, StringType())

# here we register the udf to sql
spark.udf.register("to_upper_case", udf_toUpper_case)

df = spark.createDataFrame([("alice",), ("bob",)], ["name"])
df.createOrReplaceTempView("people")

result = spark.sql("SELECT name, to_upper_case(name) AS uppercase_name FROM people")
result.show()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE FUNCTION to_upper_case(input_text TEXT)
# MAGIC RETURNS TEXT AS $$
# MAGIC BEGIN
# MAGIC     RETURN UPPER(input_text)
# MAGIC END; 
# MAGIC -- $$ LANGUAGE plpgsql;
# MAGIC
# MAGIC SELECT `name`, to_upper_case(`name`) FROM people;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 21. Identifying the Location of a User-Defined Function (UDF)
# MAGIC In the context of a SQL-based system like Databricks' Unity Catalog or any database supporting UDFs, the location of a UDF is essential for managing its usage, security, and accessibility.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 22. Describe the security model for sharing SQL UDFs
# MAGIC
# MAGIC When sharing SQL User Defined Functions (UDFs), it is essential to follow a well-defined security model to ensure data integrity, prevent misuse, and maintain access control. 
# MAGIC Here's an overview of the key principles and mechanisms involved in the security model for sharing SQL UDFs:
# MAGIC 1. Access Control
# MAGIC 2. Data Scope and Security
# MAGIC 3. Code Security
# MAGIC 4. Versioing and Dependency Management
# MAGIC 5. Encryption and Secure Data Transfer

# COMMAND ----------

# MAGIC %md
# MAGIC ### 23. Use CASE/WHEN in SQL code
# MAGIC The CASE statement in SQL is used to implement conditional logic directly in queries. It evaluates conditions and returns a specific value based on the result of those conditions.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create or Replace table emergency as
# MAGIC -- select * from csv.`/FileStore/tables/Data/911.csv`
# MAGIC
# MAGIC -- select * from default.emergency 
# MAGIC
# MAGIC select 
# MAGIC     Case 
# MAGIC         When _c3 > 19000 Then "Yes it high"
# MAGIC         WHen _c3 between 10000 and 19000 then "Hello world"
# MAGIC         Else "None"
# MAGIC     End as _c3
# MAGIC From default.emergency;

# COMMAND ----------

df = spark
    .read
    .format('csv')
    .options('inferschema', )
    .load('/FileStore/tables/Data/minifigs.json')

df.show()