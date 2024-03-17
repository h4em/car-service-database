from setuptools import setup, find_packages

setup(
    name='dbprac',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'test=dbprac.test:main',
        ],
    },
)

#  'test=dbprac.test:main',
#   test to nazwa komendy w cli, dalej to sciezka, :nazwa funkcji 


# setup(
#     name='mypackage',
#     version='0.1.0',
#     py_modules=['module'],
#     install_requires=[
#         'Click',
#     ],
#     entry_points='''
#         [console_scripts]
#         mypackage=mypackage.module:mypackage
#     ''',
# )
