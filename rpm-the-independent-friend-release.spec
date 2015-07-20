Name: rpm-the-independent-friend-release
Summary: A yum configuration for the rpm repo https://pm.the-independent-friend.de
Version: 1
Group: yum
License: MIT
Release: 1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
URL: https://github.com/OlafRadicke/rpm-the-independent-friend-release
BuildArch: noarch


%description
A yum configuration for the rpm repo https://pm.the-independent-friend.de

#%prep

#%build

%install

#rm -Rvf %{_builddir}/*
if [ $1 -eq 1 ]; then
    echo "First install"
else
    echo "Upgrade"
fi


mkdir -p %{buildroot}/etc/yum.repos.d/
echo "[%{name}]"                                     > %{buildroot}/etc/yum.repos.d/%{name}.repo
echo "name=%{name}"                                  > %{buildroot}/etc/yum.repos.d/%{name}.repo
echo "baseurl=https://pm.the-independent-friend.de/" > %{buildroot}/etc/yum.repos.d/%{name}.repo
echo "gpgcheck=0"                                    > %{buildroot}/etc/yum.repos.d/%{name}.repo


%post
if [ $1 -eq 1 ]; then
    echo "First install"
else
    echo "Upgrade"
fi



%clean
# rm -Rvf /tmp/master.zip /tmp/cxxtools-master
#rm -fr $RPM_BUILD_ROOT
rm -Rvf %{_builddir}/*
%postun

%files
/etc/yum.repos.d/%{name}.repo


%changelog
* Mon Jul 20 2015 briefkasten@olaf-radicke.de - 1.1
- Init-Version.

