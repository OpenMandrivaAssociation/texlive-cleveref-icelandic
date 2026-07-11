%global tl_name cleveref-icelandic
%global tl_revision 78578

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Icelandic grammatical declension for cleveref cross-references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cleveref-icelandic
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref-icelandic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref-icelandic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The cleveref-icelandic package extends cleveref with Icelandic
declension support, allowing cross-references to figures, tables,
equations, and sections to appear in the correct grammatical case
(nominative, accusative, dative, genitive) in both singular and plural.
Case can be specified explicitly by name (nom/acc/dat/gen or Icelandic
abbreviations nf/thf/thgf/ef), by number (0-3), or automatically
inferred from a preposition argument. Built-in declension tables are
provided for the four most common reference types. Additional reference
types and prepositions can be declared in the document preamble using
\DeclareIcrefType and \DeclareIscrefPreposition.

