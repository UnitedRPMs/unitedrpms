#           unitedrpms

[![Build Status](https://travis-ci.org/UnitedRPMs/unitedrpms.svg?branch=master)](https://travis-ci.org/UnitedRPMs/unitedrpms)
 
Summary:        UnitedRPMs Repository Configuration
 
Version:        24-28
 
License:        GPLv3



## Have you installed manually unitedrpms?

You need delete old repositories:

* su
* rm -f /etc/yum.repos.d/unitedrpms.repo
* rm -f /etc/yum.repos.d/fedora-enjoy24.repo


## Command Line Setup

**For Fedora 24-28:**

```
1) su

2) dnf -y install https://github.com/UnitedRPMs/unitedrpms/releases/download/6/unitedrpms-$(rpm -E %fedora)-6.fc$(rpm -E %fedora).noarch.rpm
```

## How to import our gpg key

Our GPG key is integrated in every `unitedrpms-*.noarch.rpm` package. You can also import it manually:

```
# rpm --import https://raw.githubusercontent.com/UnitedRPMs/unitedrpms/master/URPMS-GPG-PUBLICKEY-Fedora-24
```

## How to check if your rpm is compromised?

You can (*and must if feel doubts!*) check the GPG signature and hash sums of every package. Examples:

```
# rpm -K https://github.com/UnitedRPMs/unitedrpms/releases/download/6/unitedrpms-$(rpm -E %fedora)-6.fc$(rpm -E %fedora).noarch.rpm
```

 If all goes well, the following message is displayed: md5 gpg OK. This means that the signature of the package has been verified, and that it is [not corrupt](https://www.centos.org/docs/5/html/Deployment_Guide-en-US/s1-check-rpm-sig.html). 

## Useful packages

Video playback:
```
# dnf update
# dnf install vlc mpv ffmpeg gnome-mpv
```

Complete Gstreamer framework with all codecs:

```
# dnf install gstreamer{1,}-{ffmpeg,libav,plugins-{good,ugly,bad{,-free,-nonfree}}} --setopt=strict=0
```

Chromium and Opera with HTML5 Multimedia support:

```
# dnf install chromium-freeworld opera 
```

Gradio - superb playbox with the radiostations from around the world
```
# dnf install gradio
```

Need to work or relax with multimedia? No problemo

```
# dnf install kdenlive openshot kodi obs-studio spotify-client handbrake devede deedbeef
```
-----

# [Website](https://unitedrpms.github.io/)




 
