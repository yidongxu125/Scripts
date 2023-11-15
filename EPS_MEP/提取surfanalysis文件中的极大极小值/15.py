import os
import pandas as pd

# 获取当前文件夹下所有文件夹的路径
folder_paths = [folder for folder in os.listdir() if os.path.isdir(folder)]

# 存储所有数据的列表
data_list = []

# 遍历每个文件夹
for folder_path in folder_paths:
    # 拼接文件路径
    file_path = os.path.join(folder_path, "surfanalysis.txt")

    # 检查文件是否存在
    if not os.path.isfile(file_path):
        continue

    # 读取文本文件
    with open(file_path, 'r') as file:
        data = file.readlines()

    # 提取"Number of surface minima"中的数据并排序
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

    sorted_minima_data = sorted(minima_data)

    # 提取"Number of surface maxima"到结尾的数据并排序
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

    sorted_maxima_data = sorted(maxima_data, reverse=True)

    # 从排序后的数据中选择前5个值
    top_minima = sorted_minima_data[:5]
    top_maxima = sorted_maxima_data[:5]

    # 提取"Number of surface minima"和"Number of surface maxima"行中的数据
    minima_value = None
    maxima_value = None
    for line in data:
        if "Number of surface minima" in line:
            values = line.split(":")
            if len(values) >= 2:
                try:
                    minima_value = int(values[1])
                except ValueError:
                    pass
            continue
        if "Number of surface maxima" in line:
            values = line.split(":")
            if len(values) >= 2:
                try:
                    maxima_value = int(values[1])
                except ValueError:
                    pass
            break

    # 创建数据行
    data_row = [folder_path] + top_minima + top_maxima + [minima_value, maxima_value]
    data_list.append(data_row)

# 创建DataFrame并添加列名
column_names = ["Folder"] + [f"Minima_{i+1}" for i in range(5)] + [f"Maxima_{i+1}" for i in range(5)] + ["Number of surface minima", "Number of surface maxima"]
df = pd.DataFrame(data_list, columns=column_names)

# 导出到Excel
with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
