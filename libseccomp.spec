Summary:	High level interface to the Linux Kernel's seccomp filter
Name:		libseccomp
Version:	2.1.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libseccomp/%{name}-%{version}.tar.gz
# Source0-md5:	1f41207b29e66a7e5e375dd48a64de85
Patch0:		%{name}-pc.patch
URL:		http://libseccomp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libseccomp library provides and easy to use, platform independent,
interface to the Linux Kernel's syscall filtering mechanism: seccomp.
The libseccomp API is designed to abstract away the underlying BPF
based syscall filter language and present a more conventional
function-call based filtering interface that should be familiar to,
and easily adopted by application developers.

%package devel
Summary:	Header files for Seccomp library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Seccomp library.

%prep
%setup -q
%patch0 -p1

%build
export GCC="%{__cc}"
export CFLAGS="%{rpmcflags}"
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README
%attr(755,root,root) %{_bindir}/scmp_sys_resolver
%attr(755,root,root) %ghost %{_libdir}/libseccomp.so.2
%attr(755,root,root) %{_libdir}/libseccomp.so.*.*.*
%{_mandir}/man1/scmp_sys_resolver.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libseccomp.so
%{_includedir}/seccomp.h
%{_pkgconfigdir}/libseccomp.pc
%{_mandir}/man3/seccomp_*.3*

