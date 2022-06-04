from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='re_check',
    version='0.0.1',
    description='Check your Regexes in Python!',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nihilok/re_check',
    author='Michael Jarvis',
    author_email='mjfullstack@gmail.com',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    include_package_data=True,
)
