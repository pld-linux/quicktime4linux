Summary:	Quicktime for Linux
Summary(pl):	Obs³uga formatu Quicktime dla Linuksa
Name:		quicktime4linux
Version:	2.0.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/heroines/%{name}-%{version}-src.tar.bz2
# Source0-md5:	c3b89779dd7082b3852db935fc18d91d
Patch0:		%{name}-acam.patch
Patch1:		%{name}-libs.patch
Patch2:		%{name}-broken.patch
URL:		http://heroinewarrior.com/quicktime.php3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	faad2-devel >= 2.0
BuildRequires:	ffmpeg-devel >= 0.4.8
BuildRequires:	glib-devel
BuildRequires:	lame-libs-devel >= 3.93.1
BuildRequires:	libdv-devel >= 0.102
BuildRequires:	libjpeg-devel
BuildRequires:	libmpeg3-devel >= 1.5.3
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	ffmpeg >= 0.4.8
Requires:	libdv >= 0.99
Requires:	libmpeg3 >= 1.5.3
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
Requires:	%{name} = %{version}-%{release}
Requires:	faad2-devel >= 2.0
Requires:	ffmpeg-devel >= 0.4.8
Requires:	glib-devel
Requires:	lame-libs-devel >= 3.93.1
Requires:	libdv-devel >= 0.99
Requires:	libjpeg-devel
Requires:	libmpeg3-devel >= 1.5.3
Requires:	libogg-devel >= 2:1.0
Requires:	libpng-devel >= 1.0.8
Requires:	libvorbis-devel >= 1:1.0

%description devel
Header files and development documentation for quicktime4linux.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki quicktime4linux.

%package progs
Summary:	Useful tools to operate at Quicktime files
Summary(pl):	Po¿yteczne narzêdzia od operowania na plikach w formacie Quicktime
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description progs
Useful tools to operate at Quicktime files.

%description progs -l pl
Po¿yteczne narzêdzia od operowania na plikach w formacie Quicktime.

%package static
Summary:	Static quicktime4linux libraries
Summary(pl):	Biblioteki statyczne quicktime4linux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static quicktime4linux libraries.

%description static -l pl
Biblioteki statyczne quicktime4linux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -rf faad2 ffmpeg-* jpeg jpeg-mmx-* lame-* libdv-* libogg-* libvorbis-*
%{__perl} -pi -e 's@"faad2/include/faad\.h"@<faad.h>@' mp4a.c

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-vorbistest

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%doc docs/*.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/quicktime

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
