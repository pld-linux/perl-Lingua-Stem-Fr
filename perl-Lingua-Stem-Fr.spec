#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Lingua
%define		pnam	Stem-Fr
%include	/usr/lib/rpm/macros.perl
Summary:	Lingua::Stem::Fr - Porter's stemming algorithm for French
Summary(pl.UTF-8):	Lingua::Stem::Fr - algorytm Portera określający rdzenie słów dla języka francuskiego
Name:		perl-Lingua-Stem-Fr
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b4ea5dd1d942b190160e9cbc73115b20
URL:		http://search.cpan.org/dist/Lingua-Stem-Fr/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module applies the Porter Stemming Algorithm to its parameters,
returning the stemmed words.

The algorithm is implemented exactly as described in:
http://snowball.tartarus.org/italian/stemmer.html .

%description -l pl.UTF-8
Ten moduł stosuje do swoich parametrów algorytm Portera określający
rdzenie słów, zwracając te rdzenie.

Zaimplementowany został algorytm opisany na stronie:
http://snowball.tartarus.org/italian/stemmer.html .

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Lingua/Stem/*.pm
%{_mandir}/man3/*
