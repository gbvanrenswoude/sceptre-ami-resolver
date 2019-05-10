from setuptools import setup

setup(
    name='amiresolver',
    py_modules=['amiresolver'],
    entry_points={
        'sceptre.resolvers': [
            'amiresolver = amiresolver:CustomResolver',
        ],
    }
)
