from pathlib import Path
from dagfactory import load_yaml_dags
gjcj

config_file = Path("/usr/local/airflow/include/dag_configs/retail_orders.yml")

load_yaml_dags(
    globals_dict=globals(),
    config_filepath=str(config_file),
)
