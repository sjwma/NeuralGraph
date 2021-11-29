import pymeshlab
import os
import argparse
from pathlib import Path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_mesh_dir', action='store', dest='input_mesh_dir', required=True, help='Provide input watertight mesh directory')
    parser.add_argument('--output_data_dir', action='store', dest='output_data_dir', required=True, help='Provide output directory')
    parser.add_argument('--file_type', action='store', dest='file_type', required=True, help='Provide the file type to process')

    args = parser.parse_args()

    input_mesh_dir = args.input_mesh_dir
    output_data_dir = args.output_data_dir
    file_type = args.file_type

    ms = pymeshlab.MeshSet()


    for entry in os.scandir(input_mesh_dir):
        if entry.path.endswith(file_type):

            Path(output_data_dir).mkdir(parents=True, exist_ok=True)
            
            filename = entry.path.split("/")[-1].split(".")[0]

            ms.load_new_mesh(input_mesh_dir + "/" + filename + file_type)
            ms.load_filter_script('scripts/screened_poisson.mlx')
            ms.apply_filter_script()
            ms.save_current_mesh(output_data_dir + "/" + filename + ".ply")
            ms.clear()
