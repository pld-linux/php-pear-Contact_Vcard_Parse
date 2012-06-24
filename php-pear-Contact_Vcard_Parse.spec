%include	/usr/lib/rpm/macros.php
%define		_class		Contact_Vcard_Parse
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - parse vCard 2.1 and 3.0 files
Summary(pl.UTF-8):	%{_pearname} - analiza plików vCard 2.1 i 3.0
Name:		php-pear-%{_pearname}
Version:	1.32.0
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d4a305d49434e05c7d7022c5d12faaab
URL:		http://pear.php.net/package/Contact_Vcard_Parse/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Contact_Vcard_Parse-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to parse vCard files and text blocks, and get back an array
of the elements of each vCard in the file or text.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa pozwala na analizowanie plików i bloków tekstu vCard i pobranie
tablicy elementów z każdego vCard w pliku lub tekście.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/%{_class}.php
%dir %{php_pear_dir}/Contact/Vcard
%{php_pear_dir}/Contact/Vcard/Parse.php
