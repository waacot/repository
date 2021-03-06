%define debug_package %{nil}

# end of distribution specific definitions

Summary:    Cryptography and SSL/TLS Toolkit
Name:       ulyaoth-openssl1.0.0
Version:    1.0.0t
Release:    4%{?dist}
BuildArch: x86_64
License:    OpenSSL
Group:      System Environment/Libraries
URL:        https://www.openssl.org/
Vendor:     OpenSSL
Packager:   Sjir Bagmeijer <sbagmeijer@ulyaoth.net>
%if 0%{?fedora}  == 19
Source0:    http://www.openssl.org/source/openssl-%{version}.tar.gz
%else
Source0:    https://www.openssl.org/source/openssl-%{version}.tar.gz
%endif
Source1:    https://raw.githubusercontent.com/ulyaoth/repository/master/ulyaoth-openssl/SOURCES/ulyaoth-openssl1.0.0.conf
BuildRoot:  %{_tmppath}/openssl-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: ulyaoth-openssl1.0.0-libs

Provides: ulyaoth-openssl1.0.0
Provides: ulyaoth-openssl1.0.0t

%description
The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured, and Open Source toolkit implementing the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols as well as a full-strength general purpose cryptography library. The project is managed by a worldwide community of volunteers that use the Internet to communicate, plan, and develop the OpenSSL toolkit and its related documentation.
OpenSSL is based on the excellent SSLeay library developed by Eric Young and Tim Hudson. The OpenSSL toolkit is licensed under an Apache-style license, which basically means that you are free to get and use it for commercial and non-commercial purposes subject to some simple license conditions.

%package libs
Summary: A general purpose cryptography library with TLS implementation
Group: System Environment/Libraries
Provides: ulyaoth-openssl1.0.0-libs
%description libs
The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured, and Open Source toolkit implementing the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols as well as a full-strength general purpose cryptography library.
The openssl-libs package contains the libraries that are used by various applications which support cryptographic algorithms and protocols.

%package devel
Summary: Files for development of applications which will use OpenSSL
Group: Development/Libraries
Requires: ulyaoth-openssl1.0.0-libs
Provides: ulyaoth-openssl1.0.0-devel
%description devel
The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured, and Open Source toolkit implementing the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols as well as a full-strength general purpose cryptography library.
The openssl-devel package contains include files needed to develop applications which support various cryptographic algorithms and protocols.

%package static
Summary: Libraries for static linking of applications which will use OpenSSL
Group: Development/Libraries
Requires: ulyaoth-openssl1.0.0-devel
Provides: ulyaoth-openssl1.0.0-static
%description static
The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured, and Open Source toolkit implementing the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols as well as a full-strength general purpose cryptography library.
The openssl-static package contains static libraries needed for static linking of applications which support various cryptographic algorithms and protocols.

%package perl
Summary: Perl scripts provided with OpenSSL
Group: Applications/Internet
Requires: perl
Requires: ulyaoth-openssl1.0.0
%description perl
The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured, and Open Source toolkit implementing the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols as well as a full-strength general purpose cryptography library.
The openssl-perl package provides Perl scripts for converting certificates and keys from other formats to the formats used by the OpenSSL toolkit.


%prep
%setup -q -n openssl-%{version}

%build
export C_INCLUDE_PATH=/usr/local/ulyaoth/openssl1.0.0/include
export LIBRARY_PATH=/usr/local/ulyaoth/openssl1.0.0/lib
export LD_RUN_PATH=/usr/local/ulyaoth/openssl1.0.0/lib

./config -Wl,-rpath=/usr/local/ulyaoth/openssl1.0.0/lib --openssldir=/usr/local/ulyaoth/openssl1.0.0 no-ssl2 no-ssl3 shared
make depend
make all
make rehash
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/local/ulyaoth/openssl1.0.0

make INSTALL_PREFIX=$RPM_BUILD_ROOT install

mv $RPM_BUILD_ROOT/usr/local/ulyaoth/openssl1.0.0/misc/* $RPM_BUILD_ROOT/usr/local/ulyaoth/openssl1.0.0/bin/
rm -rf $RPM_BUILD_ROOT/usr/local/ulyaoth/openssl1.0.0/certs
rm -rf $RPM_BUILD_ROOT/usr/local/ulyaoth/openssl1.0.0/private
rm -rf $RPM_BUILD_ROOT/usr/local/ulyaoth/openssl1.0.0/misc

%{__mkdir} -p $RPM_BUILD_ROOT/etc/ld.so.conf.d/
%{__install} -m 644 -p %{SOURCE1} \
    $RPM_BUILD_ROOT/etc/ld.so.conf.d/ulyaoth-openssl1.0.0.conf

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%files
%defattr(-,root,root,-)
%dir /usr/local/ulyaoth
%dir /usr/local/ulyaoth/openssl1.0.0
/usr/local/ulyaoth/openssl1.0.0/bin/openssl
%doc /usr/local/ulyaoth/openssl1.0.0/man/man1*/*
%doc /usr/local/ulyaoth/openssl1.0.0/man/man5*/*
%doc /usr/local/ulyaoth/openssl1.0.0/man/man7*/*
%exclude /usr/local/ulyaoth/openssl1.0.0/man/man1*/*.pl*
%exclude /usr/local/ulyaoth/openssl1.0.0/man/man1*/tsget*


