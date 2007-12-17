Name:		pam_ssh
Version:	1.91
Release:	%mkrel 3
Summary:	A Pluggable Authentication Module (PAM) for use with SSH
Source0:	http://belnet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		pam_ssh-1.91-fix-missing-headers.patch.bz2
URL:		http://sourceforge.net/projects/pam-ssh/
License:	BSD
Group:		System/Libraries
Requires:	openssh
BuildRequires:	pam-devel 
BuildRequires:  openssl-devel
BuildRequires:  openssh-clients
BuildRequires:	autoconf2.5


%description
This PAM module provides single sign-on behavior for UNIX using SSH. Users
are authenticated by decrypting their SSH private keys with the password
provided (probably to XDM). In the PAM session phase, an ssh-agent process is
started and keys are added.

%prep
%setup -q
%patch0 -p1 -b .fix_headers

%build
%configure2_5x --with-pam-dir=/%_lib/security
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README ChangeLog TODO
/%{_lib}/security/pam_ssh.*
%{_mandir}/man[^3]/pam_ssh*

