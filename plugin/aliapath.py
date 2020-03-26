import vim
import re
import os
import glob

startup_path = os.getcwd()
file_path = vim.current.buffer.name.split('/')
file_path.pop(-1)
file_path = '/'.join(file_path)

available_first_sym_pattern = re.compile('^(\w|\.|\/)')
relative_path_pattern = re.compile('\.')
absolute_path_pattern = re.compile('\/')
back_path_pattern = re.compile(r'\w+\/\.\.\/')

def remove_back_dir(pth):
    if back_path_pattern.search(pth):
        return remove_back_dir(re.sub(back_path_pattern, '', pth))
    else:
        return pth

def prepare_path(path):
    # remove first sym if not a letter/dot/slash
    if not available_first_sym_pattern.match(path):
        path = path[1:]
    return path

def clean_path(path):
    path = re.sub('\/\*\*\/', '/', path) # replace /**/ with /
    path = re.sub('\/+', '/', path) # replace // with /
    path = remove_back_dir(path) # remove **/../ (back path)
    return path

def try_to_open(path):
    if os.path.isdir(path):
        return glob.glob(path + '/index.*')
    elif os.path.isfile(path):
        return glob.glob(path)
    else:
        return glob.glob(path + '.*')

def find(_path):
    path = prepare_path(_path)
    paths = path.split('/')
    finded_files = []

    def find_alas():
        path = startup_path + '/**/' + '/**/'.join(paths)
        ff = glob.glob(path + '.*', recursive=True)
        if not ff:
            ff = glob.glob(path + '/index.*', recursive=True)
        if ff:
            return ff
        return []

    if relative_path_pattern.match(path):
        finded_files = try_to_open(clean_path(file_path + '/' + path))
    elif  absolute_path_pattern.match(path):
        finded_files = try_to_open(path)
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
    initial_path = re.sub(r"['|\"]", '', str[0])
    find(initial_path)

open()
