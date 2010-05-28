%define		doc_version	2.6.14
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Template engine for PHP
Summary(pl.UTF-8):	System szablonów dla PHP
Name:		Smarty
Version:	2.6.26
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://www.smarty.net/distributions/%{name}-%{version}.tar.gz
# Source0-md5:	e0da351443b8613e1013c481ab30cb84
# Source1Download: http://www.smarty.net/download-docs.php
Source1:	http://www.smarty.net/distributions/manual/en/%{name}-%{doc_version}-docs.tar.gz
# Source1-md5:	5123152dd248898a84b96b806f551e78
Source2:	%{name}-function.html_input_image.php
URL:		http://www.smarty.net/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-pcre
Requires:	php-tokenizer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		appdir	%{php_data_dir}/Smarty

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
Version:	%{doc_version}
Group:		Development/Languages/PHP

%description doc
Documentation for Smarty template engine.

%description doc -l pl.UTF-8
Dokumentacja do systemu szablonów Smarty.

%prep
%setup -q -a1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{appdir}/{internals,plugins},%{php_pear_dir}}

cp -a libs/{Config_File,Smarty{,_Compiler}}.class.php $RPM_BUILD_ROOT%{appdir}
cp -a libs/debug.tpl $RPM_BUILD_ROOT%{appdir}
cp -a libs/internals/*.php $RPM_BUILD_ROOT%{appdir}/internals
cp -a libs/plugins/*.php $RPM_BUILD_ROOT%{appdir}/plugins
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{appdir}/plugins/function.html_input_image.php

# backards compatible
ln -s %{appdir} $RPM_BUILD_ROOT%{php_pear_dir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

# make compat symlink, the symlink is discarded using %ghost on package uninstall
%triggerpostun -- Smarty < 2.6.10-4
if [ -d %{php_pear_dir}/%{name}/plugins ]; then
	mv %{php_pear_dir}/%{name}/plugins/* %{appdir}/plugins
	rmdir %{php_pear_dir}/%{name}/plugins 2>/dev/null
fi
rmdir %{php_pear_dir}/%{name} 2>/dev/null || mv -v %{php_pear_dir}/%{name}{,.rpmsave}
ln -s %{appdir} %{php_pear_dir}/%{name}

%post
[ -e %{php_pear_dir}/%{name} ] || ln -s %{appdir} %{php_pear_dir}/%{name}

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog FAQ INSTALL NEWS README RELEASE_NOTES TODO
%dir %{appdir}
%dir %{appdir}/internals
%dir %{appdir}/plugins
%{appdir}/Config_File.class.php
%{appdir}/Smarty.class.php
%{appdir}/Smarty_Compiler.class.php
%{appdir}/debug.tpl
%{appdir}/internals/*.php
%{appdir}/plugins/*.php

# for the sake of bc when installed to pear dir
%ghost %{php_pear_dir}/%{name}

%files doc
%defattr(644,root,root,755)
%doc manual/*
