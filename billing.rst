Billing
=======

.. _balance:

Balance
-------

Allowed HTTP methods
~~~~~~~~~~~~~~~~~~~~

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics




Listing
~~~~~~~

.. http:get:: /balance/

    Get the balance and currency of the current account.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_balance_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_balance_list
        :language: javascript

Schema
~~~~~~

   .. literalinclude:: dumps/response_balance_schema
        :language: javascript
Schema listing for getting the balance and currency of the current account:

1. allowed_detail_http_methods:Array of allowed HTTP methods for detailed views.

2. allowed_list_http_methods:Array of allowed HTTP methods for listing.

3. default_format:Default format for the response (e.g., "application/json").

4. default_limit:Default limit for the number of items in a response.

fields:

5. balance: This field represents the amount of money in the account. It is read-only, meaning it cannot be updated directly, and it's required as it is a fundamental piece of information about the account. The data type is decimal, which is appropriate for handling monetary values.

6. credit_limit: This field indicates the credit limit applied to the account, if applicable. Like balance, it is read-only and required. The data type is a string, suggesting that credit limits might be represented as alphanumeric values.

7. currency: This field specifies the currency of the account. It is read-only, required, and has a data type of string, indicating that it holds textual information about the currency.

filtering:

7. name:Filter Type: "exact", This filter allows to retrieval objects where the "name" field exactly matches the specified value.

8. name__contains:Filter Type: "exact", Similar to the name filter, this allows retrieving objects where the "name" field exactly matches the specified value.

9. tag:Filter Type: "exact", This filter enables retrieval objects based on an exact match for the "tag" field. If you have objects tagged with specific identifiers, you can use this filter to fetch those objects precisely.

10. uuid: This filter is designed to retrieve objects based on an exact match for the "uuid" (Universally Unique Identifier) field.

**Note**:
  * The API allows to retrieval of information about available discount periods and their corresponding values.

  * The discount periods are provided in the "objects" array, each with a "period" and a "value."

  * The "period" indicates the duration for which the discount is applicable (e.g., 3 months, 6 months).

  * The "value" represents the discount value, provided as a string representing a decimal number.

Pricing
-------

Allowed HTTP methods
~~~~~~~~~~~~~~~~~~~~

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics




Listing
~~~~~~~

.. http:get:: /pricing/

    Gets the pricing information that applies to the cloud. Subscription prices use a burst level of 0.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_pricing_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_pricing_list
        :language: javascript



  * Current: current contains the current burst level

The parameters inside the "objects" section represent different types of resources or services and their corresponding usage counts. Here's an explanation for each parameter:

  * backup: The number of instances or units of backup service currently in use.

  * CPU: The number of instances or units of CPU resources currently in use.

  * cpu_vmware: The number of instances or units of CPU resources specific to VMware currently in use.

  * dedicated_host_6148: The number of instances or units of dedicated hosts with model 6148 currently in use.

  * dedicated_node_large: The number of instances or units of large dedicated nodes currently in use.

  * dedicated_node_medium: The number of instances or units of medium dedicated nodes currently in use.

  * dedicated_node_small: The number of instances or units of small dedicated nodes currently in use.

  * disaster_recovery: The number of instances or units of disaster recovery service currently in use.

  * dssd: The number of instances or units of DSSD (Data Scale-out Storage) currently in use.

  * dssd_vmware: The number of instances or units of DSSD specific to VMware currently in use.

  * EPC: The number of instances or units of EPC (Evolved Packet Core) currently in use.

  * gpu_amd_mi50: The number of instances or units of AMD MI50 GPUs (Graphics Processing Units) currently in use.

  * gpu_nvidia_a100: The number of instances or units of NVIDIA A100 GPUs currently in use.

  * gpu_nvidia_a6000: The number of instances or units of NVIDIA A6000 GPUs currently in use.

  * intel_cpu: The number of instances or units of Intel CPUs currently in use. (Note: It has a count of 2)

  * intel_mem: The number of instances or units of Intel memory currently in use.

  * ip: The number of instances or units of IP addresses currently in use.

  * ip_vmware: The number of instances or units of IP addresses specific to VMware currently in use.

  * mem: The number of instances or units of memory currently in use.

  * mem_vmware: The number of instances or units of memory specific to VMware currently in use.

  * Migration: The number of instances or units of migration service currently in use.

  * msft_6wc_00002: The number of instances or units of a Microsoft service with code "6wc_00002" currently in use.

  * msft_7jq_00341: The number of instances or units of a Microsoft service with code "7jq_00341" currently in use.

  * msft_7nq_00302: The number of instances or units of a Microsoft service with code "7nq_00302" currently in use.

  * msft_9ea_00039: The number of instances or units of a Microsoft service with code "9ea_00039" currently in use.

  * msft_p73_04837_core: The number of instances or units of a Microsoft service with code "p73_04837_core" currently in use.

  * msft_tfa_00523: The number of instances or units of a Microsoft service with code "tfa_00523" currently in use.

