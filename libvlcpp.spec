Summary:	C++ bindings for libvlc
Summary(pl.UTF-8):	Wiązania C++ do libvlc
Name:		libvlcpp
Version:	0.1.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Libraries
#Source0Download: https://code.videolan.org/videolan/libvlcpp/-/tags
Source0:	https://code.videolan.org/videolan/libvlcpp/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	5cbcb7aae7c4a6c23864a1ea4687c99a
URL:		https://code.videolan.org/videolan/libvlcpp
BuildRequires:	cmake >= 2.8
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	vlc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ bindings for libvlc.

%description -l pl.UTF-8
Wiązania C++ do libvlc.

%package devel
Summary:	C++ bindings for libvlc
Summary(pl.UTF-8):	Wiązania C++ do libvlc
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.7

%description devel
C++ bindings for libvlc.

%description devel -l pl.UTF-8
Wiązania C++ do libvlc.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/vlcpp,%{_pkgconfigdir}}

cp -p vlcpp/*.hpp $RPM_BUILD_ROOT%{_includedir}/vlcpp

cat >$RPM_BUILD_ROOT%{_pkgconfigdir}/libvlcpp.pc <<'EOF'
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libvlcpp
Description: libvlc C++ bindings
Version: %{version}
Cflags: -I${includedir}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%{_includedir}/vlcpp
%{_pkgconfigdir}/libvlcpp.pc
