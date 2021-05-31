Contributing
****

.. contents::
    :backlinks: none

.. sectnum::

Setup
=====
1. Fork it.

2. Clone it

3. Create a `virtualenv <http://pypi.python.org/pypi/virtualenv>`__

.. code:: bash

    $ virtualenv develop              # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/ab-anand/Zdrive.git
    (develop)$ cd Zdrive
    (develop)$ pip install -r requirements.txt  # Install requirements for 'Zdrive' in virtual environment

Or, if ``virtualenv`` is not installed on your system:

.. code:: bash

    $ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    $ python virtualenv.py develop    # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/ab-anand/Zdrive.git
    (develop)$ cd Zdrive
    (develop)$ pip install -r requirements.txt  # Install requirements for 'Zdrive' in virtual environment

3. Create your feature branch (``$ git checkout -b my-new-awesome-feature``)

4. Commit your changes (``$ git commit -am 'Added <xyz> feature'``)


Conform to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__ and if everything is running fine, integrate your feature

5. Push to the branch (``$ git push origin my-new-awesome-feature``)

6. Create new Pull Request

Hack away!

To do
====

-  Make pickling of credentials optional
-  Write unittests
- There are lot of filters for searching a file/folder in Drive. Use the link available in the section `below <https://github.com/ab-anand/Zdrive/blob/master/CONTRIBUTING.rst#useful-references>`__ and try implementing anything you find interesting.

Useful References
====

- https://developers.google.com/drive/api/v3/about-files


