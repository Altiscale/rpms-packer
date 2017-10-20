%global debug_package %{nil}

name: packer
version: 1.1.1
release: 3%{?dist}
summary: build automated machine images
group: development/tools
license: mplv2.0
url: https://www.packer.io/

source0: https://releases.hashicorp.com/packer/%{version}/packer_%{version}_linux_amd64.zip

%description
packer is a tool for creating machine and container images for multiple platforms from a single source configuration.

%prep

%setup -c

%build

%install
echo 'PATH=/opt/packer/bin:$PATH' > %{_tmppath}/packer.sh
install -Dp -m 0755  %{_builddir}/%{name}-%{version}/%{name} %{buildroot}/opt/packer/bin/%{name}
install -D -m 0644  %{_tmppath}/packer.sh %{buildroot}/etc/profile.d/packer.sh
mkdir -p %{buildroot}/%{_bindir}
ln -s /opt/packer/bin/%{name} %{buildroot}/%{_bindir}

%files
/opt/packer
/opt/packer/*
/etc/profile.d/packer.sh
/usr/bin/%{name}

%changelog
 * Tue Oct 20 2017 Karthik <karthik@altiscale.com> 1.1.1-2
  - for non-login shell
 * Tue Oct 17 2017 Karthik <karthik@altiscale.com> 1.1.1-2
  - Use install command
