%define		_doc_version	2.6.11
%include	/usr/lib/rpm/macros.php
Summary:	Template engine for PHP
Summary(pl):	System szablonów dla PHP
Name:		Smarty
Version:	2.6.13
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://smarty.php.net/distributions/%{name}-%{version}.tar.gz
# Source0-md5:	2ca9bf476cf0920b9d4fee69633f6f65
Source1:	http://smarty.php.net/distributions/manual/en/%{name}-%{_doc_version}-docs.tar.gz
# Source1-md5:	7a0eaeda82eef073c87997141ee6207c
URL:		http://smarty.php.net/
BuildRequires:	rpm-php-pearprov >= 4.3
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_smartydir	%{_datadir}/php/Smarty

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
install -d $RPM_BUILD_ROOT{%{_smartydir}/{internals,plugins},%{php_pear_dir}}

install libs/{Config_File,Smarty{,_Compiler}}.class.php $RPM_BUILD_ROOT%{_smartydir}
install libs/debug.tpl $RPM_BUILD_ROOT%{_smartydir}
install libs/internals/*.php $RPM_BUILD_ROOT%{_smartydir}/internals
install libs/plugins/*.php $RPM_BUILD_ROOT%{_smartydir}/plugins

# backards compatible
ln -s %{_smartydir} $RPM_BUILD_ROOT%{php_pear_dir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

# make compat symlink, the symlink is discarded using %ghost on package uninstall
%triggerpostun -- Smarty < 2.6.10-4
if [ -d %{php_pear_dir}/%{name}/plugins ]; then
	mv %{php_pear_dir}/%{name}/plugins/* %{_smartydir}/plugins
	rmdir %{php_pear_dir}/%{name}/plugins 2>/dev/null
fi
rmdir %{php_pear_dir}/%{name} 2>/dev/null || mv -v %{php_pear_dir}/%{name}{,.rpmsave}
ln -s %{_smartydir} %{php_pear_dir}/%{name}

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog FAQ INSTALL NEWS README RELEASE_NOTES TODO
%dir %{_smartydir}
%dir %{_smartydir}/internals
%dir %{_smartydir}/plugins
%{_smartydir}/*.class.php
%{_smartydir}/debug.tpl
%{_smartydir}/internals/*.php
%{_smartydir}/plugins/*.php

# for the sake of bc
%ghost %{php_pear_dir}/%{name}

%files doc
%defattr(644,root,root,755)
%doc manual/*