nvme: The number of instances or units of NVMe (Non-Volatile Memory Express) currently in use.

  * object_storage: The number of instances or units of object storage service currently in use.

  * rx_foreign: The number of instances or units of foreign RX (Receive) currently in use.

  * rx_local: The number of instances or units of local RX (Receive) currently in use.

  * ssd: The number of instances or units of SSD (Solid State Drive) currently in use.

  * tx: The number of instances or units of TX (Transmit) currently in use.

  * tx_foreign: The number of instances or units of foreign TX (Transmit) currently in use.

  * tx_local: The number of instances or units of local TX (Transmit) currently in use.

  * tx_vmware: The number of instances or units of TX (Transmit) specific to VMware currently in use.

  * virtual_private_cloud: The number of instances or units of virtual private cloud service currently in use.

  * vlan: The number of instances or units of VLANs (Virtual Local Area Networks) currently in use.

  * vlan_ecx: The number of instances or units of VLANs specific to Equinix Cloud Exchange currently in use.

  * vlan_ecx_1000: The number of instances or units of VLANs with a specific bandwidth (1000 Mbps) currently in use.

  * vlan_ecx_200: The number of instances or units of VLANs with a specific bandwidth (200 Mbps) currently in use.

  * vlan_ecx_500: The number of instances or units of VLANs with a specific bandwidth (500 Mbps) currently in use.

  * vlan_vmware: The number of instances or units of VLANs specific to VMware currently in use.

  * vpc: The number of instances or units of VPCs (Virtual Private Clouds) currently in use.

  * vrouter_basic: The number of instances or units of a basic virtual router currently in use.

  * vrouter_basic_500: The number of instances or units of a basic virtual router with a specific bandwidth (500 Mbps) currently in use.

  * vrouter_enterprise: The number of instances or units of an enterprise virtual router currently in use.

  * vrouter_premium: The number of instances or units of a premium virtual router currently in use.

  * zadara: The number of instances or units of Zadara storage currently in use.

These parameters provide a detailed breakdown of the current usage of various resources or services in the listed environment.

  * Next: next contains the next burst level

the parameters for the count and usage status of different resources or services in a system:

  * backup: The number of instances or units of backup service currently in use.

  * CPU: The number of instances or units of CPU resources currently in use.

  * cpu_vmware: The number of instances or units of CPU resources specific to VMware currently in use.

  * dedicated_host_6148: The number of instances or units of dedicated hosts with model 6148 currently in use.

  * dedicated_node_large: The number of instances or units of large dedicated nodes currently in use.

  * dedicated_node_medium: The number of instances or units of medium dedicated nodes currently in use.

  * dedicated_node_small: The number of instances or units of small dedicated nodes currently in use.

  * disaster_recovery: The number of instances or units of disaster recovery service currently in use.

  * dssd: The number of instances or units of DSSD (Data Scale-out Storage) currently in use.

  * dssd_vmware: The number of instances or units of DSSD specific to VMware currently in use.

  * EPC: The number of instances or units of EPC (Evolved Packet Core) currently in use.

  * gpu_amd_mi50: The number of instances or units of AMD MI50 GPUs (Graphics Processing Units) currently in use.

  * gpu_nvidia_a100: The number of instances or units of NVIDIA A100 GPUs currently in use.

  * gpu_nvidia_a6000: The number of instances or units of NVIDIA A6000 GPUs currently in use.

  * intel_cpu: The number of instances or units of Intel CPUs currently in use. (Note: It has a count of 2)

  * intel_mem: The number of instances or units of Intel memory currently in use.

  * ip: The number of instances or units of IP addresses currently in use.

  * ip_vmware: The number of instances or units of IP addresses specific to VMware currently in use.

  * mem: The number of instances or units of memory currently in use.

  * mem_vmware: The number of instances or units of memory specific to VMware currently in use.

  * Migration: The number of instances or units of migration service currently in use.

