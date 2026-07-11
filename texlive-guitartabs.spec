%global tl_name guitartabs
%global tl_revision 48102

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A class for drawing guitar tablatures easily
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/guitartabs
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/guitartabs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/guitartabs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides is a simple LaTeX2e class that allows guitarists
to create basic guitar tablatures using LaTeX. Create music and do not
be bothered with macro programming. The class depends on the LaTeX
packages geometry, harmony, inputenc, intcalc, musixtex, tikz, and
xifthen, as well as the article class.

