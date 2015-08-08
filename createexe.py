from distutils.core import setup
import py2exe

setup(console=["tcpreplay_scapy.py"],options = { 'py2exe': {"dll_excludes": ['packet']}})
