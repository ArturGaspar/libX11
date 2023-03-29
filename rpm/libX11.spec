Name:       libX11
Version:    1.8.9
Release:    1%{?dist}
Summary:    Core X11 protocol client library
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/lib/libx11
Source0:    %{name}-%{version}.tar.bz2
Requires:   %{name}-data = %{version}-%{release}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xcb) >= 1.11.1
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.15
BuildRequires:  pkgconfig(xproto) >= 7.0.25
BuildRequires:  pkgconfig(xtrans)

%description
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client programs
located either on the same machine or elsewhere in the network. Xlib
is a C subroutine library that application programs (clients) use to
interface with the window system by means of a stream connection.

%package data
Summary:    Shared data for %{name} and %{name}-xcb.

%description data
The %{name}-data package contains files shared between %{name} and %{name}-xcb.

%package xcb
Summary:    X Library XCB interface
Requires:   %{name}-data = %{version}-%{release}

%description xcb
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client programs
located either on the same machine or elsewhere in the network. Xlib
is a C subroutine library that application programs (clients) use to
interface with the window system by means of a stream connection.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-xcb = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:    Documentation for %{name}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*
%{_datadir}/X11

%files data
%license COPYING
%{_datadir}/X11

%files xcb
%license COPYING
%{_libdir}/%{name}-xcb.so.*

%files devel
%license COPYING
%{_includedir}/X11
%{_libdir}/%{name}.so
%{_libdir}/%{name}-xcb.so
%{_libdir}/pkgconfig/x11.pc
%{_libdir}/pkgconfig/x11-xcb.pc

%files doc
%license COPYING
%{_docdir}/libX11
%{_mandir}/man3/*.3*
%{_mandir}/man5/*.5*
