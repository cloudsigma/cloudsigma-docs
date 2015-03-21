Server Context
==============

Server context is a way for the VM to get information on the way it was set-up, i.e. get it's definition. Server
context is communicated over a virtual serial port device, which on UNIX-like operating system would usually appear as
``/dev/ttyS1`` and on Windows as ``COM2``. The serial port device for server context is the second serial device
attached to the VM, because some UNIX operating systems configure a serial console on the first serial port.

Having the server definition accessible by the VM can be useful in various ways. For example it is possible to easily
determine from within the VM, which network interfaces are connected to public and which to private network. Another
use is to pass some data to initial VM setup scripts, like setting the hostname to the VM name or passing ssh public
keys through server metadata.

At first sight, it might be confusing with the presence of both 'server context' and 'server metadata'.
'server metadata' is really a subset of 'server context'. The 'server metadata' itself is a key-value store for
user-defined data on a server definition. The 'server context' on the other hand is one step above. It includes the
full server definition, as well as the server metadata, along with attached drives definitions.

Context schema
--------------

The server context has almost the same schema as the */server/<uuid>/detail/* API request schema. It differs in that it
lacks owner, subscriptions, status, and runtime information. The other difference is that the drives attributes are
expanded to the corresponding */drive/<uuid>/detail/* which also lacks owner and runtime information. There is also
a ``global_context`` attribute, which contains context available on all servers (see :ref:`drive edit <drive-edit>`).


Setting up the virtual serial port
----------------------------------

The virtual serial port device in not connected to a hardware device on the other side, so setting serial port hardware
settings, such as baud rate and parity bits, does not affect the actual communication. However on Unix-like operating
systems it may be necessary to set up the virtual terminal connected to the serial device. In general it is advisable
to use the terminal in raw mode so that all characters are received uninterpreted. It is also important to not echo
back received responses, because the may fill up the receive buffer, which may eject pending requests.

To set-up the terminal to raw mode on most unix systems one needs to the following command:

.. sourcecode:: bash

    stty -F /dev/ttyS1 raw -echo

It is also possible to use `cooked mode <https://en.wikipedia.org/wiki/Cooked_mode>`_  terminal for checking data on
command line using standard utilities such as ``echo``, ``read``, and ``cat``. As all responses are followed by newline
and an `End of Transmission <https://en.wikipedia.org/wiki/End-of-transmission_character>`_ character (usually
represented as ``^D`` or ``"\0x04"``), so setting the terminal to cooked mode would make it interpret the EOT character
as an `End-Of-File <https://en.wikipedia.org/wiki/End_of_file>`_ condition, which makes it possible to use ``read`` and
``cat`` on the terminal device file (/dev/ttyS1) to receive the response. To set up cooked mode use the following
command:

.. sourcecode:: bash

    stty -F /dev/ttyS1 cooked -echo

If the default EOF character is different on your terminal it may be necessary to change it using:

.. sourcecode:: bash

    stty -F /dev/ttyS1 cooked -echo eol ^D


Server Context Protocol
-----------------------

Requesting the complete server context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a simple protocol to retrieve the server context from the serial device. To request the whole server context
one needs to send two newlines enclosed between inequality signs (aka pointy brackets, angle brackets). The newline
can be either ``CRLF`` or just ``LF``. In most programming languages the string to send will look like ``"<\n\n>"``.

The resulting response is a single-line json string representing the definition of the VM followed by newline (line
feed character) and and an `End of Transmission <https://en.wikipedia.org/wiki/End-of-transmission_character>`_
character (usually represented as ``^D`` or ``"\0x04"``). On Unix-like operating systems, if the terminal is set to
cooked mode it is possible that the EOT character is interpreted as End-Of-File and is not present in the response.

The example below is for a server with the following definition:

.. literalinclude:: dumps/request_guest_for_context
    :language: http


Request the complete server context using python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The best way to access the context is to use a serial port communication library from your favourite programming
language. Below is an example using the Python programming language and the pySerial libraray:

.. sourcecode:: python

    #!/bin/env python

    # This will work on python 2.6 and python 2.7

    import serial;  # pySerial module is called 'serial'

    s = serial.Serial("/dev/ttyS1")  # initialize a serial connection to '/dev/ttyS1'
    s.write("<\n\n>")  # write an empty request to get the full context

    context_str_raw = s.readline()  # read one line, which is the whole context as there are no newlines in the context
    # Take the context string and remove any starting/trailing newlines and \x04 symbols
    context_str = context_str_raw.strip("\x04\n")
    print context_str  # print the context to stdout

Here the same code, as a one-liner, which can be executed directly in bash, or another shell:

.. literalinclude:: dumps/request_context_all_robust
    :language: bash

**Example:**

.. literalinclude:: dumps/request_context_all_robust
    :language: bash

Result:

.. literalinclude:: dumps/response_context_all
    :language: javascript


Request the complete server context using bash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is also possible to issue the reques using just standard commands such as ``read``, ``echo``, and ``cat``.
Unfortunately that method is prone to errors because it breaks if there are escaped json values, such as
``"value contains quote: \""``, so it is higly recommended to use a serial communication library, such as the python
example above.
Below is an example of making a request, reading the result, and printing it on Linux in the bash shell:

.. sourcecode:: bash

    #!/bin/bash

    # set the terminal to cooked mode:
    stty -F /dev/ttyS1 cooked -echo eol ^D
    # use -e to parse newline escapes, and -n to remove the trailing newline:
    echo -en "<\n\n>" > /dev/ttyS1
    # read with timeout of 3 seconds and print the value which is put in the variable READVALUE
    read -t 3 READVALUE < /dev/ttyS1 && echo $READVALUE

**Example:**

Request command. Including a flushing read before the actual request with echo:

.. literalinclude:: dumps/request_context_all
    :language: bash

Result:

.. literalinclude:: dumps/response_context_all
    :language: javascript


Requesting a partial server context or a single value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To request a part of the definition json one can provide a path in the request. The path contains strings or integers
separated by a forward slash (/). To request only the part of the json which is the NICs definitoins one can request
the path *"/nics"*. To request an element from a list value one can use an index in the path. Note that counting starts
from 0. For example to get the defintion of the first network interface one can use the following path *"/nics/0"*.

If the value of pointed to the path is a leaf value (it does not contain a json object or alist), it is returned without
the surrounding quotes so requesting ``<\nname\n>`` from a server named "myserver" would return:

.. sourcecode:: bash

    myserver\n\0xd

and *NOT*:

.. sourcecode:: bash

    "myserver"\n\0xd

Be advised that the returned strings won't contain surrounding quotes but ASCII control characters will be backslash
escaped. For example line-feed will become ``\n``, carriage-return will become ``\r``, and tab will become ``\t``. Also
there is no way to represent ``null`` json values so this will be converted to an empty string. Make sure that you
parse the escaped characters if you need the original unescaped text in your scripts. An easy way to do it on UNIX-like
OS is to use ``echo -e $READVALUE``.

**Examples:**

.. literalinclude:: dumps/request_context_single_value
    :language: bash

Result:

.. literalinclude:: dumps/response_context_single_value


Passing information to the VM
-----------------------------

The most suitable place to store information for passing to the VM through the context interface is the server
``meta`` field, or drive ``meta``. Check :doc:`meta` for more information on editing the ``meta`` field.

For example in the server definition from above examples, the meta looks like:

.. includejson:: dumps/response_guest_for_context
    :accessor: meta
    :keys: ssh_public_key
    :hide_header: true

One can retrieve the ``ssh_public_key`` from the ``meta`` from within the VM using:

.. literalinclude:: dumps/request_context_single_value_ssh_key
    :language: bash

Result:

.. literalinclude:: dumps/response_context_single_value_ssh_key

Note that there isn't anything special about the ``ssh_public_key`` attribute of the metadata. It can be stored under
any other key in the server metadata, as long as client software is aware where to look for it. It is also possible to
store the key in one of the attached drives' meta.

.. _global-context:

Global context
--------------

Global context can be used to hold server context information common to all user's servers. Like ``meta`` field on
servers, it can store arbitrary key-value pairs, but as the name suggests it is global for the user account, and the
same for all servers.

Global context is centrally managed at the */global_context/* API url. Within the VM context it resides in the
``global_context`` attribute of the server server definition.

Get or update global context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /global_context/
.. http:post:: /global_context/


**Example:**

Add a value to the global context.

.. literalinclude:: dumps/request_update_global_context
    :language: http

The resulting global context is:

.. literalinclude:: dumps/response_update_global_context
    :language: javascript

Using the server from examples above, we can check the context from the server shell:

Request command:

.. literalinclude:: dumps/request_global_context_all_robust
    :language: bash

Result:

.. literalinclude:: dumps/response_global_context_all
    :language: javascript

Notice how the value of the ``global_context`` changed:

.. includejson:: dumps/response_global_context_all
    :keys: global_context
    :hide_header: true
