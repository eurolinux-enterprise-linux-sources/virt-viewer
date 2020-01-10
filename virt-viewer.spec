# -*- rpm-spec -*-

# Default to skipping autoreconf.  Distros can change just this one line
# (or provide a command-line override) if they backport any patches that
# touch configure.ac or Makefile.am.
%{!?enable_autotools:%define enable_autotools 1}

%define with_gtk3 0
%if 0%{?fedora} >= 15
%define with_gtk3 1
%endif

%define with_spice 0
%if 0%{?fedora} >= 16
%define with_spice 1
%endif

%if 0%{?rhel} >= 6
%define with_spice 1
%endif

# spice-gtk is x86 x86_64 only currently:
%ifnarch %{ix86} x86_64
%define with_spice 0
%endif

Name: virt-viewer
Version: 0.5.6
Release: 8%{?dist}%{?extra_release}.3
Summary: Virtual Machine Viewer
Group: Applications/System
License: GPLv2+
URL: http://virt-manager.org/
Source0: http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
Patch1: 0001-Post-release-version-bump.patch
Patch2: 0002-Sync-spec-with-Fedora.patch
Patch3: 0003-remote-viewer-set-auto-conf-before-fullscreen.patch
Patch4: 0004-Do-not-restrict-disabling-display-to-0.patch
Patch5: 0005-misc-fix-typo.patch
Patch6: 0006-spice-make-sure-display-ready-hint-is-sync-after-cre.patch
Patch7: 0007-Allow-to-fullscreen-and-position-display-independent.patch
Patch8: 0008-Add-to-seperate-program-arguments-to-server-in-man-h.patch
Patch9: 0009-man-document-running-remote-viewer-without-URI.patch
Patch10: 0010-window-fix-send-key-menu-popup-position.patch
Patch11: 0011-window-leave-fullscreen-on-current-window.patch
Patch12: 0012-Only-fullscreen-the-new-window.patch
Patch13: 0013-window-wait-until-mapped-before-fullscreen.patch
Patch14: 0014-Remove-the-container-logic-used-by-legacy-browser-pl.patch
Patch15: 0015-Rename-variable-fix-gcc-warning.patch
Patch16: 0016-Silence-unused-arguments-warnings.patch
Patch17: 0017-Move-connect-dialog-to-remote-viewer.c.patch
Patch18: 0018-spice-session-use-a-more-robust-signal-connect.patch
Patch19: 0019-Show-connect-dialog-again-if-connection-from-dialog-.patch
Patch20: 0020-Fix-trivial-critical.patch
Patch21: 0021-app-move-display-on-client-monitors-with-full-screen.patch
Patch22: 0022-build-sys-add-debug-helper-rule.patch
Patch23: 0023-Use-a-more-descriptive-FileDescription.patch
Patch24: 0024-man-document-auto-conf-fullscreen-option.patch
Patch25: 0025-Support-Spice-controller-auto-display-res-flag.patch
Patch26: 0026-spec-Deprecate-spice-client.patch
Patch27: 0027-spec-Add-missing-in-if-0-fedora.patch
Patch28: 0028-ovirt-Set-host-subject-if-needed.patch
Patch29: 0029-Use-format-string.patch
Patch30: 0030-Fix-build-without-spice-gtk.patch
Patch31: 0031-Use-H-instead-of-h-for-the-short-hotkeys.patch
Patch32: 0032-data-remote-viewer.desktop-Fix-missing-trailing.patch
Patch33: 0033-Revert-Post-release-version-bump.patch
Patch34: 0034-virt-viewer-Allow-TLS-only-SPICE-connections.patch
Patch35: 0035-Unregister-events-and-callbacks-on-dispose.patch
Patch36: 0036-vnc-implement-release_cursor.patch
Patch37: 0037-app-always-use-maybe_quit.patch
Patch38: 0038-spice-show-an-error-dialog-if-password-is-invalid.patch
Patch39: 0039-Remove-debugging-leftover.patch
Patch40: 0040-display-add-fullscreen-property.patch
Patch41: 0041-window-set-display-fullscreen-state.patch
Patch42: 0042-Use-display-fullscreen-state-instead-of-app-state.patch
Patch43: 0043-window-move-window-again-after-fullscreen.patch
# Non upstream patch, CtrlAltDel propagation will be dropped
Patch44: 0044-Propagate-SEND_CAD-from-controller-to-SpiceSession.patch
Patch45: 0045-Fix-scaling-of-window-upon-resize.patch
Patch46: 0046-Fix-race-with-metacity-in-fullscreen.patch
# Non upstream patch
Patch47: 0047-set-auto-conf-when-fullscreen-is-set-in-vv-file.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: openssh-clients
Requires(post):   %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%if 0%{?enable_autotools}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: libtool
%endif

