%bcond_with libproxy
Name:           glib-networking
Version:        2.38.0
Release:        0
License:        LGPL-2.1+
Summary:        Network-related GIO modules for glib
Group:          System/Libraries
Source:         http://download.gnome.org/sources/glib-networking/2.35/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
Source1001:     glib-networking.manifest
Url:            http://www.gnome.org
BuildRequires:  intltool
BuildRequires:  which
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.6
BuildRequires:  pkgconfig(gnutls) >= 2.11.0
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(libtzplatform-config)
BuildRequires:  ca-certificates-devel
Requires: ca-certificates
%if %{with libproxy}
BuildRequires:  pkgconfig(libproxy-1.0)
%endif

%description
This package contains network-related GIO modules for glib.

Currently, there is only a proxy module based on libproxy.

%lang_package

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen \
    --disable-static \
%if %{with libproxy}
    --with-libproxy  \
%endif
%if "%{?profile}" == "tv"
    --enable-tizen-multiple-certificate=yes \
    --enable-tizen-tv-update-default-priority \
    --enable-tizen-dlog \
    --enable-tizen-performance-test-log \
%endif
%if "%{?profile}" == "tv"
    --with-ca-certificates=%{TZ_SYS_RO_CA_CERTS}
%else
    --with-ca-certificates=%{TZ_SYS_RO_CA_BUNDLE}
%endif

%__make %{?_smp_mflags} V=1

%install
%if "%{?profile}" == "tv"
rm -rf %{buildroot}
mkdir -p %{buildroot}%{TZ_SYS_SHARE}/ca-certificates/
cp wss.pem %{buildroot}%{TZ_SYS_SHARE}/ca-certificates/
%endif
%make_install
%find_lang %{name}

%post
%glib2_gio_module_post

%postun
%glib2_gio_module_postun

%files
%manifest %{name}.manifest
%defattr(-, root, root)
%doc COPYING
%{_libdir}/gio/modules/libgiognutls.so
%if "%{?profile}" == "tv"
%{TZ_SYS_SHARE}/ca-certificates/wss.pem
%endif

%if %{with libproxy}
%{_libdir}/gio/modules/libgiolibproxy.so
%{_libexecdir}/glib-pacrunner
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service
%endif
