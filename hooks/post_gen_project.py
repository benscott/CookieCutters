import subprocess
from venv import EnvBuilder
import os

ENV_DIR = '.venv'

EnvBuilder(prompt="{{cookiecutter.project_name}}", with_pip=True).create(ENV_DIR)

env_dir_path = os.path.abspath(ENV_DIR)
subprocess.run([f"{env_dir_path}/bin/pip", "install", "ipykernel"]) 
subprocess.run([f"{env_dir_path}/bin/python", "-m", "ipykernel", "install", "--user", "--display-name", "{{cookiecutter.project_name}}", "--name", "{{cookiecutter.project_name}}"]) 


