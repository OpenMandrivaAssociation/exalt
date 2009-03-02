%define	name	exalt
%define version 0.6
%define release %mkrel 1

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
Conflicts:	%{mklibname evas1}-devel

BuildRequires: 	eet-devel >= 1.1.0
buildrequires:  ecore-devel >= 0.9.9.050, eet-devel >= 1.1.0
buildrequires:	e_dbus-devel >= 0.1.0.002,
buildrequires:  dbus-devel >= 0.1,
buildrequires:  evas-devel >= 0.9.9.050
buildrequires:  elementary-devel >= 0.1.0.0

%description
efl based front end network manager
This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary: Exalt Libraries
Group: System/Libraries
Conflicts:	%{mklibname evas1}

%description -n %{libname}
efl based front end network manager

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libnamedev
Summary: Exalt Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = 2:%{version}
Provides: %{name}-devel = 2:%{version}-%{release}
Conflicts:	%{mklibname evas1}-devel
Obsoletes: %mklibname -d evas 0

%description -n %libnamedev
Exxalt development headers and development libraries.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
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

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.0*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/*a
%{_includedir}/*.h
%{_libdir}/pkgconfig/*
