Hardware Specs 
==============

The qubinode supports deploying multiple Red Hat products,
such as IdM and Satellite. The primary products that we're focusing on are
OCP4, IdM, Satellite, and Ansible Tower.

The table below defines what is needed for an OpenShift Deployment.

OpenShift Single Node Hardware Spec Table
-----------------------------------------

This was originally created base on OCP3. We have not validated the
minimum requirements for OCP4. However, the recommended should work for
both OCP3 and OCP4.

=================== =========== ===============
                    **Minimum** **Recommended**
=================== =========== ===============
**CPU**             6 Core      8 core or more
**Memory**          64 GB       128 or more
**Root Disk**       80 GB SSD   500 or more
**Secondary Drive** 500 GB SSD  1 TB Nvme Drive
=================== =========== ===============

Recommended Hardware
--------------------

Here are some hardware we recommend for standing up an OCP cluster on a
single node. We have validated that the below is enough to deploy a
production like OCP cluster. That will be sufficient for a operator
needing to learn OpenShift and also validate some production type
deployment. The hardware may not be sufficient to run some workloads. We
have not yet explore the limits in terms of what sorts of apps you can
run with reasonable performance.

**Router**

The router and cables are optional. The router makes the qubinode
portable. You can plug the router into an existing wired network or
bridge an existing wireless network. If you plug it into an existing
wired network, you would need to setup static routes. Bridging a
wireless network is the easiest way to drop the qubinode into any
network.

.. figure:: documents/img/QubinodeHardware.jpeg
   :alt: Example Router Usage

   Example Router Usage

Option 1: SuperServer E200-8D 6 Cores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before the AMD system below this was the cheapest option available.

+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| **Componets**                    | **Description**                                       | **Estimated Unit Cost** | **Quantity** | **Cost(usd)** | **Where it can be found** |
+==================================+=======================================================+=========================+==============+===============+===========================+
| System                           | superserver e200-8d                                   | $858.95                 | 1            | 858.95        | https://amzn.to/2VZMIX4   |
|                                  | * Cores: 6                                            |                         |              |               |                           |
|                                  | * Threads: 12                                         |                         |              |               |                           |
|                                  | * CPU: 1.9 Ghz                                        |                         |              |               |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Memory                           | samsung m393a4k40bb1-CRC LP ECC Reg Server Memory     | $101                    | 4            | $402          | https://amzn.to/2MZuf8G   |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Solid State Drive(SSD)           | WD Blue 3D NAND 500GB Internal PC SSD WD S500G2B0A    | $63.99                  | 1            | $63.99        | https://amzn.to/2P0JXDh   |
|                                  | * SATA III 6Gb/s                                      |                         |              |               |                           |
|                                  | * 2.5"/7mm                                            |                         |              |               |                           |
|                                  | * Up to 560 MP/s                                      |                         |              |               |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| NonVolatile Memory Express(NVME) | Intel SSD 660P Series, 1TB                            | $99.99                  | 1            | $99.99        | https://amzn.to/2MTnIMW   |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Router                           | GL.iNet GL-AR750S-Ext Gigabit Travel AC Router(slate) | $69.99                  | 1            | $69.99        | https://amzn.to/33GUuYr   |
|                                  | * Up to 300Mbps (2.4G)                                |                         |              |               |                           |
|                                  | * Up to 433Mbps (5G)                                  |                         |              |               |                           |
|                                  | * Wi-Fi                                               |                         |              |               |                           |
|                                  | * RAM: 128MB                                          |                         |              |               |                           |
|                                  | * MicroSD support                                     |                         |              |               |                           |
|                                  | * OpenWRT/LEDE pre-installed                          |                         |              |               |                           |
|                                  | * CloudFlare DNS                                      |                         |              |               |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Cable                            | InstallerParts Ethernet Cable CAT6                    | $5.79                   | 2            | $11.78        | https://amzn.to/2VTXEoQ   |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
|                                  |                                                       | **Total Cost**          |              | $1,506.50     |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+

Option 2: Superserver E301-9D-8CN4 8 Cores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This system has not been tested, however, we included it here because of
the price for a 8 core/16 thread system. This is a better buy vs option

