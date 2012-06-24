%include	/usr/lib/rpm/macros.php
%define		_class		Contact_Vcard_Parse
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - parse vCard 2.1 and 3.0 files
Summary(pl):	%{_pearname} - analiza plik�w vCard 2.1 i 3.0
Name:		php-pear-%{_pearname}
Version:	1.31.0
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d03d91831b85fbd467f9bf6366b3481e
URL:		http://pear.php.net/package/Contact_Vcard_Parse/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to parse vCard files and text blocks, and get back an array
of the elements of each vCard in the file or text.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa pozwala na analizowanie plik�w i blok�w tekstu vCard i pobranie
tablicy element�w z ka�dego vCard w pliku lub tek�cie.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
