from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='django-cybersource-hosted-checkout',
    version="0.0.6",
    description='This package provides utilities for using CyberSource Secure Acceptance Hosted Checkout.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tim Allen',
    author_email='tallen@wharton.upenn.edu',
    url='https://github.com/wharton/django-cybersource-hosted-checkout',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'Django',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
