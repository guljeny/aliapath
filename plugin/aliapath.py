import vim
import re
import os
import glob

startup_path = os.getcwd()
file_path = vim.current.buffer.name.split('/')
file_path.pop(-1)
file_path = '/'.join(file_path)

wrong_sym_pattern = re.compile('^(\w|\.|\/)')
relative_path_pattern = re.compile('^(\.|\/)')

def prepare_path(path):
    if not wrong_sym_pattern.match(path):
        path = path[1:]
    path = re.sub('\/\*\*\/', '/', path)
    path = re.sub(r'(.+)/.\/', r'\g<1>/', path)
    return path

def find(_path):
    path = prepare_path(_path)
    paths = path.split('/')
    finded_files = []

    def find_relative():
        file_name = paths.pop(-1)
        path = '/'.join(paths)
        if path[0] == '.':
            path = re.sub('\.', file_path, path)
        print(path + '/' + file_name)
        if os.path.isdir(path + '/' + file_name):
            return glob.glob(path + '/' + file_name + '/index.*')
        else:
            return glob.glob(path + '/' + file_name + '.*')

    def find_alas():
        path = startup_path + '/**/' + '/**/'.join(paths)
        ff = glob.glob(path + '.*', recursive=True)
        if not ff:
            ff = glob.glob(path + '/index.*', recursive=True)
        if ff:
            return ff
        return []

    if relative_path_pattern.match(path):
        finded_files = find_relative()
    else:
        finded_files = find_alas()

    if len(finded_files):
        vim.command('e ' + finded_files[0])
    else:
        print('dont find file ' + _path)

def open():
  str = re.findall("['|\"].*['|\"]", vim.current.line)
  if not str:
    print('not find path')
    return
  initial_path = prepare_path(re.sub(r"['|\"]", '', str[0]))
  find(initial_path)

open()
