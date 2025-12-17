# Databricks notebook source
# MAGIC %md
# MAGIC ### Production Pipline
# MAGIC
# MAGIC A Production Data Pipeline is a reliable, scalable, and automated system that moves and transforms data from various sources to destinations, ensuring data is ready for analytics, machine learning, or business operations.
# MAGIC
# MAGIC Key features:
# MAGIC 1. Data Quality Checkups
# MAGIC 2. Fault Tolerance
# MAGIC 3. Scalability
# MAGIC 4. Automation
# MAGIC 5. Security and Compliance
# MAGIC
# MAGIC Types of Production Pipline:
# MAGIC 1. Batch Piplines -> Processes large data in chunks (e.g., daily ETL).
# MAGIC 2. Real-Time(Streaming) Piplines -> Processes data instantly (e.g., Kafka, Spark Streaming).
# MAGIC 3. Hybrid Pipelines -> Mix of batch and real-time processing.
# MAGIC
# MAGIC Tools for Building Production Pipelines
# MAGIC 1. ETL/ELT 
# MAGIC 2. Data Processing
# MAGIC 3. Streaming
# MAGIC 4. Monitoring and Logging

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify the benefits of using multiple tasks in Jobs
# MAGIC Their are many benifits of using production piplines:
# MAGIC 1. Parallel Execution
# MAGIC     - Running multiple tasks in parallel reduces the overall execution time.
# MAGIC     - Example: Extracting data from multiple sources at the same time instead of sequentially.
# MAGIC 2. Modularity and Reuseability
# MAGIC     - Breaking a job into multiple tasks allows better modularity and reusability.
# MAGIC     - Example: A task that cleans data can be reused across multiple pipelines.
# MAGIC 3. Fault Tolerence and Error Handling
# MAGIC     - If one task fails, the others can still run. You can retry or restart only the failed tasks instead of rerunning the entire job.
# MAGIC     - Example: If data ingestion fails but transformation works, you can retry only ingestion.
# MAGIC 4. Scalability
# MAGIC     - Tasks can be distributed across multiple nodes in a cluster, making the pipeline more scalable.
# MAGIC     - Example: Processing large datasets using Spark parallelism.
# MAGIC 5. Dependency Management
# MAGIC     - Jobs can have task dependencies, ensuring that each step runs in the right order.
# MAGIC     - Example: Data must be ingested before transformation starts.
# MAGIC 6. Better Resource Utilization
# MAGIC     - Different tasks can run on optimized resources (CPU/GPU/memory).
# MAGIC     - Example: A lightweight extraction task vs. a heavy ML model training task.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set up a predecessor task in Jobs
# MAGIC In Databricks, a predecessor task in a job is a task that must complete successfully before another task (the successor task) can run. You can set up dependencies between tasks within a job to ensure tasks run in the correct order.
# MAGIC
# MAGIC Steps to Set Up a Predecessor Task in Databricks Jobs
# MAGIC 1. Create a New Job or Edit an Existing Job
# MAGIC 2. Add Tasks to the Job
# MAGIC 3. Set Up Task Dependencies (Predecessor Task)
# MAGIC 4. Save and Run the Job
# MAGIC
# MAGIC Example: Task Dependency Setup
# MAGIC
# MAGIC Assume you have two tasks in a job:
# MAGIC - Task A: Extracts data from a source.
# MAGIC - Task B: Transforms the data extracted by Task A.
# MAGIC - You want Task B to run only after Task A completes successfully. In this case, Task A is the predecessor and Task B is the successor.
# MAGIC - Task A (Predecessor) → Task B (Successor)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Review a task's execution history
# MAGIC Example: Reviewing Task Execution History
# MAGIC   1. Select a Job: You want to view a task's execution history for a job called ETL_Pipeline.
# MAGIC   1. Click on Job Runs: Open ETL_Pipeline and click on View Runs.
# MAGIC   1. Select a Run: You see multiple runs. Click on the most recent one.
# MAGIC   1. Check Task Status: In the job run details, you see a task called ExtractData.
# MAGIC   1. If it’s failed, you can click on logs to view the error messages that can help you troubleshoot.
# MAGIC   1. If it’s successful, you can verify that all tasks completed as expected.
# MAGIC
# MAGIC Key Details in Task Execution History
# MAGIC   1. Task Status: Indicates whether the task was successful or failed.
# MAGIC   1. Start Time and End Time: To measure how long a task took to execute.
# MAGIC   1. Logs: Helps to debug if a task fails.
# MAGIC   1. Resource Metrics: Shows CPU and memory consumption, which helps in optimizing performance.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify CRON as a scheduling opportunity.
# MAGIC CRON is a powerful tool used to schedule tasks in Unix-like systems, and it can also be used in Databricks Jobs to automate and schedule job executions at specific times or intervals.
# MAGIC
# MAGIC In the context of Databricks Jobs, you can use CRON expressions to define custom schedules for when your jobs should run. CRON expressions allow you to specify complex schedules that would be hard to express with standard scheduling options.
# MAGIC
# MAGIC ---
# MAGIC What is CRON?
# MAGIC CRON is a time-based job scheduler in Unix-like operating systems. It allows you to specify the exact time and frequency at which a command or script should run.
# MAGIC A CRON expression is a string of five or six fields representing the minute, hour, day of the month, month, day of the week, and optionally year.
# MAGIC
# MAGIC ---
# MAGIC Example of a CRON expression:
# MAGIC 0 12 * * *
# MAGIC
# MAGIC This runs a task at 12:00 PM every day.
# MAGIC
# MAGIC ---
# MAGIC Steps to Use CRON Scheduling in Databricks:
# MAGIC 1. Go to databricks job
# MAGIC 2. Create or edit the job
# MAGIC 3. Set the schedule (Here CRON Use to schedule the jobs)
# MAGIC 4. Save and Execution

