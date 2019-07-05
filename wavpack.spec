%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	Lossless Audio compressor
Name:		wavpack
Version:	5.1.0
Release:	4
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
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%doc README ChangeLog
%{_bindir}/wavpack
%{_bindir}/wvunpack
%{_bindir}/wvgain
%{_bindir}/wvtag
%{_mandir}/man1/*1*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{devname}
#Remove, no file in upstream.
#doc doc/*.txt
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/wavpack
