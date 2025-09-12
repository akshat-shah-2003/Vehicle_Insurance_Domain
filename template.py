from pathlib import Path
import os

project_root = "src"

files_list = [
    f"{project_root}/components/data_ingestion.py",
    f"{project_root}/components/data_validation.py",
    f"{project_root}/components/data_transformation.py",
    f"{project_root}/components/model_training.py",
    f"{project_root}/components/model_evaluation.py"
    ]

for eachfile in files_list:
    filepath = Path(eachfile)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
    if not filepath.exists():
        with open(filepath, "w") as f:
            pass
        print(f"Created file: {eachfile}")
    else:
        print(f"File already exists: {eachfile}")
