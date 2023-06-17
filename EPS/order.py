# 用法：对当前文件夹中excel文件的工作表每一列数字进行排序，有大到小，用作共晶部分极大值和极小值的排序
import pandas as pd
import os

# 获取当前文件夹下的所有 Excel 文件
folder_path = '.'  # 当前文件夹路径
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx') or f.endswith('.xls')]

# 创建一个 ExcelWriter 对象，用于保存合并后的数据
output_file_path = os.path.join(folder_path, 'merged_sorted_excel.xlsx')
writer = pd.ExcelWriter(output_file_path)

# 遍历每个 Excel 文件
for file in excel_files:
    file_path = os.path.join(folder_path, file)

    # 使用 pd.ExcelFile 读取 Excel 文件
    xls = pd.ExcelFile(file_path)

    # 遍历每个工作表
    for sheet_name in xls.sheet_names:
        # 读取工作表数据
        sheet_df = pd.read_excel(file_path, sheet_name=sheet_name)

        # 对每一列进行排序
        for column in sheet_df.columns:
            # 仅处理数字类型的列
            if sheet_df[column].dtype == 'float64' or sheet_df[column].dtype == 'int64':
                sheet_df[column] = sheet_df[column].sort_values(ascending=False).values

        # 将排序后的工作表写入到 ExcelWriter 对象中的对应工作表名称下
        sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

# 保存并关闭 ExcelWriter 对象
writer.save()
writer.close()
