import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lolHeroes",
    version="0.0.1",
    author="Torres-圣君",
    author_email="2653644677@qq.com",
    description="基于NoneBot2实现，获取LOL英雄的背景故事和图片",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cjladmin/lolheroes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3'
)