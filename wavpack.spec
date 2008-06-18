%define name wavpack
%define version 4.41.0
%define release %mkrel 2

%define major 1
%define libname %mklibname %name %major

#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Summary: Lossless Audio compressor
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: BSD
Group: Sound
Url: http://www.wavpack.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libncurses-devel

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

%package -n %libname
Group: System/Libraries
Summary: Lossless Audio compression library

%description -n %libname
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

%package -n %mklibname -d %name
Group: Development/C
Summary: Lossless Audio compression library
Provides: lib%name-devel = %version-%release
Obsoletes: %mklibname -d %name 1
Requires: %libname = %version

%description -n %mklibname -d %name
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
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README ChangeLog
%_bindir/wavpack
%_bindir/wvunpack
%_bindir/wvgain

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %mklibname -d %name
%defattr(-,root,root)
%doc doc/*.txt
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_libdir/pkgconfig/%name.pc
%_includedir/wavpack/


