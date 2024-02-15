import os


def split_patent_numbers_into_files(base_path, file_path):
    files_per_dir = 100
    dirs_per_super_dir = 100

    # 读取专利号列表
    with open(file_path, 'r') as file:
        patent_numbers = file.readlines()

    total_files = len(patent_numbers)

    for file_index, patent_number in enumerate(patent_numbers):
        patent_number = patent_number.strip()  # 移除末尾的换行符

        # 计算文件应该位于的目录和上级目录
        super_dir_index = file_index // (files_per_dir * dirs_per_super_dir)
        dir_index = (file_index // files_per_dir) % dirs_per_super_dir

        # 构建目标目录路径
        target_dir = os.path.join(base_path, f"super_{super_dir_index}", f"dir_{dir_index}")

        # 如果目录不存在，则创建它
        os.makedirs(target_dir, exist_ok=True)

        # 为每个专利号创建实际文件
        file_name = f"{patent_number}.txt"
        file_path = os.path.join(target_dir, file_name)
        with open(file_path, 'w') as file:
            file.write(patent_number)

        # 实时展示进度
        progress = (file_index + 1) / total_files * 100
        print(f"Progress: {progress:.2f}%, File {file_index + 1}/{total_files}: {file_path}")


# 设置基础路径和专利号文件路径
base_path = r"D:\Jupyter\bigdata\homework\homework10\bigdata_econ_2023"  # 请替换为实际的基础路径
patent_file_path = r'D:\bigdata\data\assignment_cml\pubnr_cn.txt'  # 请替换为实际的专利号文件路径

# 在你的本地环境中运行
split_patent_numbers_into_files(base_path, patent_file_path)