msft_6wc_00002: The number of instances or units of a Microsoft service with code "6wc_00002" currently in use.

  * msft_7jq_00341: The number of instances or units of a Microsoft service with code "7jq_00341" currently in use.

  * msft_7nq_00302: The number of instances or units of a Microsoft service with code "7nq_00302" currently in use.

  * msft_9ea_00039: The number of instances or units of a Microsoft service with code "9ea_00039" currently in use.

  * msft_p73_04837_core: The number of instances or units of a Microsoft service with code "p73_04837_core" currently in use.

  * msft_tfa_00523: The number of instances or units of a Microsoft service with code "tfa_00523" currently in use.

  * nvme: The number of instances or units of NVMe (Non-Volatile Memory Express) currently in use.

  * object_storage: The number of instances or units of object storage service currently in use.

  * rx_foreign: The number of instances or units of foreign RX (Receive) currently in use.

  * rx_local: The number of instances or units of local RX (Receive) currently in use.

  * ssd: The number of instances or units of SSD (Solid State Drive) currently in use.

  * tx: The number of instances or units of TX (Transmit) currently in use.

  * tx_foreign: The number of instances or units of foreign TX (Transmit) currently in use.

  * tx_local: The number of instances or units of local TX (Transmit) currently in use.

  * tx_vmware: The number of instances or units of TX (Transmit) specific to VMware currently in use.

  * virtual_private_cloud: The number of instances or units of virtual private cloud service currently in use.

  * vlan: The number of instances or units of VLANs (Virtual Local Area Networks) currently in use.

  * vlan_ecx: The number of instances or units of VLANs specific to Equinix Cloud Exchange currently in use.

  * vlan_ecx_1000: The number of instances or units of VLANs with a specific bandwidth (1000 Mbps) currently in use.

  * vlan_ecx_200: The number of instances or units of VLANs with a specific bandwidth (200 Mbps) currently in use.

  * vlan_ecx_500: The number of instances or units of VLANs with a specific bandwidth (500 Mbps) currently in use.

  * vlan_vmware: The number of instances or units of VLANs specific to VMware currently in use.

  * vpc: The number of instances or units of VPCs (Virtual Private Clouds) currently in use.

  * vrouter_basic: The number of instances or units of a basic virtual router currently in use.

  * vrouter_basic_500: The number of instances or units of a basic virtual router with a specific bandwidth (500 Mbps) currently in use.

  * vrouter_enterprise: The number of instances or units of an enterprise virtual router currently in use.

  * vrouter_premium: The number of instances or units of a premium virtual router currently in use.

  * zadara: The number of instances or units of Zadara storage currently in use.

The parameters for the current usage of various resources or services in the listed environment:

  * objects: An array containing information about individual resources and their pricing details. Each object in the array represents a specific resource. Let's explain the parameters for one of the resource objects:

  * Currency: The currency in which the pricing information is provided (e.g., "AUD" for Australian Dollar).

  * id: A unique identifier for the resource.

  * Level: The level or category of the resource. In this example, it's set to 4.

  * multiplier: A value used as a multiplier to calculate the price. In this case, it's 3600000.

  * price: The price of the resource. It's a decimal value, and in this example, it's "0.02400000000000000000."

  * resource: The type or category of the resource (e.g., "intel_cpu").

unit: The unit in which the resource usage is measured. In this case, it's "GHz/hour."

This information provides details about the Current and next burst levels.

This is the API call to get the current usage and pricing for various resources, including their currency, identifier, level, multiplier, price, resource type, and unit of measurement. The objects array contains details for each resource present in the listing.

The burst levels are calculated every 5 minutes based on the usage of the cloud and are applied 5 minutes later (when the next burst levels are calculated)

The billing cycle is executed every five minutes, and the burst is calculated for all the customers.

If a customer is bursting a resource, then the system bills for that:

Example:

Burst: 4.50 GB of dssd for 5 minutes at 2014-06-05 09:06

