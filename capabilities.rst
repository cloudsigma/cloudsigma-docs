Capabilities
============

Allowed HTTP methods
--------------------

+--------+--------------------------------------------------+
| Method | Description                                      |
+========+==================================================+
| GET    | get the capabilities object                      |
+--------+--------------------------------------------------+

.. note::
    
    See :rfc:`2616#section-9` for more details on HTTP methods semantics



The capabilities API call is used to gather all the basic, sensible limits of the API, to prevent applying static
limits inside the client application.

Bare in mind, that these capabilities are dynamic - they are based on the cloud usage, location, etc. For example
a location might not support **lssd**, but support **magnetic** disk option, or vise versa. If a feature is not supported or
is disabled, it will disappear from the result of this call. Most entries are obvious limits on the guest or drive properties.

:hosts:
    A list of available host types and their limitations.

    :cpu_per_smp:
        This gives a range of valid cpu values, per smp, for the given host type. For example, for AMD hosts, one CPU must be
        between 1000 and 2500MHz: a guest 2000MHz cpu and 2 smp has 1000MHz per smp and is valid, but a guest with
        8000MHz cpu and 2 smp has a 4000MHz per smp is not.

.. _hypervisors:

:hypervisors:
    A list of hypervisors and which hosts they are available on. More details on the hosts can be found in the in the
    hosts entry.

:drives:
    A list of available drive types and their limitations. The values in max_size and min_size are deprecated and are
    identical to the nested ones in size.

:snapshots:
    Information about the current and maximum number of snapshots allowed for the account. These are global, not per drive.

:servers:
    This entry is deprecated and contains the same values for amd hosts.

.. http:get:: /capabilities/

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_capabilities
    :language: http

**Response**:

.. literalinclude:: dumps/response_capabilities
    :language: javascript

### This is an explanation of the API response parameters:

* id: It is the unique identifier for the currency. In this case, "CHF" represents the Swiss Franc.

* name: It is the common or display name for the currency. In this case, "chf" represents the abbreviation or name used to refer to the Swiss Franc.

So, this entry indicates that the system supports the Swiss Franc (CHF) as a currency, and "chf" is the identifier or name used within the system for this currency.

* default_inactive_period: The default inactive period is defined as days. A value of 45 indicates the inactive period is 45 days.

This value is used to find the users with the last login made 45 days ago(using the value in the previous paragraph) and mark them as INACTIVE users.

* default_storage_type: Indicates the default storage type (e.g., "dssd").

* drives: Provides detailed information about available drive types and their limitations, including IOPS and size ranges. Example:

```
{
  "dssd": {
    // Details about dssd drive type
  },
  "nvme": {
    // Details about nvme drive type
  },
  "zadara": {
    // Details about zadara drive type
  }
}
```

* epc: The epc values are related to the Intel SGX enclaves.

More information here:
```
{
  "epc_mem_ratio": 0.5,
  "max_per_host": 68719476736
}
```

* epc_mem_ratio: The epc_mem_ratio represents the ratio of memory needed to start a guest that supports SGX.

* max_per_host: Represents the maximum free Enclave Page Cache (EPC) available in the location. The value is in bytes.

* gpus: Lists GPU models with their maximum CPU, memory, SMP, and other relevant configurations.
```
{
  "nvidia_a100": {
    // Details about Nvidia A100 GPU
  }
}
```
* hosts: Details limitations for different host types (e.g., AMD, Intel) concerning CPU, CPU per SMP, memory, and SMP.
```
{
  "amd": {
    // Details about AMD host type
  },
  "intel": {
    // Details about Intel host type
  }
}
```
* hypervisors: Specifies which hypervisors (e.g., KVM) are available on particular host types (e.g., Intel, AMD).

The "hypervisors" parameter informs users about the available hypervisors and the types of hosts (architectures) each hypervisor supports. In this specific case, the KVM hypervisor supports both "intel" and "amd" architectures.
```
{
  "kvm": ["intel", "amd"]
}
```
* inactive_period_range: Defines the maximum and minimum values accepted for the Inactivation Timeout defined by the user https://tbc.cloudsigma.com/ui/5.0/security

* remote_snapshots: Contains information about remote snapshots, including the current count, maximum allowed, and locations.

As a note, the difference between a snapshot and a remote snapshot is that the snapshot is stored in the same location as the source drive; the remote snapshot is stored in a different location.

* servers : Details about server properties, including CPU, memory, SMP, and start methods.
```
{
  "cpu": { "max": 96000, "min": 250 },
  // ... (other server details)
}
```

* snapshots: Specifies the current count, maximum allowed, and maximum per drive for snapshots.

a "snapshot" refers to a point-in-time copy of the state of a virtual machine or a storage drive. Snapshots are typically used for backup, recovery, or cloning purposes.

* vmware_drives: Provides details about VMware drive storage capacity limits.
```
{
  "storage_capacity": {
    "limit": 6291200.0,
    "units": "MB",
    "used": 2127040.0
  }
}
```
* vmware_servers:

Description: Indicates VMware server compute capacity limits for CPU and memory.
```
{
  "compute_capacity": {
    "cpu_max": 117797,
    "mem_max": 271061
  }
}
```


