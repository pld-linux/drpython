%define 	orgname DrPython
Summary:	DrPython - cross-platform IDE to aid programming in Python
Summary(pl.UTF-8):	DrPython - wieloplatformowe IDE wspomagające programowanie w Pythonie
Name:		drpython
Version:	3.11.3
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/project/drpython/DrPython%20Current/%{version}/%{orgname}_%{version}.zip
# Source0-md5:	eb59cf61d840af274d2940ce1a3c2bd4
URL:		http://drpython.sourceforge.net/
BuildRequires:	pydoc
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
%pyrequires_eq	python-modules
Requires:	python-wxPython >= 2.8.11.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DrPython is a clean and simple yet powerful and highly customizable
editor/environment for developing programs written in the Python
programming Language. It is written in Python, and uses the wxWidgets
GUI Library through the use of wxPython.

%description -l pl.UTF-8
DrPython to przejrzysty i prosty, ale potężny i wysoko konfigurowalny
edytor/środowisko do tworzenia programów napisanych w języku Python.
Jest napisany w Pythonie i używa biblioteki graficznej wxWidgets
poprzez interfejs wxPython.

%prep
%setup -q -n %{orgname}

%build
chmod 644 *.py
%{_bindir}/%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

echo '#!/bin/sh' > $RPM_BUILD_ROOT%{_bindir}/drpython
echo 'exec python %{py_sitescriptdir}/drpython/drpython.pyw' >> $RPM_BUILD_ROOT%{_bindir}/drpython
chmod 755 $RPM_BUILD_ROOT%{_bindir}/drpython

find $RPM_BUILD_ROOT%{py_sitescriptdir} -not -wholename '*/drpython/examples/*' -name \*.py -exec rm -f {} \;
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/drpython/bitmaps/{16,24}/.xvpics
# win32 only
rm $RPM_BUILD_ROOT%{_bindir}/postinst.py
# replace by %{_bindir}/drpython
rm $RPM_BUILD_ROOT%{py_sitescriptdir}/drpython/drpython.lin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.txt History.txt Notes.txt todo.txt documentation/*
%attr(755,root,root) %{_bindir}/drpython
%dir %{py_sitescriptdir}/drpython
%{py_sitescriptdir}/drpython/drpython.pyw
%{py_sitescriptdir}/drpython/*.py[oc]
%{py_sitescriptdir}/drpython/examples
%doc %{py_sitescriptdir}/drpython/documentation
%dir %{py_sitescriptdir}/drpython/bitmaps
%{py_sitescriptdir}/drpython/bitmaps/*.ico
%{py_sitescriptdir}/drpython/bitmaps/*.png
%dir %{py_sitescriptdir}/drpython/bitmaps/16
%{py_sitescriptdir}/drpython/bitmaps/16/*.png
%dir %{py_sitescriptdir}/drpython/bitmaps/24
%{py_sitescriptdir}/drpython/bitmaps/24/*.png
%{py_sitescriptdir}/*.egg-info
