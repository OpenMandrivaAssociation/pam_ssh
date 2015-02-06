Name:		pam_ssh
Version:	1.97
Release:	4
Summary:	A Pluggable Authentication Module (PAM) for use with SSH
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/pam-ssh/
License:	BSD
Group:		System/Libraries
Requires:	openssh
BuildRequires:	pam-devel 
BuildRequires:  openssl-devel
BuildRequires:  openssh-clients
BuildRequires:	autoconf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
This PAM module provides single sign-on behavior for UNIX using SSH. Users
are authenticated by decrypting their SSH private keys with the password
provided (probably to XDM). In the PAM session phase, an ssh-agent process is
started and keys are added.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x --with-pam-dir=/%_lib/security
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README ChangeLog TODO
/%{_lib}/security/pam_ssh.*
%{_mandir}/man[^3]/pam_ssh*



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.97-3mdv2011.0
+ Revision: 614472
- the mass rebuild of 2010.1 packages

* Thu Apr 15 2010 Funda Wang <fwang@mandriva.org> 1.97-2mdv2010.1
+ Revision: 535072
- rebuild

* Thu Jul 23 2009 Frederik Himpe <fhimpe@mandriva.org> 1.97-1mdv2010.0
+ Revision: 399096
- Update to new version 1.97
- Remove patch integrated upstream

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.91-5mdv2009.0
+ Revision: 254999
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.91-3mdv2008.1
+ Revision: 141036
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import pam_ssh


* Sun Jun 18 2006 Pascal Terjan <pterjan@mandriva.org> 1.91-3mdv2007.0
- use autoconf2.5
- go to the right place on x86_64

* Sun Apr 23 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.91-2mdk
- Add BuildRequires

* Sat Apr 22 2006 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 1.91-1mdk
- fix buildrequires
- add missing headers (P0)
- cleanup package uploaded by Hawkwind (SoS)

* Mon Mar 15 2004 Patrice Dumas <pertusus@free.fr> 0:1.9-0.fdr.1
- Use fedora-newrpmspec to update the spec file

* Fri Aug 16 2002 Dumas Patrice <dumas@centre-cired.fr>
- Initial build.
