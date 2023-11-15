import pandas as pd

# 读取文本文件
with open('surfanalysis.txt', 'r') as file:
    data = file.readlines()

# 提取"Number of surface minima"中的数据
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

# 提取"Number of surface maxima"到结尾的数据
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

# 创建DataFrame并导出到Excel
df_minima = pd.DataFrame([minima_data], columns=[f"Minima_{i+1}" for i in range(len(minima_data))])
df_maxima = pd.DataFrame([maxima_data], columns=[f"Maxima_{i+1}" for i in range(len(maxima_data))])

with pd.ExcelWriter('output.xlsx') as writer:
    df_minima.to_excel(writer, sheet_name='Minima', index=False)
    df_maxima.to_excel(writer, sheet_name='Maxima', index=False)
