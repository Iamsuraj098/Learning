# Databricks notebook source
# MAGIC %md
# MAGIC ###  Identify the four areas of data governance
# MAGIC
# MAGIC 1. Data Quality
# MAGIC     - Ensures that data is accurate, complete, consistent, and reliable.
# MAGIC     - Focuses on improving the usability of data for business processes and decision-making.
# MAGIC 2. Data Security
# MAGIC     - Protects data from unauthorized access, breaches, and misuse.
# MAGIC     - Ensures that sensitive information is secure both in transit and at rest.
# MAGIC 3. Data Privacy
# MAGIC     - Ensures compliance with laws and regulations regarding how data is collected, stored, and used.
# MAGIC     - Protects personal and sensitive information from misuse or exposure.
# MAGIC 4. Data Compliance
# MAGIC     - Ensures that data management practices adhere to legal, regulatory, and organizational policies.
# MAGIC     - Avoids penalties and maintains trust with customers and stakeholders.
# MAGIC
# MAGIC ### Compare and contrast metastores and catalogs
# MAGIC
# MAGIC | **Aspect**              | **Metastore**                                                                 | **Catalog**                                                                   |
# MAGIC |--------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
# MAGIC | **Definition**           | A metastore is a centralized repository that stores metadata about data objects such as tables, views, and schemas. | A catalog organizes and groups multiple schemas or databases, acting as a high-level abstraction for managing data. |
# MAGIC | **Scope**                | Focuses on managing metadata for individual databases or schemas.            | Provides a broader structure, often organizing multiple metastores or schemas under one umbrella. |
# MAGIC | **Purpose**              | Stores detailed information about tables, columns, data types, and file locations. | Organizes datasets into logical groups, making data discovery and access easier. |
# MAGIC | **Granularity**          | Operates at the schema or database level.                                    | Operates at the catalog level, encompassing multiple databases or schemas.    |
# MAGIC | **Examples**             | - Hive Metastore<br>- AWS Glue Data Catalog<br>- Databricks Metastore        | - Unity Catalog (Databricks)<br>- AWS Glue Catalog for grouping multiple schemas |
# MAGIC | **Data Organization**    | Organizes data into schemas and tables.                                      | Organizes schemas and databases under a catalog hierarchy.                    |
# MAGIC | **Security Controls**    | Provides metadata-level security and schema-specific access control.         | Offers broader security policies that span multiple databases and schemas, often with centralized governance. |
# MAGIC | **Usability**            | Primarily designed for metadata storage and management.                      | Focused on providing a unified view and governance over multiple datasets.    |
# MAGIC | **Governance**           | Limited governance capabilities, usually applied at the schema or table level. | Enhanced governance capabilities with role-based access control and centralized policy enforcement. |
# MAGIC | **Interoperability**     | Often specific to a single framework or tool (e.g., Hive or Spark).          | Supports interoperability across tools and frameworks with unified APIs.      |
# MAGIC
# MAGIC ### Syntax of Grant/Revoke command:
# MAGIC 1. Grant **privilages** on **object access** to **user \ person**
# MAGIC 2. Revoke **privilages** on **object access** from **user \ person**
# MAGIC
# MAGIC ### Data Object
# MAGIC |**Object**|**Scope**|
# MAGIC |----------|---------|
# MAGIC |CATALOG |controls access to the entire data catalog.|
# MAGIC |SCHEMA |controls access to a database.|
# MAGIC |TABLE |controls access to a managed or external table.|
# MAGIC |VIEW |controls access to SQL views.|
# MAGIC |FUNCTION |controls access to a named function.|
# MAGIC |ANY FILE |controls access to the underlying filesystem.|
# MAGIC
# MAGIC ### Unity Catalog Privilages
# MAGIC |**Privilege**| **Ability**|
# MAGIC |---------|---------|
# MAGIC |SELECT |read access to an object.|
# MAGIC |MODIFY |add, delete, and modify data to or from an object.|
# MAGIC |CREATE |create an object|
# MAGIC |READ_METADATA |view an object and its metadata.|
# MAGIC |USAGE |No effect! required to perform any action on a database object.|
# MAGIC |ALL PRIVILEGES| gives all privileges|
# MAGIC ### Identify the cluster security modes compatible with Unity Catalog
# MAGIC
# MAGIC Unity Catalog, a unified governance solution for managing data and resources in Databricks, is compatible with the following cluster security modes:
# MAGIC 1. Single User Access Mode
# MAGIC     - In this mode, the cluster is configured for a single user.
# MAGIC     - All operations on the cluster are performed as the specified user, and the user’s identity is propagated for governance and access control.
# MAGIC     - Use Case: Best suited for scenarios where one user is solely responsible for all data operations
# MAGIC 2. Shared Access Mode
# MAGIC     - Allows multiple users to share the same cluster, but the cluster enforces user-specific identity and permissions when accessing data.
# MAGIC     - Ensures that Unity Catalog policies are applied at a user level, even in a shared environment.
# MAGIC     - Use Case: Useful in collaborative environments where multiple users need access to a shared cluster.
# MAGIC 3. No isolation Security Mode
# MAGIC     - Not compatible with Unity Catalog due to the lack of strict user isolation and access controls.

