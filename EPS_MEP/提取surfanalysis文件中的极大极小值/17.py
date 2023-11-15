# version 2.0
# by yidongxu
#用法：对EPS的极大值和极小值所有的进行提取并排序，为脚本16提取的数据进行校对作用或者单独自从处理
import os
import pandas as pd

# 获取当前目录
current_directory = os.getcwd()

# 存储所有文件的数据的列表
all_minima_data = []
all_maxima_data = []
file_names = []

# 遍历所有文件夹和文件
for root, dirs, files in os.walk(current_directory):
    for file_name in files:
        if file_name == 'surfanalysis.txt':
            # 获取文件夹名字作为file_name
            folder_name = os.path.basename(root)
            file_names.append(folder_name)

            # 获取文件路径
            file_path = os.path.join(root, file_name)

            # 读取文本文件
            with open(file_path, 'r') as file:
                data = file.readlines()

            # 从"Number of surface minima"部分提取数据
            minima_data = []
            is_minima_section = False
            for line in data:
                if "Number of surface minima" in line:
                    is_minima_section = True
                    continue
                if "Number of surface maxima" in line:
                    break
                if is_minima_section and line.strip():
                    values = line.split()
                    if values[3] != 'kcal/mol':
                        try:
                            value = float(values[3])
                            minima_data.append(value)
                        except ValueError:
                            pass

            # 从"Number of surface maxima"部分提取数据到结尾
            maxima_data = []
            is_maxima_section = False
            for line in data:
                if "Number of surface maxima" in line:
                    is_maxima_section = True
                    continue
                if is_maxima_section and line.strip():
                    values = line.split()
                    if values[3] != 'kcal/mol':
                        try:
                            value = float(values[3])
                            maxima_data.append(value)
                        except ValueError:
                            pass

            # 对数据进行排序
            sorted_minima_data = sorted(minima_data)
            sorted_maxima_data = sorted(maxima_data, reverse=True)

            all_minima_data.append(sorted_minima_data)
            all_maxima_data.append(sorted_maxima_data)

# 创建包含最小值数据的 DataFrame
df_minima = pd.DataFrame(all_minima_data, columns=[f"Min{i+1}" for i in range(len(max(all_minima_data, key=len)))])
# 创建包含最大值数据的 DataFrame
df_maxima = pd.DataFrame(all_maxima_data, columns=[f"Max{i+1}" for i in range(len(max(all_maxima_data, key=len)))])

# 添加文件夹名字列
df_minima.insert(0, 'Folder', file_names)
df_maxima.insert(0, 'Folder', file_names)

# 创建 Excel writer 并将 DataFrame 导出到 Excel 文件
with pd.ExcelWriter('outputsingle.xlsx') as writer:
    df_minima.to_excel(writer, sheet_name='Minima', index=False)
    df_maxima.to_excel(writer, sheet_name='Maxima', index=False)
