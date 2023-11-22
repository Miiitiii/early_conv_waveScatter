from setuptools import setup, find_packages

setup(
  name = 'early-convolutions-vit-pytorch-wave-scatter',
  packages = find_packages(exclude=['notebooks']),
  version = '0.0.1',
  license='MIT',
  description = 'Early Convolutions - wavelet Scatter Vision Transformer - Pytorch',
  author = 'Mahdi Firouzbakht',
  author_email = 'mahdifiruzbakht23@gmail.com',
  url = 'https://github.com/Miiitiii/early_conv_waveScatter',
  keywords = [
    'artificial intelligence',
    'attention mechanism',
    'image recognition',
    'wavelet Scattering'
  ],
  install_requires=[
    'einops>=0.3',
    'torch>=1.6',
    'torchvision',
    'kymatio'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10.12',
  ],
)