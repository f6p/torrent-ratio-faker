Name:		torrent-ratio-faker
Summary:	HTTP proxy that fakes downloaded and uploaded values
Version:	0.1.0
Release:	1%{?dist}

License:	GPLv3
URL:		https://github.com/f6p/%{name}
Source0:	https://github.com/f6p/%{name}/archive/v%{version}.tar.gz
BuildArch:	noarch

Requires:	python
Requires:	python-twisted

BuildRequires:	systemd-units


%description
HTTP proxy that fakes downloaded and uploaded values.


%prep
%setup -q


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
cp -p bin/trf %{buildroot}%{_bindir}/
cp -p misc/service/* %{buildroot}%{_unitdir}/


%files
%defattr(- root root -)
%{_unitdir}/trf.service
%attr(755 root -) %{_bindir}/trf


%changelog
* Tue Feb 07 2013 f6p - 0.1.0
- Initial release
