Name:           perl-GDGraph
Version:        1.44
Release:        7%{?dist}
Epoch:          1
Summary:        Graph generation package for Perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/GDGraph/
Source0:        http://www.cpan.org/authors/id/B/BW/BWARFIELD/GDGraph-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(GD), perl(GD::Text)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
%{summary}.


%prep
%setup -q -n GDGraph-%{version}
%{__perl} -pi -e 's{^#!/usr/local/bin/perl\b}{#!%{__perl}}' samples/sample1A.pl
%{__perl} -pi -e 's/\r\n/\n/' samples/sample64.pl


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES README samples/
%{perl_vendorlib}/GD/
%{_mandir}/man3/*.3pm*


%changelog
* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1:1.44-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.44-4
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.44-3
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.44-2.2
- add BR: perl(Test::More)

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.44-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sat Jun  9 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:1.44-2
- Bumping release (due to dist tag mismatches).

* Sat May  5 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:1.44-1
- Update to 1.44.

* Thu May 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4308-1
- Update to 1.4308.

* Mon Feb 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4307-1
- Update to 1.4307.

* Mon Feb  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4306-1
- Update to 1.4306.

* Thu Dec 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4305-1
- Update to 1.4305.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.43-4
- rebuilt

* Sun Jul 11 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.43-0.fdr.3
- Unowned directory: %%{perl_vendorlib}/GD (see bug 1800 comment #1).

* Wed Jun 30 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.43-0.fdr.2
- Bring up to date with current fedora.us perl spec template.
- Added the samples directory to the documentation files.

* Sun Oct 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.43-0.fdr.1
- First build.
