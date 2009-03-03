%define	name	exalt
%define version 0.6
%define release %mkrel 3

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	efl based front end network manager
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot

BuildRequires: 	eet-devel >= 1.1.0
buildrequires:  ecore-devel >= 0.9.9.050, eet-devel >= 1.1.0
buildrequires:	e_dbus-devel >= 0.1.0.002,
buildrequires:  dbus-devel >= 0.1,
buildrequires:  evas-devel >= 0.9.9.050
buildrequires:  elementary-devel >= 0.1.0.0
buildrequires:	wpa_supplicant dhcp-client

%description
efl based front end network manager
This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary: Exalt Libraries
Group: System/Libraries

%description -n %{libname}
efl based front end network manager

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libnamedev
Summary: Exalt Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %libnamedev
Exxalt development headers and development libraries.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
export PATH=$PATH:/usr/sbin/:/sbin && %configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/dbus-1/system.d/exalt.conf
%{_sbindir}/exalt-client
%{_sbindir}/exalt-command
%{_sbindir}/exalt-daemon
%{_datadir}/%name/icons/*.png

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/*a
%{_includedir}/exalt/*.h
%{_includedir}/exalt_dbus/*.h
%{_libdir}/pkgconfig/*
