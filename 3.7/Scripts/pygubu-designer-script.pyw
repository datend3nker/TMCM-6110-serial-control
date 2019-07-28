#!C:\Users\ludwi\source\repos\TMCM-6110-serial-control\3.7\Scripts\pythonw.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pygubu==0.9.8.2','gui_scripts','pygubu-designer'
__requires__ = 'pygubu==0.9.8.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pygubu==0.9.8.2', 'gui_scripts', 'pygubu-designer')()
    )
