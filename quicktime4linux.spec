Summary:	Quicktime for Linux
Summary(pl):	Obs≥uga formatu Quicktime dla Linuksa
Name:		quicktime4linux
Version:	1.4
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://heroinewarrior.com/%{name}-%{version}.tar.gz
Source1:	qt4linux-Makefile.am
Source2:	qt4linux-configure.in
Patch0:		%{name}-libraw1394.patch
URL:		http://heroinewarrior.com/quicktime.php3
BuildRequires:	glib-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libjpeg-devel
BuildRequires:	libdv-devel >= 0.9
BuildRequires:	libraw1394-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Quicktime4linux is a library for reading and writing Quicktime files
on UNIX systems. Supported by this library video is MJPA, JPEG Photo,
PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression and supported audio is
IMA4, ulaw, and any linear PCM format.

%description -l pl
Quicktime4linux jest bibliotek± do odczytywania i zapisu plikÛw w
formacie Quicktime przeznaczon± dla systemÛw Unix. Obecnie wspiera ona
nastÍpuj±ce formaty video: MJPA, JPEG Photo, PNG, RGB, YUV 4:2:2 oraz
YUV 4:2:0, a takøe audio IMA4, ulaw i liniowy format PCM.

%package devel
Summary:	Header files and development documentation for quicktime4linux
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja do quicktime4linux
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for quicktime4linux.

%description -l pl devel
Pliki nag≥Ûwkowe i dokumentacja do biblioteki quicktime4linux.

%package progs
Summary:	Useful tools to operate at Quicktime files
Summary(pl):	Poøyteczne narzÍdzia od operowania na plikach w formacie Quicktime
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Group(pt):	AplicaÁıes/Gr·ficos
Requires:	%{name} = %{version}

%description progs
Useful tools to operate at Quicktime files.

%description -l pl progs
Poøyteczne narzÍdzia od operowania na plikach w formacie Quicktime.

%package static
Summary:	Static quicktime4linux libraries
Summary(pl):	Biblioteki statyczne quicktime4linux
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static quicktime4linux libraries.

%description -l pl static
Biblioteki statyczne quicktime4linux.

%prep
%setup -q
%patch -p1
rm -f Makefile global_config configure
install %{SOURCE1} Makefile.am
install %{SOURCE2} configure.in

%build
aclocal
automake -a -c
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%dir %{_includedir}/quicktime
%{_includedir}/quicktime/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
