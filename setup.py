from setuptools import find_packages, setup

setup(
    name='django-runas',
    version='0.1.2',
    license='BSD',
    author='Sam Kingston',
    author_email='sam@sjkwi.com.au',
    description='Impersonate a user using the Django admin',
    url='https://github.com/sjkingo/django-runas',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
