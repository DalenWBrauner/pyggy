from distutils.core import setup
import os

from Hello_World import IMAGE_FILES, SOUND_FILES

# The main entry point of the program
script_file = 'Hello_World.py'

# Create a list of data files.
mydata_files = [('', SOUND_FILES), ('', IMAGE_FILES)]

# Setup args that apply to all setups, including ordinary distutils.
setup_args = dict(data_files=mydata_files)
    
# py2exe options
import py2exe

setup_args.update(dict(
    windows=[dict(script=script_file)],
    options={
        "py2exe": {
            'bundle_files':1,
            'compressed':True,
            'ascii':True,
            'dll_excludes':['w9xpopen.exe'],
            }}),


                  zipfile = None)

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
