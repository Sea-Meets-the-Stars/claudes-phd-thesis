
# Standard imports
import glob, os
from setuptools import setup, find_packages


# Begin setup
setup_keywords = dict()
setup_keywords['name'] = 'claudes_phd_thesis'
setup_keywords['description'] = 'Code, analyses, and figures behind a PhD thesis written by Claude'
setup_keywords['author'] = 'J. Xavier Prochaska'
setup_keywords['author_email'] = 'jxp@ucsc.edu'
setup_keywords['license'] = 'BSD'
setup_keywords['url'] = ''  # TODO: set once the GitHub repository exists
setup_keywords['version'] = '0.0.dev0'
# Use README.md as long_description.
setup_keywords['long_description'] = ''
if os.path.exists('README.md'):
    with open('README.md') as readme:
        setup_keywords['long_description'] = readme.read()
setup_keywords['provides'] = [setup_keywords['name']]
setup_keywords['python_requires'] = '>=3.12'
# Core scientific stack only.  The thesis topic is not settled yet (see the
# "Thesis topic" prompt in claude_prompts/start_up.md); domain dependencies get
# added here, and to requirements.txt, once it is.
setup_keywords['install_requires'] = [
    'numpy', 'scipy', 'pandas', 'matplotlib', 'seaborn',
    'scikit-learn', 'tqdm', 'IPython', 'pytest']
setup_keywords['zip_safe'] = False
setup_keywords['packages'] = find_packages()

if os.path.isdir('bin'):
    setup_keywords['scripts'] = [fname for fname in glob.glob(os.path.join('bin', '*'))
                                 if not os.path.basename(fname).endswith('.rst')]

setup(**setup_keywords)
