#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-uharfbuzz
Version  : 0.25.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/f9/e3/4116b4cf1ca40573aa8a4703b9cb4ab9480c2f40595099b7d1598b86db39/uharfbuzz-0.25.0.zip
Source0  : https://files.pythonhosted.org/packages/f9/e3/4116b4cf1ca40573aa8a4703b9cb4ab9480c2f40595099b7d1598b86db39/uharfbuzz-0.25.0.zip
Summary  : Streamlined Cython bindings for the harfbuzz shaping engine
Group    : Development/Tools
License  : Apache-2.0 MIT OFL-1.1
Requires: pypi-uharfbuzz-license = %{version}-%{release}
Requires: pypi-uharfbuzz-python = %{version}-%{release}
Requires: pypi-uharfbuzz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
[![Githun CI Status](https://github.com/harfbuzz/uharfbuzz/workflows/Build%20+%20Deploy/badge.svg)](https://github.com/harfbuzz/uharfbuzz/actions?query=workflow%3A%22Build+%2B+Deploy%22)
[![PyPI](https://img.shields.io/pypi/v/uharfbuzz.svg)](https://pypi.org/project/uharfbuzz)

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
%setup -q -n uharfbuzz-0.25.0
cd %{_builddir}/uharfbuzz-0.25.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650995884
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz
cp %{_builddir}/uharfbuzz-0.25.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/uharfbuzz-0.25.0/tests/data/LICENSE_AdobeBlank.txt %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz/ec660b17dff69058c2bbf122ca85ab83b920fce7
cp %{_builddir}/uharfbuzz-0.25.0/tests/data/LICENSE_MutatorSans.txt %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz/f16f6141ff149dc59d7c4007c89c5dfea5145057
cp %{_builddir}/uharfbuzz-0.25.0/tests/data/LICENSE_OpenSans.ttf %{buildroot}/usr/share/package-licenses/pypi-uharfbuzz/6f72adeceef57cbfad261360c1c0933be952557e
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
/usr/lib/python3*/*
