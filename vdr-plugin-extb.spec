
%define plugin	extb
%define name	vdr-plugin-%plugin
%define version	0.2.14
%define rel	4

Summary:	VDR plugin: control the extb board
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://deltab.de/vdr/extb.html
Source:		http://deltab.de/vdr/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
The extb plugin controls the VDR Extension Board.

%prep
%setup -q -n %plugin-%version

%vdr_plugin_params_begin %plugin
# sets the lirc-device to other device than /dev/lircd
var=LIRCDEV
param=--device=LIRCDEV
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY contrib wakeup


