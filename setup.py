from setuptools import find_packages, setup

setup(
    name="htmlfetcher",
    version="0.0.2",
    description="No pain HTML fetching library.",
    author="Jiuli Gao",
    author_email="gaojiuli@gmail.com",
    url='https://github.com/gaojiuli/htmlfetcher',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
