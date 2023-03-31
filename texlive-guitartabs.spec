Name:		texlive-guitartabs
Version:	48102
Release:	2
Summary:	A class for drawing guitar tablatures easily
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/guitartabs
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitartabs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitartabs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides is a simple LaTeX2e class that allows
guitarists to create basic guitar tablatures using LaTeX.
Create music and do not be bothered with macro programming. The
class depends on the LaTeX packages geometry, harmony,
inputenc, intcalc, musixtex, tikz, and xifthen, as well as the
article class.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/guitartabs
%doc %{_texmfdistdir}/doc/latex/guitartabs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
