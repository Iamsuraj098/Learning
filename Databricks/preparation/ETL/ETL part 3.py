# Databricks notebook source
# MAGIC %md
# MAGIC ### Materialized View
# MAGIC A Materialized View is a precomputed result set **stored as a physical table**, which can improve query performance by avoiding expensive computations each time the query runs. Unlike regular views, a **materialized view stores the query results and requires periodic refreshing to stay updated.**
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC A data engineer is tasked with constructing a table in Databricks, sourcing data from the organization's pre-existing SQLite database. To accomplish this, they execute the command below:
# MAGIC
# MAGIC `CREATE TABLE jdbc_customer360`
# MAGIC
# MAGIC `USING org.apache.spark.sql.jdbc`
# MAGIC
# MAGIC `OPTIONS (`
# MAGIC
# MAGIC     `url "jdbc:sqlite:/customers.db",`
# MAGIC     `datatable "customer360"`
# MAGIC `)`
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC UDF(User Define Function):
# MAGIC A User-Defined Function (UDF) in Spark SQL allows you to define a custom function that can be used in SQL queries to process and transform data beyond built-in functions.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table demo_udf(
# MAGIC   id int,
# MAGIC   age int,
# MAGIC   name varchar(20)
# MAGIC );
# MAGIC
# MAGIC insert into demo_udf values (2, 20, "Rakesh"), (3, 25, "Ranjan"), (4, 30, "Kamal"), (4, 35, "Lala");

# COMMAND ----------

# MAGIC %sql
# MAGIC -- create function age_check as "com.example.udf.AgeChecker";
# MAGIC CREATE FUNCTION age_check AS (age INT) -> STRING 
# MAGIC RETURN CASE 
# MAGIC   WHEN age > 18 THEN 'Adult' 
# MAGIC   ELSE 'Under age' 
# MAGIC END;
# MAGIC
# MAGIC SELECT
# MAGIC   age,
# MAGIC   age_check(age) AS result
# MAGIC FROM demo_udf;
# MAGIC -- it through error because we have to register the UDF before using it.

# COMMAND ----------

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def age_check(age):
    return "Adult" if age > 18 else "Under age"

spark.udf.register("age_check", age_check, StringType());

# COMMAND ----------

# MAGIC %sql
# MAGIC select age, age_check(age) as result from demo_udf;

# COMMAND ----------

# MAGIC %md
# MAGIC ### schema_of_json
# MAGIC schema_of_json is a built-in function in Spark SQL that infers the schema of a JSON string and returns it as a string representation of the schema.

# COMMAND ----------

# MAGIC %md
# MAGIC ### PIVOT Clause in Spark SQL
# MAGIC The PIVOT clause in Spark SQL is used to convert row-based data into column-based format. It helps in summarizing data by rotating unique values from one column into separate columns.
# MAGIC  When to Use PIVOT?
# MAGIC   - When you want to convert row-based data into column format.
# MAGIC   - When you need summary reports (e.g., sales per product per month).
# MAGIC   - When grouping and aggregation are required for better readability.

# COMMAND ----------

# MAGIC %md
# MAGIC ### From_Json
# MAGIC The FROM_JSON function in Spark SQL parses a JSON string and converts it into a structured/struct column using a specified schema.
# MAGIC
# MAGIC When to Use FROM_JSON?
# MAGIC - When you need to parse JSON data from a string column.
# MAGIC - When working with semi-structured JSON data in Spark SQL.
# MAGIC - When converting JSON logs or API responses into structured data.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     FROM_JSON(json_data, 'struct<name:string, age:int, city:string>') AS parsed_json 
# MAGIC FROM json_table;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Array functions: 
# MAGIC |Function|	Description|
# MAGIC |--------|-------------|
# MAGIC |ARRAY(<values>)|	Creates an array from given values.|
# MAGIC |SIZE(array)|	Returns the number of elements in an array.|
# MAGIC |ARRAY_CONTAINS(array, value)|	Checks if a value exists in an array.|
# MAGIC |ELEMENT_AT(array, index)|	Returns the element at a specific index (1-based).|
# MAGIC |SLICE(array, start, length)|	Returns a subset of an array.|
# MAGIC |ARRAY_POSITION(array, value)|	Returns the index (1-based) of a value in the array.|
# MAGIC |EXPLODE(array)|	Converts an array into multiple rows.|
# MAGIC |POSEXPLODE(array)|	Like EXPLODE, but includes position (index).|
# MAGIC |ARRAY_JOIN(array, delimiter)|	Converts an array to a string with a delimiter.|
# MAGIC |ARRAY_SORT(array)|	Sorts an array in ascending order.|
# MAGIC |ARRAY_DISTINCT(array)|	Removes duplicate elements.|
# MAGIC |ARRAY_INTERSECT(arr1, arr2)|	Returns common elements between two arrays.|
# MAGIC |ARRAY_UNION(arr1, arr2)|	Returns a union of two arrays.|
# MAGIC |ARRAY_EXCEPT(arr1, arr2)|	Returns elements in arr1 but not in arr2.|

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temp view dataa_arr as select Array(1, 10, 5, 2, 3, 4, 5, 6, 8, 0) as data;

# COMMAND ----------

# MAGIC %sql
# MAGIC select explode(data) from dataa_arr;
# MAGIC select posexplode(data) from dataa_arr;

# COMMAND ----------

# MAGIC %sql
# MAGIC select explode(array_distinct(data)) from dataa_arr;