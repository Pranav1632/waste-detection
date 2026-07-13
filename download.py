import kagglehub
import shutil
from pathlib import Path

# Download the latest version
cache_path = kagglehub.dataset_download(
    "techsash/waste-classification-data"
)

print(f"Downloaded to cache: {cache_path}")

# Copy dataset into your project
project_dataset = Path("dataset")

if project_dataset.exists():
    shutil.rmtree(project_dataset)

shutil.copytree(cache_path, project_dataset)

print(f"\nDataset copied to: {project_dataset.resolve()}")