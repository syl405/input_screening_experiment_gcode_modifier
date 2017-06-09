def swap_col_gcode(base_gcode_path, col_gcode_path, recombinant_gcode_path, base_slice_thickness, col_slice_thickness, base_thickness, col_temp):
	"""
	Grafts G-code lines corresponding to experimental column layers onto a stub gcode file corresponding to a datum base printed using almost-default settings. 

	Inputs:
	- base_gcode_path: string containing path to gcode file from which base layers will be taken
	- col_gcode_path: string containing path to gcode file from which column layers will be taken
	- recombinant_gcode_path: string containing path to which recombinant gcode file will be written
	- base_slice_thickness: slice thickness (layer height) setting used in base gcode file
	- col_slice_thickness: slice thickness (layer height) setting used in column gcode file
	- base_thickness: nominal value of total base thickness. Must be an integral multiple of both base_slice_thickness and col_slice_thickness so that beginning of col layers line up
	- col_temp: hotend temperature used to print column layers, recombinant gcode adjusts temperature after printing base layers and before printing col layers

	Outputs:
	- recombinant_gcode_path: returns path to recombinant gcode file upon successful completion
	"""

	# Validate base thickness is integral multiple of slice thickness
	# if not base_thickness%base_slice_thickness < 0.0000001:
	# 	raise ValueError('Base slice thickness is not integral multiple of slice thickness.')
	# elif not base_thickness%col_slice_thickness < 0.0000001:
	# 	raise ValueError('Column slice thickness is not integral multiple of slice thickness.')

	# Determine location in base gcode file at which to insert graft
	insert_after_layer = base_thickness/base_slice_thickness - 1 # add 1 because layers are zero-indexed

	# Determine location in col gcode file from which to take graft section
	take_from_layer = base_thickness/col_slice_thickness # do not add 1 because inclusive

	# Open filestreams for input and output gcode files
	base_fs = open(base_gcode_path)
	col_fs = open(col_gcode_path)
	output_fs = open(recombinant_gcode_path,'w')

	# Pass lines for base layers through to output file
	for base_line in base_fs:
		if base_line.startswith(';$ layer ' + str(int(insert_after_layer + 1))):
			#print 'finished writing base layers'
			break # exit once the last base layer is passes through
		output_fs.write(base_line) # pass lines straight through for base layers
	base_fs.close() # close stream for the base gcode

	# Append lines for column layers on to the end of output file
	base_layers_completed = 0 # toggle variable denoting if all base layers have been passed through
	for col_line in col_fs:
		if col_line.startswith(';$ layer ' + str(int(take_from_layer))): # flip toggle once first layer reached
			base_layers_completed = 1
			#print('start writing col layers')
			output_fs.write('; BEGIN GRAFT\n')
			output_fs.write('G0 X189 F10800\n')
			output_fs.write('G0 Y0\n')
			output_fs.write('G1 Z' + str(base_thickness+col_slice_thickness) + ' F12000.000\n')
			output_fs.write('M104 S'+ str(col_temp) + '; set temperature\n')
			output_fs.write('M109 T0 R' + str(col_temp) + '; wait for nozzle to heat or cool\n')
		if base_layers_completed:
			output_fs.write(col_line)
	col_fs.close()

	output_fs.close()

	return recombinant_gcode_path