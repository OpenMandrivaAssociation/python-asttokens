%define module asttokens
%bcond_without test

Name:		python-asttokens
Version:	3.0.0
Release:	2
Summary:	Annotate AST trees with source code positions
URL:		https://pypi.org/project/asttokens/
License:	Apache-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/a/asttokens/asttokens-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(astroid)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(toml)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Annotate AST trees with source code positions.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
pytest -v tests/
%endif

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}*.*-info
%license LICENSE
%doc README.rst
