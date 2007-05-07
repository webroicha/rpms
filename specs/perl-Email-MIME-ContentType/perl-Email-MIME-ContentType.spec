# $Id$
# Authority: dries
# Upstream: Simon Cozens <simon$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-ContentType

Summary: Parse a MIME Content-Type Header
Name: perl-Email-MIME-ContentType
Version: 1.014
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-ContentType/

Source: http://www.cpan.org/modules/by-module/Email/Email-MIME-ContentType-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Parse a MIME Content-Type Header.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Email::MIME::ContentType.3pm*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/MIME/
%{perl_vendorlib}/Email/MIME/ContentType.pm

%changelog
* Sat May 05 2007 Dag Wieers <dag@wieers.com> - 1.014-1
- Updated to release 1.014.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