+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| **Componets**                    | **Description**                                       | **Estimated Unit Cost** | **Quantity** | **Cost(usd)** | **Where it can be found** |
+==================================+=======================================================+=========================+==============+===============+===========================+
| System                           | supermicro A+ Server E301-9D-8CN4                     | $999.95                 | 1            | 999.95        | https://amzn.to/31vYbhU   |
|                                  | * Cores: 8                                            |                         |              |               |                           |
|                                  | * Threads: 16                                         |                         |              |               |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Memory                           | samsung m393a4k40bb1-CRC 32GB                         | $101                    | 4            | $402          | https://amzn.to/2MZuf8G   |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Solid State Drive(SSD)           | WD Blue 3D NAND 500GB Internal PC SSD WD S500G2B0A    | $63.99                  | 1            | $63.99        | https://amzn.to/2P0JXDh   |
|                                  | * SATA III 6Gb/s                                      |                         |              |               |                           |
|                                  | * 2.5"/7mm                                            |                         |              |               |                           |
|                                  | * Up to 560 MP/s                                      |                         |              |               |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| NonVolatile Memory Express(NVME) | Intel SSD 660P Series, 1TB                            | $99.99                  | 1            | $99.99        | https://amzn.to/2MTnIMW   |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Router                           | GL.iNet GL-AR750S-Ext Gigabit Travel AC Router(slate) | $69.99                  | 1            | $69.99        | https://amzn.to/33GUuYr   |
|                                  | * Up to 300Mbps (2.4G)                                |                         |              |               |                           |
|                                  | * Up to 433Mbps (5G)                                  |                         |              |               |                           |
|                                  | * Wi-Fi                                               |                         |              |               |                           |
|                                  | * RAM: 128MB                                          |                         |              |               |                           |
|                                  | * MicroSD support                                     |                         |              |               |                           |
|                                  | * OpenWRT/LEDE pre-installed                          |                         |              |               |                           |
|                                  | * CloudFlare DNS                                      |                         |              |               |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Cable                            | InstallerParts Ethernet Cable CAT6                    | $5.79                   | 2            | $11.78        | https://amzn.to/2VTXEoQ   |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
|                                  |                                                       | **Total Cost**          |              | $1,647.50     |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+


Option 3: Superserver E300-9D-8CN8TP 8 Cores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Qubinode developers and testers are using the following model. Assuming Option 2 works well, it’s a more
cost effective than this. You can the same amount of cores and threads.

+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| **Componets**                    | **Description**                                       | **Estimated Unit Cost** | **Quantity** | **Cost(usd)** | **Where it can be found** |
+==================================+=======================================================+=========================+==============+===============+===========================+
| System                           | supermicro A+ Server E301-9D-8CN4                     | $999.95                 | 1            | 999.95        | https://amzn.to/31vYbhU   |
|                                  | * Cores: 8                                            |                         |              |               |                           |
|                                  | * Threads: 16                                         |                         |              |               |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Memory                           | samsung m393a4k40bb1-CRC 32GB                         | $101                    | 4            | $402          | https://amzn.to/2MZuf8G   |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Solid State Drive(SSD)           | WD Blue 3D NAND 500GB Internal PC SSD WD S500G2B0A    | $63.99                  | 1            | $63.99        | https://amzn.to/2P0JXDh   |
|                                  | * SATA III 6Gb/s                                      |                         |              |               |                           |
|                                  | * 2.5"/7mm                                            |                         |              |               |                           |
|                                  | * Up to 560 MP/s                                      |                         |              |               |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| NonVolatile Memory Express(NVME) | Intel SSD 660P Series, 1TB                            | $99.99                  | 1            | $99.99        | https://amzn.to/2MTnIMW   |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Router                           | GL.iNet GL-AR750S-Ext Gigabit Travel AC Router(slate) | $69.99                  | 1            | $69.99        | https://amzn.to/33GUuYr   |
|                                  | * Up to 300Mbps (2.4G)                                |                         |              |               |                           |
|                                  | * Up to 433Mbps (5G)                                  |                         |              |               |                           |
|                                  | * Wi-Fi                                               |                         |              |               |                           |
|                                  | * RAM: 128MB                                          |                         |              |               |                           |
|                                  | * MicroSD support                                     |                         |              |               |                           |
|                                  | * OpenWRT/LEDE pre-installed                          |                         |              |               |                           |
|                                  | * CloudFlare DNS                                      |                         |              |               |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
| Cable                            | InstallerParts Ethernet Cable CAT6                    | $5.79                   | 2            | $11.78        | https://amzn.to/2VTXEoQ   |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+
|                                  |                                                       | **Total Cost**          |              | $1,647.50     |                           |
+----------------------------------+-------------------------------------------------------+-------------------------+--------------+---------------+---------------------------+

