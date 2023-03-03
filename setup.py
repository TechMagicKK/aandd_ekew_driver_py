from setuptools import setup
import os
from glob import glob

package_name = 'aandd_ekew_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='koki-ogura',
    maintainer_email='koki.balian@gmail.com',
    description='aandd_ekew_driver',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'aandd_ekew_driver_node = aandd_ekew_driver.aandd_ekew_driver_node:main',
            'aandd_ekew_driver_test = aandd_ekew_driver.aandd_ekew_driver_test:main',
        ],
    },
)