%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	Lossless Audio compressor
Name:		wavpack
Version:	4.60.1
Release:	7
License:	BSD
Group:		Sound
Url:		http://www.wavpack.com/
Source0:	http://www.wavpack.com/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(ncurses)

%description
WavPack is a completely open audio compression format providing
lossless, high-quality lossy, and a unique hybrid compression
mode. Although the technology is loosely based on previous versions of
WavPack, the new version 4 format has been designed from the ground up
to offer unparalleled performance and functionality.

In the default lossless mode WavPack acts just like a WinZip
compressor for audio files. However, unlike MP3 or WMA encoding which
can affect the sound quality, not a single bit of the original
information is lost, so there's no chance of degradation. This makes
lossless mode ideal for archiving audio material or any other
situation where quality is paramount. The compression ratio depends on
the source material, but generally is between 30% and 70%.

The hybrid mode provides all the advantages of lossless compression
with an additional bonus. Instead of creating a single file, this mode
creates both a relatively small, high-quality lossy file that can be
used all by itself, and a "correction" file that (when combined with
the lossy file) provides full lossless restoration. For some users
this means never having to choose between lossless and lossy
compression!

%package -n %{libname}
Group:		System/Libraries
Summary:	Lossless Audio compression library

%description -n %{libname}
WavPack is a completely open audio compression format providing
lossless, high-quality lossy, and a unique hybrid compression
mode. Although the technology is loosely based on previous versions of
WavPack, the new version 4 format has been designed from the ground up
to offer unparalleled performance and functionality.

In the default lossless mode WavPack acts just like a WinZip
compressor for audio files. However, unlike MP3 or WMA encoding which
can affect the sound quality, not a single bit of the original
information is lost, so there's no chance of degradation. This makes
lossless mode ideal for archiving audio material or any other
situation where quality is paramount. The compression ratio depends on
the source material, but generally is between 30% and 70%.

The hybrid mode provides all the advantages of lossless compression
with an additional bonus. Instead of creating a single file, this mode
creates both a relatively small, high-quality lossy file that can be
used all by itself, and a "correction" file that (when combined with
the lossy file) provides full lossless restoration. For some users
this means never having to choose between lossless and lossy
compression!

%package -n %{devname}
Group:		Development/C
Summary:	Lossless Audio compression library
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
WavPack is a completely open audio compression format providing
lossless, high-quality lossy, and a unique hybrid compression
mode. Although the technology is loosely based on previous versions of
WavPack, the new version 4 format has been designed from the ground up
to offer unparalleled performance and functionality.

In the default lossless mode WavPack acts just like a WinZip
compressor for audio files. However, unlike MP3 or WMA encoding which
can affect the sound quality, not a single bit of the original
information is lost, so there's no chance of degradation. This makes
lossless mode ideal for archiving audio material or any other
situation where quality is paramount. The compression ratio depends on
the source material, but generally is between 30% and 70%.

The hybrid mode provides all the advantages of lossless compression
with an additional bonus. Instead of creating a single file, this mode
creates both a relatively small, high-quality lossy file that can be
used all by itself, and a "correction" file that (when combined with
the lossy file) provides full lossless restoration. For some users
this means never having to choose between lossless and lossy
compression!

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc README ChangeLog
%{_bindir}/wavpack
%{_bindir}/wvunpack
%{_bindir}/wvgain
%{_mandir}/man1/*1*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{devname}
%doc doc/*.txt
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/wavpack




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 4.60.1-3mdv2011.0
+ Revision: 670783
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 4.60.1-2mdv2011.0
+ Revision: 608151
- rebuild

* Mon Jan 04 2010 Emmanuel Andry <eandry@mandriva.org> 4.60.1-1mdv2010.1
+ Revision: 486263
- New version 4.60.1

* Thu Oct 01 2009 Götz Waschk <waschk@mandriva.org> 4.60.0-1mdv2010.0
+ Revision: 451984
- new version
- fix source URL

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.50.1-2mdv2010.0
+ Revision: 427535
- rebuild

* Mon Jul 21 2008 Götz Waschk <waschk@mandriva.org> 4.50.1-1mdv2009.0
+ Revision: 239311
- new version

* Fri Jun 27 2008 Götz Waschk <waschk@mandriva.org> 4.50.0-1mdv2009.0
+ Revision: 229473
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 4.41.0-2mdv2009.0
+ Revision: 225924
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Feb 20 2008 Frederik Himpe <fhimpe@mandriva.org> 4.41.0-1mdv2008.1
+ Revision: 173350
- New library policy devel name

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 22 2007 Götz Waschk <waschk@mandriva.org> 4.41.0-1mdv2008.0
+ Revision: 29709
- new version


* Sat Dec 23 2006 Götz Waschk <waschk@mandriva.org> 4.40.0-1mdv2007.0
+ Revision: 101915
- new version
- new major

* Fri Nov 03 2006 Götz Waschk <waschk@mandriva.org> 4.32-2mdv2007.1
+ Revision: 76182
- Import wavpack

* Tue Apr 25 2006 Götz Waschk <waschk@mandriva.org> 4.32-1mdk
- update file list
- New release 4.32

* Thu Nov 17 2005 Götz Waschk <waschk@mandriva.org> 4.3-1mdk
- New release 4.3

* Wed Jun 29 2005 Götz Waschk <waschk@mandriva.org> 4.2-2mdk
- fix buildrequires

* Tue Jun 28 2005 Götz Waschk <waschk@mandriva.org> 4.2-1mdk
- initial package

