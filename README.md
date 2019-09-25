#           [unitedrpms](https://unitedrpms.github.io/)

[![Build Status](https://travis-ci.org/UnitedRPMs/unitedrpms.svg?branch=master)](https://travis-ci.org/UnitedRPMs/unitedrpms)
 
**Summary:**        UnitedRPMs Repository Configuration
 
**Version:**        29-32
 
**License:**        GPLv3


## Command Line Setup

**For Fedora 29-31:**

```
sudo dnf -y install https://github.com/UnitedRPMs/unitedrpms/releases/download/15/unitedrpms-$(rpm -E %fedora)-15.fc$(rpm -E %fedora).noarch.rpm
```

## How to import our gpg key

Our GPG key is integrated in every `unitedrpms-*.noarch.rpm` package. You can also import it manually:

```
# rpm --import https://raw.githubusercontent.com/UnitedRPMs/unitedrpms/master/URPMS-GPG-PUBLICKEY-Fedora
```

## How to check if your rpm is compromised?

You can (*and must if feel doubts!*) check the GPG signature and hash sums of every package. Examples:

```
# rpm -K https://github.com/UnitedRPMs/unitedrpms/releases/download/15/unitedrpms-$(rpm -E %fedora)-15.fc$(rpm -E %fedora).noarch.rpm
```

 If all goes well, the following message is displayed: md5 gpg OK. This means that the signature of the package has been verified, and that it is [not corrupt](https://www.centos.org/docs/5/html/Deployment_Guide-en-US/s1-check-rpm-sig.html). 

## Useful packages

*Video playback*
```
sudo dnf update
sudo dnf install vlc mpv celluloid
```

*Basic codecs*

```
sudo dnf install gstreamer1-{libav,plugins-{good,ugly,bad{-free,-nonfree}}} --setopt=strict=0
```

*Brave, Chromium and Opera with HTML5 Multimedia support*

```
sudo dnf install brave 
sudo dnf install chromium-freeworld 
sudo dnf install opera 
```

*Multimedia toolset*

```
sudo dnf install kdenlive openshot kodi obs-studio spotify-client handbrake devede deedbeef
```





 
