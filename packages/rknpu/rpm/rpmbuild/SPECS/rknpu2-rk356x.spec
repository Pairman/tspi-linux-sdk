Name: rknpu2-rk356x
Version: 2.2.0
Release: 1%{?dist}
Summary: RKNPU2 provides an advanced interface to access Rockchip NPU.

License: Apache-2.0
URL: https://github.com/airockchip/rknn-toolkit2
Source0: rknpu2-rk356x-2.2.0.tar.xz

BuildArch: aarch64

Requires: glibc >= 2.17
Requires: libgcc >= 3.0
Requires: libstdc++ >= 6
Provides: librknnrt

%description
Media Process Platform.

%prep
%setup -q

%install
rm -rf %{buildroot}/*
cp -r %{_builddir}/rknpu2-rk356x-2.2.0/* %{buildroot}

%post
/usr/sbin/ldconfig

%postun
/usr/sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/include/rknn_matmul_api.h
/usr/include/rknn_custom_op.h
/usr/include/rknn_api.h
/usr/bin/start_rknn.sh
/usr/bin/restart_rknn.sh
/usr/bin/rknn_server
/usr/lib64/librknnrt.so

%changelog
* Thu Oct 10 2024 Randall Zhuo <randall.zhuo@rock-chips.com> - 2.2.0
- Initial RPM release.

