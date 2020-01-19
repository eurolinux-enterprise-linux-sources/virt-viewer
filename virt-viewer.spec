# -*- rpm-spec -*-

%global _hardened_build 1

# Default to skipping autoreconf.  Distros can change just this one line
# (or provide a command-line override) if they backport any patches that
# touch configure.ac or Makefile.am.
%{!?enable_autotools:%global enable_autotools 1}

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
Version: 5.0
Release: 15%{?dist}%{?extra_release}
Summary: Virtual Machine Viewer
Group: Applications/System
License: GPLv2+
URL: https://virt-manager.org/
Source0: https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

Patch0001: 0001-spice-Fix-display-id-in-the-warning-log.patch
Patch0002: 0002-spice-Replace-g_warning-with-g_debug.patch
Patch0003: 0003-Set-guest-name-at-the-same-time-as-uuid.patch
Patch0004: 0004-app-Update-warning-msg-in-virt-viewer-s-window.patch
Patch0005: 0005-remote-viewer-Extend-ifdef-HAVE_OVIRT-block.patch
Patch0006: 0006-ovirt-foreign-menu-Set-new-ISO-name-using-GTask-API.patch
Patch0007: 0007-ovirt-foreign-menu-Fetch-ISO-names-using-GTask-API.patch
Patch0008: 0008-ovirt-foreign-menu-Add-accessors-for-current-iso-and.patch
Patch0009: 0009-Introduce-ISO-List-dialog.patch
Patch0010: 0010-Run-ISO-dialog-when-Change-CD-menu-is-activated.patch
Patch0011: 0011-README-Update-links.patch
Patch0012: 0012-README-switch-to-Markdown-syntax.patch
Patch0013: 0013-Update-for-README.md.patch
Patch0014: 0014-iso-dialog-Do-not-use-string-directly.patch
Patch0015: 0015-Do-not-print-password-in-the-debug-log.patch
Patch0016: 0016-iso-dialog-Avoid-crash-when-closing-dialog-early.patch
Patch0017: 0017-session-spice-Pass-hostname-to-authentication-dialog.patch
Patch0018: 0018-Show-errors-generated-by-connection-dialog.patch
Patch0019: 0019-man-Mention-that-ssh-agent-can-be-useful.patch
Patch0020: 0020-spice-Remove-unneeded-braces.patch
Patch0021: 0021-file-transfer-Fix-label-of-the-dialog.patch
Patch0022: 0022-Fix-build-when-building-without-oVirt.patch
Patch0023: 0023-Avoid-harmless-warnings-due-lack-of-oVirt-on-build.patch
Patch0024: 0024-Don-t-define-function-without-oVirt-integration.patch
Patch0025: 0025-virt-viewer-Allow-more-precise-VM-selection.patch
Patch0026: 0026-virt-viewer-Adjust-name-id-uuid-comment.patch
Patch0027: 0027-Comment-out-folder-sharing-menus.patch
Patch0028: 0028-virt-viewer-Fix-comparison-in-domain-selection.patch
Patch0029: 0029-vnc-Set-display-as-enabled-on-init.patch
Patch0030: 0030-window-Allow-to-control-zoom-using-keypad.patch
Patch0031: 0031-virt-viewer-Support-newer-libvirt-xml-format.patch
Patch0032: 0032-app-Allow-to-connect-to-channel-using-unix-socket.patch
Patch0033: 0033-virt-viewer-Ensure-to-not-close-during-migration.patch
Patch0034: 0034-Make-the-progress-bar-smooth-during-file-transfer.patch
Patch0036: 0036-Update-translation-from-internal-zanata.patch
Patch0037: 0037-window-Do-not-show-fullscreen-toolbar-if-in-kiosk-mo.patch
Patch0038: 0038-kiosk-Show-authentication-dialog-again-if-cancelled.patch
Patch0039: 0039-spice-do-not-show-error-on-cancel-close-of-auth-dial.patch
Patch0040: 0040-vnc-do-not-show-error-on-cancel-close-of-auth-dialog.patch
Patch0041: 0041-remote-viewer-Show-authentication-dialog-again-if-in.patch
Patch0042: 0042-remote-viewer-connect-Keep-the-dialog-window-on-top.patch
Patch0043: 0043-Change-default-screenshot-name-to-Screenshot.png.patch
Patch0044: 0044-Report-errors-when-saving-screenshot.patch
Patch0045: 0045-Screenshot-reject-unknown-image-type-filenames.patch
Patch0046: 0046-configure-check-for-new-functions-in-libgovirt.patch
Patch0047: 0047-foreign-menu-Use-query-for-fetching-virtual-machines.patch
Patch0048: 0048-ovirt-foreign-menu-Fetch-host-cluster-and-data-cente.patch
Patch0049: 0049-foreign-menu-Check-if-storage-domain-is-active-for-d.patch
Patch0050: 0050-remote-viewer-Pass-guri-to-remote_viewer_session_con.patch
Patch0051: 0051-doc-Adjust-reference-to-spice-gtk-man-page.patch
Patch0052: 0052-doc-Adjust-reference-to-spice-gtk-man-page-for-remot.patch
Patch0053: 0053-Update-translations-from-zanata.patch
Patch0054: 0054-remote-viewer-remove-spice-controller.patch
Patch0055: 0055-remote-viewer-connect-centralize-window.patch
Patch0056: 0056-app-Always-add-guest-name-comment.patch
Patch0057: 0057-Mark-PrintScreen-as-translatable.patch
Patch0058: 0058-ovirt-foreign-menu-Bypass-errors-from-Host-Cluster-D.patch
Patch0059: 0059-Spice-listen-for-new-SpiceSession-disconnected-signa.patch
Patch0060: 0060-Fix-a-regression-when-initial-connection-fails.patch
Patch0061: 0061-configure-Fix-check-for-govirt-functions.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: openssh-clients
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%if 0%{?enable_autotools}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: libtool
%endif

