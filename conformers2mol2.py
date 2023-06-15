# version 1.0
# by yidongxu
#用法：将mercury计算的构象的mol2文件分成单个的mol2文件
import os

def extract_molecules(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    molecules = []
    molecule = []
    for line in lines:
        if line.startswith('@<TRIPOS>MOLECULE'):
            if molecule:
                molecules.append(molecule)
                molecule = []
        molecule.append(line)

    if molecule:
        molecules.append(molecule)

    return molecules

def save_molecules(molecules, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for i, molecule in enumerate(molecules, 1):
        output_file = os.path.join(output_dir, f'{i}.mol2')
        with open(output_file, 'w') as f:
            f.writelines(molecule)

        print(f'Saved molecule {i} to {output_file}')

if __name__ == '__main__':
    # 获取当前文件夹中所有.mol2文件
    file_list = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.mol2')]
    
    # 遍历所有文件，并将每个文件分割成单独的mol2文件
    for input_file in file_list:
        output_directory = os.path.splitext(input_file)[0] # 使用输入总的mol2文件命名文件夹
        molecules = extract_molecules(input_file)
        save_molecules(molecules, output_directory)
