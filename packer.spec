%global debug_package %{nil}

name: packer
version: 1.1.1
release: 1%{?dist}
summary: build automated machine images
group: development/tools
license: mplv2.0
url: https://www.packer.io/

source0: https://releases.hashicorp.com/packer/1.1.1/packer_%{version}_linux_amd64.zip

%description
packer is a tool for creating machine and container images for
multiple platforms from a single source configuration.

%prep

%setup -c

%build

%install
mkdir -p %{buildroot}/opt/packer/bin
mkdir -p %{buildroot}/etc/profile.d
echo 'PATH=/opt/packer/bin:$PATH' > %{buildroot}/etc/profile.d/packer.sh
cp %{_builddir}/%{name}-%{version}/%{name} %{buildroot}/opt/packer/bin/%{name}

%files
/opt/packer
/opt/packer/*
/etc/profile.d/packer.sh