BuildRequires: pkgconfig(glib-2.0) >= 2.38
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(libvirt) >= 0.10.0
BuildRequires: pkgconfig(libvirt-glib-1.0) >= 0.1.8
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires: pkgconfig(gtk-vnc-2.0) >= 0.4.0
%if %{with_spice}
BuildRequires: pkgconfig(spice-client-gtk-3.0) >= 0.35
BuildRequires: pkgconfig(spice-protocol) >= 0.12.12
%endif
BuildRequires: /usr/bin/pod2man
BuildRequires: intltool
%if %{with_govirt}
BuildRequires: pkgconfig(govirt-1.0) >= 0.3.3
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
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1
%patch0034 -p1
%patch0036 -p1
%patch0037 -p1
%patch0038 -p1
%patch0039 -p1
%patch0040 -p1
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1

%build

%if 0%{?enable_autotools}
autoreconf -if
%endif

%if %{with_spice}
%define spice_arg --with-spice-gtk
%else
%define spice_arg --without-spice-gtk
%endif

%if %{with_govirt}
%define govirt_arg --with-ovirt
%endif

%configure %{spice_arg} %{govirt_arg} --with-buildid=%{release} --disable-update-mimedb --with-osid=rhel%{?rhel}
%__make %{?_smp_mflags} V=1


%install
rm -rf $RPM_BUILD_ROOT
%__make install  DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/bin/touch --no-create %{_datadir}/mime/packages &> /dev/null || :
%{_bindir}/update-desktop-database -q %{_datadir}/applications
if [ $1 -eq 2 ] ; then
  # Here due 1658325, postun alone is not enough. Can be removed later on.
  %{_sbindir}/update-alternatives --remove spice-xpi-client %{_libexecdir}/spice-xpi-client-remote-viewer || :
fi

