from generate_slicer_config import generate_slicer_config

base_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\slicer_config_files\\sc1_base_config.ini'
out_dir_path = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\slicer_config_files\\sc1_column_config_files\\'

levels = ['000000',
		  '000101',
		  '001011',
		  '001110',
		  '010011',
		  '010110',
		  '011000',
		  '011101',
		  '100010',
		  '100111',
		  '101001',
		  '101100',
		  '110001',
		  '110100',
		  '111010',
		  '111111']

for expt_run in levels:
	out_path = out_dir_path + expt_run + '.ini'
	generate_slicer_config(int(expt_run[0]),
						   int(expt_run[1]),
						   int(expt_run[2]),
						   int(expt_run[3]),
						   int(expt_run[4]),
						   int(expt_run[5]),
						   base_path,
						   out_path)
