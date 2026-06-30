import os
from dotenv import load_dotenv
import kagglehub


load_dotenv()  # Loads variables from .env

# Optional: You can also set it as env var for kagglehub if needed
os.environ["KAGGLE_API_TOKEN"] = os.getenv("KAGGLE_API_TOKEN")

# Download the dataset
path = kagglehub.dataset_download("wkirgsn/electric-motor-temperature")
print(f"Dataset downloaded to: {path}")