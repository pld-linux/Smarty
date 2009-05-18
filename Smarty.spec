%define		_doc_version	2.6.14
%include	/usr/lib/rpm/macros.php
Summary:	Template engine for PHP
Summary(pl.UTF-8):	System szablonów dla PHP
Name:		Smarty
Version:	2.6.24
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://www.smarty.net/distributions/%{name}-%{version}.tar.gz
# Source0-md5:	ea4b651bcd8f1a6596a214ad2c8fc302
Source1:	http://www.smarty.net/distributions/manual/en/%{name}-%{_doc_version}-docs.tar.gz
# Source1-md5:	5123152dd248898a84b96b806f551e78
Source2:	%{name}-function.html_input_image.php
URL:		http://www.smarty.net/
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

%description -l pl.UTF-8
Smarty jest systemem szablonów dla PHP. Pozwala na podstawowe
podstawianie wartości zmiennych oraz dynamiczne operacje na blokach;
idzie o krok dalej, aby być "mądrym" silnikiem szablonów, dodając
takie możliwości jak pliki konfiguracyjne, funkcje, zmienne
modyfikatory oraz czyniąc całą funkcjonalność jak najłatwiejszą w
użyciu jednocześnie dla programistów i projektantów szablonów.

%package doc
Summary:	Template engine for PHP - documentation
Summary(pl.UTF-8):	System szablonów dla PHP - dokumentacja
Version:	%{_doc_version}
Group:		Development/Languages/PHP

%description doc
Documentation for Smarty template engine.

%description doc -l pl.UTF-8
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
install %{SOURCE2} $RPM_BUILD_ROOT%{_smartydir}/plugins/function.html_input_image.php

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

%post
[ -e %{php_pear_dir}/%{name} ] || ln -s %{_smartydir} %{php_pear_dir}/%{name}

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
