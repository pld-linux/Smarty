%define		_doc_version	2.4.0
Summary:	Template engine for PHP
Summary(pl):	System szablonów dla PHP
Name:		Smarty
Version:	2.4.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://smarty.php.net/distributions/%{name}-%{version}.tar.gz
Source1:	http://smarty.php.net/distributions/manual/en/%{name}-%{_doc_version}-docs.tar.gz
Requires:	php
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smarty is a template engine for PHP. Smarty provides your basic
variable substitution and dynamic block functionality, and also takes
a step further to be a "smart" template engine, adding features such
as configuration files, template functions, variable modifiers, and
making all of this functionality as easy as possible to use for both
programmers and template designers.

%description -l pl
Smarty jest systemem szablonów dla PHP. Pozwala na podstawowe
podstawianie warto¶ci zmiennych oraz dynamiczne operacje na blokach;
idzie o krok dalej, aby byæ "m±drym" silnikiem szablonów, dodaj±c
takie mo¿liwo¶ci jak pliki konfiguracyjne, funkcje, zmienne
modyfikatory oraz czyni±c ca³± funkcjonalno¶æ jak naj³atwiejsz± w
u¿yciu jednocze¶nie dla programistów i projektantów szablonów.

%package doc
Summary:	Template engine for PHP - documentation
Summary(pl):	System szablonów dla PHP - dokumentacja
Version:	%{_doc_version}
Group:		Development/Languages/PHP

%description doc
Documentation for Smarty template engine.

%description doc -l pl
Dokumentacja do systemu szablonów Smarty.

%prep
%setup -q -a 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pear/%{name}/plugins

install {Config_File,Smarty{,_Compiler}}.class.php $RPM_BUILD_ROOT%{_datadir}/pear/%{name}
install debug.tpl $RPM_BUILD_ROOT%{_datadir}/pear/%{name}
install plugins/*.php $RPM_BUILD_ROOT%{_datadir}/pear/%{name}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CREDITS ChangeLog FAQ INSTALL NEWS QUICKSTART README RELEASE_NOTES RESOURCES TESTIMONIALS TODO
%dir %{_datadir}/pear/%{name}
%dir %{_datadir}/pear/%{name}/plugins
%{_datadir}/pear/%{name}/*.class.php
%{_datadir}/pear/%{name}/debug.tpl
%{_datadir}/pear/%{name}/plugins/*.php

%files doc
%defattr(644,root,root,755)
%doc manual/*
