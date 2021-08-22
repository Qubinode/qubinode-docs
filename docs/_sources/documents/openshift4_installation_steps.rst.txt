Installing an OpenShift 4.x Cluster on a Single Node
====================================================

The following documentation will help you deploy an OpenShift Container
Platform (OCP) 4.3 cluster, on a single node. The installation steps
deploys a production like OCP4 cluster, in a environment with 3
controlplane and 3 computes on a KVM hosts running Red Hat Enterprise
Linux (RHEL) |image0|

Prerequisites
-------------

Refer to the `Getting Started Guide <../README.md>`__ to ensure RHEL 7
is installed.

Get Subscriptions
~~~~~~~~~~~~~~~~~

-  Get a Red Hat OpenShift Container Platform (OCP) `60-day evalution
   subscription <https://www.redhat.com/en/technologies/cloud-computing/openshift/try-it?intcmp=701f2000000RQykAAG&extIdCarryOver=true&sc_cid=701f2000001OH74AAG>`__.

Getting the OpenShift Pull Secret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Using Token

.. raw:: html

   </td>

.. raw:: html

   <td>

Downloading

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Navigate to OpenShift Cluster Manager API Token to generate a token and
save it as ocp_token. This token will be used to download your pull
secret.

.. raw:: html

   </td>

.. raw:: html

   <td>

From your web browser, navigate to Red Hat OpenShift Cluster Manager.
Find the Pull secret heading to either download or copy your pull
secret, save it as pull-secret.txt.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

Install OpenShift
-----------------

The qubinode-installer
~~~~~~~~~~~~~~~~~~~~~~

Download and extract the qubinode-installer as a non root user.

.. code:: shell=

   cd $HOME
   wget https://github.com/Qubinode/qubinode-installer/archive/master.zip
   unzip master.zip
   rm master.zip
   mv qubinode-installer-master qubinode-installer

Place your pull secret and the rhel qcow image under the
qubinode-installer directory.

If you are using tokens it should be:

::

   * $HOME/qubinode-installer/ocp_token
   * $HOME/qubinode-installer/rhsm_token

If you downloaded the files instead it should be:

::

   * $HOME/qubinode-installer/pull-secret.txt
   * $HOME/qubinode-installer/rhel-server-7.8-x86_64-kvm.qcow2
   * $HOME/qubinode-installer/rhel-8.2-x86_64-kvm.qcow2

Install Options
~~~~~~~~~~~~~~~

Choose one of the below options. The quick start is ideal if you meet
your resource requirements documented in our `hardware
guide <hardwareguide.md>`__. The advanced option will provide the most
flexibilty as you can decide which modules you want to execute and also
customize your OCP4 cluster size.

+-----------------------------------+-----------------------------------+
| `Standard                         | `Custom                           |
| Deploy                            | Depl                              |
| ment <ocp4_standard_deploy.md>`__ | oyment <ocp4_custom_deploy.md>`__ |
+===================================+===================================+
| Answer questions from the         | This option will allow you to     |
| installer to deploy a 6 node      | deploy a 3 only or 4 node cluster |
| OpenShift 4.x cluster, 3          | or to customize the size of the   |
| controlplane and 3 computes.      | cluster.                          |
+-----------------------------------+-----------------------------------+

Additional Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

-  `Qubinode OpenShift Cluster Operations <ocp4_cluster_ops.md>`__
-  `LDAP OpenShift configuration <openshift_ldap_config.md>`__

Troubleshooting Tips
~~~~~~~~~~~~~~~~~~~~

`Troubleshooting installation <troubleshooting-monitoring.md>`__

.. |image0| image:: https://i.imgur.com/n8TQAyB.png
