Name:		torrent-ratio-faker
Summary:	HTTP proxy that fakes downloaded and uploaded values
Version:	0.1.0
Release:	1%{?dist}

License:	GPL-3.0-only
URL:		https://github.com/f6p/%{name}
Source0:	https://github.com/f6p/%{name}/archive/v%{version}.tar.gz
BuildArch:	noarch

Requires:	python3
Requires:	python3-twisted

BuildRequires:	systemd-rpm-macros


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


%post
%systemd_post trf.service


%preun
%systemd_preun trf.service


%postun
%systemd_postun_with_restart trf.service


%files
%defattr(-,root,root,-)
%{_unitdir}/trf.service
%attr(755,root,root) %{_bindir}/trf


%changelog
* Thu Feb 07 2013 f6p - 0.1.0
- Initial release
