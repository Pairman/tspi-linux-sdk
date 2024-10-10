Name: rockchip-mpp
Version: 1.5.0
Release: 1%{?dist}
Summary: Mali GPU User-Space Binary Drivers

License: Apache-2.0
URL: https://github.com/rockchip-linux/mpp
Source0: rockchip-mpp-1.5.0.tar.xz

BuildArch: aarch64

Requires: glibc >= 2.29
Requires: libstdc++ >= 5
Provides: librockchip_mpp
Provides: librockchip_vpu

%description
Media Process Platform.

%prep
%setup -q

%install
rm -rf %{buildroot}/*
cp -r %{_builddir}/rockchip-mpp-1.5.0/* %{buildroot}

%post
/usr/sbin/ldconfig

%postun
/usr/sbin/ldconfig

%files
%defattr(-,root,root,-)
%dir /usr/share/doc/rockchip-mpp
/usr/share/doc/rockchip-mpp/copyright
/usr/lib64/librockchip_mpp.so.0
/usr/lib64/librockchip_mpp.so
/usr/lib64/librockchip_mpp.so.1
/usr/lib64/librockchip_vpu.so.1
/usr/lib64/librockchip_vpu.so
/usr/lib64/librockchip_vpu.so.0

%changelog
* Thu Oct 10 2024 Randy Li <randy.li@rock-chips.com> - 1.5.0
- Initial RPM release.

