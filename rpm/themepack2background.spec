Summary: Convert themepack file to Slackware package.

Name: themepack2background
Version: 2.0
Release: 2

BuildArch: noarch

License: GNU General Public Licence - Version 3.0
URL: https://github.com/MauricioFerrari-NovaTrento/themepack2background

BuildRoot: ~/rpmbuild

Requires: cabextract

%description

Convert themepack file of the Windows 7 and deskthemepack of the Windows 8, 8.1 and 10 in txz packages for Slackware.

%prep

echo “BUILDROOT = $RPM_BUILD_ROOT“
mkdir -p $RPM_BUILD_ROOT/usr/{bin,doc/themepack2background-2.0}
mv ../themepack2background $RPM_BUILD_ROOT/usr/bin
mv ../themepack2rpm $RPM_BUILD_ROOT/usr/bin
mv ../LICENSE $RPM_BUILD_ROOT/usr/doc/themepack2background-2.0
mv ../INFO $RPM_BUILD_ROOT/usr/doc/themepack2background-2.0

%files

%attr(0755, root, root) /usr/bin/*
%attr(0644, root, root) /usr/doc/themepack2background-2.0/*
