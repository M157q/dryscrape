from distutils.core import setup, Command

setup(name='dryscrape',
      version='1.0.1',
      description='a lightweight Javascript-aware, headless web scraping library for Python',
      author='Niklas Baumstark',
      author_email='niklas.baumstark@gmail.com',
      license='MIT',
      url='https://github.com/niklasb/dryscrape',
      packages=['dryscrape', 'dryscrape.driver'],
      install_requires=['webkit_server==1.0-tagtoo', 'lxml', 'xvfbwrapper'],
      dependency_links=['git+git://github.com/Tagtoo/webkit-server.git#egg=webkit_server-1.0-tagtoo'],
      )
