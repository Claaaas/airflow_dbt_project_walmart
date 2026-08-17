# Airflow × dbt × Databricks

End-to-end data pipeline built around **Ghost PostgreSQL**, **Databricks**, **dbt** and **Apache Airflow**.

The project follows a **Medallion Architecture**:

```text
Ghost
(PostgreSQL)
    │
    │ ingestion
    ▼
┌───────────────┐
│    BRONZE     │
│   Databricks │
│   Raw data    │
└───────┬───────┘
        │
        │ dbt
        ▼
┌───────────────┐
│    SILVER     │
│   Databricks │
│ Cleaned data  │
└───────┬───────┘
        │
        │ dbt
        ▼
┌───────────────┐
│     GOLD      │
│   Databricks │
│ Analytics     │
└───────────────┘

        ▲
        │ orchestration
        │
┌───────┴───────┐
│    AIRFLOW    │
│    Docker     │
│    Local      │
└───────────────┘
```

## Stack

| Component              | Role                           |
| ---------------------- | ------------------------------ |
| **Ghost / PostgreSQL** | Source                         |
| **Databricks**         | Data platform & storage        |
| **dbt**                | Transformation & data modeling |
| **Airflow**            | Orchestration                  |
| **Docker**             | Local Airflow environment      |

## Pipeline

**PostgreSQL → Databricks Bronze → dbt Silver → dbt Gold**

Airflow handles the orchestration of the different stages locally through Docker.

### Architecture

* **Bronze** — raw data ingested from PostgreSQL
* **Silver** — cleaned, standardized and transformed data
* **Gold** — business-ready datasets for analytics
* **Airflow** — schedules and orchestrates the pipeline
* **dbt** — manages transformations and dependencies between models
