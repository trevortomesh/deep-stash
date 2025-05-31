from setuptools import setup

setup(
    name='ds',
    version='1.0.0',
    py_modules=['ds'],
    entry_points={
        'console_scripts': [
            'ds = ds:main',
        ],
    },
    author='Trevor Tomesh',
    description='🧳 A minimal tool for deep-stashing and restoring files and folders using .ds metadata.',
    long_description=(
        "📦 **ds** is a tiny command-line utility to help you save disk space by deep-stashing files and folders.\n"
        "Use it to move items to an external location while keeping a local `.ds` file as a placeholder. "
        "Later, use the same command to restore them with ease. Handles wildcards, directories, and metadata cleanup.\n\n"
        "✅ Now with improved permission error handling — clear messages when access is denied to either the source or the stash directory.\n\n"
        "Commands:\n"
        "  • `ds --init` → Set your deepstash folder\n"
        "  • `ds <file or folder>` → Deepstash item\n"
        "  • `ds <file>.ds` → Restore stashed item\n"
    ),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
)
