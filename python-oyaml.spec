Name:		python-oyaml
Version:	1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/oyaml/oyaml-%{version}.tar.gz
Summary:	Ordered YAML: drop-in replacement for PyYAML which preserves dict ordering
URL:		https://pypi.org/project/oyaml/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Ordered YAML: drop-in replacement for PyYAML which preserves dict ordering

%prep
%autosetup -p1 -n oyaml-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/oyaml.py
%{py_sitedir}/oyaml-*.*-info
