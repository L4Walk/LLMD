from modelscope.hub.snapshot_download import snapshot_download
from utils.config import config

def down_models(model_name):
    print("开始下载")
    print(config.model_dir)
    model_dir = snapshot_download(model_name, cache_dir=config.model_dir, revision='master')