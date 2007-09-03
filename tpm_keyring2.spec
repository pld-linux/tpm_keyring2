Summary:	TPM Keyring - A key manager for TPM based eCryptfs keys
Summary(pl.UTF-8):	TPM Keyring - zarządca kluczy do kluczy eCryptfs opartych na TPM
Name:		tpm_keyring2
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/trousers/%{name}-%{version}.tar.gz
# Source0-md5:	b7d72616a4bf7ad7893b13ffcba8e0a5
URL:		http://trousers.sourceforge.net/tpm_keyring2/quickstart.html
BuildRequires:	openssl-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	swig-python
BuildRequires:	trousers-devel
Requires:	%{_fontsdir}/TTF
Requires(post,postun):	fontpostinst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TPM Keyring is a key manager for TPM based eCryptfs keys.

%description -l pl.UTF-8
TPM Keyring to zarządca kluczy do kluczy eCryptfs opartych na TPM.

%prep
%setup -q

%build
%{__make} \
	OPTS="%{rpmcflags} -Wall" \
	PYTHON_INCLUDES="%{rpmcflags} -I%{py_incdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_bindir},%{_fontsdir}/TTF}

%{__make} install \
	PYTHON_INSTALL_DEST=$RPM_BUILD_ROOT%{py_sitedir} \
	TPM_KEYRING_INSTALL_DEST=$RPM_BUILD_ROOT%{_bindir} \
	DOCS_INSTALL_DEST=`pwd`/docs

install -D sandoval.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc BUGS README TODO doc
%attr(755,root,root) %{_bindir}/tpm_keyring
%attr(755,root,root) %{py_sitedir}/_tpm_keyring_util.so
%{py_sitedir}/tpm_keyring_util.py[co]
%{_fontsdir}/TTF/sandoval.ttf
