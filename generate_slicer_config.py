def generate_slicer_config(W,L,M,V,C,T,base_path,output_path):

	#validate treatment levels
	all_ok = W in (0,1) and L in (0,1) and M in (0,1) and V in (0,1) and C in (0,1) and T in (0,1)
	if not all_ok:
		raise ValueError('Invalid coded values detected. Expecting 0 for low, 1 for high.')

	with open(base_path) as base_fs:
		base_line_list = base_fs.readlines()

	levels = {'W':(0.4,0.6), #treatment (low,high) levels
			  'L':(0.1,0.35),
			  'M':(0.95,1),
			  'V':(30,150),
			  'C':(0,100),
			  'T':(190,240)}

	W_lvl = levels['W'][W]
	L_lvl = levels['L'][L]
	M_lvl = levels['M'][M]
	V_lvl = levels['V'][V]
	C_lvl = levels['C'][C]
	T_lvl = levels['T'][T]

	output_line_list = [];

	for base_line in base_line_list:
		if base_line.startswith('fill_density ='): #constant at 75%
			output_line_list.append('fill_density = 75%\n')
			continue
		elif base_line.startswith('layer_height ='):
			output_line_list.append('layer_height = %.2f\n' % L_lvl)
			continue
		elif base_line.startswith('first_layer_height ='):
			output_line_list.append('first_layer_height = %.2f\n' % L_lvl)
			continue
		elif base_line.startswith('extrusion_width ='):
			output_line_list.append('extrusion_width = %.2f\n' % W_lvl)
			continue
		elif base_line.startswith('external_perimeter_extrusion_width ='):
			output_line_list.append('external_perimeter_extrusion_width = %d\n' % 0)
			continue
		elif base_line.startswith('first_layer_extrusion_width ='):
			output_line_list.append('first_layer_extrusion_width = %d\n' % 0)
			continue
		elif base_line.startswith('perimeter_extrusion_width ='):
			output_line_list.append('perimeter_extrusion_width = %d\n' % 0)
			continue
		elif base_line.startswith('infill_extrusion_width ='):
			output_line_list.append('infill_extrusion_width = %d\n' % 0)
			continue
		elif base_line.startswith('solid_infill_extrusion_width ='):
			output_line_list.append('solid_infill_extrusion_width = %d\n' % 0)
			continue
		elif base_line.startswith('top_solid_infill_extrusion_width ='):
			output_line_list.append('top_solid_infill_extrusion_width = %d\n' % 0)
			continue
		elif base_line.startswith('perimeter_speed ='):
			output_line_list.append('perimeter_speed = %d\n' % V_lvl)
			continue
		elif base_line.startswith('small_perimeter_speed ='):
			output_line_list.append('small_perimeter_speed = %d\n' % V_lvl)
			continue
		elif base_line.startswith('external_perimeter_speed ='):
			output_line_list.append('external_perimeter_speed = %d\n' % V_lvl)
			continue
		elif base_line.startswith('infill_speed ='):
			output_line_list.append('infill_speed = %d\n' % V_lvl)
			continue
		elif base_line.startswith('solid_infill_speed ='):
			output_line_list.append('solid_infill_speed = %d\n' % V_lvl)
			continue
		elif base_line.startswith('top_solid_infill_speed ='):
			output_line_list.append('top_solid_infill_speed = %d\n' % V_lvl)
			continue
		elif base_line.startswith('bridge_speed ='):
			output_line_list.append('bridge_speed = %d\n' % V_lvl)
			continue
		elif base_line.startswith('gap_fill_speed ='):
			output_line_list.append('gap_fill_speed = %d\n' % V_lvl)
			continue
		elif base_line.startswith('extrusion_multiplier ='):
			output_line_list.append('extrusion_multiplier = %2f\n' % M_lvl)
			continue
		elif base_line.startswith('cooling ='):
			output_line_list.append('cooling = 0\n')
			continue
		elif base_line.startswith('fan_always_on ='):
			output_line_list.append('fan_always_on = 1\n')
			continue
		elif base_line.startswith('min_fan_speed ='):
			output_line_list.append('min_fan_speed = %d\n' % C_lvl)
			continue
		elif base_line.startswith('temperature ='):
			output_line_list.append('temperature = %d\n' % T_lvl)
			continue
		output_line_list.append(base_line) #pass through original line from base config

	with open(output_path,'w') as output_fs:
		output_fs.writelines(output_line_list)

	return 1
