#
# TODO: Which package should Model/DBIC directory belong to?
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Model-DBIC-Schema
Summary:	Catalyst::Model::DBIC::Schema - DBIx::Class::Schema Model Class
Summary(pl.UTF-8):	Catalyst::Model::DBIC::Schema - klasa modelu DBIx::Class::Schema
Name:		perl-Catalyst-Model-DBIC-Schema
Version:	0.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ceea60ddf8170ce6142f9c232760789c
URL:		http://search.cpan.org/dist/Catalyst-Model-DBIC-Schema/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.70
BuildRequires:	perl-Class-Accessor >= 0.22
BuildRequires:	perl-Class-C3 >= 0.20
BuildRequires:	perl-Class-C3-XS >= 0.08
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-UNIVERSAL-require >= 0.10
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Catalyst Model for DBIx::Class::Schema-based Models. See the
documentation for Catalyst::Helper::Model::DBIC::Schema and
Catalyst::Helper::Model::DBIC::SchemaLoader for information on
generating these Models via Helper scripts. The latter of the two will
also generated a DBIx::Class::Schema::Loader-based Schema class for
you.

%description -l pl.UTF-8
To jest model Catalysta dla modeli opartych o DBIx::Class::Schema.
Informacje na temat generowania tych modeli poprzez skrypty pomocnicze
można znaleźć w dokumentacji dla Catalyst::Helper::Model::DBIC::Schema
i Catalyst::Helper::Model::DBIC::SchemaLoader. Ten drugi moduł
wygeneruje także klasę schematu opartą o DBIx::Class::Schema::Loader.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Model/DBIC/*.pm
%{perl_vendorlib}/Catalyst/Helper/Model/DBIC/Schema.pm
%{_mandir}/man3/*
