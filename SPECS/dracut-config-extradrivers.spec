Summary: Force dracut to add drivers during install.
Name: dracut-config-extradrivers
Version: 0.2
Release: 2%{?dist}
License: public domain
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-root
Requires: dracut
Source0: 99-ded.conf
Source1: 98-bananapi-m3.conf
Source2: 98-odroid-hc1.conf

ExclusiveArch: %{arm}

%description
Force dracut to add drivers during install.

%install
mkdir -p %{buildroot}/etc/dracut.conf.d/
cp %SOURCE0 %{buildroot}/etc/dracut.conf.d/
cp %SOURCE1 %{buildroot}/etc/dracut.conf.d/
cp %SOURCE2 %{buildroot}/etc/dracut.conf.d/

%files
/etc/dracut.conf.d/*.conf
