import os
model_folder = 'model'

try:
    os.makedirs(model_folder)
except FileExistsError:
    # directory already exists 
    pass