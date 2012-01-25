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
Version:	0.59
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce1f34c55797d4f9525cca505e621fba
URL:		http://search.cpan.org/dist/Catalyst-Model-DBIC-Schema/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Catalyst::Devel) >= 1.0
BuildRequires:	perl-Carp-Clan
BuildRequires:	perl-Catalyst >= 5.80005
BuildRequires:	perl-Catalyst-Component-InstancePerContext
BuildRequires:	perl-CatalystX-Component-Traits >= 0.14
BuildRequires:	perl-DBIx-Class >= 0.08114
BuildRequires:	perl-DBIx-Class-Cursor-Cached
BuildRequires:	perl-DBIx-Class-Schema-Loader >= 0.04005
BuildRequires:	perl-Hash-Merge
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Moose >= 1.12
BuildRequires:	perl-MooseX-Traits-Pluggable
BuildRequires:	perl-MooseX-Types
#BuildRequires:	perl(MooseX::MarkAsMethods) >= 0.13
#BuildRequires:	perl(MooseX::NonMoose) >= 0.16
BuildRequires:	perl(Tie::IxHash)
BuildRequires:	perl-namespace-autoclean >= 0.09
BuildRequires:	perl-Try-Tiny
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl-DBD-SQLite
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
	--skipdeps \
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
%dir %{perl_vendorlib}/Catalyst/Model/DBIC
%{perl_vendorlib}/Catalyst/Model/DBIC/*.pm
%dir %{perl_vendorlib}/Catalyst/Helper/Model/DBIC
%{perl_vendorlib}/Catalyst/Helper/Model/DBIC/Schema.pm
%dir %{perl_vendorlib}/Catalyst/Model/DBIC
%dir %{perl_vendorlib}/Catalyst/Model/DBIC/Schema
%{perl_vendorlib}/Catalyst/Model/DBIC/Schema/Types.pm
%dir %{perl_vendorlib}/Catalyst/TraitFor
%dir %{perl_vendorlib}/Catalyst/TraitFor/Model
%dir %{perl_vendorlib}/Catalyst/TraitFor/Model/DBIC
%dir %{perl_vendorlib}/Catalyst/TraitFor/Model/DBIC/Schema
%{perl_vendorlib}/Catalyst/TraitFor/Model/DBIC/Schema/*.pm
%{_mandir}/man3/*
