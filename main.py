import importlib

filename = input('Enter the input file: ')

inputscript = importlib.import_module(filename)
simulation = inputscript.simulation
