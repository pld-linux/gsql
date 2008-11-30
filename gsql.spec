#
Summary:	GNOME SQL IDE
Name:		gsql
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://gsql.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	054aec4b92b76a3ecb60c4084bacb892
URL:		http://gsql.org/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	gtksourceview2-devel
#BuildRequires:	intltool
#BuildRequires:	libtool
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	vte-devel
#Patch0: %{name}-DESTDIR.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
# if not running libtool or automake, but config.sub is too old:
#cp -f /usr/share/automake/config.sub .
%configure \
	--with-htmldir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/gconf/schemas/gsql-engine-mysql.schemas
%{_sysconfdir}/gconf/schemas/gsql-plugins.schemas
%{_sysconfdir}/gconf/schemas/gsql.schemas
%attr(755,root,root) %{_bindir}/gsql
%{_libdir}/gsql/engines/libgsqlengine_mysql.so
%attr(755,root,root)    %{_libdir}/gsql/engines/libgsqlengine_mysql.so.0
%attr(755,root,root)    %{_libdir}/gsql/engines/libgsqlengine_mysql.so.0.0.0
%attr(755,root,root)    %{_libdir}/gsql/plugins/libgsqlplugin_exporter.so.0
%attr(755,root,root)    %{_libdir}/gsql/plugins/libgsqlplugin_exporter.so.0.0.0
%{_libdir}/gsql/plugins/libgsqlplugin_exporter.so
%{_libdir}/gsql/plugins/libgsqlplugin_runner.so
%attr(755,root,root)    %{_libdir}/gsql/plugins/libgsqlplugin_runner.so.0
%attr(755,root,root)    %{_libdir}/gsql/plugins/libgsqlplugin_runner.so.0.0.0
%{_libdir}/gsql/plugins/libgsqlplugin_vte.so
%attr(755,root,root)    %{_libdir}/gsql/plugins/libgsqlplugin_vte.so.0
%attr(755,root,root)    %{_libdir}/gsql/plugins/libgsqlplugin_vte.so.0.0.0
%attr(755,root,root)    %{_libdir}/libgsql.so.0
%attr(755,root,root)    %{_libdir}/libgsql.so.0.0.0
%{_datadir}/gnome/apps/Applications/gsql.desktop
%{_datadir}/gnome/help/gsql/C/authors.xml
%{_datadir}/gnome/help/gsql/C/figures/null.png
%{_datadir}/gnome/help/gsql/C/gsql.xml
%{_datadir}/gnome/help/gsql/C/interface.xml
%{_datadir}/gnome/help/gsql/C/legal.xml
%{_datadir}/gnome/help/gsql/C/license.xml
%{_datadir}/gnome/help/gsql/C/preferences.xml
%{_datadir}/gnome/help/gsql/C/queryoperations.xml
%{_datadir}/gsql
%{_datadir}/gtk-doc/html/gsql/GSQLCellRendererDateTime.html
%{_datadir}/gtk-doc/html/gsql/GSQLContent.html
%{_datadir}/gtk-doc/html/gsql/GSQLCursor.html
%{_datadir}/gtk-doc/html/gsql/GSQLEditor.html
%{_datadir}/gtk-doc/html/gsql/GSQLNavigation.html
%{_datadir}/gtk-doc/html/gsql/GSQLSession.html
%{_datadir}/gtk-doc/html/gsql/GSQLVariable.html
%{_datadir}/gtk-doc/html/gsql/GSQLWorkspace.html
%{_datadir}/gtk-doc/html/gsql/gsql-architecture.html
%{_datadir}/gtk-doc/html/gsql/gsql-common.html
%{_datadir}/gtk-doc/html/gsql/gsql-conf.html
%{_datadir}/gtk-doc/html/gsql/gsql-editor.html
%{_datadir}/gtk-doc/html/gsql/gsql-engines.html
%{_datadir}/gtk-doc/html/gsql/gsql-menu.html
%{_datadir}/gtk-doc/html/gsql/gsql-notify.html
%{_datadir}/gtk-doc/html/gsql/gsql-plugins.html
%{_datadir}/gtk-doc/html/gsql/gsql-stock.html
%{_datadir}/gtk-doc/html/gsql/gsql-utils.html
%{_datadir}/gtk-doc/html/gsql/gsql.devhelp
%{_datadir}/gtk-doc/html/gsql/gsql.devhelp2
%{_datadir}/gtk-doc/html/gsql/gsql.schema.png
%{_datadir}/gtk-doc/html/gsql/home.png
%{_datadir}/gtk-doc/html/gsql/index.html
%{_datadir}/gtk-doc/html/gsql/index.sgml
%{_datadir}/gtk-doc/html/gsql/left.png
%{_datadir}/gtk-doc/html/gsql/right.png
%{_datadir}/gtk-doc/html/gsql/rn01.html
%{_datadir}/gtk-doc/html/gsql/style.css
%{_datadir}/gtk-doc/html/gsql/up.png
%{_mandir}/man1/gsql.1*
%{_datadir}/omf/gsql/gsql-C.omf
%{_pixmapsdir}/gsql

%if 0

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/libgsql.pc
%{_libdir}/libgsql.so
%{_includedir}/libgsql
%{_libdir}/gsql/plugins/libgsqlplugin_runner.la
%{_libdir}/gsql/engines/libgsqlengine_mysql.la
%{_libdir}/gsql/plugins/libgsqlplugin_exporter.la
%{_libdir}/gsql/plugins/libgsqlplugin_vte.la
%{_libdir}/libgsql.la

%files static
%defattr(644,root,root,755)
%{_libdir}/gsql/engines/libgsqlengine_mysql.a
%{_libdir}/gsql/plugins/libgsqlplugin_exporter.a
%{_libdir}/gsql/plugins/libgsqlplugin_runner.a
%{_libdir}/gsql/plugins/libgsqlplugin_vte.a
%{_libdir}/libgsql.a
%endif
