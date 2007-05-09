%define real_name Apache2-Filter-HTTPHeadersFixup

Summary:	Apache2::Filter::HTTPHeadersFixup - Manipulate Apache 2 HTTP Headers
Name:		perl-%{real_name}
Version:	0.06
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache2/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	apache-mod_perl
BuildRequires:  apache-mod_perl-devel
BuildRequires:	perl(Apache::Test) >= 1.25
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Apache2::Filter::HTTPHeadersFixup is a super class which provides an
easy way to manipulate HTTP headers without invoking any mod_perl HTTP
handlers. This is accomplished by using input and/or output connection
filters.

It supports KeepAlive connections.

This class cannot be used as is. It has to be sub-classed.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Apache2/Filter/HTTPHeadersFixup.pm
%{_mandir}/*/*

