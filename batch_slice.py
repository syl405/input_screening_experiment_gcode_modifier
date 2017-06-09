import os
import subprocess

SLICER_EXE_PATH = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\Slic3r\\Slic3r-console.exe'

stl_dir_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\test_part\\labeled_parts_stl\\'
config_dir_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\slicer_config_files\\sc1_column_config_files\\'
base_config_file_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\slicer_config_files\\sc1_column_config_files\\sc1_base_config.ini'
col_gcode_output_dir_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\gcode\\expt_1\\col_gcode\\'
base_gcode_output_dir_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\gcode\\expt_1\\base_gcode\\'

stl_file_list = os.listdir(stl_dir_path)
config_file_list = os.listdir(config_dir_path)

for stl_name in stl_file_list:
	stl_file_path = stl_dir_path + '\\' + stl_name
	col_config_file_path = config_dir_path + stl_name[0:6] +'.ini'

	#slice base
	subprocess.call([SLICER_EXE_PATH,stl_file_path,'--load',base_config_file_path,'--output',base_gcode_output_dir_path])
	#slice col
	subprocess.call([SLICER_EXE_PATH,stl_file_path,'--load',col_config_file_path,'--output',col_gcode_output_dir_path])