# COMMAND ----------

# MAGIC %md
# MAGIC ###Terms Explations:
# MAGIC 1. Data Lineage: Data Lineage Tracking is the process of automatically capturing the flow of data from its origin (source) to its final destination (reports, dashboards, ML models, etc.). It helps organizations understand how data moves, transforms, and is used across their data ecosystem.
# MAGIC - Importance of Data Lineages: 
# MAGIC     - Debugging and Troubleshooting
# MAGIC     - Compliance and Auditing
# MAGIC     - Impact Analysis
# MAGIC     - Data Trust and quality
# MAGIC 2. Role Based Access Control(RBAC): Role-Based Access Control (RBAC) is a security model that restricts access to resources based on user roles instead of assigning permissions directly to individuals.
# MAGIC     - Users are assigned roles (e.g., Admin, Data Engineer, Analyst).
# MAGIC     - Roles have predefined permissions (e.g., read, write, execute).
# MAGIC     - Users inherit permissions based on their assigned roles.
# MAGIC
# MAGIC 3. Attribute-Based Access Control (ABAC): is an advanced security model where access is granted based on user attributes rather than predefined roles. It allows for dynamic and fine-grained access control by using metadata like:
# MAGIC     - User attributes → Department, job title, location, seniority.
# MAGIC     - Resource attributes → Table sensitivity, data classification, ownership.
# MAGIC     - Environment attributes → Time of access, device type, security level.
# MAGIC
# MAGIC 4. Difference between RBAC and ABAC: 
# MAGIC |Feature|	RBAC (Role-Based)|	ABAC (Attribute-Based)|
# MAGIC |-------|-----------------|---------------------------|
# MAGIC |Access Control|	Based on static roles (Admin, Analyst, Engineer).|	Based on dynamic attributes (Department, Data Sensitivity).|
# MAGIC |Flexibility|	Less flexible, requires manual updates for new roles.	|Highly flexible, permissions adjust automatically.|
# MAGIC |Granularity|	Grants access at role level (broad control).	|Grants access at column, row, and attribute level (fine-grained).|
# MAGIC |Use Case|	Best for small organizations with fixed roles.|	Best for large enterprises with dynamic access needs.|

# COMMAND ----------

