#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-port_for
Version  : 0.6.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/6b/de/34724ce0498f8fe3a3d4925c7f36185977abfbc60c029ff622cc4bb3736d/port-for-0.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/6b/de/34724ce0498f8fe3a3d4925c7f36185977abfbc60c029ff622cc4bb3736d/port-for-0.6.2.tar.gz
Summary  : Utility that helps with local TCP ports management. It can find an unused TCP localhost port and remember the association.
Group    : Development/Tools
License  : MIT
Requires: pypi-port_for-bin = %{version}-%{release}
Requires: pypi-port_for-license = %{version}-%{release}
Requires: pypi-port_for-python = %{version}-%{release}
Requires: pypi-port_for-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
========
port-for
========
.. image:: https://img.shields.io/pypi/v/port-for.svg
:target: https://pypi.python.org/pypi/port-for
:alt: PyPI Version

%package bin
Summary: bin components for the pypi-port_for package.
Group: Binaries
Requires: pypi-port_for-license = %{version}-%{release}

%description bin
bin components for the pypi-port_for package.


%package license
Summary: license components for the pypi-port_for package.
Group: Default

%description license
license components for the pypi-port_for package.


%package python
Summary: python components for the pypi-port_for package.
Group: Default
Requires: pypi-port_for-python3 = %{version}-%{release}

%description python
python components for the pypi-port_for package.


%package python3
Summary: python3 components for the pypi-port_for package.
Group: Default
Requires: python3-core
Provides: pypi(port_for)

%description python3
python3 components for the pypi-port_for package.


%prep
%setup -q -n port-for-0.6.2
cd %{_builddir}/port-for-0.6.2
pushd ..
cp -a port-for-0.6.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656395156
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-port_for
cp %{_builddir}/port-for-0.6.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-port_for/8375d44da4da4fdb84131e2c704745dc9faaa177
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/port-for

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-port_for/8375d44da4da4fdb84131e2c704745dc9faaa177

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
