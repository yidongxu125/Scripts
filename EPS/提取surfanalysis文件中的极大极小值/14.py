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
            minima_value = line.split(":")[1].strip()
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
            maxima_value = line.split(":")[1].strip()
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

    # 从排序后的数据中选择前7个值
    top_minima = sorted_minima_data[:7]
    top_maxima = sorted_maxima_data[:7]

    # 创建数据行
    data_row = [folder_path, minima_value, maxima_value] + top_minima + top_maxima
    data_list.append(data_row)

# 创建DataFrame并添加列名
column_names = ["Folder", "Minima_Value", "Maxima_Value"] + [f"Minima_{i+1}" for i in range(7)] + [f"Maxima_{i+1}" for i in range(7)]
df = pd.DataFrame(data_list, columns=column_names)

# 导出到Excel
with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
