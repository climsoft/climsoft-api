import os.path

from setuptools import find_packages, setup
from setuptools.command.install import install

with open("requirements.txt", "r") as requirements_file:
    requirements = [r.strip("\n") for r in requirements_file.readlines()]


class InstallWithCompile(install):
    def run(self):
        from babel.messages.frontend import compile_catalog
        compiler = compile_catalog()
        compiler.use_fuzzy = True
        compiler.domain = ["climsoft_messages"]
        compiler.directory = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)
            ),
            "src/climsoft_api/locale/"
        )
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
        ]
    },
    cmdclass={
        'install': InstallWithCompile
    },
    setup_requires=[
        'Babel'
    ]
)
