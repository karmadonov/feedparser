from distutils.core import setup

# patch distutils if it can't cope with the "classifiers" or "download_url"
# keywords (prior to python 2.3.0).
from distutils.dist import DistributionMetadata
if not hasattr(DistributionMetadata, 'classifiers'):
    DistributionMetadata.classifiers = None
if not hasattr(DistributionMetadata, 'download_url'):
    DistributionMetadata.download_url = None
    
setup(
    name = 'feedparser',
    version = '3.0',
    description = 'Universal feed parser, handles RSS 0.9x, RSS 1.0, '
                  'RSS 2.0, CDF, Atom feeds',
    long_description = """\
Universal feed parser
---------------------

Handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom feeds

Required: Python 2.1 or later
Recommended: Python 2.3 or later
Recommended: libxml2 <http://xmlsoft.org/python.html>
""",
    author='Mark Pilgrim',
    author_email = 'mark@diveintomark.org',
    url = 'http://diveintomark.org/projects/feed_parser/',
    download_url = 'http://diveintomark.org/projects/feed_parser/',
    license = "Python",
    platforms = ['POSIX', 'Windows'],
    keywords = ['feed parser', 'feeds', 'rss', 'atom', 'cdf'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    py_modules = ['feedparser',]
    )
