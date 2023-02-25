import os
from tfx.orchestration.beam.beam_dag_runner import BeamDagRunner
from modules import components, pipeline


PIPELANE_NAME = "diabetes-pipeline"

# Pipeline inputs
DATA_ROOT = "data"
TRANSFORM_MODULE_FILE = "modules/transform.py"
TUNER_MODULE_FILE = "modules/tuner.py"
TRAINER_MODULE_FILE = "modules/trainer.py"

# Pipeline outputs
OUTPUT_BASE = "outputs"

serving_model_dir = os.path.join(OUTPUT_BASE, "serving_model")
pipeline_root = os.path.join(OUTPUT_BASE, PIPELANE_NAME)
metadata_path = os.path.join(pipeline_root, "metadata.sqlite")


components_args = {
    "data_dir": DATA_ROOT,
    "trainer_module": TRAINER_MODULE_FILE,
    "tuner_module": TUNER_MODULE_FILE,
    "transform_module": TRANSFORM_MODULE_FILE,
    "train_steps": 1000,
    "eval_steps": 800,
    "serving_model_dir": serving_model_dir,
}

components = components.init_components(components_args)

pipeline = pipeline.init_pipeline(
    pipeline_root,
    PIPELANE_NAME,
    metadata_path,
    components
)
BeamDagRunner().run(pipeline)
