Summary:	DrPython - cross-platform IDE to aid programming in Python
Summary(pl):	DrPython - wieloplatformowe IDE wspomagaj±ce programowanie w Pythonie
Name:		drpython
Version:	3.6.8
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/drpython/%{name}-%{version}.zip
# Source0-md5:	bafc92efcb435c29dc41ffe5486da36a
# Source0-size:	468343
URL:		http://drpython.sourceforge.net/
BuildRequires:	python-modules >= 2.3
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
chmod 0644 *.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/drpython}

install *.py $RPM_BUILD_ROOT%{_datadir}/drpython
cp -a examples bitmaps $RPM_BUILD_ROOT%{_datadir}/drpython

echo '#!/bin/sh' > $RPM_BUILD_ROOT%{_bindir}/drpython
echo 'cd %{_datadir}/drpython' >> $RPM_BUILD_ROOT%{_bindir}/drpython
echo 'exec python drpython.pyo' >> $RPM_BUILD_ROOT%{_bindir}/drpython
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/drpython

%py_comp $RPM_BUILD_ROOT%{_datadir}/drpython
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/drpython

find $RPM_BUILD_ROOT%{_datadir} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt documentation/*
%attr(755,root,root) %{_bindir}/drpython
%{_datadir}/drpython
