# %define		_doc_version	2.4.0
%include	/usr/lib/rpm/macros.php
Summary:	Template engine for PHP
Summary(pl):	System szablon�w dla PHP
Name:		Smarty
Version:	2.6.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://smarty.php.net/distributions/%{name}-%{version}.tar.gz
# Source0-md5:	e7bf2f46c6a188220493f1e12ab55c19
Source1:	http://smarty.php.net/distributions/manual/en/%{name}-%{version}-docs.tar.gz
# Source1-md5:	3035699c5785c06b0492832d372ffc62
BuildRequires:	rpm-php-pearprov >= 4.3
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
Smarty jest systemem szablon�w dla PHP. Pozwala na podstawowe
podstawianie warto�ci zmiennych oraz dynamiczne operacje na blokach;
idzie o krok dalej, aby by� "m�drym" silnikiem szablon�w, dodaj�c
takie mo�liwo�ci jak pliki konfiguracyjne, funkcje, zmienne
modyfikatory oraz czyni�c ca�� funkcjonalno�� jak naj�atwiejsz� w
u�yciu jednocze�nie dla programist�w i projektant�w szablon�w.

%package doc
Summary:	Template engine for PHP - documentation
Summary(pl):	System szablon�w dla PHP - dokumentacja
Version:	%{_doc_version}
Group:		Development/Languages/PHP

%description doc
Documentation for Smarty template engine.

%description doc -l pl
Dokumentacja do systemu szablon�w Smarty.

%prep
%setup -q -a 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/plugins

install libs/{Config_File,Smarty{,_Compiler}}.class.php $RPM_BUILD_ROOT%{php_pear_dir}/%{name}
install libs/debug.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{name}
install libs/plugins/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog FAQ INSTALL NEWS README RELEASE_NOTES TODO
%dir %{php_pear_dir}/%{name}
%dir %{php_pear_dir}/%{name}/plugins
%{php_pear_dir}/%{name}/*.class.php
%{php_pear_dir}/%{name}/debug.tpl
%{php_pear_dir}/%{name}/plugins/*.php

%files doc
%defattr(644,root,root,755)
%doc manual/*
