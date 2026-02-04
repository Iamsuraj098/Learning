# Databricks notebook source
# MAGIC %md
# MAGIC ### How to reduce size of cluster:
# MAGIC 1. Reduce the number of node: 
# MAGIC     - If using fixed nodes, reduce the worker count.
# MAGIC     - If using autoscaling, lower the minimum and maximum number of worker nodes.
# MAGIC 2. Use smaller instance types
# MAGIC 3. Enable Autoscaling
# MAGIC 4. Use spot instances
# MAGIC 5. Reduce driver node
# MAGIC 6. Terminate idle cluster

# COMMAND ----------

# MAGIC %md
# MAGIC Where are Interactive notebook results stored in Databricks product architecture?
# MAGIC
# MAGIC Ans: 
# MAGIC - short-term storage (Control Plane - WebApp Layer)
# MAGIC - Long-term storage (DBFS, External Storage, or Delta Tables - Data Plane)

# COMMAND ----------