Billing — CloudSigma API v2 documentation

How burst is calculated?

Example:

A user has subscriptions for 100Gb, but she has two drives, 75Gb each.

That means her current usage is 150Gb.

100Gb are covered by the subscription

The billing cycle will bill the extra 50Gb

  * Multiplier: The multiplier is a factor applied to calculate the price based on the unit of the resource. In this case, it's used to determine the cost of one unit per second for the specified resource.

To find the cost for a certain amount of the resource, that amount should be multiplied by the multiplier.

In response, for finding the cost of using 1 GB of the specified resource for one month, this formula can be used: The price is calculated using the formula:

bill = price * interval(seconds) * amount / resource.multiplier

The multiplier value is a large integer (2783138807808000), and its specific significance would depend on the internal calculations or conventions used by the API provider.

In summary, the multiplier is a factor applied to calculate the price for a specific resource, and its exact interpret

Burst levels
~~~~~~~~~~~~
    The current and future burst levels are provided in objects at the root of the response. The burst levels are calculated every 5 minutes based on the usage of the cloud and are applied 5 minutes later (when the next burst levels are calculated)

    .. includejson:: dumps/response_pricing_list
        :keys: current, next

Schema
~~~~~~

   .. literalinclude:: dumps/response_pricing_schema
        :language: javascript

Discounts
---------

Allowed HTTP methods
~~~~~~~~~~~~~~~~~~~~

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
~~~~~~~

.. http:get:: /discount/

   Get discount information.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_discount_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_discount_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_discount_schema
        :language: javascript




Transaction list
----------------

Allowed HTTP methods
~~~~~~~~~~~~~~~~~~~~

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
~~~~~~~

.. http:get:: /ledger/

   Get the transactions for the account.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_ledger_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_ledger_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_ledger_schema
        :language: javascript


  * Amount: The numeric value representing the amount of the transaction. In this context, it's "0.00014583333333333333." this is the actual value of the transaction, which could represent monetary values or quantities associated with the transaction.

  * billing_cycle: An identifier associated with the billing cycle. In this response, it's "105157." this is an identifier associated with the billing cycle, indicating when the transaction occurred in the billing cycle.

  * end: A timestamp or numeric value indicating the end of a particular period or transaction. In this case, it's "469291.07488238102453490453." This indicates the end of the transaction or the end of a specific period.

  * human_interval: A human-readable representation of the interval. In this context, it's "5 minutes." this is a human-readable representation of the interval, providing an easy-to-understand description of the duration.

  * id: A unique identifier for the transaction. Here, it's "39509304."

initial: A numeric value representing the initial state or value. In this response, it's "469291.07502821435786823786."

  * interval: The duration of the interval, measured in seconds. In this case, it's "300" seconds (5 minutes).

  * poll_time: A timestamp indicating the time of polling or recording the transaction. For response, "2014-06-05T09:06:06.713945+00:00."

  * Reason: A human-readable explanation or reason for the transaction. In this context, it's "Burst: 4.50 GB of dssd for 5 minutes at 2014-06-05 09:06."

  * resource_amount: A numeric value representing the amount of a specific resource associated with the transaction. Here, it's "4831838208."

  * Time: A timestamp indicating the time of the transaction. For instance, "2014-06-05T09:08:47.992023+00:00."


Discounts
---------

Allowed HTTP methods
~~~~~~~~~~~~~~~~~~~~

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
~~~~~~~

.. http:get:: /discount/

   Get discount information.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_discount_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_discount_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_discount_schema
        :language: javascript

.. _current-usage:

Current usage
-------------

Allowed HTTP methods
~~~~~~~~~~~~~~~~~~~~

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
~~~~~~~

.. http:get:: /currentusage/

    Get the current usage of the user.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/request_currentusage_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_currentusage_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_currentusage_schema
        :language: javascript

The response from the Current Usage API provides information about the current usage of various resources associated with the user.

  * Balance: The current balance associated with the user's account. In the response, it's "155367.99237092264288897986."

  * Currency: The currency of the balance. In the response, it's "EUR."

