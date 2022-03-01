import os.path

from setuptools import find_packages, setup
from setuptools.command.install import install

with open("requirements.txt", "r") as requirements_file:
    requirements = [r.strip("\n") for r in requirements_file.readlines()]


class InstallWithCompile(install):
    def run(self):
        from babel.messages.frontend import compile_catalog
        compiler = compile_catalog(self.distribution)
        option_dict = self.distribution.get_option_dict('compile_catalog')
        compiler.use_fuzzy = True
        compiler.domain = [option_dict['domain'][1]]
        compiler.directory = option_dict['directory'][1]
        compiler.run()
        super().run()


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
        'install': InstallWithCompile
    },
    setup_requires=[
        'Babel'
    ]
)
