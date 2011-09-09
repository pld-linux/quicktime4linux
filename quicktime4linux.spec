Summary:	Quicktime for Linux
Summary(pl.UTF-8):	Obsługa formatu Quicktime dla Linuksa
Name:		quicktime4linux
Version:	2.3
Release:	15
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/heroines/%{name}-%{version}-src.tar.bz2
# Source0-md5:	db3724400a0b29b49bf494bbb047caf9
Patch0:		%{name}-acam.patch
Patch1:		%{name}-libs.patch
Patch2:		%{name}-x264.patch
Patch3:		%{name}-ffmpeg.patch
URL:		http://heroinewarrior.com/quicktime.php3
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	faac-devel >= 1.24
BuildRequires:	faad2-devel >= 2.0
BuildRequires:	ffmpeg-devel >= 0.6
BuildRequires:	lame-libs-devel >= 3.93.1
BuildRequires:	libdv-devel >= 0.104
BuildRequires:	libjpeg-devel
BuildRequires:	libmpeg3-devel >= 1.8
BuildRequires:	libogg-devel >= 2:1.1.2
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.1.1
BuildRequires:	libx264-devel >= 0.1.2-1.20061024_2245.1
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	ffmpeg >= 0.4.9-4.20080822
Requires:	libdv >= 0.104
Requires:	libmpeg3 >= 1.8
Requires:	libx264 >= 0.1.2-1.20060828_2245.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quicktime4linux is a library for reading and writing Quicktime files
on UNIX systems. Supported by this library video is MJPA, JPEG Photo,
PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression and supported audio is
IMA4, ulaw, and any linear PCM format.

%description -l pl.UTF-8
Quicktime4linux jest biblioteką do odczytywania i zapisu plików w
formacie Quicktime przeznaczoną dla systemów Unix. Obecnie wspiera ona
następujące formaty video: MJPA, JPEG Photo, PNG, RGB, YUV 4:2:2 oraz
YUV 4:2:0, a także audio IMA4, ulaw i liniowy format PCM.

%package devel
Summary:	Header files and development documentation for quicktime4linux
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do quicktime4linux
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	faad2-devel >= 2.0
Requires:	ffmpeg-devel >= 0.4.9-4.20080822
Requires:	lame-libs-devel >= 3.93.1
Requires:	libdv-devel >= 0.104
Requires:	libjpeg-devel
Requires:	libmpeg3-devel >= 1.8
Requires:	libogg-devel >= 2:1.1.2
Requires:	libpng-devel >= 1.0.8
Requires:	libvorbis-devel >= 1:1.1.1
Requires:	libx264-devel >= 0.1.2-1.20060828_2245.1
Obsoletes:	libquicktime-devel

%description devel
Header files and development documentation for quicktime4linux.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do biblioteki quicktime4linux.

%package static
Summary:	Static quicktime4linux libraries
Summary(pl.UTF-8):	Biblioteki statyczne quicktime4linux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libquicktime-static

%description static
Static quicktime4linux libraries.

%description static -l pl.UTF-8
Biblioteki statyczne quicktime4linux.

%package progs
Summary:	Useful tools to operate at Quicktime files
Summary(pl.UTF-8):	Pożyteczne narzędzia od operowania na plikach w formacie Quicktime
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description progs
Useful tools to operate at Quicktime files.

%description progs -l pl.UTF-8
Pożyteczne narzędzia od operowania na plikach w formacie Quicktime.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

%{__rm} -r thirdparty/{faac-1.24,faad2-2.0,ffmpeg.*,jpeg,jpeg-mmx.*,lame-*,libdv-*,libogg-*,libvorbis-*,x264.*}

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
%attr(755,root,root) %{_libdir}/libquicktime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libquicktime.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/*.html
%attr(755,root,root) %{_libdir}/libquicktime.so
%{_libdir}/libquicktime.la
%{_includedir}/quicktime

%files static
%defattr(644,root,root,755)
%{_libdir}/libquicktime.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
