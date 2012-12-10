#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/exalt exalt; \
#cd exalt; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "exalt" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf exalt-$PKG_VERSION.tar.xz exalt/ --exclude .svn --exclude .*ignore

%define svnrev 76819

%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary: 	ELF based front end network manager
Name:		exalt
Version:	0.9
Release:	1.%{svnrev}.2
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
EFL based front end network manager.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary:	Exalt Libraries
Group:		System/Libraries

%description -n %{libname}
ELF based front end network manager

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{develname}
Summary:	Exalt Library headers and development libraries
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

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


%changelog
* Thu Jan 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.9-1.64527.1
+ Revision: 760474
- new snapshot 0.9.64527
- cleaned up spec
- merged UnityLinux spec

* Mon Jan 03 2011 Crispin Boylan <crisb@mandriva.org> 0.9-0.20101107.1mdv2011.0
+ Revision: 627852
- Update source tarball from svn

* Fri Jul 16 2010 Funda Wang <fwang@mandriva.org> 0.9-0.20100707.1mdv2011.0
+ Revision: 554385
- New snapshot

* Sat Aug 08 2009 Funda Wang <fwang@mandriva.org> 0.8-0.20080808.1mdv2010.0
+ Revision: 411613
- adjust BR
- New snapshot

* Thu Jul 09 2009 Funda Wang <fwang@mandriva.org> 0.6-5mdv2010.0
+ Revision: 393744
- rebuild

* Wed Mar 04 2009 Antoine Ginies <aginies@mandriva.com> 0.6-4mdv2009.1
+ Revision: 348440
- provide std C math function of GCC
- try to fix 2009.0 build

* Tue Mar 03 2009 Antoine Ginies <aginies@mandriva.com> 0.6-3mdv2009.1
+ Revision: 347884
- add wpa_supplicant and dhcp support for exalt

* Mon Mar 02 2009 Antoine Ginies <aginies@mandriva.com> 0.6-2mdv2009.1
+ Revision: 347519
- fix bad conflits and obsolete and provides

* Mon Mar 02 2009 Antoine Ginies <aginies@mandriva.com> 0.6-1mdv2009.1
+ Revision: 347451
- fix %%files tag
- import exalt