%files libs
%dir /usr/local/ulyaoth
%dir /usr/local/ulyaoth/openssl1.0.0
%config(noreplace) /usr/local/ulyaoth/openssl1.0.0/openssl.cnf
%attr(0755,root,root) /usr/local/ulyaoth/openssl1.0.0/lib/libcrypto.so.1.0.0
%attr(0755,root,root) /usr/local/ulyaoth/openssl1.0.0/lib/libssl.so.1.0.0
%attr(0755,root,root) /usr/local/ulyaoth/openssl1.0.0/lib/engines/*
/etc/ld.so.conf.d/ulyaoth-openssl1.0.0.conf

%files devel
%dir /usr/local/ulyaoth
%dir /usr/local/ulyaoth/openssl1.0.0
%dir /usr/local/ulyaoth/openssl1.0.0/lib/pkgconfig
/usr/local/ulyaoth/openssl1.0.0/lib/*.so
/usr/local/ulyaoth/openssl1.0.0/include/*
%doc /usr/local/ulyaoth/openssl1.0.0/man/man3*/*
/usr/local/ulyaoth/openssl1.0.0/lib/pkgconfig/*.pc

%files static
/usr/local/ulyaoth/openssl1.0.0/lib/*.a

%files perl
/usr/local/ulyaoth/openssl1.0.0/bin/c_rehash
/usr/local/ulyaoth/openssl1.0.0/bin/CA.pl
/usr/local/ulyaoth/openssl1.0.0/bin/tsget
/usr/local/ulyaoth/openssl1.0.0/bin/CA.sh
/usr/local/ulyaoth/openssl1.0.0/bin/c_hash
/usr/local/ulyaoth/openssl1.0.0/bin/c_info
/usr/local/ulyaoth/openssl1.0.0/bin/c_issuer
/usr/local/ulyaoth/openssl1.0.0/bin/c_name
%doc /usr/local/ulyaoth/openssl1.0.0/man/man1*/*.pl*
%doc /usr/local/ulyaoth/openssl1.0.0/man/man1*/tsget*

%post
/sbin/ldconfig
cat <<BANNER
----------------------------------------------------------------------

Thanks for using ulyaoth-openssl1.0.0!

Please find the official documentation for OpenSSL here:
* https://www.openssl.org

For any additional help please visit our website at:
* https://www.ulyaoth.net

Ulyaoth repository could use your help! Please consider a donation:
* https://www.ulyaoth.net/donate.html

----------------------------------------------------------------------
BANNER

%post libs
/sbin/ldconfig
cat <<BANNER
----------------------------------------------------------------------

Thank you for using ulyaoth-openssl1.0.0-libs!

Please find the official documentation for OpenSSL here:
* https://www.openssl.org

For any additional help please visit our website at:
* https://www.ulyaoth.net

Ulyaoth repository could use your help! Please consider a donation:
* https://www.ulyaoth.net/donate.html

----------------------------------------------------------------------
BANNER

%post devel
/sbin/ldconfig
cat <<BANNER
----------------------------------------------------------------------

Thank you for using ulyaoth-openssl1.0.0-devel!

Please find the official documentation for OpenSSL here:
* https://www.openssl.org

For any additional help please visit our website at:
* https://www.ulyaoth.net

Ulyaoth repository could use your help! Please consider a donation:
* https://www.ulyaoth.net/donate.html

----------------------------------------------------------------------
BANNER

%post static
/sbin/ldconfig
cat <<BANNER
----------------------------------------------------------------------

Thank you for using ulyaoth-openssl1.0.0-static!

Please find the official documentation for OpenSSL here:
* https://www.openssl.org

For any additional help please visit our website at:
* https://www.ulyaoth.net

Ulyaoth repository could use your help! Please consider a donation:
* https://www.ulyaoth.net/donate.html

----------------------------------------------------------------------
BANNER

%post perl
/sbin/ldconfig
cat <<BANNER
----------------------------------------------------------------------

Thank you for using ulyaoth-openssl1.0.0-perl!

Please find the official documentation for OpenSSL here:
* https://www.openssl.org

For any additional help please visit our website at:
* https://www.ulyaoth.net

Ulyaoth repository could use your help! Please consider a donation:
* https://www.ulyaoth.net/donate.html

----------------------------------------------------------------------
BANNER

%postun -p /sbin/ldconfig

%changelog
* Sun Mar 26 2017 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 1.0.0t-4
- Changed directory structure.
- ld fixes.
- split into sub packages, perl, static, libs, devel.

* Mon Oct 10 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 1.0.0t-3
- Added ldd fixes.

* Mon Jan 11 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 1.0.0t-2
- added "shared" to compile options.

* Sun Jan 10 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 1.0.0t-1
- Initial release with openssl 1.0.0t.