**usage**:

  * amd_cpu: Information about the usage of AMD CPU.

  * burst: The burst level of AMD CPU usage.

  * subscribed: The subscribed or allocated amount of AMD CPU resources.

  * using: The currently used amount of AMD CPU resources.

  * amd_mem: Information about the usage of AMD memory.

  * burst: The burst level of AMD memory usage.

  * subscribed: The subscribed or allocated amount of AMD memory resources.

  * using: The currently used amount of AMD memory resources.

  **CPU**: Information about the usage of general CPU resources.

  * burst: The burst level of CPU usage.

  * subscribed: The subscribed or allocated amount of general CPU resources.

  * using: The currently used amount of general CPU resources.

  * dssd(Distributed ssd) : Following the next example

A user has subscriptions for 100Gb, but she has two drives, 75Gb each.

That means the current usage is 150Gb.

100Gb are covered by the subscription

The billing cycle will bill the extra 50Gb

The values for every field are:

burst: 50Gb

subscribed: 100Gb

using: 150Gb

The logic is the same for all the resources.

  * burst: The burst level of DSSD usage.

  * subscribed: The subscribed or allocated amount of DSSD resources.

  * using: The currently used amount of DSSD resources.

  * IP: Information about the usage of IP addresses.

  * burst: The burst level of IP address usage.

  * subscribed: The subscribed or allocated amount of IP addresses.

  * using: The currently used amount of IP addresses.

  * mem: Information about the usage of general memory resources.

  * burst: The burst level of memory usage.

  * subscribed: The subscribed or allocated amount of general memory resources.

  * using: The currently used amount of general memory resources.

  * msft_7jq_00341 to zadara: Similar information about the usage of other specific resources. Each resource has the same structure:

  * burst: The burst level of resource usage.

  * subscribed: The subscribed or allocated amount of the specific resource.

  * using: The currently used amount of the specific resource.

These parameters collectively provide a detailed snapshot of the user's current resource usage across various categories, including CPU, memory, storage, IP addresses, and other specific resources. The information includes burst levels, subscribed amounts, and currently used amounts for each resource category.


.. _billing-license:

Licenses list
-------------

Allowed HTTP methods
~~~~~~~~~~~~~~~~~~~~

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
~~~~~~~

.. http:get:: /licenses/

   Get the licenses available on the cloud. The type of the license can be one of:

   :statuscode 200: no error

   * install - These licenses are billed per installation, regardless of whether it is attached to a running server or not.
   * instance - These licenses are billed per running instance of a server. A license attached to a guest that's stopped is not billed.
   * stub - These licenses are billed per a metric specified by the customer (i.e. per number of users license)

   The user metric field specifies what attribute on the instance of the server is used for determining the number of
   licenses. For example, "smp" will count one license for each CPU/core in the virtual machine.

    **Example request**:

    .. literalinclude:: dumps/request_licenses_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_licenses_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_licenses_schema
        :language: javascript

The Licenses endpoint provides information about the licenses available on the cloud. the parameters collectively provide information about the licenses available on the cloud, including their types, burstability, names, and associated metrics for determining usage. The objects array contains details for each license present in the cloud.

**meta**:

  * Limit: The maximum number of results to be returned. In the response, it's set to 20.

  * offset The starting index for the current set of results. In the response, it's set to 0.

  * total_count: The total number of available licenses. In the response, it's 4.

  * objects: (number of licenses the customer can use without being charged) An array containing information about individual licenses. Each license object has the following parameters:

  * burstable: Indicates whether the license is burstable or not. If true, the license is burstable; if false, it's not burstable(It means you need a subscription to use the license.).

  * long_name: The full or long name of the license. For response, "SQL Server Enterprise Edition" or "Windows Server."

  * Name: A short or abbreviated name of the license. For response, "msft_7jq_00341" or "msft_p73_04837_core."

  * resource_uri: The URI (Uniform Resource Identifier) that can be used to access detailed information about the license.

  * type: The type of the license, which can be one of the following:

  * install: These licenses are billed per installation, regardless of whether it is attached to a running server or not.

  * instance: These licenses are billed per running instance of a server. A license attached to a guest that’s stopped is not billed.

  * stub: These licenses are billed per a metric specified by the customer (e.g., per number of users).

  * user_metric: If the license type is a stub, this field specifies what attribute on the instance of the server is used for determining the number of licenses. For response, "smp" will count as one license for each CPU/core in the virtual machine.
