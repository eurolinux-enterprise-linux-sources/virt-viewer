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
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
%define with_govirt 1
%endif

# spice-gtk is x86 x86_64 arm only currently:
%ifnarch %{ix86} x86_64 %{arm}
%define with_spice 0
%endif

Name: virt-viewer
Version: 2.0
Release: 12%{?dist}%{?extra_release}
Summary: Virtual Machine Viewer
Group: Applications/System
License: GPLv2+
URL: http://virt-manager.org/
Source0: http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
Patch1: 0001-Take-direct-into-consideration-when-checking-if-a-gu.patch
Patch2: 0002-Update-geometry-when-enabling-disabling-displays.patch
Patch3: 0003-VirtViewerApp-create-main-window-after-constructor.patch
Patch4: 0004-Use-constructed-vfunc-instead-of-constructor.patch
Patch5: 0005-Monitor-config-at-sometimes-leaves-additional-monito.patch
Patch6: 0006-virt-viewer-Bring-back-debug-log-about-nonexistent-g.patch
Patch7: 0007-foreign-menu-Don-t-show-empty-foreign-menu-on-second.patch
Patch8: 0008-Do-not-add-https-and-api-to-oVirt-URI.patch
Patch9: 0009-virt-viewer-Add-a-GError-arg-to-extract_connect_info.patch
Patch10: 0010-virt-viewer-Add-a-GError-arg-to-update_display.patch
Patch11: 0011-virt-viewer-app-Add-a-GError-arg-to-create_session.patch
Patch12: 0012-virt-viewer-app-create_session-should-return-a-boole.patch
Patch13: 0013-virt-viewer-Avoid-simple_message_dialog-when-errors-.patch
Patch14: 0014-remote-viewer-Avoid-simple_message_dialog-when-error.patch
Patch15: 0015-virt-viewer-Do-not-wait-for-a-guest-that-will-never-.patch
Patch16: 0016-virt-viewer-app-Do-not-show-error-dialog-twice-for-u.patch
Patch17: 0017-Use-ZOOM-constants-instead-of-numbers.patch
Patch18: 0018-virt-viewer-display-Use-MIN_DISPLAY_WIDTH-HEIGHT-ins.patch
Patch19: 0019-virt-viewer-window-Change-zoom-of-the-display-only-w.patch
Patch20: 0020-virt-viewer-window-Set-zoom-when-display-is-enabled-.patch
Patch21: 0021-virt-viewer-window-Return-early-when-zoom-of-window-.patch
Patch22: 0022-display-spice-Do-not-ignore-change-of-position.patch
Patch23: 0023-virt-viewer-main-Require-domain-name-as-argument-for.patch
Patch24: 0024-virt-viewer-app-Set-hotkeys-when-app-is-constructed.patch
Patch25: 0025-Revert-virt-viewer-main-Require-domain-name-as-argum.patch
Patch26: 0026-virt-viewer-main-wait-should-not-be-used-without-dom.patch
Patch27: 0027-virt-viewer-window-Make-sure-that-minimum-zoom-level.patch
Patch28: 0028-virt-viewer-window-Set-initial-zoom-only-once.patch
Patch29: 0029-session-spice-Destroy-the-channel-instead-of-emit-a-.patch
Patch30: 0030-spice-session-use-the-error-message-when-available-o.patch
Patch31: 0031-ovirt-Add-support-for-an-admin-key-in-vv-file.patch
Patch32: 0032-Enable-hotkeys-after-setting-them-in-virt_viewer_app.patch
Patch33: 0033-build-sys-Don-t-substitute-buildid-when-it-was-not-s.patch
Patch34: 0034-build-sys-Always-prepend-to-BUILDID.patch
Patch35: 0035-vv-file-Move-version-checking-code-in-its-own-functi.patch
Patch36: 0036-vv-file-Refactor-virt_viewer_file_check_min_version.patch
Patch37: 0037-vv-file-Add-VirtViewerFile-versions.patch
Patch38: 0038-build-sys-Add-with-osid.patch
Patch39: 0039-Show-osid-in-remote-viewer-version.patch
Patch40: 0040-vv-file-Use-versions-in-min-version-check.patch
Patch41: 0041-util-Replace-virt_viewer_compare_version-with-_compa.patch
Patch42: 0042-test-Add-test-case-for-virt_viewer_compare_buildid.patch
Patch43: 0043-vv-file-Add-newer-version-url-key-to-.vv-files.patch
Patch44: 0044-vv-file-Show-newer-version-url-when-version-check-fa.patch
Patch45: 0045-Avoid-Dereference-of-a-null-pointer.patch
Patch46: 0046-virt-viewer-set-keepAlive-on-libvirt-connection.patch
Patch47: 0047-Remove-unnecessary-parameter-from-virt_viewer_window.patch
Patch48: 0048-virt-viewer-window-Allow-to-resize-window-to-any-siz.patch
Patch49: 0049-events-ensure-event-callbacks-are-threadsafe.patch
Patch50: 0050-events-register-event-using-GOnce-to-avoid-multiple-.patch
Patch51: 0051-events-remove-timeout-and-handle-from-arrays.patch
Patch52: 0052-glib-compat-Use-g_new0-GMutex-1-if-GLib-2.31.patch
Patch53: 0053-events-allow-zero-timeouts-for-timer.patch
Patch54: 0054-events-remove-unused-virt_viewer_events_find_-handle.patch
Patch55: 0055-events-protect-handles-and-timeouts-against-concurre.patch
Patch56: 0056-events-don-t-reschedule-deleted-timeouts-watches.patch
Patch57: 0057-events-don-t-hold-events-lock-when-dispatching-free-.patch
Patch58: 0058-events-don-t-create-glib-IO-watch-for-disabled-handl.patch
Patch59: 0059-events-allow-to-remove-disabled-timers-and-handles.patch
Patch60: 0060-events-don-t-leak-GIOChannel-when-destroying-IO-hand.patch
Patch61: 0061-Exit-normally-when-canceling-dialog.patch
Patch62: 0062-Clear-GError-in-cleanup-section.patch
Patch63: 0063-Report-errors-in-one-place.patch
Patch64: 0064-virt-viewer-Clean-up-if-no-vm-was-chosen.patch
Patch65: 0065-Set-enabled-status-of-all-displays-when-we-get-a-mon.patch
Patch66: 0066-app-Add-helper-for-number-of-client-monitors.patch
Patch67: 0067-app-Do-not-map-display-to-non-existent-monitor.patch
Patch68: 0068-session-spice-Disable-extra-displays-in-fullscreen-m.patch
Patch69: 0069-app-Compute-monitor-mapping-only-in-fullscreen.patch
Patch70: 0070-ovirt-Take-into-account-SPICE-proxy.patch
Patch71: 0071-virt-viewer-display-vnc-Set-guest-name-when-using-VN.patch
Patch72: 0072-virt-viewer-display-vnc-Set-uuid-when-using-VNC.patch
Patch73: 0073-Stop-polling-after-reconnecting-to-libvirtd.patch
Patch74: 0074-Fix-crash-when-disabling-last-enabled-display.patch
Patch75: 0075-Use-the-display-ID-to-configure-fullscreen-monitors.patch
Patch76: 0076-session-Only-create-a-hashtable-if-apply_monitor_geo.patch
Patch77: 0077-util-Fix-the-size-of-sorted_displays-allocation.patch
Patch78: 0078-spice-vv-file-do-not-ignore-usb-filter.patch
Patch79: 0079-ovirt-Only-use-active-ISO-domains-for-foreign-menu.patch
Patch80: 0080-display-set-min-value-for-desktop-width-height-props.patch
Patch81: 0081-display-Set-useful-values-for-MIN_DISPLAY_-WIDTH-HEI.patch
Patch82: 0082-ovirt-Don-t-try-to-use-ovirt-if-jsessionid-is-not-se.patch
Patch83: 0083-ovirt-Error-reporting-improvements-on-invalid-VM-nam.patch
Patch84: 0084-ovirt-Fix-OvirtApi-memory-handling.patch
Patch85: 0085-vv-file-Add-support-for-sso-token-field-in-ovirt.patch
Patch86: 0086-ovirt-Use-sso-token-when-set-in-.vv-file.patch
Patch87: 0087-app-monitor-config-do-it-all-or-nothing.patch
Patch88: 0088-app-Return-early-on-empty-monitor-mapping.patch
Patch89: 0089-vnc-display-Disable-default-grab-sequence.patch
Patch90: 0090-spice-avoid-crashing-when-using-invalid-video-config.patch
Patch91: 0091-Add-some-missing-mnemonics-to-menu-items.patch
Patch92: 0092-Add-mnemonics-for-each-display-item.patch
Patch93: 0093-Add-file-transfer-dialog.patch
Patch94: 0094-Add-some-timeouts-to-file-transfer-dialog.patch
Patch95: 0095-app-Use-debug-to-inform-about-smartcard-shortcuts-st.patch
Patch96: 0096-app-Check-validity-of-hotkey.patch
Patch97: 0097-Update-timer-to-refresh-ovirt-foreign-menu.patch
Patch98: 0098-monitor-alignment-Do-not-crash-on-NULL-display.patch
Patch99: 0099-remote-viewer-GtkRecentChooserWidget-is-not-suitable.patch
Patch100: 0100-remote-viewer-Use-a-different-mnemonic-for-Connectio.patch
Patch101: 0101-app-window-Set-display-menu-not-sensitive-when-neede.patch
Patch102: 0102-virt-viewer-Set-toolbar-buttons-not-sensitive-when-n.patch
Patch103: 0103-app-Do-not-show-usbredir-button-without-session.patch
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

