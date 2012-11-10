Name:           glib-networking
Version:        2.32.3
Release:        0
License:        LGPL-2.1+
Summary:        Network-related GIO modules for glib
Group:          System/Libraries
Source:         http://download.gnome.org/sources/glib-networking/2.32/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
# For directory ownership
BuildRequires:  pkgconfig(dbus-1)
# If this BuildRequires changes because of a gio library version change, change gio_real_package accordingly
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.6
BuildRequires:  pkgconfig(gnutls) >= 2.11.0
#BuildRequires:  pkgconfig(gsettings-desktop-schemas)
#BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(p11-kit-1) >= 0.8
# org.gnome.system.proxy schema is used
Requires:       gsettings-desktop-schemas
%define gio_real_package %(rpm -q --qf '%%{name}' --whatprovides gio)
%glib2_gio_module_requires

%description
This package contains network-related GIO modules for glib.

Currently, there is only a proxy module based on libproxy.

%lang_package

%prep
%setup -q

%build
%configure \
    --disable-static \
    --with-ca-certificates=/etc/ssl/ca-bundle.pem
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name}


%post
%glib2_gio_module_post

%postun
%glib2_gio_module_postun

%files
%defattr(-, root, root)
%doc COPYING
#%{_libdir}/gio/modules/libgiognomeproxy.so
%{_libdir}/gio/modules/libgiognutls.so
#%{_libdir}/gio/modules/libgiolibproxy.so
#%{_libexecdir}/glib-pacrunner
#%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service


%changelog
