Summary:	quicktime for Linux
Name:		quicktime4linux
Version:	1.1.9
Release:	2
License:	GPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://heroine.linuxbox.com/%{name}-%{version}.tar.gz
Patch0:		%{name}-automake.patch
URL:		http://heroine.linuxbox.com/quicktime.html
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quicktime4linux is a library for reading and writing Quicktime files
on UNIX systems. Supported by this library video is MJPA, JPEG Photo,
PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression and supported audio is
IMA4, ulaw, and any linear PCM format.

%description -l pl
Quicktime4linux jest bibliotek± do odczytywania i zapisu plików
Quicktime przeznaczona dla systemów Unix. Obecnie biblioteka wspiera
nastêpuj±ce nastepuj±ce formaty video: MJPA, JPEG Photo, PNG, RGB, YUV
4:2:2 i YUV 4:2:0, a tak¿e audio IMA4, ulaw i liniowy format PCM.

%package devel
Summary:	Header files and development documentation for quicktime4linux
Summary(pl):	Pliki nag³ówkowe i dokumentacja do quicktime4linux
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for quicktime4linux.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do biblioteki quicktime4linux.

%package progs
Summary:	Useful tools to operate at quicktime files
Summary(pl):	Po¿yteczne narzêdzia od operowania na plikach quicktime
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Requires:	%{name} = %{version}

%description progs
Useful tools to operate at quicktime files.

%description -l pl progs
Po¿yteczne narzêdzia od operowania na plikach quicktime.

%package static
Summary:	Static quicktime4linux libraries
Summary(pl):	Biblioteki statyczne quicktime4linux
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static quicktime4linux libraries.

%description -l pl static
Biblioteki statyczne quicktime4linux.

%prep
%setup -q
%patch -p1 

%build
aclocal
autoheader
automake
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--program-transform-name="s/^qt// ; s/^/qt/"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS README NEWS 

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
%doc docs/*.html
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
