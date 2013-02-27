from distutils.core import setup
import py2exe

setup(name="Agenda",
      version="1.0",
      license="GPL",
    windows=[{"script":"agenda.py", "icon_resources":[(1, "img/agenda.ico")]}])

