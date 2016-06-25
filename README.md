#           unitedrpms
 
Summary:        UnitedRPMs Repository Configuration
 
Version:        24
 
License:        GPLv3



## Have you installed manually unitedrpms?

You need delete old repositories:

* su
* rm -f /etc/yum.repos.d/unitedrpms.repo
* rm -f /etc/yum.repos.d/fedora-enjoy24.repo


## Command Line Setup using rpm

* su -c 'dnf -y install https://raw.githubusercontent.com/UnitedRPMs/unitedrpms/master/RPM/unitedrpms-24-2.noarch.rpm'



 
