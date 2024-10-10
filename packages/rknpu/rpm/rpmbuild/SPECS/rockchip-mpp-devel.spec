Name: rockchip-mpp-devel
Version: 1.5.0
Release: 1%{?dist}
Summary: Mali GPU User-Space Binary Drivers

License: Apache-2.0
URL: https://github.com/rockchip-linux/mpp
Source0: rockchip-mpp-devel-1.5.0.tar.xz

BuildArch: aarch64

Requires: rockchip-mpp = 1.5.0
Provides: rockchip-mpp-devel

%description
Media Process Platform.

%prep
%setup -q

%install
rm -rf %{buildroot}/*
cp -r %{_builddir}/rockchip-mpp-devel-1.5.0/* %{buildroot}

%files
%defattr(-,root,root,-)
%dir /usr/include/rockchip
/usr/include/rockchip/rk_venc_rc.h
/usr/include/rockchip/vpu_api.h
/usr/include/rockchip/mpp_log.h
/usr/include/rockchip/rk_venc_ref.h
/usr/include/rockchip/rk_vdec_cmd.h
/usr/include/rockchip/rk_mpi.h
/usr/include/rockchip/mpp_meta.h
/usr/include/rockchip/mpp_rc_api.h
/usr/include/rockchip/vpu.h
/usr/include/rockchip/rk_mpi_cmd.h
/usr/include/rockchip/mpp_rc_defs.h
/usr/include/rockchip/mpp_packet.h
/usr/include/rockchip/mpp_buffer.h
/usr/include/rockchip/mpp_err.h
/usr/include/rockchip/mpp_compat.h
/usr/include/rockchip/mpp_frame.h
/usr/include/rockchip/mpp_task.h
/usr/include/rockchip/rk_venc_cfg.h
/usr/include/rockchip/mpp_log_def.h
/usr/include/rockchip/rk_vdec_cfg.h
/usr/include/rockchip/rk_hdr_meta_com.h
/usr/include/rockchip/rk_type.h
/usr/include/rockchip/rk_venc_cmd.h
%dir /usr/share/doc/rockchip-mpp-devel
/usr/share/doc/rockchip-mpp-devel/copyright
/usr/lib64/pkgconfig/rockchip_mpp.pc
/usr/lib64/pkgconfig/rockchip_vpu.pc

%changelog
* Thu Oct 10 2024 Randy Li <randy.li@rock-chips.com> - 1.5.0
- Initial RPM release.

