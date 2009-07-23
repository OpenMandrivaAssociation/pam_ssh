Name:		pam_ssh
Version:	1.97
Release:	%mkrel 1
Summary:	A Pluggable Authentication Module (PAM) for use with SSH
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/pam-ssh/
License:	BSD
Group:		System/Libraries
Requires:	openssh
BuildRequires:	pam-devel 
BuildRequires:  openssl-devel
BuildRequires:  openssh-clients
BuildRequires:	autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
This PAM module provides single sign-on behavior for UNIX using SSH. Users
are authenticated by decrypting their SSH private keys with the password
provided (probably to XDM). In the PAM session phase, an ssh-agent process is
started and keys are added.

%prep
%setup -q

%build
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

