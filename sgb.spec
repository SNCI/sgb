Name: sgb
Version: 20090810
Release: 16
Packager: Andreas Scherer <andreas@komputer.de>
Summary: The Stanford GraphBase
License: Copyright 1993 Stanford University
URL: http://www-cs-faculty.stanford.edu/~uno/sgb.html
Group: Productivity/Development
Distribution: Kubuntu 12.04 (i386)
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: i386
Source: ftp://ftp.cs.stanford.edu/pub/sgb/%{name}.tar.gz
Patch0: 0001-GCC-complains-about-int-long-conflicts.patch
Patch1: 0002-GCC-Wformat-security.patch
Patch2: 0004-GCC-Wall.patch
Patch3: 0006-GCC-Wall-Wextra.patch

%description
The Stanford GraphBase: A Platform for Combinatorial Computing.
.
A highly portable collection of programs and data is now available to
researchers who study combinatorial algorithms and data structures. All files
are in the public domain and usable with only one restriction: They must not be
changed! A ``change file'' mechanism allows local customization while the
master files stay intact.

%prep
%setup -c -q
%patch -P 0 1 2 3 -p1

%build
%{__ln_s} PROTOTYPES/*.ch .
%{__sed} -e "s/#SYS/SYS/" -e "s/= -g/= -g -Wall -Wextra/" -i Makefile
%{__make} tests assign_lisa book_components econ_order football girth ladders \
	miles_span multiply queen roget_components take_risc word_components
%{__pdftex} abstract.plaintex

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT/usr/bin
%{__cp} assign_lisa book_components econ_order football girth ladders \
	miles_span multiply queen roget_components take_risc word_components \
	$RPM_BUILD_ROOT/usr/bin
%{__mkdir_p} $RPM_BUILD_ROOT/usr/share/sgb
%{__cp} *.dat $RPM_BUILD_ROOT/usr/share/sgb
%{__mkdir_p} $RPM_BUILD_ROOT/usr/include/sgb
%{__cp} *.h $RPM_BUILD_ROOT/usr/include/sgb
%{__mkdir_p} $RPM_BUILD_ROOT/usr/lib
%{__cp} libgb.a $RPM_BUILD_ROOT/usr/lib
%{__mkdir_p} $RPM_BUILD_ROOT/usr/lib/cweb
%{__cp} boilerplate.w gb_types.w $RPM_BUILD_ROOT/usr/lib/cweb
%{__mkdir_p} $RPM_BUILD_ROOT/usr/share/doc/sgb
%{__cp} abstract.pdf $RPM_BUILD_ROOT/usr/share/doc/sgb

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_usr}/bin/assign_lisa
%{_usr}/bin/book_components
%{_usr}/bin/econ_order
%{_usr}/bin/football
%{_usr}/bin/girth
%{_usr}/bin/ladders
%{_usr}/bin/miles_span
%{_usr}/bin/multiply
%{_usr}/bin/queen
%{_usr}/bin/roget_components
%{_usr}/bin/take_risc
%{_usr}/bin/word_components
%{_usr}/share/sgb
%{_usr}/include/sgb
%{_usr}/lib/libgb.a
%{_usr}/lib/cweb/boilerplate.w
%{_usr}/lib/cweb/gb_types.w
%doc %{_usr}/share/doc/sgb

%post

%postun

%changelog
* Thu Oct 29 2015 Andreas Scherer <andreas_tex@freenet.de> 20090810-16
- Fully parametrized specfile using tons of configuration macros.
* Mon Sep 07 2015 Andreas Scherer <andreas_tex@freenet.de> 20090810-15
- Compile with -Wall and -Wextra and fix the inflicted source modules.
* Thu Sep 03 2015 Andreas Scherer <andreas_tex@freenet.de> 20090810-14
- Compile with -Wall and fix the inflicted source modules.
* Sat Aug 15 2015 Andreas Scherer <andreas_tex@freenet.de> 20090810-13
- Provide consistent information in URL and Source.
* Mon Jul 06 2015 Andreas Scherer <andreas_tex@freenet.de> 20090810-13
- Update sgb.spec by using %setup with suitable options.
* Wed Jul 04 2015 Andreas Scherer <andreas_tex@freenet.de> 20090810-12
- GCC warns about uses of format functions that represent possible security
  problems.
* Wed Jul 01 2015 Andreas Scherer <andreas_tex@freenet.de> 20090810-11
- Update sgb.spec for new debbuild 0.10.1
* Fri Sep 02 2011 Andreas Scherer <andreas_tex@freenet.de> 20090810-10
- GCC complains about strlen and friends; set SYS=SYSV accordingly
- GCC complains about a few int/long conflicts; let's apply a patch
* Mon Aug 01 2011 Andreas Scherer <andreas_tex@freenet.de> 20090810-9
- dpkg complains about missing maintainer
* Tue Nov 23 2009 Andreas Scherer <andreas_tex@freenet.de> 20090810-8
- CWEB utilities come from TeXLive 2009 installation
* Tue Nov 09 2009 Andreas Scherer <andreas_tex@freenet.de> 20090810-7
- Update for 2009 sources
* Tue Dec 18 2007 Andreas Scherer <andreas_tug@freenet.de> 20070421-6
- Matching version number for Ubuntu/Debian
* Sat Apr 21 2007 Andreas Scherer <andreas_tug@freenet.de> 20070421-5
- Update for 2007 sources
* Fri Jun 09 2006 Andreas Scherer <andreas_tug@freenet.de> 20050329-4
- No Ubuntu, no Debian; system installation
* Thu Nov 03 2005 Andreas Scherer <andreas_tug@freenet.de> 20050329-3
- Update for 2005 sources and Debian version scheme
* Wed Nov 02 2005 Andreas Scherer <andreas_tug@freenet.de> 20030623-2
- Build from original source archive
* Thu Oct 29 2005 Andreas Scherer <andreas_tug@freenet.de> 1.0-1
- Initial build