# MAGIC %md
# MAGIC ### What is Unity Catalog?
# MAGIC Unity Catalog is a **unified data governance and cataloging solution** for **managing data, permissions, and metadata across multiple clouds in Databricks**. It enables organizations to centrally control access to data while providing features like fine-grained security, lineage tracking, and auditing.
# MAGIC
# MAGIC #### Key features of Unity Catalog: 
# MAGIC 1. Fined-Grained Access Control
# MAGIC     - Define who can access what data at schema, table, column, and row levels.
# MAGIC     - Supports Attribute-Based Access Control (ABAC) for dynamic permissions.
# MAGIC     - Uses SCIM integration to sync users and groups with identity providers (e.g., Azure AD).
# MAGIC 2. Automated Data Lineage Tracking
# MAGIC     - Tracks how data flows across different tables, jobs, and notebooks.
# MAGIC     - Helps in debugging, compliance audits, and impact analysis.
# MAGIC 3. Centralized Data and Metadata Management:
# MAGIC     - Provides a single data catalog across multiple Databricks workspaces.
# MAGIC     - Manages tables, views, functions, and storage locations under a three-level namespace:
# MAGIC       - `catalog.schema.table`
# MAGIC       - Catalog: Top-level container (e.g., finance_catalog)
# MAGIC       - Schema (Database): Organizes tables (e.g., sales_db)
# MAGIC       - Table: Stores actual data (e.g., transactions)
# MAGIC 4. Delta Sharing:
# MAGIC     - Enables secure data sharing with external partners and teams without duplicating data.
# MAGIC     - Supports open-source Delta Sharing protocol.
# MAGIC 5. Multi-Cloud and Multi-Workspace Compatibility: 
# MAGIC     - Works across AWS, Azure, and Google Cloud for seamless data governance.
# MAGIC     - Supports Lakehouse Federation, allowing users to query data across multiple platforms.
# MAGIC
# MAGIC #### Managing Access in Unity Catalog
# MAGIC - Grant Access to a Table
# MAGIC     - `GRANT SELECT ON TABLE finance_catalog.sales_db.transactions TO user 'john@example.com';`
# MAGIC - Revoke Access
# MAGIC     - `REVOKE SELECT ON TABLE finance_catalog.sales_db.transactions FROM user 'john@example.com';`
# MAGIC - View Data Lineage
# MAGIC     - `DESCRIBE HISTORY finance_catalog.sales_db.transactions;`
# MAGIC
# MAGIC #### How Unity Catalog Works in Databricks?
# MAGIC 1. Admins define access policies at the catalog/schema/table level.
# MAGIC 1. Users authenticate via SSO, Azure AD, or AWS IAM.
# MAGIC 1. Queries execute with enforced permissions, ensuring data security.
# MAGIC 1. Data lineage automatically captures transformations for compliance.
# MAGIC 1. External teams securely access data using Delta Sharing without needing full database access.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Difference Between Catalog and Unity Catalog
# MAGIC
# MAGIC | **Feature**             | **Catalog** (Standard in Databricks) | **Unity Catalog** (Advanced Governance) |
# MAGIC |-------------------------|-------------------------------------|-----------------------------------------|
# MAGIC | **Definition**          | A logical namespace that organizes schemas (databases) and tables within a Databricks workspace. | A centralized **data governance layer** for managing catalogs, schemas, tables, and permissions across multiple workspaces and clouds. |
# MAGIC | **Namespace Hierarchy** | `database.table` (limited to a single workspace) | `catalog.schema.table` (multi-workspace, cross-cloud) |
# MAGIC | **Access Control**      | Basic **workspace-level** permissions. | Fine-grained **column, row, and table-level security** with **RBAC & ABAC**. |
# MAGIC | **Data Lineage Tracking** |  **Not available** | **Automatically tracks lineage** from source to consumption. |
# MAGIC | **Multi-Cloud & Multi-Workspace** | Works **only within a single Databricks workspace**. |  **Supports multiple workspaces** across **AWS, Azure, GCP**. |
# MAGIC | **Data Sharing**        | No built-in sharing mechanism. |  Supports **Delta Sharing** for secure external collaboration. |
# MAGIC | **Governance & Compliance** | Requires manual tracking and permissions management. |  Provides **centralized governance, auditing, and security policies**. |
# MAGIC | **Use Case**           | Best for **individual workspace users** managing their own databases. | Best for **enterprise-wide data management, compliance, and cross-team collaboration**. |
# MAGIC
# MAGIC
# MAGIC Note: Catalog is a part of Unity Catalog
# MAGIC - Unity Catalog is a governance and management layer in Databricks that organizes and secures data across multiple workspaces.
# MAGIC - Catalog is a logical container within Unity Catalog that holds schemas (databases) and tables.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a UC-enabled all-purpose cluster.
# MAGIC Create a Unity Catalog (UC)-enabled all-purpose cluster in Databricks, step by step:
# MAGIC 1. Login to Databricks
# MAGIC 2. Go to the Clusters Page
# MAGIC 3. Configure Cluster Details
# MAGIC 4. Select Databricks Runtime
# MAGIC 5. Enable Unity Catalog
# MAGIC 6. Set Cluster Access Control
# MAGIC 7. Create the Cluster

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a DBSQL warehouse.
# MAGIC 1. Click SQL Warehouses in the sidebar.
# MAGIC 2. Click Create SQL Warehouse.
# MAGIC 3. Enter a Name for the warehouse.
# MAGIC 4. Click Create.
# MAGIC
# MAGIC We can check the warehouse
# MAGIC
# MAGIC SELECT 'DBSQL Warehouse is ready!' AS message;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 'DBSQL Warehouse is ready!' AS message;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify how to query a three-layer namespace.
# MAGIC 1. Catalog: The highest-level container for schemas and tables.
# MAGIC 2. Schema (or Database): A logical grouping of tables.
# MAGIC 3. Table: The actual data storage unit.
# MAGIC
# MAGIC #### Considerations
# MAGIC - Default Catalog: If a catalog isn't specified, Databricks may use the default hive_metastore.
# MAGIC - Permissions: Ensure that the user has access to the specified catalog and schema.
# MAGIC - Unity Catalog: If using Unity Catalog, it enforces governance across catalogs and schemas.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- CREATE or replace TABLE hive_metastore.default.sale (
# MAGIC --     id INT,
# MAGIC --     name STRING,
# MAGIC --     sales DECIMAL(10,2)
# MAGIC -- );
# MAGIC
# MAGIC -- INSERT into hive_metastore.default.sale values (1, "toy", 23.09);
# MAGIC
# MAGIC SELECT * FROM hive_metastore.default.sale;
# MAGIC
# MAGIC -- catalog -> hive_metastore
# MAGIC -- schema -> defualt
# MAGIC -- table -> table_name

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Object Access Control: 
# MAGIC **Data Object Access Control** in Databricks refers to **managing access to data objects** such as:
# MAGIC - 📂 **Catalogs**
# MAGIC - 📂 **Schemas (Databases)**
# MAGIC - 📄 **Tables**
# MAGIC - 📄 **Views**
# MAGIC - 📄 **Columns (Fine-grained control)**
# MAGIC
# MAGIC Databricks **Unity Catalog** provides **Role-Based Access Control (RBAC)** and **Attribute-Based Access Control (ABAC)** to manage permissions at multiple levels.
# MAGIC
# MAGIC ---
# MAGIC ### Implement data object access control
# MAGIC
# MAGIC - In Databricks, Data Object Access Control is managed using Unity Catalog (for workspace-wide governance) or SQL permissions (for individual warehouses).
# MAGIC - You can control access at different levels: catalogs, schemas, tables, views, and functions.
# MAGIC - By using grant and revoke command we can control the object access

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Grant Access to a Catalog
# MAGIC GRANT USAGE ON CATALOG enterprise TO user@example.com;
# MAGIC -- Grant Access to a Schema
# MAGIC GRANT USAGE ON SCHEMA enterprise.retail TO user@example.com;
# MAGIC -- Grant Access to a Table
# MAGIC GRANT SELECT, INSERT ON TABLE enterprise.retail.sales_data TO user@example.com;
# MAGIC -- Revoke Access
# MAGIC REVOKE SELECT ON TABLE enterprise.retail.sales_data FROM user@example.com;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify colocating metastores with a workspace as best practice
# MAGIC Colocating metastores with a Databricks workspace means deploying the Unity Catalog Metastore in the same cloud region as the workspace. This is a best practice for performance, cost efficiency, and compliance.
# MAGIC
# MAGIC #### Why Colocate a Metastore with a Workspace?
# MAGIC 1. Performance Optimisation: Reduces query latency by ensuring metadata operations happen within the same region.
# MAGIC 2. Cost Efficiency: Avoids cross-region data transfer costs
# MAGIC 3. Security and Compliances: Prevents data sovereignty issues many industries require metadata and data to stay within the same region.
# MAGIC
# MAGIC #### Best Practices for Colocating a Metastore
# MAGIC
# MAGIC - Deploy the Metastore in the Same Cloud Region
# MAGIC   - If your Databricks workspace is in us-east-1, your Unity Catalog Metastore should also be in us-east-1.
# MAGIC   - Check your cloud provider’s region-specific capabilities before deploying.
# MAGIC - Use a Single Metastore per Cloud Region
# MAGIC   - Unity Catalog allows one metastore per region per account.
# MAGIC   - If you have multiple workspaces in the same region, they should share the same metastore.
# MAGIC - Configure External Storage in the Same Region
# MAGIC   - AWS: Use S3 buckets in the same region as the workspace.
# MAGIC   - Azure: Use ADLS Gen2 storage in the same region.
# MAGIC   - GCP: Use GCS buckets in the same region.
# MAGIC
# MAGIC #### Steps to Set Up a Colocated Metastore
# MAGIC 1. Create a Unity Catalog Metastore in the Same Region
# MAGIC     - Go to Databricks Admin Console → Unity Catalog
# MAGIC     - Click Create Metastore
# MAGIC     - Choose the same region as your Databricks workspace
# MAGIC     - Attach the correct cloud storage (S3, ADLS, GCS)
# MAGIC     - Assign the metastore to workspaces in the same region
# MAGIC 2. Link Workspaces to the Metastore
# MAGIC     - ALTER METASTORE my_metastore SET ASSIGNMENT my_workspace_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify using service principals for connections as best practice
# MAGIC 1. Service Principal: A service principal is a non-human identity used to securely authenticate and authorize applications, scripts, or automated processes in Databricks, Azure, or AWS IAM.
# MAGIC
# MAGIC 2. Why Use Service Principals for Connections
# MAGIC     - Enhanced Scurity
# MAGIC     - Automation and Scalability
# MAGIC     - Compliance & Auditing
# MAGIC
# MAGIC 3. How to Set Up a Service Principal in Databricks
# MAGIC     - Create a Service Principal in Azure
# MAGIC         - Go to Azure Portal → Azure Active Directory → App registrations.
# MAGIC         - Click New registration → Provide a name (e.g., databricks-svc-principal).
# MAGIC         - Note the Application (client) ID and Directory (tenant) ID.
# MAGIC         - Create a client secret in Certificates & secrets.
# MAGIC     - Assign Permissions in Databricks
# MAGIC         - GRANT USAGE ON CATALOG my_catalog TO `service_principal:your-sp-id`;
# MAGIC         - GRANT SELECT ON TABLE my_catalog.my_table TO `service_principal:your-sp-id`;
# MAGIC     - Use the Service Principal to Authenticate
# MAGIC         - Using OAuth Token
# MAGIC           - databricks configure --aad-token
# MAGIC         - or programmatically in Python:
# MAGIC           - from databricks import sql
# MAGIC           - conn = sql.connect(
# MAGIC               server_hostname="your-databricks-instance",
# MAGIC               http_path="sql/protocolv1/o/1234567890/your-sql-warehouse",
# MAGIC               access_token="your-oauth-token")
# MAGIC
# MAGIC 4. Avoid These Common Mistakes
# MAGIC     - Using personal credentials in production scripts.
# MAGIC     - Granting excessive privileges to service principals.
# MAGIC     - Storing secrets in plain text instead of Azure Key Vault / AWS Secrets Manager.
# MAGIC     - Not monitoring service principal activities in audit logs.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify the segregation of business units across catalog as best practice
# MAGIC
# MAGIC 1. Catalog Based Seggregation: In Databricks Unity Catalog, segregating business units across catalogs means creating separate catalogs for different departments, teams, or functions within an organization. This provides better governance, security, and access control.
# MAGIC #### **Why Segregate Business Units Across Catalogs?**
# MAGIC Segregating business units using **separate catalogs** in **Databricks Unity Catalog** ensures:
# MAGIC 1. **Data Isolation** → Each business unit (BU) accesses only relevant data.  
# MAGIC 1. **Access Control** → Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC) at the **catalog level**.  
# MAGIC 1. **Governance & Compliance** → Meets **GDPR, HIPAA, SOC 2** by restricting data access.  
# MAGIC 1. **Improved Performance** → Reduces metadata complexity and query latency.  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## **🔹 Catalog Segregation Structure**
# MAGIC ### **1️⃣ Catalog per Business Unit (Recommended)**
# MAGIC Each **business unit** gets its own **catalog**, ensuring clear segregation:
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Data Explorer
# MAGIC - Data Explorer allow user to manage permission and grants for tables, views and databases.
# MAGIC - It provides a UI-based interface where you can view, grant, or revoke permissions on tables, schemas, and catalogs.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Transfer table ownership
# MAGIC   - The ALTER TABLE command is used to change the ownership of a table in Databricks.
# MAGIC   - Using OWNER TO 'group_name', you can transfer ownership to a group, allowing multiple users to manage permissions.
# MAGIC   - This is useful when a team member leaves, ensuring that no single user solely owns critical resources.
# MAGIC   - `ALTER TABLE table_name OWNER TO group_name`
# MAGIC
# MAGIC To transfer the owenership of table we not used the Grant because: 
# MAGIC The GRANT statement in Databricks is used to assign privileges (like SELECT, INSERT, UPDATE, etc.) to users, roles, or groups. However, it does not transfer ownership of a table because: