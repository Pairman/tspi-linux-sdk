Modified [CmST0us/tspi-linux-sdk](https://github.com/CmST0us/tspi-linux-sdk.git) for building Fedora.

Setup env on Fedora 40 host:
```
sudo dnf group install -y development-tools
sudo dnf install -y dtc lz4 python2 rpm-build
```

Clone and build a Fedora Server 40 update image:
```
TSPI_LINUX_SDK_URL="https://github.com/Pairman/tspi-linux-sdk"
git clone "$TSPI_LINUX_SDK_URL" -b main --depth 1
cd tspi-linux-sdk
wget -O fedora/fedora.tar.xz "$TSPI_LINUX_SDK_URL/releases/download/2024.10.10/fedora.tar.xz"
./build.sh init
./build.sh
```
