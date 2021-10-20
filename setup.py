import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="todosync",
    version="0.3.1",
    author="Aloïs Micard",
    author_email="alois@micard.lu",
    description="Synchronize issues & tasks from different sources into Todoist.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/creekorful/todosync",
    project_urls={
        "Bug Tracker": "https://github.com/creekorful/todosync/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
)
