%define module cabalrpmdeps
%define _no_haddock 0
%global debug_package %{nil}

Summary:	Tools to build rpm dependencies from Cabal
Name:		ghc-%{module}
Version:	0.0.4
Release:	14
License:	GPLv2+
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
# actualize code for ghc-7.6.1
# thanks to Roman Cheplyaka:
# https://groups.google.com/group/haskell-russian/browse_thread/thread/507bf0121ecebe60
Patch0:		cabalrpmdeps-0.0.4.nohaskell98.patch
BuildRequires:	ghc-devel
BuildRequires:	haskell-macros
Requires(post,preun):	ghc
Obsoletes:	haskell-%{module} < 0.0.4-13
Obsoletes:	%{module} < 0.0.4-13

%description
Tools to build rpm dependencies from Cabal.

%files
%{_bindir}/*
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .nohaskell98

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

