#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Run each test in a forked subprocess
Summary(pl.UTF-8):	Uruchamianie każdego testu w oddzielnym procesie
Name:		python-pytest-forked
Version:	0.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-forked/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-forked/pytest-forked-%{version}.tar.gz
# Source0-md5:	133167c9c56c9121c80852f9cd702140
URL:		https://github.com/pytest-dev/pytest-forked
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-pytest >= 2.6.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest >= 2.6.0
%endif
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

%package -n python3-pytest-forked
Summary:	Run each test in a forked subprocess
Summary(pl.UTF-8):	Uruchamianie każdego testu w oddzielnym procesie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-pytest-forked
Run each test in a forked subprocess.

%description -n python3-pytest-forked -l pl.UTF-8
Uruchamianie każdego testu w oddzielnym procesie.

%prep
%setup -q -n pytest-forked-%{version}

# kill precompiled objects
%{__rm} -r testing/*.pyc testing/__pycache__

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest testing
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest testing
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst example/boxed.txt
%{py_sitescriptdir}/pytest_forked
%{py_sitescriptdir}/pytest_forked-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-forked
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst example/boxed.txt
%{py3_sitescriptdir}/pytest_forked
%{py3_sitescriptdir}/pytest_forked-%{version}-py*.egg-info
%endif
