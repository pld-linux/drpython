Summary:	DrPython - cross-platform IDE to aid programming in Python
Summary(pl):	DrPython - wieloplatformowe IDE wspomagaj±ce programowanie w Pythonie
Name:		drpython
Version:	3.10.12
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/drpython/%{name}-%{version}.zip
# Source0-md5:	78222b14e65f457dc366219ad512b927
URL:		http://drpython.sourceforge.net/
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	unzip
%pyrequires_eq	python-modules
Requires:	python-wxPython >= 2.5.1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DrPython is a clean and simple yet powerful and highly customizable
editor/environment for developing programs written in the Python
programming Language. It is written in Python, and uses the wxWidgets
GUI Library through the use of wxPython.

%description -l pl
DrPython to przejrzysty i prosty, ale potê¿ny i wysoko konfigurowalny
edytor/¶rodowisko do tworzenia programów napisanych w jêzyku Python.
Jest napisany w Pythonie i u¿ywa biblioteki graficznej wxWidgets
poprzez interfejs wxPython.

%prep
%setup -q 

%build
chmod 644 *.py
%{_bindir}/python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

echo '#!/bin/sh' > $RPM_BUILD_ROOT%{_bindir}/drpython
echo 'cd %{py_sitescriptdir}/drpython' >> $RPM_BUILD_ROOT%{_bindir}/drpython
echo 'exec python drpython.pyo' >> $RPM_BUILD_ROOT%{_bindir}/drpython
chmod 755 $RPM_BUILD_ROOT%{_bindir}/drpython

find $RPM_BUILD_ROOT%{py_sitescriptdir} -not -wholename '*/drpython/examples/*' -name \*.py -exec rm -f {} \;
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/drpython/bitmaps/{16,24}/.xvpics

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt documentation/*
%attr(755,root,root) %{_bindir}/drpython
%dir %{py_sitescriptdir}/drpython
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
