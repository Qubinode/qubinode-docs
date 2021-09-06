OpenShift Container Platform Workshop
=====================================

Jig - Workshop Service Worker
-----------------------------

This is a PHP application built to provide advanced functionality to Red
Hat workshops. 
`Click here to
contribute <https://github.com/kenmoini/jig>`__

Qubinode Requirements
^^^^^^^^^^^^^^^^^^^^^

-  Local storage with at 10Gigs os storage
   ``this can be changed if you would like``

Qubinode JIG installation steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Install kustomize `kustomize <https://kubernetes-sigs.github.io/kustomize/installation/>`__

.. code:: bash

   $ curl -s "https://raw.githubusercontent.com/\
   kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  | bash
   $ sudo mv kustomize /usr/local/bin/

2. Clone the jig repo

::

   git clone https://github.com/kenmoini/jig.git\

3. cd into jig folder

::

   cd jig

4. Deploy to OpenShift using kustomize

.. code:: bash

   oc new-project  jig-workshop-worker

5. Deploy mysql database

.. code:: bash

   oc process -f deploy/overlay/openshift/mysql-template.yaml  --param=VOLUME_CAPACITY=10Gi | oc create -f -  -n jig-workshop-worker

6. **Optional** update patch-env.yaml
| *This will update the configmap for your deployment*

::

   vim deploy/overlay/openshift/patch-env.yaml

7. Validate Configs

.. code:: bash

   kustomize build deploy/overlay/openshift/ | less

8. Deploy application

.. code:: bash

   kustomize build deploy/overlay/openshift/ | oc create -f -

9. Get admin password

.. code:: bash

   oc exec $(oc get pods -n jig-workshop-worker | grep jig-workshop-worker- | awk '{print $1}')  -- cat storage/app/generated_admin_password

**Admin username** \* ``admin@admin.com``

Delete JIG project
^^^^^^^^^^^^^^^^^^

1. To delete deployment

.. code:: bash

   oc process -f deploy/overlay/openshift/mysql-template.yaml  --param=VOLUME_CAPACITY=10Gi | oc delete -f -  -n jig-workshop-worker
   kustomize build deploy/overlay/openshift/ | oc delete -f -
   oc project delete  jig-workshop-worker