BuildRequires: glib2-devel >= 2.22
%if %{with_gtk3}
BuildRequires: gtk3-devel >= 3.0.0
%else
BuildRequires: gtk2-devel >= 2.18.0
Requires: gtk2 >= 2.18.0
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
BuildRequires: spice-gtk3-devel >= 0.31
%else
BuildRequires: spice-gtk-devel >= 0.31
%endif
BuildRequires: spice-protocol >= 0.10.1
%endif
BuildRequires: /usr/bin/pod2man
BuildRequires: intltool
%if %{with_govirt}
BuildRequires: libgovirt-devel >= 0.3.2
%endif

%if 0%{?fedora} >= 20
Obsoletes: spice-client < 0.12.3-2
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
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/mime/packages/virt-viewer-mime.xml
%ghost %{_libexecdir}/spice-xpi-client
%{_libexecdir}/spice-xpi-client-remote-viewer
%{_mandir}/man1/virt-viewer.1*
%{_mandir}/man1/remote-viewer.1*

%changelog
* Wed Sep 14 2016 Pavel Grunt <pgrunt@redhat.com> - 2.0-12
- Update translations
  Resolves: rhbz#1182470

* Fri Jul 22 2016 Pavel Grunt <pgrunt@redhat.com> - 2.0-11
- Fix sensitivity of menu items
  Resolves: rhbz#1354291

