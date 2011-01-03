%define	name	exalt
%define version 0.9
%define release %mkrel 0.20101107.1

%define major 1
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
buildrequires:  ecore-devel >= 0.9.9.050
buildrequires:	e_dbus-devel >= 0.1.0.002
buildrequires:  dbus-devel >= 0.1
buildrequires:  evas-devel >= 0.9.9.050
buildrequires:	edje >= 0.9.92.050
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
%setup -q -n %name-%version

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x --disable-static \
	--with-wpa-supplicant=%{_sbindir} \
	--with-dhcp=/sbin
%make

%install
rm -fr %buildroot
%makeinstall_std

rm -f %buildroot%_libdir/*.la

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/exalt-command
%{_sbindir}/exalt-daemon

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
