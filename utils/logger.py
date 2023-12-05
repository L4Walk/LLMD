import logging
import os
from datetime import datetime

# 设置日志文件夹路径
log_directory = "./log"

# 如果日志文件夹不存在，则创建它
if not os.path.exists(log_directory):
    os.makedirs(log_directory)


# 获取当前时间并格式化为年月日时分秒
current_time = datetime.now().strftime("%Y%m%d%H%M%S")

# 设置日志文件名，包含当前时间
log_filename = f"{log_directory}/app_{current_time}.log"

logger = None

def setup_logger():
    global logger
    if logger is None:
         logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename=log_filename,
                        filemode='a')

    logger = logging.getLogger(__name__)
    return logger
