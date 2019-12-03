from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='cython_pyqt5',
    ext_modules=cythonize(
        [
            'run.pyx',
            'core/main.py',
            'gui/DialogMain.py',
            'gui/Ui_DialogMain.py'
        ]
    )
)
