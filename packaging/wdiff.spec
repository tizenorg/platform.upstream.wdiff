Name:           wdiff
Version:        1.0.1
Release:        1
License:        GPL-2.0+
Summary:        Display Word Differences Between Text Files
Url:            ftp://mirrors.kernel.org/gnu/wdiff/
Group:          Productivity/Text/Utilities
Source:         http://alpha.gnu.org/gnu/wdiff/wdiff-%{version}.tar.bz2
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
wdiff compares two files and finds which words have been deleted or
added to old_file to get new_file. A word is considered to be anything
between whitespace.

Xwdiff is a handy X Window System front-end, based on Tcl/Tk.

%package lang
License:        GPL-2.0+
Summary:        Translations for Wdiff
Group:          Productivity/Text/Utilities
Requires:       %{name} = %{version}

%description lang
Contains language specific files for of wdiff.

%prep
%setup -q

%build
# those autoconf tools never really work, do they?
# error: AC_REQUIRE: circular dependency of AC_GNU_SOURCE
# autoreconf -fi
LIBS=-lncurses \
CFLAGS="%{optflags} -pipe -DPROTOTYPES" \
GETOPT="" \
%configure
make

%install
make "DESTDIR=%{buildroot}" install
%find_lang %{name}-gnulib
%find_lang %{name}

%files
%defattr(-,root,root)
%license COPYING
%{_infodir}/wdiff.info*
/usr/bin/*
%{_mandir}/man1/*

%files lang -f %{name}-gnulib.lang -f %{name}.lang


%changelog
