Clone naming
============

When cloning drives or whole servers the paramater for the name of the cloned entity could be omitted.
In that scenario clone naming strategy based on the profile settings is being invoked.

Clone naming strategies are kept on ``clone_naming`` property in the user profile object. Possible values for it:

- ``NONE`` do not append anything to the cloned drive's name. **[default]**
- ``COUNTER`` appends a number at the end of the name or increase it in case there is a number already.
- ``DATE`` appends the current date or try to update it in case there is one already.
- ``TIMESTAMP`` appends the current timestamp or try to update it in case there is one already.

If the date/timestamp at the end is already up-to-date the clone naming strategy will fallback to ``COUNTER``
**without** stripping the date/timestamp before.

Example
--------

Let's say we have a drive named "test_drive_x" and we're going to clone it.
First we want to check out how the counter strategy is working and we're going to set the ``clone_naming`` property
to "COUNTER".

    **Example request**:

    .. includejson:: dumps/request_drive_clone_naming_set_profile_to_counter



    **Example response**:

    .. includejson:: dumps/response_drive_clone_naming_set_profile_to_counter


Great. And now we could clone the drive without bothering to make up a new name for it:

    **Example request**:

    .. includejson:: dumps/request_drive_clone_naming_counter



    **Example response**:

    .. includejson:: dumps/response_drive_clone_naming_counter


Done. Our new drive is named "test_drive_x_1". If you have never changed the ``clone_naming`` property it will be set
to "COUNTER" by default. Let's see how the other two strategies are working.

Starting with "DATE"... *(responses below here are stripped for better readability)*

    **Example request**:

    .. includejson:: dumps/request_drive_clone_naming_set_profile_to_date


Great. And now cloning:

    **Example request**:

    .. includejson:: dumps/request_drive_clone_naming_date



    **Example response**:

    .. includejson:: dumps/response_drive_clone_naming_date
        :accessor: objects.0
        :keys: name


Similary with "TIMESTAMP"...

    **Example request**:

    .. includejson:: dumps/request_drive_clone_naming_set_profile_to_timestamp



Great. And now cloning:

    **Example request**:

    .. includejson:: dumps/request_drive_clone_naming_timestamp


    **Example response**:

    .. includejson:: dumps/response_drive_clone_naming_timestamp
        :accessor: objects.0
        :keys: name
