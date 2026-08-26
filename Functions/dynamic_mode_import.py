import os



modes_dir='Modes'
modelist = [ item for item in os.listdir(modes_dir) if os.path.isdir(os.path.join(modes_dir, item)) ]
#print(modelist)

imported_modes = {}
for mode in modelist:
    mode_info= mode + "_info"
    import_mode = f'Modes.{mode}.{mode_info}'
    imported_modes[mode_info] = __import__(import_mode, fromlist=[mode_info])

for mode in modelist:
    main_file_name = imported_modes[mode + "_info"].main_file_name
    imported_main_mode_files[mode] = __import__(f'Modes.{mode}.{main_file_name}', fromlist=[main_file_name])


