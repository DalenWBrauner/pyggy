from distutils.core import setup

import os

# The main entry point of the program
script_file = 'Hello World.py'

# Create a list of data files.
##sound_files = []
##for file in os.listdir('data\sounds'):
##    file = os.path.join('data\sounds', file)
##    if os.path.isfile(file):
##        sound_files.append(file)
##
##        
##image_files = []
##for file in os.listdir('data\images'):
##    file = os.path.join('data\images', file)
##    if os.path.isfile(file):
##        image_files.append(file)
##
##mydata_files = [('data\sounds', sound_files), ('data\images', image_files)]
sound_files = ['boing.wav','coin.wav']
image_files = ['resolution_buttons.png',
               'resolution_button_individual.png',
               'resolution_labels.png',
               'resolution_button_individual_selected_rotated.png',
               'save_label.png']
mydata_files = [('', sound_files), ('', image_files)]

# Setup args that apply to all setups, including ordinary distutils.
setup_args = dict(
    data_files=mydata_files)
    
# py2exe options
try:
    import py2exe
    setup_args.update(dict(
        windows=[dict(
            script=script_file
        )],
        options={"py2exe": {
                            'bundle_files':1,
                            'compressed':True,
                            'ascii':True}}),
        zipfile = None,
        )
except ImportError:
    pass

# py2app options
# try:
#     import py2app
#     setup_args.update(dict(
#         app=[script_file],
#         options=dict(py2app=dict(
#             argv_emulation=True,
#             iconfile='assets/app.icns',
#         )),
#     ))
# except ImportError:
#     pass

setup(**setup_args)
