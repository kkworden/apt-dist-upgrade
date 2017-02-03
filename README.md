# apt-dist-upgrade
When you upgrade Ubuntu to a new version (e.g. 16.04 -> 16.10), your `/etc/apt/sources.list.d` sources are commented out to prevent breaking changes. This Python utility uncomments them so you do not have to go through each file manually and uncomment them.

To run this utility, simply open a terminal and use: `python3 main.py`

This utility is meant to be run with Python 3.x.x, but should be compatible with Python 2.

After you run this utility, it is useful to run `sudo apt update` to check if the repositories are compatible with your OS version.
