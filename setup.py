from setuptools import setup, find_packages

def parse_requirements(filename):
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith('#')]

setup(name='VideoGPT', version='1.0',
      description='PyTorch package for VideoGPT',
      url='http://github.com/LuthandoMaqondo/VideoGPT',
      author='Luthando Maqondo',
      author_email='luthando@appimate.com',
      license='BSD',
      packages=['videogpt'],
      install_requires=parse_requirements('requirements.txt'),
      zip_safe=True)
