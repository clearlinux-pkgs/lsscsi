#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lsscsi
Version  : 0.28
Release  : 3
URL      : https://github.com/hreinecke/lsscsi/archive/v0.28.tar.gz
Source0  : https://github.com/hreinecke/lsscsi/archive/v0.28.tar.gz
Summary  : List SCSI devices (or hosts) and associated information
Group    : Development/Tools
License  : GPL-2.0
Requires: lsscsi-bin = %{version}-%{release}
Requires: lsscsi-license = %{version}-%{release}
Requires: lsscsi-man = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: fix_major_minor_header.patch

%description
Uses information provided by the sysfs pseudo file system in the Linux
kernel 2.6 series, and later, to list SCSI devices (Logical
Units (e.g. disks)). It can list transport identifiers (e.g. SAS address
of a SAS disk), protection information configuration and size for storage
devices. Alternatively it can be used to list SCSI hosts (e.g. HBAs). By
default one line of information is output per device (or host).

Author:
--------
    Doug Gilbert <dgilbert at interlog dot com>

%package bin
Summary: bin components for the lsscsi package.
Group: Binaries
Requires: lsscsi-license = %{version}-%{release}

%description bin
bin components for the lsscsi package.


%package license
Summary: license components for the lsscsi package.
Group: Default

%description license
license components for the lsscsi package.


%package man
Summary: man components for the lsscsi package.
Group: Default

%description man
man components for the lsscsi package.


%prep
%setup -q -n lsscsi-0.28
cd %{_builddir}/lsscsi-0.28
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604542367
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604542367
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lsscsi
cp %{_builddir}/lsscsi-0.28/COPYING %{buildroot}/usr/share/package-licenses/lsscsi/74a8a6531a42e124df07ab5599aad63870fa0bd4
cp %{_builddir}/lsscsi-0.28/debian/copyright %{buildroot}/usr/share/package-licenses/lsscsi/8f416baf384d4c28700e815e622e08be8217bf7a
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lsscsi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lsscsi/74a8a6531a42e124df07ab5599aad63870fa0bd4
/usr/share/package-licenses/lsscsi/8f416baf384d4c28700e815e622e08be8217bf7a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/lsscsi.8
