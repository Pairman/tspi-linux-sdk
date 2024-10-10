Name: libmali-bifrost-g52-g13p0-wayland-gbm
Version: 1.9
Release: 1%{?dist}
Summary: Mali GPU User-Space Binary Drivers

License: Proprietary
URL: https://github.com/rockchip-linux/libmali
Source0: libmali-bifrost-g52-g13p0-wayland-gbm-1.9.tar.xz

BuildArch: aarch64

Requires: glibc >= 2.17
Requires: libdrm >= 2.3.1
Requires: libgcc >= 4.2
Requires: libstdc++ >= 6
Requires: libwayland-client >= 1.11.0
Requires: libwayland-server >= 1.2.0
Conflicts: libmali
Provides: libmali

%description
Mali GPU User-Space Binary Drivers for Bifrost architecture, including Wayland GBM support.

%prep
%setup -q

%install
rm -rf %{buildroot}/*
cp -r %{_builddir}/libmali-bifrost-g52-g13p0-wayland-gbm-1.9/* %{buildroot}

%post
/usr/sbin/ldconfig

%postun
/usr/sbin/ldconfig

%files
%defattr(-,root,root,-)
/etc/ld.so.conf.d/00-aarch64-mali.conf
%dir /etc/OpenCL/
%dir /etc/OpenCL/vendors/
/etc/OpenCL/vendors/mali.icd
%dir /usr/share/doc/libmali-bifrost-g52-g13p0-wayland-gbm/
/usr/share/doc/libmali-bifrost-g52-g13p0-wayland-gbm/copyright
%dir /usr/lib64/mali/
/usr/lib64/mali/libGLESv2.so
/usr/lib64/mali/libGLESv2.so.2
/usr/lib64/mali/libGLESv1_CM.so
/usr/lib64/mali/libGLESv1_CM.so.1
/usr/lib64/mali/libEGL.so
/usr/lib64/mali/libEGL.so.1
/usr/lib64/mali/libMaliOpenCL.so
/usr/lib64/mali/libMaliOpenCL.so.1
/usr/lib64/mali/libwayland-egl.so
/usr/lib64/mali/libwayland-egl.so.1
/usr/lib64/mali/libgbm.so
/usr/lib64/mali/libgbm.so.1
/usr/lib64/libmali.so
/usr/lib64/libmali.so.1
/usr/lib64/libmali.so.1.9.0
/usr/lib64/libmali-bifrost-g52-g13p0-wayland-gbm.so
/usr/lib64/libmali-hook-injector.a
/usr/lib64/libmali-hook.so
/usr/lib64/libmali-hook.so.1
/usr/lib64/libmali-hook.so.1.9.0
/usr/lib64/pkgconfig/mali.pc

%changelog
* Thu Oct 10 2024 Putin Lee <putin.li@rock-chips.com> - 1.9-1
- Initial RPM release.

