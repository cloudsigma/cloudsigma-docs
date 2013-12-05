Upload or Download Drive Images
================================

Uploading a drive image
-------------------------

.. http:post:: https://direct.{loc}.cloudsigma.com/api/2.0/drives/upload/

A drive image can be uploaded by issuing a POST request with the image to ``/drive/upload/``. Note that there is a
different domain endpoint for uploads ``direct.{loc}.cloudsigma.com``.

Currently only raw disk images are supported. The request body should contain the raw byte stream of disk a image and
should specify correct content type (``Content-Type: application/octet-stream``) in the request headers. The drive
upload API *supports only Basic HTTP authentication*.

It is very important that the ``Content-Length`` contains the correct size of the data to be sent,
because it determines the size of the drive which will be created. Note that if the uploaded image is smaller than the
minimum drive size (Check :doc:`capabilities`), it will be resized automatically on upload completion.

It is possible to specify the file name in the path, i.e. to upload the image to ``/drive/upload/file_name`` path, but
the file name is ignored. This makes it easier to use tools, such as *curl*, which usually upload to a path ending with
the name of the file.

The returned response contains the UUID of the created drive.

Below is an example on how to upload a drive image using *curl*:

.. sourcecode:: bash

    curl --request POST --user email@example.com:password \
         --header 'Content-Type: application/octet-stream' \
         --upload-file /path/to/file \
         https://direct.zrh.cloudsigma.com/api/2.0/drives/upload/

Note that in the above command specifying the ``Content-Type`` header also sets curl to not encode the body of the
request and leave it as an octet-stream.

The command prints the UUID of the uploaded image. You may want to save it to a file with an output redirect by
appending ``> uploaded_drive_uuid`` at the end of the command.

By default curl does not show upload progress. You may add *--verbose* (*-v*) option if you use curl on the command
line to print the progress and speed of upload.

Downloading a drive image
--------------------------

.. http:get::  https://direct.{loc}.cloudsigma.com/api/2.0/drives/{uuid}/download/

To download a drive image issue a GET request to ``/drives/{uuid}/download/``. Note that there is a different domain
endpoint for image download ``direct.{loc}.cloudsigma.com``. The download client **should handle HTTP redirects**
correctly. The resulting response contains an ``Content-Type: application/octet-stream`` file. The file name is set
to the image UUID in the ``Content-Disposition`` header.

Below is an example on how to download a drive image using *curl*:

.. sourcecode:: bash

    curl --location \
         --remote-name --remote-header-name \
         --user email@example.com:password \
         https://direct.zrh.cloudsigma.com/api/2.0/drives/ad64ded1-be81-454a-aa14-d7809cca93eb/download/

The *--location* option instructs curl to follow redirects. The client is expected to follow HTTP redirects.

The above command uses *--remote-header-name* to save the image into a file named as specified in
``Content-Disposition``. The name in the content disposition is set to the drive UUID. It is possible to specify a
different output name/path with the *--output* (*-o*) option. Note that *--remote-header-name* should always be used
together with *--remote-name*.
