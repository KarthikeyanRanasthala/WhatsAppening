from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'whatsappening',
    version = '1.0.0',
    description = 'A WhatsApp activity tracker',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url = 'https://www.github.com/KarthikeyanRanasthala/WhatsAppening',
    author = 'Karthikeyan Ranasthala',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',

    ],
    keywords = 'whatsapp tracker tracking monitor monitoring',
    packages = find_packages(),
    python_requires = '>=3.5',
    install_requires = ['selenium'],
    entry_points = {
        'console_scripts': [
            'whatsappening = whatsappening.main:main',
        ],
    },
    project_urls = {
        'Source': 'https://www.github.com/KarthikeyanRanasthala/WhatsAppening',
    },
)