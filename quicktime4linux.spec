Summary:	Quicktime for Linux
Summary(pl):	Obs³uga formatu Quicktime dla Linuksa
Name:		quicktime4linux
Version:	1.4
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://heroinewarrior.com/%{name}-%{version}.tar.gz
Source1:	qt4linux-Makefile.am
Source2:	qt4linux-configure.in
Patch0:		%{name}-libraw1394.patch
URL:		http://heroinewarrior.com/quicktime.php3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libjpeg-devel
BuildRequires:	libdv-devel >= 0.9
BuildRequires:	libraw1394-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quicktime4linux is a library for reading and writing Quicktime files
on UNIX systems. Supported by this library video is MJPA, JPEG Photo,
PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression and supported audio is
IMA4, ulaw, and any linear PCM format.

%description -l pl
Quicktime4linux jest bibliotek± do odczytywania i zapisu plików w
formacie Quicktime przeznaczon± dla systemów Unix. Obecnie wspiera ona
nastêpuj±ce formaty video: MJPA, JPEG Photo, PNG, RGB, YUV 4:2:2 oraz
YUV 4:2:0, a tak¿e audio IMA4, ulaw i liniowy format PCM.

%package devel
Summary:	Header files and development documentation for quicktime4linux
Summary(pl):	Pliki nag³ówkowe i dokumentacja do quicktime4linux
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib-devel
Requires:	libpng-devel >= 1.0.8
Requires:	libjpeg-devel
Requires:	libdv-devel
Requires:	libraw1394-devel

%description devel
Header files and development documentation for quicktime4linux.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki quicktime4linux.

%package progs
Summary:	Useful tools to operate at Quicktime files
Summary(pl):	Po¿yteczne narzêdzia od operowania na plikach w formacie Quicktime
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description progs
Useful tools to operate at Quicktime files.

%description progs -l pl
Po¿yteczne narzêdzia od operowania na plikach w formacie Quicktime.

%package static
Summary:	Static quicktime4linux libraries
Summary(pl):	Biblioteki statyczne quicktime4linux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static quicktime4linux libraries.

%description static -l pl
Biblioteki statyczne quicktime4linux.

%prep
%setup -q
%patch -p1
rm -f Makefile global_config configure
install %{SOURCE1} Makefile.am
install %{SOURCE2} configure.in

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
cp codecs.h funcprotos.h colormodels.h graphics.h $RPM_BUILD_ROOT/%{_includedir}/quicktime

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%doc docs/*.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/quicktime

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
