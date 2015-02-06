%define plugin	extb

Summary:	VDR plugin: control the extb board
Name:		vdr-plugin-%plugin
Version:	0.3.1
Release:	6
Group:		Video
License:	GPL
URL:		http://deltab.de/
Source:		vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
The extb plugin controls the VDR Extension Board.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# sets the lirc-device to other device than /dev/lircd
var=LIRCDEV
param=--device=LIRCDEV
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY contrib wakeup


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.3.1-4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.3.1-3mdv2009.1
+ Revision: 359314
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.3.1-2mdv2009.0
+ Revision: 197926
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 197618
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.2.14-6mdv2008.1
+ Revision: 145091
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.2.14-5mdv2008.1
+ Revision: 103091
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 4mdv2008.0-current
+ Revision: 49997
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.2.14-3mdv2008.0
+ Revision: 42083
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.2.14-2mdv2008.0
+ Revision: 22752
- rebuild for new vdr


* Fri Mar 02 2007 Anssi Hannula <anssi@mandriva.org> 0.2.14-1mdv2007.0
+ Revision: 130879
- 0.2.14

* Fri Dec 08 2006 Anssi Hannula <anssi@mandriva.org> 0.2.13-5mdv2007.1
+ Revision: 93600
- raise release
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.2.13-3mdv2007.1
+ Revision: 74005
- rebuild for new vdr
- Import vdr-plugin-extb

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.2.13-2mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.2.13-1mdv2007.0
- 0.2.13
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.2.12-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.2.12-2mdv2007.0
- rebuild for new vdr

* Tue Jul 11 2006 Anssi Hannula <anssi@mandriva.org> 0.2.12-1mdv2007.0
- initial Mandriva release