* Fri Jul 01 2016 Pavel Grunt <pgrunt@redhat.com> - 2.0-10
- Avoid crashing when using invalid video config
  Resolves: rhbz#1250820
- Add mnemonics for remote-viewer connection dialog
  Resolves: rhbz#1351487

* Thu Jun 30 2016 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 2.0-9
- Adjust timer to refresh ovirt foreign menu
  Resolves: rhbz#1347726

* Wed Jun 08 2016 Pavel Grunt <pgrunt@redhat.com> - 2.0-8
- Utilize SSO to authenticate against oVirt engine for foreign menu support
  Resolves: rhbz#1286696
- monitor-config: do it all or nothing
  Resolves: rhbz#1339493
- Return early on empty monitor mapping
  Resolves: rhbz#1339491
- Disable default vnc grab sequence
  Resolves: rhbz#1339575
- Avoid crashing when using invalid video config
  Resolves: rhbz#1250820
- Add missing access keys
  Resolves: rhbz#1332545
- Add progress bar for file transfer
  Resolves: rhbz#1324521
- Improve logs when parsing hotkeys
  Resolves: rhbz#1339572

* Thu Mar 17 2016 Pavel Grunt <pgrunt@redhat.com> - 2.0-7
- Fix for extra monitors on start up
  Resolves: rhbz#1153372
- Add support for proxy-url libgovirt property
  Resolves: rhbz#1292761
