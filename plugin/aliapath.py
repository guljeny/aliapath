import vim
import re
import os
import glob
import subprocess

current_file_path = vim.current.buffer.name.split('/')
current_file_path.pop(-1)
current_file_path = '/'.join(current_file_path)

window_params = '"window": {"width": 0.9, "height": 0.6}'

relative_path_pattern = re.compile('\.')
absolute_path_pattern = re.compile('\/')

def try_to_open(path):
    pathes = []

    if os.path.isfile(path):
        pathes = glob.glob(path)
    elif os.path.isdir(path):
        pathes = glob.glob(path + '/index.*')
    else:
        pathes = glob.glob(path + '.*')

    if (len(pathes)):
        vim.command('e ' + pathes[0])
    else:
        print('Cannot open file: ' + path)

def find_file(path):
    if relative_path_pattern.match(path):
        global_path = os.path.normpath(os.path.join(current_file_path, path))
        return try_to_open(global_path)
    if  absolute_path_pattern.match(path):
        return try_to_open(path)


    path_regex = re.sub('\/', '.*', path)
    ag_files = subprocess.run(['ag', '-g', path_regex], stdout=subprocess.PIPE, text=True).stdout
    file_list = ag_files.split()

    if (not len(file_list)):
        print('Cannot find file: ' + path)
        return
    if(len(file_list) == 1):
        vim.command('e ' + file_list[0])
        return

    better_file_regex = re.compile('.*\/' + path.split('/')[-1] + '\.\w+$')
    filtered_files = list(filter(better_file_regex.match, file_list))

    if(len(filtered_files) == 1):
        vim.command('e ' + filtered_files[0])
        return

    vim_list = '[\'' + '\', \''.join(file_list) + '\']'
    vim.command('call fzf#run({ "source": ' + vim_list + ', "sink": "e",' + window_params + '})');

def run():
    result = re.search("['|\"](.*)['|\"]", vim.current.line)

    if not result:
        print('There is no path string!')
        return

    find_file(result.groups()[0])

run()
