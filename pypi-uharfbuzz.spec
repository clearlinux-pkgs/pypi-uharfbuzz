#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : pypi-uharfbuzz
Version  : 0.45.0
Release  : 40
URL      : https://files.pythonhosted.org/packages/28/af/bbf0f0bf78f3d6a81fd97c7a5b90aa4172d4dbc8560a5db467ef511b09b0/uharfbuzz-0.45.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/28/af/bbf0f0bf78f3d6a81fd97c7a5b90aa4172d4dbc8560a5db467ef511b09b0/uharfbuzz-0.45.0.tar.gz
Summary  : Streamlined Cython bindings for the harfbuzz shaping engine
Group    : Development/Tools
License  : Apache-2.0 MIT OFL-1.1
Requires: pypi-uharfbuzz-license = %{version}-%{release}
Requires: pypi-uharfbuzz-python = %{version}-%{release}
Requires: pypi-uharfbuzz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(pkgconfig)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Githun CI Status](https://github.com/harfbuzz/uharfbuzz/workflows/Build%20+%20Deploy/badge.svg)](https://github.com/harfbuzz/uharfbuzz/actions?query=workflow%3A%22Build+%2B+Deploy%22)
[![PyPI](https://img.shields.io/pypi/v/uharfbuzz.svg)](https://pypi.org/project/uharfbuzz)
[![Documentation Status](https://readthedocs.org/projects/uharfbuzz/badge/?version=latest)](https://uharfbuzz.readthedocs.io/en/latest/?badge=latest)

%package license
Summary: license components for the pypi-uharfbuzz package.
Group: Default

%description license
license components for the pypi-uharfbuzz package.


%package python
Summary: python components for the pypi-uharfbuzz package.
Group: Default
Requires: pypi-uharfbuzz-python3 = %{version}-%{release}

%description python
python components for the pypi-uharfbuzz package.


%package python3
Summary: python3 components for the pypi-uharfbuzz package.
Group: Default
Requires: python3-core
Provides: pypi(uharfbuzz)

%description python3
python3 components for the pypi-uharfbuzz package.


%prep
%setup -q -n uharfbuzz-0.45.0
cd %{_builddir}/uharfbuzz-0.45.0
pushd ..
cp -a uharfbuzz-0.45.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736798189
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz
cp %{_builddir}/uharfbuzz-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/uharfbuzz-%{version}/tests/data/LICENSE_AdobeBlank.txt %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz/ec660b17dff69058c2bbf122ca85ab83b920fce7 || :
cp %{_builddir}/uharfbuzz-%{version}/tests/data/LICENSE_MutatorSans.txt %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz/f16f6141ff149dc59d7c4007c89c5dfea5145057 || :
cp %{_builddir}/uharfbuzz-%{version}/tests/data/LICENSE_OpenSans.txt %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz/6f72adeceef57cbfad261360c1c0933be952557e || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-uharfbuzz/6f72adeceef57cbfad261360c1c0933be952557e
/usr/share/package-licenses/pypi-uharfbuzz/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/pypi-uharfbuzz/ec660b17dff69058c2bbf122ca85ab83b920fce7
/usr/share/package-licenses/pypi-uharfbuzz/f16f6141ff149dc59d7c4007c89c5dfea5145057

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
