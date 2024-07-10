import os
import shutil
import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.resolve()  # 项目根目录
BUILD_WORK_DIR = PROJECT_DIR.joinpath("build")  # 构建工作目录
shutil.rmtree(BUILD_WORK_DIR, ignore_errors=True)
BUILD_WORK_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    """
    打包主程序
    :return:
    """
    distpath = BUILD_WORK_DIR.joinpath("dist")
    shutil.rmtree(distpath, ignore_errors=True)
    os.chdir(PROJECT_DIR)
    res_dir = PROJECT_DIR.joinpath("ChatTTS", "res")
    models_dir = PROJECT_DIR.joinpath("models")
    static_dir = PROJECT_DIR.joinpath("static")
    templates_dir = PROJECT_DIR.joinpath("templates")
    env_file = PROJECT_DIR.joinpath(".env")
    command = (
        f"""poetry run pyinstaller """
        f"""-D """
        f"""--add-data {res_dir}:{res_dir.relative_to(PROJECT_DIR)}  """
        f"""--add-data {models_dir}:{models_dir.relative_to(PROJECT_DIR)}  """
        f"""--add-data {static_dir}:{static_dir.relative_to(PROJECT_DIR)}  """
        f"""--add-data {templates_dir}:{templates_dir.relative_to(PROJECT_DIR)}  """
        f"""--add-data {env_file}:. """
        # f"""--windowed """
        f"""-y """
        f"""--contents-directory . """  # 把exe跟资源打包到一起
        f"""--workpath {BUILD_WORK_DIR} """
        f"""--distpath {distpath} """
        f"""app.py"""
    )
    print(f"打包main命令是{command}")
    subprocess.run(command, shell=True, check=True)
    print(f"打包完成")


if __name__ == '__main__':
    main()
