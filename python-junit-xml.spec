#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Create JUnit XML test result documents that can be read by tools such as Jenkins
Summary(pl.UTF-8):	Tworzenie dokumentów wynikowych testów jako JUnit XML do odczytu przez np. Jenkinsa
Name:		python-junit-xml
Version:	1.9
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/junit-xml/
Source0:	https://files.pythonhosted.org/packages/source/j/junit-xml/junit-xml-%{version}.tar.gz
# Source0-md5:	a21d0456f5e44c7baedb029e174e8e42
URL:		https://pypi.org/project/junit-xml/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module for creating JUnit XML test result documents that can
be read by tools such as Jenkins or Bamboo. If you are ever working
with test tool or test suite written in Python and want to take
advantage of Jenkins' or Bamboo's pretty graphs and test reporting
capabilities, this module will let you generate the XML test reports.

%description -l pl.UTF-8
Moduł Pythona do tworzenia dokumentów wynikowych testów w formacie
JUnit XML, które mogą być czytane przez narzędzia takie jak Jenkins
czy Bamboo. Pozwala to na wykorzystanie możliwości raportowania i
ładnych wykresów Jenkinsa lub Bamboo na podstawie raportów XML.

%package -n python3-junit-xml
Summary:	Create JUnit XML test result documents that can be read by tools such as Jenkins
Summary(pl.UTF-8):	Tworzenie dokumentów wynikowych testów jako JUnit XML do odczytu przez np. Jenkinsa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-junit-xml
A Python module for creating JUnit XML test result documents that can
be read by tools such as Jenkins or Bamboo. If you are ever working
with test tool or test suite written in Python and want to take
advantage of Jenkins' or Bamboo's pretty graphs and test reporting
capabilities, this module will let you generate the XML test reports.

%description -n python3-junit-xml -l pl.UTF-8
Moduł Pythona do tworzenia dokumentów wynikowych testów w formacie
JUnit XML, które mogą być czytane przez narzędzia takie jak Jenkins
czy Bamboo. Pozwala to na wykorzystanie możliwości raportowania i
ładnych wykresów Jenkinsa lub Bamboo na podstawie raportów XML.

%prep
%setup -q -n junit-xml-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc LICENSE.txt README.rst
%{py_sitescriptdir}/junit_xml
%{py_sitescriptdir}/junit_xml-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-junit-xml
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/junit_xml
%{py3_sitescriptdir}/junit_xml-%{version}-py*.egg-info
%endif
