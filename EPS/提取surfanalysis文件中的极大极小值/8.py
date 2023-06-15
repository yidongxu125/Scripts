import pandas as pd

# 读取文本文件
with open('data.txt', 'r') as file:
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

# 创建DataFrame
df_minima = pd.DataFrame([top_minima], columns=[f"Minima_{i+1}" for i in range(len(top_minima))])
df_maxima = pd.DataFrame([top_maxima], columns=[f"Maxima_{i+1}" for i in range(len(top_maxima))])

# 导出到Excel
with pd.ExcelWriter('output.xlsx') as writer:
    df_minima.to_excel(writer, sheet_name='Minima', index=False)
    df_maxima.to_excel(writer, sheet_name='Maxima', index=False)