%postun
%{_sbindir}/update-alternatives --remove spice-xpi-client %{_libexecdir}/spice-xpi-client-remote-viewer || :
if [ $1 -eq 0 ] ; then
  /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
  %{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null || :
fi
%{_bindir}/update-desktop-database -q %{_datadir}/applications

%posttrans
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%{_bindir}/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README.md COPYING AUTHORS ChangeLog NEWS
%{_bindir}/%{name}
%{_bindir}/remote-viewer
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/devices/*
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/appdata/remote-viewer.appdata.xml
%{_datadir}/mime/packages/virt-viewer-mime.xml
%{_mandir}/man1/virt-viewer.1*
%{_mandir}/man1/remote-viewer.1*

%changelog
* Fri May 31 2019 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 5.0.15
- Fix check for ovirt functions
  Related: rhbz#1427467

* Wed May 22 2019 Victor Toso <victortoso@redhat.com> - 5.0-14
- Listen to SpiceSession::disconnected
  Resolves: rhbz#1505809

* Wed Apr 10 2019 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 5.0.13
- Bypass errors from oVirt foreign menu queries
  Related: rhbz#1428401

* Fri Mar 15 2019 Victor Toso <victortoso@redhat.com> - 5.0-12
- Centralize recent dialog
  Resolves: rhbz#1508274
- Always add guest name as comment
  Resolves: rhbz#1623756
- Mark PrintScreen as translatable
  Resolves: rhbz#1510411
- Remove symlink to spice-xpi-client-remote-viewer on update (it was dropped)
  Resolves: rhbz#1658325

* Wed Jun 13 2018 Victor Toso <victortoso@redhat.com> - 5.0-11
- Disable spice-controller in virt-viewer
  Resolves: rhbz#1590457

* Mon Dec 11 2017 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 5.0-10
- Adjust reference to spice-gtk man page for remote-viewer
  Resolves: rhbz#1477966
- Update translations
  Resolves: rhbz#1481243

* Fri Nov 17 2017 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 5.0-9
- Drop downstream specific patch reverting string change
  Related: rhbz#1481243
- Fix scope declaration of enable_autotools macro
  Resolves: rhbz#1504132
- Fix wrong date in previous changelog entry
  Resolves: rhbz#1504132
- Save oVirt uri after connecting to guest
  Resolves: rhbz#1459792
- Adjust reference to spice-gtk man page
  Resolves: rhbz#1477966

* Mon Oct 02 2017 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 5.0-8
- Show authentication dialog if in kiosk mode and connecting to ovirt
  Resolves: rhbz#1459808
- Keep the remove-viewer-connect dialog window on top
  Resolves: rhbz#1459800
- Show overwrite confirmation when saving screenshot file
  Resolves: rhbz#1455832
- Fix REST endpoint used to load the storagedomains
  Resolves: rhb#1427467

* Tue Jun 06 2017 Victor Toso <victortoso@redhat.com> - 5.0-7
- Do not show error on cancel/close of auth dialog - vnc fix
  Resolves: rhbz#1446161

* Thu Jun 01 2017 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 5.0-6
- Do not show error on cancel/close of auth dialog
  Resolves: rhbz#1446161

* Thu Jun 01 2017 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 5.0-5
- Do not allow exit fullscreen in kiosk mode
  Resolves: rhbz#1446161

* Thu May 18 2017 Pavel Grunt <pgrunt@redhat.com> - 5.0-4
- Fix seamless migration in virt-viewer
  Resolves: rhbz#1442929
- Make file transfer progressbar smooth again
  Resolves: rhbz#1449572
- Update translation from internal zanata
  Resolves: rhzb#1378279

* Mon Apr 10 2017 Pavel Grunt <pgrunt@redhat.com> - 5.0-3
- Handle initial zoom settings for vnc
  Resolves: rhbz#1436991
- Allow to control zoom using numpad
  Resolves: rhbz#1337575
- Support new elements in libvirt xml
  Resolves: rhbz#1411765

* Wed Mar 15 2017 Pavel Grunt <pgrunt@redhat.com> - 5.0-2
- Really enable the hardened build
  Resolves: rhzb#1420780
- Fixup for precise VM selection
  Resolves: rhbz#1399077

* Wed Mar 15 2017 Pavel Grunt <pgrunt@redhat.com> - 5.0-1
- Rebase to the latest upstream release
  Resolves: rhbz#1413982
- Rebuild with spice-gtk 0.33
  Resolves: rbhz#1431995
- Rebuild with correct hardening flags
  Resolves: rhbz#1420780
- Fix display id inconsistencies in debug logs
  Resolves: rhbz#1368390
- Provide a dialog for selecting ISOs
  Resolves: rhbz#1414016
- Always display warning messages
  Resolves: rhbz#1386630
- Do not print password in the logs
  Resolves: rhbz#1410030
- Update qemu+ssh URL example
  Resolves: rhbz#1377283
- Add cli options for precise VM selection in virt-viewer
  Resolves: rhbz#1399077

* Mon Dec 12 2016 Pavel Grunt <pgrunt@redhat.com> - 2.0-13
- Fix connection using broken monitor mapping
  Resolves: rhbz#1351243
- Provide correct exit code on cancel
  Resolves: rhbz#1374430
- Inform user about connection failure
  Resolves: rhbz#1377100
- Recommend using ssh-agent
  Resolves: rhbz#1377283

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
