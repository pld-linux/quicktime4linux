Summary:	quicktime for Linux
Name:		quicktime4linux
Version:	1.1.8
Release:	1
Group:		Libraries
Group(pl):	Biblioteki
Copyright:	GPL
Source:		http://heroine.linuxbox.com/%{name}-%{version}.tar.gz
Patch:		quicktime4linux-automake.patch
URL:		http://heroine.linuxbox.com/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description

%package devel
Summary:	Header files and development documentation for quicktime4linux
Summary(pl):	Pliki nag³ówkowe i dokumentacja do quicktime4linux
Group:		Development/Libraries
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
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

#gzip -9nf AUTHORS README NEWS 

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
%attr(644,root,root) %{_libdir}/lib*.a

%changelog
