%include	/usr/lib/rpm/macros.php
%define         _class          Contact_Vcard_Parse
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Parse vCard 2.1 and 3.0 files
Summary(pl):	%{_pearname} - analiza plików vCard 2.1 i 3.0
Name:		php-pear-%{_pearname}
Version:	1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	b016ff097b5ee0b89da393af187c3843
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Contact_Vcard_Parse/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to parse vCard files and text blocks, and get back an array
of the elements of each vCard in the file or text.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa pozwala na analizowanie plików i bloków tekstu vCard i pobranie
tablicy elementów z ka¿dego vCard w pliku lub tek¶cie.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
