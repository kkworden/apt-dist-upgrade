import os, sys, tempfile, shutil

LINUX = 'LINUX'
WINDOWS = 'WINDOWS'
MAC = 'MAC'

def get_os():
    if sys.platform == 'linux' or sys.platform == 'linux2':
        return LINUX
    elif sys.platform == 'win32':
        return WINDOWS
    elif sys.platform == 'darwin':
        return MAC
    return 'UNKNOWN'

def get_path():
    sources_dir = '/etc/apt/sources.list.d'
    print('Default upgrade directory is:', sources_dir)
    print('Specify an upgrade folder or hit ENTER to use default.')
    sources_in = input('Path: ')
    if sources_in.strip() != '':
        sources_dir = sources_in
    else:
        print('Using default.')
    return sources_dir

def get_upgrade():
    # Specify the Ubuntu version codename for upgrading repos
    v_to = ''
    while v_to.strip() == '':
        v_to = input('Upgrading to (e.g. xenial, yakkety): ')
    return v_to.strip()

def uncomment(src, v_to):
    # Create a temporary file just in case the .list file is large
    tfile = tempfile.NamedTemporaryFile(mode='r+')
    infile = open(src, 'r')
    for line in infile:
        if v_to in line and line[0:1] == '#':
            line = line[1:].strip(' ')
        tfile.write(line)
    infile.close()
    # Move back to beginning of tfile
    tfile.seek(0)
    outfile = open(src, 'w')
    # Read all lines from beginning of tfile to end and write out
    for line in tfile:
        outfile.write(line)
    tfile.close()
    outfile.close()
    print('  Upgraded file', src, 'to', v_to)

def main():
    if get_os() == LINUX:
        path_in = get_path()
        v_to = get_upgrade()
        shutil.copytree(path_in, path_in + '.copy')
        # Get all sources by walking the user-defined path
        sources = [os.path.join(path, f) \
            for path, dirs, files in os.walk(path_in) \
            for f in files]
        for src in sources:
            ext = os.path.splitext(src)[1]
            if ext == '.list':
                uncomment(src, v_to)
    else:
        print('You must be running an Ubuntu Linux distribution to use this utility.')

main()
