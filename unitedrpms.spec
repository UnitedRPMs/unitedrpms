%global target_arch x86_64

Name:           unitedrpms
Version:        %{fedora}
Release:        16%{?dist}
Summary:        UnitedRPMs Repository Configuration

Group:          System Environment/Base
License:        GPLv3
URL:            https://unitedrpms.github.io/
Source1:        https://raw.githubusercontent.com/UnitedRPMs/unitedrpms/master/unitedrpms.repo
Source2:        https://raw.githubusercontent.com/UnitedRPMs/unitedrpms/master/URPMS-GPG-PUBLICKEY-Fedora
BuildArch:      noarch
Recommends:     unitedrpms-appstream-data

%description
UnitedRPMs is the solution for people with unstable Fedora distributions, 
increase technical skills, create a Copr-like build system for package with
licensing problems. UnitedRPMs it's not a branch maintenance of other projects,
it is only a road to give the user a fast solution without fool bureaucracy 
where everyone can help.

This package contains the UnitedRPMs GPG key, which holds
software that is not considered as Open Source Software according to the
Fedora packaging guidelines. 


%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install

# Create dirs
install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
%{__install} -Dp -m644 %{S:2} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg


# Yum .repo files
%{__install} -p -m644 %{S:1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# Signed repositories failed detecting variables $releasever and $basearch
# Sure a bug... https://bugzilla.redhat.com/show_bug.cgi?id=1636743
#sed -i 's|$releasever|%{fedora}|g' $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/unitedrpms.repo
#sed -i 's|$basearch|%{target_arch}|g' $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/unitedrpms.repo

%files
%{_sysconfdir}/pki/rpm-gpg/*
# config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/yum.repos.d/*

%changelog

* Fri Feb 07 2020 David Va <davidva AT tuta DOT io> - 30-16
- Added templates for F33 

* Fri Aug 30 2019 David Va <davidva AT tuta DOT io> - 28-15
- Added templates for F32 

* Wed May 22 2019 David Va <davidva AT tuta DOT io> - 28-14
- Gpg keys updated

* Fri May 10 2019 David Va <davidva AT tuta DOT io> - 28-13
- Deleted failovermethod

* Wed Mar 13 2019 David Va <davidva AT tuta DOT io> - 28-12
- Enabled mirror list templates for F31

* Wed Nov 07 2018 David Va <davidva AT tuta DOT io> - 28-11
- Disabled mirrorlist; bugs in official variables in libdnf and dnf...

* Sat Nov 03 2018 David Va <davidva AT tuta DOT io> - 28-10
- Go back to variables by default

* Sat Oct 06 2018 David Va <davidva AT tuta DOT io> - 28-9
- Changed to specific architectures and release in mirror list

* Wed Mar 21 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 27-8
- Mirror list enabled

* Sun Nov 19 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 27-7
- Enabled metadata
- Weak dependency to unitedrpms-appstream-data

* Sat Jul 08 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 25-6
- Added priority for avoids problems with others third-party repositories

* Thu Jun 15 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 25-5
- Replaced old config for easy migration to new release Fedora

* Mon Jun 12 2017 Sérgio Basto <sergio@serjux.com> - 25-4
- Use baseurl instead mirrorlist because mirrorlist give us problems
- Better repo names

* Tue May 16 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 
- New changes

* Tue Mar 14 2017 Pavlo Rudyi <paulcarroty at riseup.net> - 27-1
- Reconfigure for Fedora 27

* Sun Oct 16 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 26-1
- Reconfigure for Fedora 26

* Mon Jul 18 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 25-1
- Reconfigure for Fedora 25

* Fri Jun 24 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 24-2
- Added local gpg keys

* Tue Jun 07 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 24-1
- Initial build

