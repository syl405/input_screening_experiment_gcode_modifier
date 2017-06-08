def swap_column_gcode(base_gcode_path, col_gcode_path, slice_thickness, base_thickness):
	# Validate base thickness is integral multiple of slice thickness
	if not base_thickness%slice_thickness == 0:
		raise ValueError('Base thickness is not integral multiple of slice thickness.')
	