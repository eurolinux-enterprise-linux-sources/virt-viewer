# -*- rpm-spec -*-

# Default to skipping autoreconf.  Distros can change just this one line
# (or provide a command-line override) if they backport any patches that
# touch configure.ac or Makefile.am.
%{!?enable_autotools:%define enable_autotools 1}

%define with_gtk3 0
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%define with_gtk3 1
%endif

%define with_spice 0
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 6
%define with_spice 1
%endif

%define with_govirt 0
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 6
%define with_govirt 1
%endif

# spice-gtk is x86 x86_64 only currently:
%ifnarch %{ix86} x86_64
%define with_spice 0
%endif

Name: virt-viewer
Version: 2.0
Release: 18%{?dist}%{?extra_release}
Summary: Virtual Machine Viewer
Group: Applications/System
License: GPLv2+
URL: http://virt-manager.org/
Source0: http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
Patch1: 0001-foreign-menu-Fix-build-with-GLib-older-than-2.32.patch
Patch2: 0002-Fix-crash-when-trying-to-connect-to-VNC-display.patch
Patch3: 0003-Take-direct-into-consideration-when-checking-if-a-gu.patch
Patch4: 0004-Update-geometry-when-enabling-disabling-displays.patch
Patch5: 0005-VirtViewerApp-create-main-window-after-constructor.patch
Patch6: 0006-Use-constructed-vfunc-instead-of-constructor.patch
Patch7: 0007-Monitor-config-at-sometimes-leaves-additional-monito.patch
Patch8: 0008-virt-viewer-Bring-back-debug-log-about-nonexistent-g.patch
Patch9: 0009-foreign-menu-Don-t-show-empty-foreign-menu-on-second.patch
Patch10: 0010-Do-not-add-https-and-api-to-oVirt-URI.patch
Patch11: 0011-Revert-display-vnc-fix-zoom-level-set-by-command-lin.patch
Patch12: 0012-virt-viewer-Add-a-GError-arg-to-extract_connect_info.patch
Patch13: 0013-virt-viewer-Add-a-GError-arg-to-update_display.patch
Patch14: 0014-virt-viewer-app-Add-a-GError-arg-to-create_session.patch
Patch15: 0015-virt-viewer-app-create_session-should-return-a-boole.patch
Patch16: 0016-virt-viewer-Avoid-simple_message_dialog-when-errors-.patch
Patch17: 0017-remote-viewer-Avoid-simple_message_dialog-when-error.patch
Patch18: 0018-virt-viewer-Do-not-wait-for-a-guest-that-will-never-.patch
Patch19: 0019-virt-viewer-app-Do-not-show-error-dialog-twice-for-u.patch
Patch20: 0020-Use-ZOOM-constants-instead-of-numbers.patch
Patch21: 0021-virt-viewer-display-Use-MIN_DISPLAY_WIDTH-HEIGHT-ins.patch
Patch22: 0022-virt-viewer-window-Change-zoom-of-the-display-only-w.patch
Patch23: 0023-virt-viewer-window-Set-zoom-when-display-is-enabled-.patch
Patch24: 0024-virt-viewer-window-Return-early-when-zoom-of-window-.patch
Patch25: 0025-display-spice-Do-not-ignore-change-of-position.patch
Patch26: 0026-virt-viewer-main-Require-domain-name-as-argument-for.patch
Patch27: 0027-virt-viewer-app-Set-hotkeys-when-app-is-constructed.patch
Patch28: 0028-Revert-virt-viewer-main-Require-domain-name-as-argum.patch
Patch29: 0029-virt-viewer-main-wait-should-not-be-used-without-dom.patch
Patch30: 0030-virt-viewer-window-Allow-any-zoom-level-for-vnc.patch
Patch31: 0031-virt-viewer-window-Make-sure-that-minimum-zoom-level.patch
Patch32: 0032-virt-viewer-window-Set-initial-zoom-only-once.patch
Patch33: 0033-ovirt-Add-support-for-an-admin-key-in-vv-file.patch
Patch34: 0034-Enable-hotkeys-after-setting-them-in-virt_viewer_app.patch
Patch35: 0035-virt-viewer-set-keepAlive-on-libvirt-connection.patch
Patch36: 0036-Remove-unnecessary-parameter-from-virt_viewer_window.patch
Patch37: 0037-virt-viewer-window-Allow-to-resize-window-to-any-siz.patch
Patch38: 0038-events-ensure-event-callbacks-are-threadsafe.patch
Patch39: 0039-events-register-event-using-GOnce-to-avoid-multiple-.patch
Patch40: 0040-events-remove-timeout-and-handle-from-arrays.patch
Patch41: 0041-glib-compat-Use-g_new0-GMutex-1-if-GLib-2.31.patch
Patch42: 0042-events-allow-zero-timeouts-for-timer.patch
Patch43: 0043-events-remove-unused-virt_viewer_events_find_-handle.patch
Patch44: 0044-events-protect-handles-and-timeouts-against-concurre.patch
Patch45: 0045-events-don-t-reschedule-deleted-timeouts-watches.patch
Patch46: 0046-events-don-t-hold-events-lock-when-dispatching-free-.patch
Patch47: 0047-events-don-t-create-glib-IO-watch-for-disabled-handl.patch
Patch48: 0048-events-allow-to-remove-disabled-timers-and-handles.patch
Patch49: 0049-events-don-t-leak-GIOChannel-when-destroying-IO-hand.patch
Patch50: 0050-Exit-normally-when-canceling-dialog.patch
Patch51: 0051-Clear-GError-in-cleanup-section.patch
Patch52: 0052-Report-errors-in-one-place.patch
Patch53: 0053-virt-viewer-Clean-up-if-no-vm-was-chosen.patch
Patch54: 0054-virt-viewer-Fix-choose-VM-dialog-alt-tab-in-gnome2.patch
Patch55: 0055-Set-enabled-status-of-all-displays-when-we-get-a-mon.patch
Patch56: 0056-app-Add-helper-for-number-of-client-monitors.patch
Patch57: 0057-app-Do-not-map-display-to-non-existent-monitor.patch
Patch58: 0058-session-spice-Disable-extra-displays-in-fullscreen-m.patch
Patch59: 0059-Fix-virt-viewer-reconnect-crash-with-SPICE-VMs.patch
Patch60: 0060-Switch-over-to-use-zanata-for-managing-translations.patch
Patch61: 0061-Refresh-translations-from-zanata.patch
Patch62: 0062-ovirt-Take-into-account-SPICE-proxy.patch
Patch63: 0063-virt-viewer-display-vnc-Set-guest-name-when-using-VN.patch
Patch64: 0064-virt-viewer-display-vnc-Set-uuid-when-using-VNC.patch
Patch65: 0065-Fix-crash-when-disabling-last-enabled-display.patch
Patch66: 0066-build-sys-Don-t-substitute-buildid-when-it-was-not-s.patch
Patch67: 0067-build-sys-Always-prepend-to-BUILDID.patch
Patch68: 0068-vv-file-Move-version-checking-code-in-its-own-functi.patch
Patch69: 0069-vv-file-Refactor-virt_viewer_file_check_min_version.patch
Patch70: 0070-vv-file-Add-VirtViewerFile-versions.patch
Patch71: 0071-build-sys-Add-with-osid.patch
Patch72: 0072-Show-osid-in-remote-viewer-version.patch
Patch73: 0073-vv-file-Use-versions-in-min-version-check.patch
Patch74: 0074-util-Replace-virt_viewer_compare_version-with-_compa.patch
Patch75: 0075-test-Add-test-case-for-virt_viewer_compare_buildid.patch
Patch76: 0076-vv-file-Add-newer-version-url-key-to-.vv-files.patch
Patch77: 0077-vv-file-Show-newer-version-url-when-version-check-fa.patch
Patch78: 0078-display-set-min-value-for-desktop-width-height-props.patch
Patch79: 0079-display-Set-useful-values-for-MIN_DISPLAY_-WIDTH-HEI.patch
Patch80: 0080-Use-the-display-ID-to-configure-fullscreen-monitors.patch
Patch81: 0081-session-Only-create-a-hashtable-if-apply_monitor_geo.patch
Patch82: 0082-util-Fix-the-size-of-sorted_displays-allocation.patch
Patch83: 0083-app-Return-early-on-empty-monitor-mapping.patch
Patch84: 0084-Refresh-translations-from-Zanata.patch
Patch85: 0085-ovirt-Only-use-active-ISO-domains-for-foreign-menu.patch
Patch86: 0086-ovirt-Allow-to-cancel-authentication-without-showing.patch
Patch87: 0087-app-window-Set-display-menu-not-sensitive-when-neede.patch
Patch88: 0088-virt-viewer-Set-toolbar-buttons-not-sensitive-when-n.patch
Patch89: 0089-app-Do-not-show-usbredir-button-without-session.patch
Patch90: 0090-remote-viewer-GtkRecentChooserWidget-is-not-suitable.patch
Patch91: 0091-remote-viewer-Use-a-different-mnemonic-for-Connectio.patch
Patch92: 0092-Add-some-missing-mnemonics-to-menu-items.patch
Patch93: 0093-Add-mnemonics-for-each-display-item.patch
Patch94: 0094-spice-avoid-crashing-when-using-invalid-video-config.patch
Patch95: 0095-monitor-alignment-Do-not-crash-on-NULL-display.patch
Patch96: 0096-spice-vv-file-do-not-ignore-usb-filter.patch
Patch97: 0097-Move-monitor-mapping-parsing-from-app-to-util.patch
Patch98: 0098-virt_viewer_parse_monitor_mappings-Add-parameter-for.patch
Patch99: 0099-test-Add-tests-for-monitor-mapping.patch
Patch100: 0100-app-Use-debug-to-inform-about-smartcard-shortcuts-st.patch
Patch101: 0101-app-Check-validity-of-hotkey.patch
Patch102: 0102-app-Inform-user-about-connection-failure.patch
Patch103: 0103-Fix-format-of-italien-translation.patch
Patch104: 0104-Refresh-translations.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: openssh-clients
Requires(post):   %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

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
BuildRequires: spice-gtk3-devel >= 0.22
%else
BuildRequires: spice-gtk-devel >= 0.22
%endif
BuildRequires: spice-protocol >= 0.10.1
%endif
BuildRequires: /usr/bin/pod2man
BuildRequires: intltool
Requires: glib2 >= 2.26
%if %{with_govirt}
BuildRequires: libgovirt-devel >= 0.3.2
BuildRequires: rest-devel >= 0.7.92-3
%endif

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
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
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