- Show correct name and uuid for vnc guests
  Resolves: rhbz#1293879
- Stop polling after reconnecting to libvirtd
  Resolves: rhbz#1271519
- Fix crash when disabling the last display
  Resolves: rhbz#1294938
- Fix monitor mapping
  Resolves: rhbz#1267184
- Fix for usb-filter ignored by the vv-file
  Resolves: rhbz#1309634
- Show only attached CDs in the foreign menu
  Resolves: rhbz#1313371
- Set useful dimensions of virt-viewer window
  Resolves: rhbz#1297260

* Sun Aug 09 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-6
- Error message continously popping out when stopping libvirtd
  Resolves: rhbz#1246022

* Thu Jul 23 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-5
- Allow to resize window to any size
  Resolves: rhbz#1242509
- Upate virt-viewer-events.c to match libvirt-glib's event file
  Resolves: rhbz#1243228

* Fri Jul 10 2015 Fabiano Fidêncio <fidencio@redhat.com> - 2.0-4
- set keepAlive on libvirt connection
  Resolves: rhbz#1164052
- Rebase to 2.0: Add a missing bug
  Resolves: rhbz#1228759

* Wed Jun 17 2015 Jonathon Jongsma <jjongsma@redhat.com> - 2.0-3
- fix coverity warning for code introduced in 2.0
  Related: rhbz#1181288

* Tue Jun 16 2015 Jonathon Jongsma <jjongsma@redhat.com> - 2.0-2
- Add 'admin' key to [ovirt] .vv file section
  Resolves: rhbz#1210248
- Shortcuts missing from "Send key" menu when started using plugin
  Resolves: rhbz#1230602
- Add minimum version check to rhev spice-client
  Resolves: rhbz#1223469

* Mon May 18 2015 Fabiano Fidêncio <fidencio@redhat.com> 2.0-1
- Rebase to 2.0
  Resolves: rhbz#1181288
- virt-viewer cannot connect to spice VM when libvirt uses tcp port
  with sasl encryption
  Resolves: rhbz#1167354
- virt-viewer will core dump with -r option via ssh when destroying
  the guest
  Resolves: rhbz#1163647
- virt-viewer cannot set zoom level in command line for vnc guest
  Resolves: rhbz#1170071
- launching virt-viewer using --attach makes it crashes
  Resolves: rhbz#1196552
- --attach doesn't work with SELinux
  Resolves: rhbz#1141228

* Mon Dec 01 2014 Fabiano Fidêncio <fidencio@redhat.com> 0.6.0.12
- Show a debug message instead of an error message when trying to
  connect to a non-existent guest using ovirt
  Resolves: rhbz#1168495

* Tue Nov 04 2014 Fabiano Fidêncio <fidencio@redhat.com> 0.6.0.11
- Fix crash when connecting to a guest through VNC and typing a wrong
  password
  Resolves: rhbz#1159731

* Thu Oct 23 2014 Fabiano Fidêncio <fidencio@redhat.com> 0.6.0.10
- Revert "Fix bug with initial placement of fullscreen windows"
  Related: rhbz#1129477

* Wed Oct 22 2014 Fabiano Fidêncio <fidencio@redhat.com> 0.6.0-9
- Set initial window size to display desktop size and make the default
  window size a bit more useful
  Resolves: rhbz#1152981
- Force display_show_hint() when the display is se
  Resolves: rhbz#1152468
- Fix bug with initial placement of fullscreen windows
  Related: rhbz#1129477
- Don't disable "send key" menu when display isn't ready
  Related: rhbz#1152468
- VirtViewerDisplayVnc: set 'session' property
  Resolves: rhbz#1152815

* Thu Oct  9 2014 Fabiano Fidêncio <fidencio@redhat.com> 0.6.0-8
- Adapt auth_cancelled to the downstream code
  Related: rhbz#1142742
- ovirt: Allow to remove CD images
  Resolves: rhbz#1145126
- Create windows on demand, not at startup
  Resolves: rhbz#1032939
- Use socat instead of nc if possible
  Resolves: rhbz#1030487
- spice: do not open in fullscreen with CONTROLLER_AUTO_DISPLAY_RES
  Resolves: rhbz#1149352

