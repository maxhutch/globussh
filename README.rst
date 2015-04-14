globussh
========
|Version Status| |Downloads|

Python wrappers around the globus command line interface using ssh.

Example
-------
.. code:: python

   >>> from globussh import transfer
   >>> src = "globusid#endpoint1/path/to/file1"
   >>> dst = "glbousid#endpoint2/path/to/file2"
   >>> transfer("{:s} {:s}".format(src, dst), label="example_transfer")
   >>> scp(src, dst, label="example_scp")

Install
-------

``globussh`` is on the Python Package Index (PyPI):

::

    pip install globussh

``globush`` expects ssh to have a host ``globus`` in ``~/.ssh/config``, e.g.:

::

    host globus
    HostName cli.globusonline.org
    User maxhutch

.. |Version Status| image:: https://pypip.in/v/globussh/badge.png
   :target: https://pypi.python.org/pypi/globussh/
.. |Downloads| image:: https://pypip.in/d/globussh/badge.png
   :target: https://pypi.python.org/pypi/globussh/

