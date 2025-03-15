#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Run each test in a forked subprocess
Summary(pl.UTF-8):	Uruchamianie każdego testu w oddzielnym procesie
Name:		python3-pytest-forked
# keep 1.3.x here for python2 support
Version:	1.6.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-forked/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-forked/pytest-forked-%{version}.tar.gz
# Source0-md5:	c2c026fc5bc4ad54649d7f85e36a62ec
Patch0:		pytest8.patch
URL:		https://github.com/pytest-dev/pytest-forked
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools >= 1:41.4
BuildRequires:	python3-setuptools_scm >= 3.3
%if %{with tests}
BuildRequires:	python3-py
BuildRequires:	python3-pytest >= 3.10
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Run each test in a forked subprocess.

%description -l pl.UTF-8
Uruchamianie każdego testu w oddzielnym procesie.

%prep
%setup -q -n pytest-forked-%{version}
%patch -P 0 -p1

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest -p no:flaky testing
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst example/boxed.txt
%{py3_sitescriptdir}/pytest_forked
%{py3_sitescriptdir}/pytest_forked-%{version}-py*.egg-info
