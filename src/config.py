from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGE_SIZE = (224, 224)

BATCH_SIZE = 32

EPOCHS = 10

NUM_CLASSES = 2

LEARNING_RATE = 0.001

TRAIN_DIR = BASE_DIR / "dataset" / "DATASET" / "TRAIN"
TEST_DIR = BASE_DIR / "dataset" / "DATASET" / "TEST"