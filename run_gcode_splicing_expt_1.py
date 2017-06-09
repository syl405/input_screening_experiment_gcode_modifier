from swap_col_gcode import swap_col_gcode
import os

base_slice_thickness = 0.3
base_thickness = 2.1

base_gcode_dir_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\gcode\\expt_1\\base_gcode\\'
col_gcode_dir_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\gcode\\expt_1\\col_gcode\\'
spliced_gcode_dir_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\gcode\\expt_1\\spliced_gcode\\'

col_gcode_list = os.listdir(col_gcode_dir_path)

for col_gcode_name in col_gcode_list:
	col_slice_thickness_binary = int(col_gcode_name[1])
	col_slice_thickness_in_mm = (0.1,0.35)[col_slice_thickness_binary]

	col_temp_binary = int(col_gcode_name[5])
	col_temp_in_C = (190,240)[col_temp_binary]

	col_gcode_path = col_gcode_dir_path + col_gcode_name
	base_gcode_path = base_gcode_dir_path + col_gcode_name
	spliced_gcode_path = spliced_gcode_dir_path + 'spliced_' + col_gcode_name
	
	swap_col_gcode(base_gcode_path,col_gcode_path,spliced_gcode_path,base_slice_thickness,col_slice_thickness_in_mm,base_thickness,col_temp_in_C)