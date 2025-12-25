Name:		python-oyaml
Version:	1.0
Release:	4
Source0:	https://files.pythonhosted.org/packages/source/o/oyaml/oyaml-%{version}.tar.gz
Summary:	Ordered YAML: drop-in replacement for PyYAML which preserves dict ordering
URL:		https://pypi.org/project/oyaml/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Ordered YAML: drop-in replacement for PyYAML which preserves dict ordering

%files
%{py_sitedir}/oyaml.py
%{py_sitedir}/oyaml-*.*-info
