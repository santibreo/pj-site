:draft: true
:date: 2023-11-21

########################
Linux installation guide
########################

This post collects the steps I recommend to follow when you are installing a Linux distribution in your computer.


Disk partitioning
=================

Installation drive should be partitioned so, in the future, it is much easier to preserve user data and update the system.

Recommended partitions are:

1. EFI: This partition is for the **bootloader**. With 100MB is more than enough and it must be of type "primary" and used as "EFI System partition".

2. Linux System (``/``): This partition is for the distribution main files (executables, logs, etc.). Ubuntu recommends it to be at least 30GB but for gaming purposes more space is needed.
   You should select size based on your needs, define as type "primary" and use it as "ext4 journaling file system" and mount it on ``/``.

3. Home (``/home``): This partition is for the users personal data. This should be the biggest partition and must be configured the same way Linux System was, just mounted on ``/home``.

4. Swap: The swap partition is used as a RAM when there is no more RAM available. Recommended size is twice the RAM size if RAM size is less than 8GB, otherwise same as RAM size must be enough.

These are the partitions I use **for a personal computer**. You can create more partitions if you want.


Display Manager
===============