%if %{with_gtk3}
BuildRequires: gtk3-devel >= 3.0.0
%else
BuildRequires: gtk2-devel >= 2.20
Requires: gtk2 >= 2.20
%endif
BuildRequires: libvirt-devel >= 0.9.7
BuildRequires: libxml2-devel
%if %{with_gtk3}
BuildRequires: gtk-vnc2-devel >= 0.4.0
%else
BuildRequires: gtk-vnc-devel >= 0.3.8
%endif
%if %{with_spice}
%if %{with_gtk3}
BuildRequires: spice-gtk3-devel >= 0.20
%else
BuildRequires: spice-gtk-devel >= 0.20
%endif
BuildRequires: spice-protocol >= 0.10.1
%endif
BuildRequires: /usr/bin/pod2man
BuildRequires: intltool
Requires: glib2 >= 2.26

%description
Virtual Machine Viewer provides a graphical console client for connecting
to virtual machines. It uses the GTK-VNC or SPICE-GTK widgets to provide
the display, and libvirt for looking up VNC/SPICE server details.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1

%build

%if 0%{?enable_autotools}
autoreconf -if
%endif

%if %{with_spice}
%define spice_arg --with-spice-gtk
%else
%define spice_arg --without-spice-gtk
%endif

%if %{with_gtk3}
%define gtk_arg --with-gtk=3.0
%else
%define gtk_arg --with-gtk=2.0
%endif

%configure %{spice_arg} %{gtk_arg}
%__make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%__make install  DESTDIR=$RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_libexecdir}
touch %{buildroot}%{_libexecdir}/spice-xpi-client
install -m 0755 data/spice-xpi-client-remote-viewer %{buildroot}%{_libexecdir}/
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%{_sbindir}/update-alternatives --install %{_libexecdir}/spice-xpi-client \
  spice-xpi-client %{_libexecdir}/spice-xpi-client-remote-viewer 25

