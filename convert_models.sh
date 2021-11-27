# Filepaths for models to import and export
input_mesh_dir="out/raw_models/elephant-gallop"
output_data_dir="out/meshes/elephant-gallop"
file_type=".obj"

python convert_models.py --input_mesh_dir="${input_mesh_dir}" --output_data_dir="${output_data_dir}" --file_type="${file_type}"
