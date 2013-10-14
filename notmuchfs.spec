%global commit 414cd8e29e6a3d22a4af9c984eab1c76f8087c9a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           notmuchfs
Version:        0
Release:        1%{?dist}.20130928git%{shortcommit}
Summary:        A virtual maildir file system for notmuch queries

License:        GPL
URL:            https://github.com/tsto/notmuchfs
Source0:        https://github.com/tsto/notmuchfs/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  notmuch-devel
BuildRequires:	fuse-devel

Requires:	fuse

%description
Notmuchfs implements a virtual file system which creates maildirs from notmuch
mail query results. This is useful for using notmuch with tools which are not
aware of notmuch, only maildirs - such as mutt.

%prep
%setup -q -n %{name}-%{commit}


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 notmuchfs $RPM_BUILD_ROOT%{_bindir}/


%files
%doc AUTHORS COPYING COPYING-GPL-3 INSTALL ISSUES README*
%{_bindir}/notmuchfs

%changelog
* Sat Sep 28 2013 Lars Kellogg-Stedman <lars@redhat.com> - 0.20130928git414cd8e
- initial package build

