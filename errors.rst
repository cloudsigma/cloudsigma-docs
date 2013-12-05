Errors
======

Format
------

	When one or more errors occur, they are returned to the client in an object with three fields:
	
	.. _error_type:
	
	* ``error_type``: The type of error, one of: :ref:`validation <validation>`, :ref:`notexist <notexist>`, :ref:`backend <backend>`, :ref:`permission <permission>`, :ref:`database <database>`, :ref:`concurrency <concurrency>`, :ref:`billing <billing>`, :ref:`payment <payment>`
	
	.. _error_message:
	
	* ``error_message``: A description of the error that occurred.
	
	.. _error_point:
	
	* ``error_point``: The point at which the error occurred. Always present, but can sometimes be null.


Types
-----
    The types of errors:
    
    .. _validation:

    * ``validation``: An error occurred while validating the submitted data. If the error is related to a particular field, it will set the :ref:`error_point <error_point>`.
        
    .. _notexist:

    * ``notexist``: The object you are trying to access does not exist.
        
    .. _backend:

    * ``backend``: There was a problem completing the request on the backend. Please contact the support department.
        
    .. _permission:

    * ``permission``: You do not have permission to complete the operation. May set the :ref:`error_point <error_point>`.
            
    .. _database:

    * ``database``: There was a database error.
            
    .. _concurrency:

    * ``concurrency``: There was a concurrency error caused by two simultaneous conflicting operations (i.e. trying to start and delete a server at the same time). The operation should be retried.  
        
    .. _billing:

    * ``billing``: There was a billing problem. 

    .. _payment:

    * ``payment``: There was a problem processing your payment.

    
Example
-------

.. http:post:: /subscriptions/

   **Example request**:

    .. parsed-literal::    

        {
            "amount": "1",
            "from_time": "2012-03-28T14:10:15.948157",
            "period": "2 weeks"
        }
   
   **Example response**:

    .. parsed-literal::

		[
		    {
		        "error_message": "This field is required", 
		        "error_point": "resource", 
		        "error_type": "validation"
		    }
		]

