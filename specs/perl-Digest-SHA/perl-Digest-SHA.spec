# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-SHA

Summary: Digest-SHA Perl module
Name: perl-Digest-SHA
Version: 5.44
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-SHA/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-SHA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Digest-SHA Perl module

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man1/shasum.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/shasum
%dir %{perl_vendorarch}/Digest/
%{perl_vendorarch}/Digest/SHA.pm
%dir %{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/auto/Digest/SHA/

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 5.44-1
- Updated to release 5.44.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 5.43-1
- Updated to release 5.43.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 5.32-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 15 2005 Dag Wieers <dag@wieers.com> - 5.32-1
- Initial package. (using DAR)
