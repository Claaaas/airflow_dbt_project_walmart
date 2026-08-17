✈️ Airflow · dbt · Databricks Data Engineering Project

A modern Data Engineering pipeline combining Airflow, dbt and Databricks, with data ingested from Ghost PostgreSQL and progressively transformed through a Medallion Architecture.

🏗️ Architecture
                    ┌─────────────────────┐
                    │    Ghost CMS        │
                    │    PostgreSQL       │
                    └──────────┬──────────┘
                               │
                               │ Ingestion
                               ▼
                    ┌─────────────────────┐
                    │      Databricks     │
                    │       BRONZE        │
                    │   Raw / Ingested    │
                    └──────────┬──────────┘
                               │
                               │ dbt
                               ▼
                    ┌─────────────────────┐
                    │      Databricks     │
                    │       SILVER        │
                    │ Cleaned / Refined   │
                    └──────────┬──────────┘
                               │
                               │ dbt
                               ▼
                    ┌─────────────────────┐
                    │      Databricks     │
                    │        GOLD         │
                    │ Business / Analytics│
                    └─────────────────────┘
                               ▲
                               │
                    ┌──────────┴──────────┐
                    │       Airflow       │
                    │   Orchestration     │
                    │   Docker / Local    │
                    └─────────────────────┘
