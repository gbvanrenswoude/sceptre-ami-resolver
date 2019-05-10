from setuptools import setup

setup(
    name='ami_resolver',
    py_modules=['amiresolver'],
    entry_points={
        'sceptre.resolvers': [
            'amiresolver = amiresolver:CustomResolver',
        ],
    }
)