Option 4: Build-it 32 Core System with 256G Ram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is not a portable option. However, if you have the space, looking
for something with more power but don’t want to buy a used HP or Dell.
Then this is a quiet, good on power easy DIY build.

+-------+-------+----------+----------+----------+----------+----------+
| **C   | **Des | **Unit   | **QTY**  | *        | **Buy    | *        |
| ompon | cript | Cost**   |          | *Total** | URL**    | *Notes** |
| ets** | ion** |          |          |          |          |          |
+=======+=======+==========+==========+==========+==========+==========+
| M     | A     | $349.99  | 1        | $349.99  | https:   | Any LGA  |
| other | SRock |          |          |          | //bit.ly | 2011     |
| board | M     |          |          |          | /2W05Xzx | Socket   |
|       | other |          |          |          |          | mot      |
|       | board |          |          |          |          | herboard |
|       | ATX   |          |          |          |          | can be   |
|       | DDR3  |          |          |          |          | used     |
|       | 1066  |          |          |          |          | here     |
|       | Intel |          |          |          |          |          |
|       | LGA   |          |          |          |          |          |
|       | 2011  |          |          |          |          |          |
|       | EP2C  |          |          |          |          |          |
|       | 602-4 |          |          |          |          |          |
|       | L/D16 |          |          |          |          |          |
+-------+-------+----------+----------+----------+----------+----------+
| CPU   | Intel | $132.99  | 1        | $132.99  | https:/  | Most     |
|       | Mat   |          |          |          | /amzn.to | E5-26xx  |
|       | ching |          |          |          | /2P0N91G | should   |
|       | Pair  |          |          |          |          | work     |
|       | Xeon  |          |          |          |          | with     |
|       | E5    |          |          |          |          | above    |
|       | -2670 |          |          |          |          | mot      |
|       | Eight |          |          |          |          | herboard |
|       | Cores |          |          |          |          |          |
|       | Proce |          |          |          |          |          |
|       | ssors |          |          |          |          |          |
|       | 2.    |          |          |          |          |          |
|       | 60GHz |          |          |          |          |          |
|       | 20MB  |          |          |          |          |          |
|       | Smart |          |          |          |          |          |
|       | Cache |          |          |          |          |          |
|       | 8.00  |          |          |          |          |          |
|       | GT/S  |          |          |          |          |          |
|       | QPI   |          |          |          |          |          |
|       | TDP   |          |          |          |          |          |
|       | 115W  |          |          |          |          |          |
|       | SR0KX |          |          |          |          |          |
|       | BX8   |          |          |          |          |          |
|       | 0621E |          |          |          |          |          |
|       | 52670 |          |          |          |          |          |
+-------+-------+----------+----------+----------+----------+----------+
| M     | Ti    | $312.99  | 2        | $625.98  | https:/  | Cheapest |
| emory | metec |          |          |          | /amzn.to | a        |
|       | 128GB |          |          |          | /2VUqcPj | vailable |
|       | Kit   |          |          |          |          |          |
|       | (8x   |          |          |          |          |          |
|       | 16GB) |          |          |          |          |          |
|       | DDR3L |          |          |          |          |          |
|       | 16    |          |          |          |          |          |
|       | 00MHz |          |          |          |          |          |
|       | PC3-  |          |          |          |          |          |
|       | 12800 |          |          |          |          |          |
|       | Regis |          |          |          |          |          |
|       | tered |          |          |          |          |          |
|       | ECC   |          |          |          |          |          |
|       | 1.35V |          |          |          |          |          |
|       | CL11  |          |          |          |          |          |
|       | 2Rx4  |          |          |          |          |          |
|       | Dual  |          |          |          |          |          |
|       | Rank  |          |          |          |          |          |
|       | 240   |          |          |          |          |          |
|       | Pin   |          |          |          |          |          |
|       | RDIMM |          |          |          |          |          |
|       | S     |          |          |          |          |          |
|       | erver |          |          |          |          |          |
|       | M     |          |          |          |          |          |
|       | emory |          |          |          |          |          |
|       | RAM   |          |          |          |          |          |
|       | M     |          |          |          |          |          |
|       | odule |          |          |          |          |          |
|       | Up    |          |          |          |          |          |
|       | grade |          |          |          |          |          |
|       | (     |          |          |          |          |          |
|       | 128GB |          |          |          |          |          |
|       | Kit   |          |          |          |          |          |
|       | (8x1  |          |          |          |          |          |
|       | 6GB)) |          |          |          |          |          |
+-------+-------+----------+----------+----------+----------+----------+
| CPU   | N     | $79.95   | 2        | $159.90  | https:/  | Fan need |
| FAN   | octua |          |          |          | /amzn.to | to be    |
|       | NH    |          |          |          | /31q9Ij3 | co       |
|       | -D14, |          |          |          |          | mpatible |
|       | Pr    |          |          |          |          | with     |
|       | emium |          |          |          |          | L        |
|       | CPU   |          |          |          |          | GA2011-3 |
|       | C     |          |          |          |          | Square   |
|       | ooler |          |          |          |          | ILM      |
|       | with  |          |          |          |          |          |
|       | Dual  |          |          |          |          |          |
|       | N     |          |          |          |          |          |
|       | F-P14 |          |          |          |          |          |
|       | PWM   |          |          |          |          |          |
|       | and   |          |          |          |          |          |
|       | N     |          |          |          |          |          |
|       | F-P12 |          |          |          |          |          |
|       | PWM   |          |          |          |          |          |
|       | Fans  |          |          |          |          |          |
|       | (B    |          |          |          |          |          |
|       | rown) |          |          |          |          |          |
+-------+-------+----------+----------+----------+----------+----------+
| Case  | Ros   | 104.99   | 1        | 104.99   | https:/  | Not sure |
|       | ewill |          |          |          | /amzn.to | if the   |
|       | 4U    |          |          |          | /2P84R3z | mot      |
|       | S     |          |          |          |          | herboard |
|       | erver |          |          |          |          | would    |
|       | Chas  |          |          |          |          | fit in   |
|       | sis/S |          |          |          |          | standard |
|       | erver |          |          |          |          | ATX      |
|       | Case  |          |          |          |          | case.    |
|       | /Rack |          |          |          |          |          |
|       | mount |          |          |          |          |          |
|       | Case, |          |          |          |          |          |
|       | Metal |          |          |          |          |          |
|       | Rack  |          |          |          |          |          |
|       | Mount |          |          |          |          |          |
|       | Com   |          |          |          |          |          |
|       | puter |          |          |          |          |          |
|       | Case  |          |          |          |          |          |
|       | with  |          |          |          |          |          |
|       | 8     |          |          |          |          |          |
|       | Bays  |          |          |          |          |          |
|       | & 4   |          |          |          |          |          |
|       | Fans  |          |          |          |          |          |
|       | Pre   |          |          |          |          |          |
|       | -Inst |          |          |          |          |          |
|       | alled |          |          |          |          |          |
|       | (     |          |          |          |          |          |
|       | RSV-R |          |          |          |          |          |
|       | 4000) |          |          |          |          |          |
+-------+-------+----------+----------+----------+----------+----------+
| Power | CO    | $129.97  | 1        | $129.97  |          |          |
| S     | RSAIR |          |          |          |          |          |
| upply | RMX   |          |          |          |          |          |
|       | Se    |          |          |          |          |          |
|       | ries, |          |          |          |          |          |
|       | RM    |          |          |          |          |          |
|       | 850x, |          |          |          |          |          |
|       | 850   |          |          |          |          |          |
|       | Watt, |          |          |          |          |          |
|       | 80+   |          |          |          |          |          |
|       | Gold  |          |          |          |          |          |
|       | Certi |          |          |          |          |          |
|       | fied, |          |          |          |          |          |
|       | Fully |          |          |          |          |          |
|       | Mo    |          |          |          |          |          |
|       | dular |          |          |          |          |          |
|       | Power |          |          |          |          |          |
|       | S     |          |          |          |          |          |
|       | upply |          |          |          |          |          |
+-------+-------+----------+----------+----------+----------+----------+
| NVME  | Intel | $99.99   | 1        | $99.99   | https:/  |          |
|       | Solid |          |          |          | /amzn.to |          |
|       | State |          |          |          | /2MTnIMW |          |
|       | Drive |          |          |          |          |          |
|       | (     |          |          |          |          |          |
|       | SSD), |          |          |          |          |          |
|       | 660P  |          |          |          |          |          |
|       | Se    |          |          |          |          |          |
|       | ries, |          |          |          |          |          |
|       | 1 TB  |          |          |          |          |          |
+-------+-------+----------+----------+----------+----------+----------+
| PCI   | M.2   | $13.99   | 1        | $13.99   | https:/  |          |
| to    | NVMe  |          |          |          | /amzn.to |          |
| NVME  | SSD   |          |          |          | /33HbZYD |          |
| Ad    | NGFF  |          |          |          |          |          |
| apter | to    |          |          |          |          |          |
|       | PCIE  |          |          |          |          |          |
|       | 3.0   |          |          |          |          |          |
|       | X16   |          |          |          |          |          |
|       | /X4   |          |          |          |          |          |
|       | Ad    |          |          |          |          |          |
|       | apter |          |          |          |          |          |
|       | M Key |          |          |          |          |          |
|       | Inte  |          |          |          |          |          |
|       | rface |          |          |          |          |          |
|       | Card  |          |          |          |          |          |
|       | Su    |          |          |          |          |          |
|       | pport |          |          |          |          |          |
|       | PCI   |          |          |          |          |          |
|       | Ex    |          |          |          |          |          |
|       | press |          |          |          |          |          |
|       | 3.0   |          |          |          |          |          |
|       | x4    |          |          |          |          |          |
|       | 2230  |          |          |          |          |          |
|       | -2280 |          |          |          |          |          |
|       | Size  |          |          |          |          |          |
|       | m.2   |          |          |          |          |          |
|       | Full  |          |          |          |          |          |
|       | Speed |          |          |          |          |          |
|       | (     |          |          |          |          |          |
|       | Black |          |          |          |          |          |
|       | Gold  |          |          |          |          |          |
+-------+-------+----------+----------+----------+----------+----------+
| SSD   | WD    | $63.99   | 1        | $63.99   | https:/  |          |
|       | Blue  |          |          |          | /amzn.to |          |
|       | 3D    |          |          |          | /2P0JXDh |          |
|       | NAND  |          |          |          |          |          |
|       | 500GB |          |          |          |          |          |
|       | Int   |          |          |          |          |          |
|       | ernal |          |          |          |          |          |
|       | PC    |          |          |          |          |          |
|       | SSD - |          |          |          |          |          |
|       | SATA  |          |          |          |          |          |
|       | III 6 |          |          |          |          |          |
|       | Gb/s, |          |          |          |          |          |
|       | 2.5"  |          |          |          |          |          |
|       | /7mm, |          |          |          |          |          |
|       | Up to |          |          |          |          |          |
|       | 560   |          |          |          |          |          |
|       | MB/s  |          |          |          |          |          |
|       | -     |          |          |          |          |          |
|       | W     |          |          |          |          |          |
|       | DS500 |          |          |          |          |          |
|       | G2B0A |          |          |          |          |          |
+-------+-------+----------+----------+----------+----------+----------+
|       |       | **Su     |          | $        |          |          |
|       |       | btotal** |          | 1,681.79 |          |          |
+-------+-------+----------+----------+----------+----------+----------+

Other Options
~~~~~~~~~~~~~

-  Recent reddit r/homelab thread `Mini-ITX Server build: AMD EPYC 3251
   with Noctua C14S CPU Cooler, 256 GB RAM ECC + 2 x 2TB Samsung 970 EVO
   NVMe
   storage <https://www.reddit.com/r/homelab/comments/elg5ti/miniitx_server_build_amd_epyc_3251_with_noctua/>`__