%if %{with_govirt}
%define govirt_arg --with-ovirt
%endif

%configure %{spice_arg} %{gtk_arg} %{govirt_arg} --with-buildid=%{release} --disable-update-mimedb --with-osid=rhel%{?rhel}
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
update-desktop-database -q %{_datadir}/applications
%{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null

%postun
if [ $1 -eq 0 ] ; then
  /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
  %{_sbindir}/update-alternatives --remove spice-xpi-client %{_libexecdir}/spice-xpi-client-remote-viewer
fi
update-desktop-database -q %{_datadir}/applications
%{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null

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
%{_datadir}/%{name}/ui/virt-viewer-guest-details.xml
%{_datadir}/%{name}/ui/virt-viewer-vm-connection.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/devices/*
%ghost %{_libexecdir}/spice-xpi-client
%{_libexecdir}/spice-xpi-client-remote-viewer
%{_mandir}/man1/virt-viewer.1*
%{_mandir}/man1/remote-viewer.1*
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/mime/packages/virt-viewer-mime.xml

%changelog
* Tue Dec 13 2016 Pavel Grunt <pgrunt@redhat.com> - 2.0-18
- Rebuild with required rest dependency
  Resolves: rhbz#1318575

* Thu Oct 20 2016 Pavel Grunt <pgrunt@redhat.com> - 2.0-17
- Refresh translation
  Resolves: rhbz#1316354

* Tue Oct 11 2016 Pavel Grunt <pgrunt@redhat.com> - 2.0-16
- Inform about unix socket connection failure
  Resolves: rhbz#1377214
- Fix format of displayed string for it_IT
  Resolves: rhbz#1325127

* Fri Sep 16 2016 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 2.0-15
- Only use active ISO domains for foreign menu
  Resolves: rhbz#1313376
- Allow to cancel authentication without showing error dialog
  Resolves: rhbz#1318575
- Set display menu not sensitive when needed
  Resolves: rhbz#1360253
- Set toolbar buttons not sensitive when needed
  Resolves: rhbz#1360253
- Do not show usbredir button without session
  Resolves: rhbz#1360253
- GtkRecentChooserWidget is not suitable for mnemonic activation
  Related: rhbz#1351562
- Use a different mnemonic for Connection Address widget
  Related: rhbz#1351562
- Add some missing mnemonics to menu items
  Resolves: rhbz#1351890
- Add mnemonics for each display item
  Resolves: rhbz#1351890
- Avoid crashing when using invalid video config
  Resolves: rhbz#1310974
- Do not crash on NULL display
  Resolves: rhbz#1310974
- Do not ignore usb-filter in vv-file
  Resolves: rhbz#1327525
- Add parameter for client monitors in monitor-mapping
  Resolves: rhbz#1351881
- Use debug to inform about smartcard shortcuts state
  Related: rhbz#1351876
- Check validity of hotkey
  Resolves: rhbz#1351876

* Fri Mar 04 2016 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-14
- Monitor mapping doesn't properly adjust resolutions
  Resolves: rhbz#1309234
- Return early on empty monitor mapping
  Resolves: rhbz#1304648
- Update translations
  Resolves: rhbz#1194474

* Fri Jan 22 2016 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-13
- Use --with-buildid for RHEL6 builds
  Resolves: rhbz#1300639
- Set useful values for MIM_DISPLAY_{WIDTH,HEIGHT} and use them for
  desktop-{width,height} properties.
  Resolves: rhbz#1296878

* Thu Jan 07 2016 Jonathon Jongsma <jjongsma@redhat.com> - 2.0-12
- The last change was incomplete. We need to define the OSID for the build in
  order for the minum version check to work properly.
  Resolves: rhbz#1295944

* Tue Jan 05 2016 Jonathon Jongsma <jjongsma@redhat.com> - 2.0-11
- Add minimum version check to rhev spice-client
  Resolves: rhbz#1295944

* Sat Jan 02 2016 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-10
- Set guest name/uuid when using VNC
  Resolves: rhbz#1293878
- Fix crash when disabling last enabled display
  Resolves: rhbz#1294937

* Fri Dec 18 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-9
- Update translations
  Resolves: rhbz#1194474
- Add support for proxy-uri libgovirt property
  Resolves: rhbz#1292765

* Wed Dec  9 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-8
- Set initial zoom only once
  Related: rhbz#1221501
- Add 'admin' key to [ovirt] .vv file section
  Resolves: rhbz#1289969
- Shortcuts missing from "Send key" menu  when started using plugin
  Resolves: rhbz#1230603
- Set keepAlive on libvirt connection
  Resolves: rhbz#1289971
- Allow resize windows to any size
  Resolves: rhbz#1289972 and rhbz#1221501
- Update virt-viewer-events.c to match libvirt-glib's event file
  Resolves: rhbz#1246395
- Error message continuously popping out when stopping libvirtd
  Resolves: rhbz#1285163
- Fix choose VM dialog alt-tab in gnome2
  Resolves: rhbz#1223285
- Disable extra displays in fullscreen mode
  Resolves: rhbz#1212802
- Fix virt-viewer --reconnect crash with SPICE VMs
  Resolves: rhbz#1287462

* Tue May 12 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-7
- Allow any zoom level for VNC connections
  Resolves: rhbz#1211216
- Make sure that minimum zoom level is lower than NORMAL_ZOOM_LEVEL
  Related: rhbz#1206460

* Tue Apr 14 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-6
- Fix command-line API breakage
  Related: rhbz#1209398

* Fri Apr 10 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-5
- Clean up on connection's errors treatment
  Related: rhbz#1085216
- Zooming out changes display resolution of spice guest
  Resolves: rhbz#1206460
- Virtual desktops, mouse actions goes to wrong display
  Resolves: rhbz#1206216
- virt-viewer --wait option should require a domain name
  Resolves: rhbz#1209398
- virt-viewer set hotkeys for release-cursor doesn't work
  Resolves: rhbz#1206106

* Tue Mar 24 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-4
- Take --direct into consideration when checking if a guest is reachable
  Resolves: rhbz#1085216
- Update geometry when enabling/disabling displays
  Resolves: rhbz#1111425
- Monitor config at sometimes leaves additional monitors enabled
  Resolves: rhbz#1200750
- Bring back debug log about nonexistent guest
  Resolves: rhbz#1201177
- Don't show empty foreign menu on secondary displays
  Resolves: rhbz#1201605
- Do not add "https://" and "/api" to oVirt URI
  Resolves: rhbz#1201599
- Fix tiny window when opening a vnc guest
  Resolves: rhbz#1201679

* Tue Mar 10 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-3
- Fix crash when trying to connect to VNC dusplay
  Resolves: rhbz#1196517

* Fri Feb 20 2015 Jonathon Jongsma <jjongsma@redhat.com> - 2.0-2
- enable ovirt support
  Resolves: rhbz#975834

* Tue Jan 06 2015 Jonathon Jongsma <jjongsma@redhat.com> - 2.0-1
- Rebase to 2.0 release
  Resolves: rhbz#1179477, rhbz#1108523, rhbz#1085216, rhbz#1129479,
  rhbz#1085210, rhbz#1083786, rhbz#1032936, rhbz#1021841, rhbz#987549,
  rhbz#1146998

* Wed Jul 23 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.6.0-11
- Always set ask-quit setting
  Resolves: rhbz#1006737

* Wed Jul 23 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.6.0-10
- Bring back debug output for other libraries.
  Resolves: rhbz#1107518

* Mon Jun 23 2014 Jonathon Jongsma <jjongsma@redhat.com> - 0.6.0-9
- Fix unshrinkable displays on windows guest
  Resolves: rhbz#1111514

* Fri Jun 20 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.6.0-8
- Fix zoom level range in man page.
  Resolves: rhbz#1111428

* Wed Jun 18 2014 Christophe Fergeau <cfergeau@redhat.com> 0.6.0-7
- Fix wrong Requires name (trailing '$')
  Related: rhbz#1063238

* Tue Jun 17 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.6.0-6
- Remove some warnings in kiosk mode
  Resolves: rhbz#1107518
- Register remote-viewer.desktop as a handler for application/x-virt-viewer
  Resolves: rhbz#1063238
- New display will be zoomed out to a very small display size
  Resolves: rhbz#1104064
- Guest can not be resized to expected window size after zoom out
  Resolves: rhbz#1105528

* Thu Jun 05 2014 Christophe Fergeau <cfergeau@redhat.com> 0.6.0-5
- Fix authentication after failed attempt with VNC
  Resolves: rhbz#1007295
- Fix broken 'release-cursor' accel when not specified in --hotkeys
  Resolves: rhbz#1029108

* Wed Jun 04 2014 Jonathon Jongsma <jjongsma@redhat.com> - 0.6.0-4
- Fixed coverity errors discovered in 0.6.0-1 build
  Related:  rhbz#1097038
- Remote-Viewer: Zoom Out Behavior Is Not Consistent
  Resolves: rhbz#1004051

* Wed Jun  4 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.6.0-3
- Remove "Pass CAD" RHEL-only patch.
  Resolves: rhbz#1007726

* Tue Jun  3 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.6.0-2
- Use a USB icon instead of a generic settings icon
  Resolves: rhbz#804184
- Remove menu item "Automatically resize"
  Resolves: rhbz#1007649
- Client doesn't send monitor config when launched via browser plugin
  Resolves: rhbz#1038726
- Screen is blurry for some resolutions when spice window is maximized
  Resolves: rhbz#1056041
- Remove some couldn't load configuration messages
  Resolves: rhbz#1006737

* Fri May 23 2014 Jonathon Jongsma <jjongsma@redhat.com> - 0.6.0-1
- Rebase to 0.6.0. Drop all patches except one non-upstream patch that we'll
  carry for a little while longer yet.
  Resolves: rhbz#1097038

* Tue Apr 29 2014 Jonathon Jongsma <jjongsma@redhat.com> - 0.5.6-10
- Automatically adjust resolution when opened fullscreen via vv-file
  Resolves: rhbz#1083203

* Tue Oct 29 2013 Marc-André Lureau <marcandre.lureau@redhat.com> 0.5.6-9
- Move window again after fullscreen
  Resolves: rhbz#809546

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

* Fri Feb 17 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.1-1
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