# COMMAND ----------

# MAGIC %md
# MAGIC ### Debug a failed task.
# MAGIC When a task in a Databricks job fails, it’s important to investigate the logs, task configuration, and any related dependencies to identify and resolve the issue
# MAGIC
# MAGIC To debug a failed task in Databricks:
# MAGIC
# MAGIC   - Access job and task logs to identify error messages and stack traces.
# MAGIC   - Check task configuration, including cluster resources and task parameters.
# MAGIC   - Investigate dependencies between tasks to ensure no upstream issues.
# MAGIC   - Monitor resource utilization to determine if the failure was due to resource limitations.
# MAGIC   - Make necessary fixes (e.g., correct code, ensure data validity, adjust configuration), and retry the task.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set up a retry policy in case of failure.
# MAGIC   - Navigate to the Jobs Page
# MAGIC   - Create or Edit a Job
# MAGIC   - Set Retry Policy in Job Configuration
# MAGIC   - Configure Retry Interval
# MAGIC   - Save the Job Configuration
# MAGIC
# MAGIC Considerations for Retry Policies
# MAGIC 1. NUmber of Retries
# MAGIC 2. Retry Interval
# MAGIC 3. Log Monitering
# MAGIC 4. BackOff Strategy

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create an alert in the case of a failed task
# MAGIC In Databricks, you can set up alerts to notify you when a task fails. This can help you stay informed of issues without needing to constantly monitor job runs manually.
# MAGIC
# MAGIC Steps to create an Alert for a Failed Task:
# MAGIC 1. Nevigate to job page
# MAGIC 2. Create a Edit Jobs
# MAGIC 3. Set up alerts in job configuration
# MAGIC     - Scroll down to Alerts Section:
# MAGIC     - Add an Alert
# MAGIC     - Choose the alert trigger condition
# MAGIC     - Define the notification channel (Email, webhook, Databricks notification)
# MAGIC     - Set Frequency
# MAGIC     - Save the job with alerts

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify that an alert can be sent via email
# MAGIC ### Setting Up Email Alerts for a Failed Task in Databricks
# MAGIC
# MAGIC Yes, **Databricks** allows you to send **alerts via email** when specific events or conditions occur, such as task failures, job status changes, or pipeline failures.
# MAGIC
# MAGIC #### Steps to Set Up an Email Alert for a Failed Task in Databricks:
# MAGIC
# MAGIC ### 1. Navigate to the Jobs Page:
# MAGIC - Open your **Databricks Workspace**.
# MAGIC - Go to the **Jobs** tab on the left-hand sidebar.
# MAGIC
# MAGIC ### 2. Create or Edit a Job:
# MAGIC - Either create a **new job** or select an existing job you want to set up an email alert for.
# MAGIC - Click **Create Job** or choose an existing job and click the **Edit** button.
# MAGIC
# MAGIC ### 3. Set Up Alerts in Job Configuration:
# MAGIC - In the **Job Configuration** section, scroll down to find the **Alerts** section.
# MAGIC
# MAGIC ### 4. Add an Alert:
# MAGIC - Click **Add Alert** to create a new alert.
# MAGIC
# MAGIC ### 5. Select Trigger Condition:
# MAGIC - Choose **When Task Fails** or **When Job Fails** depending on whether you want an alert for a task failure or the entire job failure.
# MAGIC
# MAGIC ### 6. Set the Notification Type:
# MAGIC - Select **Email** as the notification method.
# MAGIC - Enter the **email addresses** of the recipients who should be notified. You can add multiple recipients by separating email addresses with commas.
# MAGIC
# MAGIC ### 7. Save the Job:
# MAGIC - After setting up the email alert, click **Save** to apply the changes to your job configuration.
# MAGIC
# MAGIC ## Example of an Email Alert Setup:
# MAGIC - **Condition**: When the task fails.
# MAGIC - **Recipients**: `team@example.com`
# MAGIC - **Email Subject**: "Databricks Task Failure Notification"
# MAGIC - **Email Body**: The email will contain details about the failed task, including the job name, task name, error message, and any other relevant information.
# MAGIC
# MAGIC ## Benefits of Email Alerts in Databricks:
# MAGIC - **Instant Notification**: Get real-time alerts on your email when a job or task fails, ensuring timely action.
# MAGIC - **No Monitoring Required**: You don't have to manually check logs or job statuses; the system will notify you.
# MAGIC - **Multi-Recipient Support**: You can set up alerts for multiple team members, ensuring everyone stays informed.
# MAGIC
# MAGIC Let me know if you need help configuring email alerts or have any more questions! 😊
# MAGIC