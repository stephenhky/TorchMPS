

from setuptools import setup


def install_requirements():
    return [package_string.strip() for package_string in open('requirements.txt', 'r')]


setup(name='TorchMPS',
      version="0.0.1",
      description="TorchMPS",
      long_description="TorchMPS: Matrix Product States in Pytorch",
      classifiers=[
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "License :: OSI Approved :: GPL License",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Developers"
      ],
      keywords="machine learning, tensor networks, quantum information",
      url="https://github.com/jemisjoky",
      author="Jacob Miller",
      author_email="jmjacobmiller@gmail.com",
      license='GPL-3.0',
      packages=['torchmps',],
      install_requires=install_requirements(),
      include_package_data=True,
      test_suite="test",
      zip_safe=False)
