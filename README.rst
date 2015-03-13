globussh
========
|Version Status| |Downloads|

Python wrappers around the globus command line interface using ssh.

Example
-------
.. code:: python

   >>> from globussh import transfer_sync
   >>> transfer = "globusid#endpoint1/path/to/file1 glbousid#endpoint2/path/to/file2"
   >>> transfer_sync(transfer, label="example_transfer")

Install
-------

``globussh`` is on the Python Package Index (PyPI):

::

    pip install globussh

.. |Version Status| image:: https://pypip.in/v/globussh/badge.png
   :target: https://pypi.python.org/pypi/globussh/
.. |Downloads| image:: https://pypip.in/d/globussh/badge.png
   :target: https://pypi.python.org/pypi/globussh/

