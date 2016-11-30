Summary:    The GeoIP Update program performs automatic updates of GeoIP2 and GeoIP Legacy binary databases.
Name:       ulyaoth-geoipupdate
Version:    2.2.2
Release:    1%{?dist}
BuildArch: x86_64
License:    GNUv2
Group:      Applications/System
URL:        http://dev.maxmind.com/geoip/geoipupdate/
Vendor:     MaxMind, Inc
Packager:   Sjir Bagmeijer <sbagmeijer@ulyaoth.net>
Source0:    https://github.com/maxmind/geoipupdate/archive/v%{version}.tar.gz
BuildRoot:  %{_tmppath}/geoipupdate-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: zlib-devel
BuildRequires: curl-devel

Requires: zlib
Requires: curl

Provides: geoipupdate
Provides: ulyaoth-geoipupdate

%description
The GeoIP Update program performs automatic updates of GeoIP2 and GeoIP Legacy binary databases. CSV databases are not supported.

%prep
%setup -q -n geoipupdate-%{version}

%build
./bootstrap
./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/geoipupdate
cp -rf $RPM_BUILD_ROOT/conf/GeoIP.conf.default $RPM_BUILD_ROOT%{_datadir}/geoipupdate/GeoIP.conf
   
%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%files
%defattr(-,root,root)
%docdir /usr/share/doc/geoipupdate

%dir %{_datadir}/geoipupdate

%{_bindir}/geoipupdate
%{_mandir}/man1/geoipupdate.1
%{_mandir}/man5/GeoIP.conf.5
%{_datadir}/geoipupdate/GeoIP.conf

%doc %{_datadir}/doc/geoipupdate/ChangeLog.md
%doc %{_datadir}/doc/geoipupdate/GeoIP.conf.default
%doc %{_datadir}/doc/geoipupdate/LICENSE
%doc %{_datadir}/doc/geoipupdate/README.md

%post
cat <<BANNER
----------------------------------------------------------------------

Thank you for using ulyaoth-geoipupdate!

Please find the official documentation for geoipupdate here:
* http://dev.maxmind.com/geoip/geoipupdate/

For any additional help please visit my forum at:
* https://www.ulyaoth.net

----------------------------------------------------------------------
BANNER

%preun

%postun

%changelog
* Wed Nov 30 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.2.2-1
- Initial release.