* Tue Sep 30 2014 Fabiano Fidêncio <fidencio@redhat.com> 0.6.0-7
- Revert "Add support to use numpad accelerators for zoom-in, zoom-out
  and zoom-reset
  Related: rhbz#921326
- Update virt-viewer man page for Update virt-viewer man page for oVirt
  connection support and fullscreen monitor mapping
  Resolves: rhbz#1142769
- Improve error message if input wrong username or password for a tcp
  connection
  Resolves: rhbz#1142742
- Unset app 'fullscreen' when leaving fullscreen
  Resolves: rhbz#1146997
- Don't use fallback ca-file when launching vv-file
  Resolves: rhbz#1127762
- Force displays to update geometry when agent connects
  Related: rhbz#1032971

* Thu Sep 18 2014 Fabiano Fidêncio <fidencio@redhat.com> 0.6.0-6
- Report disconnection error details
  Related: rhbz#1115986
- Add support to use numpad accelerators for zoom-in, zoom-out and
  zoom-reset
  Resolves: rhbz#921326
- Do not show duplicated menu items
  Related: rhbz#921326

* Fri Sep 12 2014 Christophe Fergeau <cfergeau@redhat.com> 0.6.0-5
- Allow to pass usernames in ovirt URIs
  Resolves: rhbz#1061826
- Add support for oVirt foreign menu - this allows to change the ISO image
  used by an oVirt VM from remote-viewer GUI
  Resolves: rhbz#1127156
- Don't attempt to connect to localhost displays with qemu+tcp:// libvirt
  connections
  Resolves: rhbz#1108523
- Provide more details in error dialog when a disconnection occurs
  Resolves: rhbz#1115986
- Fix harmless Coverity warning
  Resolves: rhbz#885108

* Fri Sep 05 2014 Jonathon Jongsma <jjongsma@redhat.com> - 0.6.0-4
- Add support for user-defined fullscreen monitor configuration file
  Resolves: rhbz#1129477

* Tue Aug 05 2014 Marc-Andre Lureau <marcandre.lureau@redhat.com> - 0.6.0-3
- Fix zoom-{in, out} accelerators. Resolves: rhbz#989407
- Fix man page spelling. Resolves: rhbz#970825

* Mon Aug 04 2014 Jonathon Jongsma <jjongsma@redhat.com> - 0.6.0-2
- add buildid to configure
- Bump gtk2 dependency to match requirement in 0.6.0
  Related: rhbz#1109400
- Improve documentation of --attach command line option
  Resolves: rhbz#999291

* Mon Jul  7 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.6.0-1
- Rebase to 0.6.0.
  Resolves: rhbz#1109400
  Resolves: rhbz#921332 rhbz#1020669 rhbz#1021350 rhbz#1022426
  Resolves: rhbz#1023253 rhbz#1024204 rhbz#1024312 rhbz#1032967 rhbz#1063237
  Resolves: rhbz#1063239 rhbz#1096718 rhbz#1096721 rhbz#1109731
- Remove "Pass CAD" RHEL-only patch
  Resolves: rhbz#923072
- Fix broken 'release-cursor' accel when not specified in --hotkeys
  Resolves: rhbz#1032869
- Should use a USB icon instead of a generic settings icon
  Resolves: rhbz#921406
- remote-viewer should add introduction for new added functions into man page and help info.
  Resolves: rhbz#970825
- ctrl-[+-0] zoom in/out/native keyboard shortcuts don't work in fullscreen (with mouse over the control bar)
  Resolves: rhbz#989407
- No box pop out when input a wrong password and retry connection for vnc guest
  Resolves: rhbz#1007306
- Menu item "Automatically resize" could be disabled if there is no spice vdagent connection
  Resolves: rhbz#1007666
- Remote-Viewer: Zoom Out Behavior Is Not Consistent
  Resolves: rhbz#1022404
- If "ctrl alt" key combination is set as the one for releasing window, the window is not released.
  Resolves: rhbz#1032869
- virt-viewer --direct fails to connect to remote guest configured with listen="0.0.0.0"
  Resolves: rhbz#1079211
