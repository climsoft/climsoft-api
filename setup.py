import logging
import os.path

from setuptools import find_packages, setup
from setuptools.command.install import install
from babel.messages.frontend import compile_catalog

with open("requirements.txt", "r") as requirements_file:
    requirements = [r.strip("\n") for r in requirements_file.readlines()]

logger = logging.getLogger("SetupLogger")
logging.basicConfig(level=logging.INFO)
BASE_PATH = os.path.dirname(
    os.path.abspath(__file__)
)


class InstallCommand(install):
    def run(self):
        logger.info("Logger in setup.py")
        self.run_command('compile_mo_files')
        if os.path.exists(
            os.path.join(
                BASE_PATH,
                "src/climsoft_api/locale/fr/LC_MESSAGES/climsoft_messages.mo"
            )
        ):
            raise FileExistsError(os.path.join(
                BASE_PATH,
                "src/climsoft_api/locale/fr/LC_MESSAGES/climsoft_messages.mo"
            ))
        install.run(self)


setup(
    name='climsoft_api',
    version='0.1.0',
    description='API to manage climsoft data.',
    author='OpenCDMS',
    author_email='info@opencdms.org',
    url='https://github.com/opencdms/climsoft-api',
    package_dir={
        "": "src"
    },
    packages=find_packages(where="./src"),
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "": [
            "src/climsoft_api/locale/*/LC_MESSAGES/*.po",
            "src/climsoft_api/locale/*/LC_MESSAGES/*.mo",
        ]
    },
    cmdclass={
        'compile_mo_files': compile_catalog,
        'install': InstallCommand
    },
    setup_requires=[
        'Babel'
    ],
    data_files=[
        (
            'climsoft_api/locale/en/LC_MESSAGES',
            ['src/climsoft_api/locale/en/LC_MESSAGES/climsoft_messages.mo']
        ),
        (
            'climsoft_api/locale/fr/LC_MESSAGES',
            ['src/climsoft_api/locale/fr/LC_MESSAGES/climsoft_messages.mo']
        )
    ]
)
