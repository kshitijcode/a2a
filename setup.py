from distutils.core import setup

setup(
    name='a2a',  # How you named your package folder (MyLib)
    packages=['a2a'],  # Chose the same as "name"
    version='0.3',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Finds corresponding service offerings in Microsoft Azure and Amazon AWS .',
    # Give a short description about your library
    author='Kshitij Sharma',  # Type in your name
    author_email='ikshitijsharma@gmail.com',  # Type in your E-Mail
    url='https://github.com/kshitijcode/a2a',  # Provide either the link to your github or to your website
    download_url='https://github.com/kshitijcode/a2a/archive/v0.1.tar.gz',  # I explain this later on
    keywords=['aws', 'service', 'mapping', 'map', 'aws', 'amazon'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'scrapy',
        'tabulate',
    ],
    scripts=['a2a/runner.py'],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
