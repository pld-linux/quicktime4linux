Summary:	Quicktime for Linux
Summary(pl):	Obs³uga formatu Quicktime dla Linuxa
Name:		quicktime4linux
Version:	1.3
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
URL:		http://heroine.linuxave.net/quicktime.html
Source0:	http://heroinewarrior.com/%{name}-%{version}.tar.gz
Source1:	qt4linux-Makefile.am
Source2:	qt4linux-configure.in
BuildRequires:	glib-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libjpeg-devel
BuildRequires:	libdv-devel
BuildRequires:	libraw1394-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for quicktime4linux.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do biblioteki quicktime4linux.

%package progs
Summary:	Useful tools to operate at Quicktime files
Summary(pl):	Po¿yteczne narzêdzia od operowania na plikach w formacie Quicktime
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Requires:	%{name} = %{version}

%description progs
Useful tools to operate at Quicktime files.

%description -l pl progs
Po¿yteczne narzêdzia od operowania na plikach w formacie Quicktime.

%package static
Summary:	Static quicktime4linux libraries
Summary(pl):	Biblioteki statyczne quicktime4linux
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static quicktime4linux libraries.

%description -l pl static
Biblioteki statyczne quicktime4linux.

%prep
%setup -q
rm -rf Makefile global_config configure
install %{SOURCE1} Makefile.am
install %{SOURCE2} configure.in

%build
aclocal
autoheader
automake -a -c
autoconf
%configure

%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README docs/*.html

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%doc docs/*.html.gz
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/quicktime
%{_includedir}/quicktime/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
