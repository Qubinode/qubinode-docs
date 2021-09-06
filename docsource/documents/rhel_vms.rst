Deploying Red Hat Enterprise Linux VMs
======================================

The qubinode-installer supports deploying Red Hat Enterprise Linux VMs.
This gives you a quick way to spin up one or multiple VMs on KVM running
RHEL.

Prerequisites
-------------

Refer to the `Getting Started Guide <qubinod_getting_started.rst>`__ to ensure your system
is setup. There is also a dependancy on IdM as a dns server, refer to
the `IdM install <idm.md>`__.

Deploying a RHEL VM
~~~~~~~~~~~~~~~~~~~

The RHEL release deployed will default to the release your system in
running. You can deploy RHEL 8 or 7 by passing the varible **release=<7
or >** to the installer **-a** argument. The **-a** agrument can be
passed multiple times for set different vairables.

**Install Options**

-  name - pet name to give the VM
-  size - the size VM to deploy
-  release - the release of RHEL to deploy
-  qty - the number of VMs to deploy

The VM name is randomly generated when the **name** option is not
specified. The naming convention is qbn-rhel-.

-  Example: qbn-rhel8-1076

**VM sizes available**

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

Small

.. raw:: html

   </td>

.. raw:: html

   <td>

Medium

.. raw:: html

   </td>

.. raw:: html

   <td>

Large

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

vCPU

.. raw:: html

   </td>

.. raw:: html

   <td>

1

.. raw:: html

   </td>

.. raw:: html

   <td>

2

.. raw:: html

   </td>

.. raw:: html

   <td>

4

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Memory

.. raw:: html

   </td>

.. raw:: html

   <td>

800Mib

.. raw:: html

   </td>

.. raw:: html

   <td>

2Gib

.. raw:: html

   </td>

.. raw:: html

   <td>

8Gib

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Disk

.. raw:: html

   </td>

.. raw:: html

   <td>

10Gib

.. raw:: html

   </td>

.. raw:: html

   <td>

60Gib

.. raw:: html

   </td>

.. raw:: html

   <td>

120Gib

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

**Deploying a RHEL 7 VM**

.. code:: =shell

   ./qubinode-installer -p rhel

**Deploying a RHEL 8 VM**

.. code:: =shell

   ./qubinode-installer -p rhel -a release=8

**Deploying a large VM**

.. code:: =shell

   ./qubinode-installer -p rhel -a release=8 -a size=large

**Deploying 4 medium size RHEL 7 VMs**

.. code:: =shell

   ./qubinode-installer -p rhel -a release=7 -a size=medium -a qty=4

**Deploying 6 small size RHEL 8 VMs named webserver**

.. code:: =shell

   ./qubinode-installer -p rhel -a release=8 -a qty=4 -a name=webserver

**Deleting a VM** Deleting a VM requires the name of the VM with the
**-d** argument.

.. code:: =shell

   ./qubinode-installer -p rhel -a name=qbn-rhel8-1076 -d

**Stopping/Starting a VM**

.. code:: =shell


   # Stop
   ./qubinode-installer -p rhel -a name=qbn-rhel8-1076 -m stop

   # Start
   ./qubinode-installer -p rhel -a name=qbn-rhel8-1076 -m start

**Get VM status**

.. code:: =shell

   ./qubinode-installer -p rhel -a name=qbn-rhel8-1076 -m status

**List all RHEL VMs**

.. code:: =shell

   ./qubinode-installer -p rhel -m list

