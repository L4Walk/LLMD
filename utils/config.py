# utils/config.py
from dotenv import load_dotenv
import os

class ConfigManager:
    def __init__(self):
        env_file = os.path.join(os.getcwd(), '.env')
        self.env_file = env_file
        load_dotenv(env_file)  # 加载 .env 文件
        self._model_dir = os.getenv('MODEL_DIR', os.path.join(os.getcwd(), 'models'))

    @property
    def model_dir(self):
        return self._model_dir

    @model_dir.setter
    def model_dir(self, value):
        self._model_dir = value

    def update_model_dir(self, new_model_dir):
        # 更新内部变量
        self._model_dir = new_model_dir

        # 更新 .env 文件
        self._update_env_file('MODEL_DIR', new_model_dir)

    def _update_env_file(self, key, value):
        # 读取 .env 文件
        if not os.path.exists(self.env_file):
            with open(self.env_file, 'w'): pass

        with open(self.env_file, 'r') as file:
            lines = file.readlines()

        # 更新指定的变量
        updated = False
        for i, line in enumerate(lines):
            if line.startswith(key + '='):
                lines[i] = f"{key}={value}\n"
                updated = True
                break

        # 如果变量不存在，则添加它
        if not updated:
            lines.append(f"{key}={value}\n")

        # 将更新后的内容写回 .env 文件
        with open(self.env_file, 'w') as file:
            file.writelines(lines)

# 创建全局实例
config = ConfigManager()
print(config.model_dir)
