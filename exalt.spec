#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/exalt exalt; \
#cd exalt; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "exalt" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf exalt-$PKG_VERSION.tar.xz exalt/ --exclude .svn --exclude .*ignore

%define svnrev	64527

%define major 1
%define libname %mklibname %{name} %major
%define develname %mklibname %{name} -d

Summary: 	ELF based front end network manager
Name:		exalt
Version:	0.9
Release:	1.%{svnrev}.1
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source0: 	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	dhcp-client
BuildRequires:	edje
BuildRequires:	wpa_supplicant
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edbus)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(evas)

%description
EFL based front end network manager
This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary: Exalt Libraries
Group: System/Libraries

%description -n %{libname}
ELF based front end network manager

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{develname}
Summary: Exalt Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
Exalt development headers and development libraries.

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--with-wpa-supplicant=%{_sbindir} \
	--with-dhcp=/sbin
%make

%install
rm -fr %{buildroot}
%makeinstall_std

%files
%{_sbindir}/exalt-command
%{_sbindir}/exalt-daemon

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

