%define upstream_name       Apache2-Filter-HTTPHeadersFixup
Name:		perl-%{upstream_name}
Version:	0.06
Release:	6

Summary:	Manipulate Apache 2 HTTP Headers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	apache-mod_perl
BuildRequires:  apache-mod_perl-devel
BuildRequires:	perl-devel
BuildRequires:	perl(Apache::Test) >= 1.25

BuildArch:	noarch

%description
Apache2::Filter::HTTPHeadersFixup is a super class which provides an
easy way to manipulate HTTP headers without invoking any mod_perl HTTP
handlers. This is accomplished by using input and/or output connection
filters.

It supports KeepAlive connections.

This class cannot be used as is. It has to be sub-classed.

%prep
%setup -q -n %{upstream_name}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Apache2/Filter/HTTPHeadersFixup.pm
%{_mandir}/*/*

