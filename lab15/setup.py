from distutils.core import setup, Extension

setup(name='c_ext', version='1.0',
      ext_modules=[Extension('c_ext', ['c_ext.c'])])
