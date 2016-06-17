import os
import sys
from ftplib import FTP

def debug_print(s):
    print s

def upload_file(local_file, remote_file):
    fileh = open(local_file, 'rb')
    ftph.storbinary('STOR %s' % remote_file, fileh)
    fileh.close()
    debug_print('Delivered %s' % remote_file)

def upload_files(local_dir, remote_dir):
    if not os.path.isdir(local_dir):
        return

    localnames = os.listdir(local_dir)

    try:
        ftph.cwd(remote_dir)
    except:
        debug_print('Failed to switch directory %s' % remote_dir)

    for item in localnames:
        if item in execlude_files:
            continue

        src = os.path.join(local_dir, item)
        dest = os.path.join(remote_dir, item)

        if os.path.isdir(src):
            try:
                ftph.mkd(dest)
            except:
                debug_print('The directory already exists %s' % dest)

            upload_files(src, dest)
        else:
            upload_file(src, dest)

ftph = FTP('172.16.193.135', 'sx90', 'wang123')

execlude_files = ['.DS_Store', '.vscode', '.svn']

upload_files('/Users/paul/Sites/bbs/mocuz', '/public_html')