%postun
if [ $1 -eq 0 ] ; then
  /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
  %{_sbindir}/update-alternatives --remove spice-xpi-client %{_libexecdir}/spice-xpi-client-remote-viewer
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README COPYING AUTHORS ChangeLog NEWS
%{_bindir}/%{name}
%{_bindir}/remote-viewer
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ui/
%{_datadir}/%{name}/ui/virt-viewer.xml
%{_datadir}/%{name}/ui/virt-viewer-auth.xml
%{_datadir}/%{name}/ui/virt-viewer-about.xml
%{_datadir}/icons/hicolor/*/apps/*
%ghost %{_libexecdir}/spice-xpi-client
%{_libexecdir}/spice-xpi-client-remote-viewer
%{_mandir}/man1/virt-viewer.1*
%{_mandir}/man1/remote-viewer.1*
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/mime/packages/virt-viewer-mime.xml

%changelog
* Wed Apr 30 2014 Jonathon Jongsma <jjongsma@redhat.com> - 0.5.6-8.3
- Automatically adjust resolution when opened fullscreen via vv-file
  Resolves: rhbz#1092871

* Tue Apr 22 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.5.6-8.2
- Fix 2 monitors are in fullscreen at only one screen.
  Resolves: rhbz#1088921

* Tue Apr 15 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.5.6-8.1
- Screen is blurry for some resolutions when window is maximized
  Resolves: rhbz#1081376

* Fri Sep 13 2013 Christophe Fergeau <cfergeau@redhat.com> 0.5.6-8
- Re-add patch to propagate 'send-ctrlaltdel' setting from the controller
  to spice-gtk, this was dropped by mistake during the 6.5 rebase
  Resolves: rhbz#1007205

* Wed Aug 14 2013 Christophe Fergeau <cfergeau@redhat.com> 0.5.6-7
- Always ask for confirmation when quitting remote-viewer, even when in
  fullscreen (rhbz#905684)
- Show an error message when trying to use a wrong SPICE password
  (rhbz#990883)
- Make sure resolution higher than native can be set in fullscreen
  (rhbz#864929)

* Mon Jul 29 2013 Christophe Fergeau <cfergeau@redhat.com> 0.5.6-6
- Unregister events and callbacks on dispose, silence a libvirtd error when
  virt-viewer shuts down (rhbz#890297)

* Mon Jul 15 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.5.6-5
- can't connect guest display console if only SPICE TLS autoport
  specified (rhbz#982840)

* Wed Jul 10 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.5.6-4
- Require gtk+ >= 2.20 (rhbz#980344)

* Fri Jul 5 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.5.6-3
- Require gtk+ >= 2.20 (rhbz#980344)

* Thu Jul 4 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.5.6-2
- Use -H instead of -h for the short --hotkeys (rhbz#980846)
- remote-viewer.desktop: Fix missing trailing ;

* Thu Jun 27 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.5.6-1.el6_5
- Rebase to v0.5.6. Resolves: #961455
- Two monitors are in fullscreen at only one screen (rhbz#809546)
- Can't Change Resolution in Full Screen (rhbz#846127)
- Connection dialog should handle connection errors (rhbz#864026)
- Allow changing guest resolution when started in fullscreen (rhbz#864929)
- "Unable to connect to the graphic server" error on guest shutdown (rhbz#875697)
- Cannot change resolution when automatically resize is off (rhbz#908057)
- full-screen=auto-conf -- setting resolution in a loop (rhbz#908408)
- Send keys menu offset in fullscreen (rhbz#913601)
- Support connection file / MIME reigstration (rhbz#908805)
- Reuse existing 'displays' submenu (rhbz#856682)
- Window too small after switching off full-screen (rhbz#805146)
- Move display on client monitors with --full-screen (rhbz#876444)
- Make window titles configurable (rhbz#904091)
- Make hotkeys configurable from the cmdline (rhbz#904094)
- Guest will keep typing '~' after press F9 and F10 in same time (rhbz#820829)
- Fail to resume guest after do S3 (rhbz#870710)
- man: document auto-conf fullscreen option (rhbz#875559)
- Title bar of second form becomes invisible (rhbz#876445)
- man: document running remote-viewer without URI (rhbz#882133)
- Fix recent connections (rhbz#882134)
- Multi-monitors fixes (rhbz#888629)
- Add a "Do not ask me again" checkbox when closing app (rhbz#905684)
- Fix menu keyboard interaction (rhbz#924577)
- man: add -- to seperate program arguments (rhbz#843103)
- Press Enter to connect in dialog (rhbz#885106)
- Change of resolution switches previously disabled display back on (rhbz#958966)
- All "windows" have the same resolution in fullscreen (rhbz#886570)
- Removed plugin

* Wed Mar 20 2013 Hans de Goede <hdegoede@redhat.com> - 0.5.2-20
- Fix fullscreen resolution occasionally still being wrong (rhbz #886570)

* Wed Mar 13 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-19
- Fix window resolution in full screen (rhbz #886570)

* Tue Dec 11 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-18
- Fix resolution when switching to fullscreen (rhbz #881020)
- Ensure correct file extension on screenshots (rhbz #875126)

* Tue Dec  4 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-17
- Fix handling of AltGr+V in non-us keyboard layouts (rhbz #860669)

* Wed Oct 24 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-16
- Don't resize to 50x50 when toggling autoresize (rhbz #856610)
- Allow zooming beyond normal size (rhbz #856678)
- Allow changing resolution when in fullsreen (rhbz #864929)

* Wed Oct 24 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-15
- Fix crash starting remote-viewer from XPI plugin (rhbz #867459)
- Fix crash connecting with wrong spice password (rhbz #867248)

* Mon Oct 15 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-14
- Add support for multi-monitors per QXL device (rhbz #842305)

* Fri Oct 12 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-13
- Propagate ctrl-alt-del from spice controller (rhbz #865793)

* Fri Oct 12 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-12
- Use real binary name in help message (rhbz #814150)
- Correctly detect IPv6 any address (rhbz #832121)
- Add --title option to remote-viewer (rhbz #828339)
- Add newline at end of verbose info output (rhbz #822794)

* Mon Sep 24 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-11
- Rebuild for change in spice-gtk soname (rhbz #854318)

* Mon Sep 24 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-10
- Rebuild for change in spice-gtk soname (rhbz #854318)

* Mon May 21 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-9
- Use weak references on channel to ensure prompt finalization (rhbz #822683)

* Tue May  8 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-8
- Fix race condition in window dispose (rhbz #819436)

* Fri May  4 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-7
- Change to Ok to Close in USB redirection (rhbz #816280)
- Fix close of windows on guest shutdown (rhbz #816550)

* Mon Apr 23 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-6
- Fix scaling of windows on i386 arch (rhbz #810544)
- Support raw IPv6 addresses in URIs (rhbz #813375)
- Set remote-viewer application name (rhbz #814043)

* Tue Apr 17 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-5
- Raise priority of spice-xpi-client alternative to 25 (rhbz #813303)
- Add missing docs for --attach parameter (rhbz #811191)
- Fix typos in docs for --full-screen parameter (rhbz #811131)
- Fix usbredirect property usage (rhbz #807298)

* Wed Apr  4 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-4
- Fix close of VNC displays (rhbz #802673)
- Add usbredirect properties (rhbz #807298)
- Add properties to disable desktop effects (rhbz #808986)

* Wed Mar 21 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.5.2-3
- Add --full-screen=auto-conf to remote-viewer (rhbz #803297)
- Correctly handle switch-host Spice migration (rhbz #802574)
- Fix USB auto-share doesn't work in full-screen (rhbz #803834)

* Wed Mar 14 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-2
- Set initial focus state & initialize threads (rhbz #803077)
- Refresh translations (rhbz #797015)

* Fri Mar  9 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-1
- Update to 0.5.2 release
- Fix connect to password protected SPICE displays over SSH (rhbz #749759)
- Add SPICE smartcard support (rhbz #789090)
- Honour hot key configuration from SPICE controller (rhbz #795437)
- Refresh translations (rhbz #797015)
- Fix crash reconnecting to SPICE after guest restart (rhbz #797082)
- Add support for foreign menus with SPICE (rhbz #799038)

* Tue Feb 17 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.1-1
- Update to 0.5.1 release (rhbz #784920, #749723, #784922)

* Tue Feb 14 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.0-1
- Update to 0.5.0 release (rhbz #784920, #749723, #784922)

* Tue Jan 31 2012 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-9
- Rebuild for spice-gtk soname change (rhbz #784536)

* Wed Oct 12 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-7
- Fix initial window title when waiting for guest (rhbz #744374)
- Fix detection of SPICE pointer grabs to update title (rhbz #744377)
- Fix incorrect key sequence for C-A-F9/10/11/12 (rhbz #744370)

* Wed Sep 28 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-6
- Fix crash when using UNIX domain sockets (rhbz #740724)

* Mon Sep 19 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-5
- Fix zoom level on non-primary monitors (rhbz #730901)
- Fix missing domain name in window title (rhbz #739007)
- Don't crash if URI parsing fails (rhbz #734769)
- Fix direct connection to VMs using a wildcard address (rhbz #730911)

* Thu Aug 18 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-4
- Fix initial zoom level setting (rhbz #730901)
- Fix potential deadlock in event callback (rhbz #731132)

* Sun Aug 14 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-3
- More fixes for ssh port tunnelling (rhbz #730346)

* Fri Aug 12 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-2
- Fix ssh port tunnelling (rhbz #730346)

* Thu Aug  4 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-1
- Update to 0.4.1 release for SPICE multihead (rhbz #680213)

* Mon Jul 25 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.0-2
- Enable SPICE in RHEL-6 (rhbz #680213)

* Tue Jul 12 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.0-1
- Update to 0.4.0 release (rhbz #680213, #680331)

* Thu Feb  3 2011 Daniel P. Berrange <berrange@redhat.com> - 0.2.1-3
- Add support for UNIX sockets (rhbz #651604)
- Fix wait for VMs based on UUID (rhbz #631667)

* Tue Jun  8 2010 Daniel P. Berrange <berrange@redhat.com> - 0.2.1-2
- Add translated po files for all available languages (rhbz #510231)

* Fri Jan 15 2010 Daniel P. Berrange <berrange@redhat.com> - 0.2.1-1
- Update to 0.2.1 release with i18n support (rhbz #510231)

* Fri Nov 13 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.2.0-1.1
- Fix conditional for RHEL

* Wed Jul 29 2009 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-1.fc12
- Update to 0.2.0 release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Daniel P. Berrange <berrange@redhat.com> - 0.0.3-5.fc12
- Fix auth against libvirt (rhbz #499594)
- Fix confusion of VNC credentials (rhbz #499595)
- Correct keyboard grab handling (rhbz #499362)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.3-3.fc10
- fix conditional comparison
- remove file dep

* Wed Jun 25 2008 Daniel P. Berrange <berrange@redhat.com> - 0.0.3-2.fc10
- Rebuild for GNU TLS ABI bump

* Mon Mar 10 2008 Daniel P. Berrange <berrange@redhat.com> - 0.0.3-1.fc9
- Updated to 0.0.3 release

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.2-4
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Daniel P. Berrange <berrange@redhat.com> - 0.0.2-3.fc9
- Set domain name as window title
- Hide input for passwd fields during auth

* Mon Oct 15 2007 Daniel P. Berrange <berrange@redhat.com> - 0.0.2-2.fc8
- Change TLS x509 credential name to sync with libvirt

* Tue Aug 28 2007 Daniel P. Berrange <berrange@redhat.com> - 0.0.2-1.fc8
- Added support for remote console access

* Fri Aug 17 2007 Daniel P. Berrange <berrange@redhat.com> - 0.0.1-2.fc8
- Restrict built to x86 & ia64 because libvirt is only on those arches

* Wed Aug 15 2007 Daniel P. Berrange <berrange@redhat.com> - 0.0.1-1.fc8
- First release

