Name:       libX11
Version:    1.8.4
Release:    1%{?dist}
Summary:    Core X11 protocol client library
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/lib/libx11
Source0:    https://gitlab.freedesktop.org/xorg/lib/libx11/-/archive/%{name}-%{version}/libx11-%{name}-%{version}.tar.bz2
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
Although a client usually runs on the same machine as the X server it
is talking to, this need not be the case.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:    Documentation for %{name}
Requires:   %{name} = %{version}-%{release}

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
%{_libdir}/%{name}-xcb.so.*
%{_datadir}/X11

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