- Unnecessary warning info show when using virt-viewer -k to launch a spice guest
  Resolves: rhbz#1107519
- Need to update virt-viewer man page
  Resolves: rhbz#921341

* Fri Feb 14 2014 Christophe Fergeau <cfergeau@redhat.com> 0.5.7-7
- Don't show ctrl+0 in "Send Keys" menu when using --hotkeys
  Resolves: rhbz#1063195

* Tue Jan 28 2014 Christophe Fergeau <cfergeau@redhat.com> 0.5.7-6
- Fix fullscreen+multiscreen bug
  Resolves: rhbz#920988

- Fix addition of hotkey combos to "Send Keys" menu
  Resolves: rhbz#922716

- Translation updates from RH translation team
  Resolves: rhbz#1047327

- Add kiosk mode
  Resolves: rhbz#1040926

- Add .vv file description to man page
  Resolves: rhbz#970825

- spice: show an error dialog if password is invalid
  Resolves: rhbz#990883


* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.5.7-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.5.7-4
- Mass rebuild 2013-12-27

* Mon Dec 16 2013 Jonathon Jongsma <jjongsma@redhat.com> 0.5.7-3
- Do all display alignment in virt-viewer (rhbz#1022769)

* Fri Sep 13 2013 Christophe Fergeau <cfergeau@redhat.com> 0.5.7-2
- Build virt-viewer for rhel7 with gtk3 and ovirt support

* Wed Jul 31 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.7-1
- Update to 0.5.7 release

* Thu May 23 2013 Christophe Fergeau <cfergeau@redhat.com> - 0.5.6-2
- Mark remote-viewer as replacing spice-client

* Wed May  1 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.6-1
- Update to 0.5.6 release

* Wed Feb 13 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.5-1
- Update to 0.5.5 release

* Fri Dec 14 2012 Cole Robinson <crobinso@redhat.com> - 0.5.4-3
- Fix crash after entering spice password (bz #880381)

* Sat Oct 13 2012 Chris Tyler <chris@tylers.info> - 0.5.4-2
- Enabled spice support for ARM archs

* Mon Sep 17 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.4-1
- Update to 0.5.4 release

* Fri Sep 14 2012 Hans de Goede <hdegoede@redhat.com> - 0.5.3-6
- Rebuild for spice-gtk ABI breakage (previous spice-gtk build was borked)

* Tue Sep 11 2012 Hans de Goede <hdegoede@redhat.com> - 0.5.3-5
- Rebuild for spice-gtk ABI breakage

* Fri Sep  7 2012 Hans de Goede <hdegoede@redhat.com> - 0.5.3-4
- Rebuild for spice-gtk soname change

* Mon Aug 13 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.3-3
- Rebuild for spice-gtk soname change

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.3-1
- Update to 0.5.3 release

* Fri Mar  9 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-1
- Update to 0.5.2 release

* Fri Feb 17 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.1-1
- Update to 0.5.1 release

* Tue Feb 14 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.0-1
- Update to 0.5.0 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.2-1
- Update to 0.4.2 release

* Sun Aug 14 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-3
- More ssh tunnelling port fixes

* Fri Aug 12 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-2
- Fix ssh tunnelling

* Thu Aug  4 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-1
- Update to 0.4.1 release

* Tue Aug  2 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.0-2
- Rebuild for accidental spice-glib soname change

* Tue Jul 12 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.0-1
- Update to 0.4.0 release
- Switch build to GTK3 instead of GTK2

* Tue May 31 2011 Daniel P. Berrange <berrange@redhat.com> - 0.3.1-2
- Rebuild for spice-glib ABI breakage

* Wed May 11 2011 Karsten Hopp <karsten@redhat.com> 0.3.1-1.1
- spice-gtk is x86 x86_64 only, don't require it on other archs

* Mon Feb 21 2011 Daniel P. Berrange <berrange@redhat.com> - 0.3.1-1
- Update to 0.3.1 release

* Mon Feb 21 2011 Daniel P. Berrange <berrange@redhat.com> - 0.3.0-1
- Update to 0.3.0 and enable SPICE

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 15 2010 Daniel P. Berrange <berrange@redhat.com> - 0.2.1-1
- Update to 0.2.1 release

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
