from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "2.0.0.4"
DESCRIPTION = 'A GUI framework built on top of tkinter, with new features.'
LONG_DESCRIPTION = ''

# Setting up
setup(
    name="Heema",
    version=VERSION,
    author="Федор Глеб | Abhay Gaur",
    author_email="<abhay.12104531@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['BlurWindow', 'pillow', 'pyaudio'],
    keywords=['Heema','heema','heema gui','HEEMA','heemagui','python', 'tkinter', 'modern', 'gui', 'tkintergui', 'browser'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)