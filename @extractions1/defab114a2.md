---
title: http://dublincore.org/specifications/dublin-core/abstract-model/2007-02-05/
source_url: http://dublincore.org/specifications/dublin-core/abstract-model/2007-02-05/
date_collected: '2025-06-19'
license: Fair Use
---

DCMI: DCMI Abstract Model



[Dublin Core
![](/images/dcmi_logo_v802.svg)](/)

Open menu

[DCMI-2025 Conference](https://www.dublincore.org/conferences/2025/)

[Specifications](/specifications/)

Events

[Annual Conferences

Continuing an unbroken sequence of more than twenty years of
DCMI Annual Conferences.](/conferences/)
[Webinars & Tutorials

Occasional webinars and online tutorials orgainized by the DCMI.](/webinars/)

[DCMI 2025 Conference](/conferences/2025/)

Community

[DCMI Community

DCMI is defined by its community which is responsible for the
innovative developments and evolving good practices.](/themes/community/)
[DCMI Education Committee

The DCMI Education Committee coordinates activities and
publications that teach and inform users about current
developments and technologies for metadata.](https://education.dublincore.org/task-groups/)
[LRMI Working Group

The LRMIâ¢ Working Group is charged with defining and executing
DCMI work on the LRMI family of metadata specifications.](/groups/lrmi/)
[Application Profiles Working Group

Working Group for a revised framework to support application
profiles, a revised abstract model, and core vocabulary of
components and constraints.](/groups/application-profiles/)

[News](/news/)

Resources

[DCPapers

The Dublin Core Papers repository is an open access resource for
scholarly articles and technical papers.](https://dcpapers.dublincore.org/)
[DCMI Blog

Occasional blog posts report on developments in metadata
innovation and practice.](/blog/)
[Metadata Basics

The DCMI approach to metadata aims at achieving pragmatic
interoperability among traditional and newer technologies on the
basis of knowledge graph design principles.](/resources/metadata-basics/)
[Dublin Coreâ¢ User Guide

A basic guide in the use of Dublin Core and other DCMI
vocabularies.](/resources/userguide/)
[Glossary

A guide to terminology used in the DCMI community, past and
present, with reflections on how our language for talking about
metadata has evolved.](/resources/glossary/)
[LRMI Resources

Archived LRMI resources including presentations, reports, and
implementations.](/resources/lrmi/)

About DCMI

[About DCMI](/about/)
[DCMI Themes](/themes/)
[DCMI History](/about/history/)
[About LRMI](/about/lrmi/)

### Organisation

[Members](/members/)
[Governance](/groups/governing-board/)
[By-laws](/about/bylaws/)
[Directorate](/about/executive/)
[Usage Board](/groups/usage-board/)
[Collaborations](/collaborations/)

[Contact](/about/contact/)

[Bluesky](https://bsky.app/profile/dublincore.org)
[Twitter](https://x.com/dublincore)
[YouTube](https://www.youtube.com/c/DublinCore)
[GitHub](https://github.com/dcmi)
[RSS Feed](https://www.dublincore.org/index.xml)

![Dublin Core](/images/dcmi_logo_v802.svg)

Close menu

[Specifications](/specifications/)
[Conferences](/conferences/)
[Webinars](/webinars/)
[Community](/themes/community/)
[Learning Resources](/resources/)

[About DCMI](/about/)
[Themes](/themes/)
[Members](/members/)
[Governing Board](/groups/governing-board/)
[Usage Board](/groups/usage-board/)
[Directorate](/directorate/)

[DCMI 2025 Conference](/conferences/2025/)

[Bluesky](https://bsky.app/profile/dublincore.org)
[Twitter](https://x.com/dublincore)
[YouTube](https://www.youtube.com/c/DublinCore)
[GitHub](https://github.com/dcmi)
[RSS Feed](https://www.dublincore.org/index.xml)

Go to...

Home

DCMI Abstract Model

Dublin Coreâ¢

DCMI Specifications

1. [Home](/)
2. [DCMI Specifications](https://www.dublincore.org/specifications/)
3. [Dublin Coreâ¢](https://www.dublincore.org/specifications/dublin-core/)
4. [DCMI Abstract Model](https://www.dublincore.org/specifications/dublin-core/abstract-model/)
5. DCMI Abstract Model

# DCMI Abstract Model

|  |  |
| --- | --- |
| Creator: | [Andy Powell](/cdn-cgi/l/email-protection#a8c9c6ccd186d8c7dfcdc4c4e8cdccdddbcddade86c7dacf86ddc3)  Eduserv Foundation, UK |
| Creator: | [Mikael Nilsson](/cdn-cgi/l/email-protection#c2afabacab82aca3a6a3eca9b6aaecb1a7)  KMR Group, CID, NADA, KTH (Royal Institute of Technology), Sweden |
| Creator: | [AmbjÃ¶rn Naeve](/cdn-cgi/l/email-protection#43222e21032d2227226d28372b6d3026)  KMR Group, CID, NADA, KTH (Royal Institute of Technology), Sweden |
| Creator: | [Pete Johnston](/cdn-cgi/l/email-protection#b0c0d5c4d59edadfd8dec3c4dfdef0d5d4c5c3d5c2c69edfc2d79ec5db)  Eduserv Foundation, UK |
| Creator: | [Thomas Baker](/cdn-cgi/l/email-protection#6e1a0c0f050b1c2e1a0c0f050b1c400a0b)  DCMI |
| Date Issued: | 2007-02-05 |
| Identifier: | [http://dublincore.org/specifications/dublin-core/abstract-model/2007-02-05/](/specifications/dublin-core/abstract-model/2007-02-05/) |
| Replaces: | [http://dublincore.org/specifications/dublin-core/abstract-model/2005-03-07/](/specifications/dublin-core/abstract-model/2005-03-07/) |
| Is Replaced By: | Not applicable |
| Latest Version: | [http://dublincore.org/specifications/dublin-core/abstract-model/](/specifications/dublin-core/abstract-model/) |
| Status of Document: | This is a DCMI [Proposed Recommendation](/specifications/dublin-core/#proposedrecommendations) |
| Description of Document: | This document describes an abstract model for Dublin Core™ metadata. |

## Table of contents

1. Introduction
2. DCMI Abstract Model
3. Descriptions, description sets and records
4. Values
5. DCMI Abstract Model semantics
6. Encoding guidelines
7. Terminology  
   Appendix A - Relationship to legacy DCMI Grammatical Principles  
   References  
   Acknowledgements

---

## 1. Introduction

This document specifies an abstract model for Dublin Coreâ¢ metadata. The primary purpose of this document is to specify the components and constructs used in Dublin Coreâ¢ metadata. It defines the nature of the components used and describes how those components are combined to create information structures. It provides a reference model which is independent of any particular encoding syntax. Such a reference model allows us to gain a better understanding of the kinds of descriptions that we are trying to encode and facilitates the development of better mappings and cross-syntax translations.

This document is primarily aimed at the developers of software applications that support Dublin Coreâ¢ metadata, people involved in developing new syntax encoding guidelines for Dublin Coreâ¢ metadata and people developing metadata application profiles based on DCMI vocabularies or on other compatible vocabularies.

The DCMI Abstract Model builds on work undertaken by the World Wide Web Consortium (W3C) on the Resource Description Framework (RDF) [RDF, RDFS]. The use of concepts from RDF is summarized below in Section 5, on DCMI Abstract Model semantics.

The DCMI Abstract Model is represented here using UML class diagrams [UML]. Readers that are not familiar with UML class diagrams should note that lines ending in a block-arrow should be read as 'is' or 'is a' (for example, "a *value* is a *resource*") and that lines starting with a block-diamond should be read as 'contains a' or 'has a' (for example, "a *statement* contains a *property URI*"). Other relationships are labeled appropriately. Note that the UML modeling used here shows the abstract model but is not intended to form a suitable basis for the development of software applications. In this document, words and phrases in italics are defined in Section 7, Terminology.

## 2. DCMI Abstract Model

The abstract model of the *resources* described by *descriptions* is as follows:

* Each *described resource* may be described using one or more *property-value pairs*.
* Each *property-value pair* is made up of one *property* and one *value*.
* Each *value* is a *resource* - the physical or conceptual entity that is associated with a *property* when a *property-value pair* is used to describe a *resource*.

![Figure 1 - the DCMI resource model](/specifications/dublin-core/abstract-model/2007-02-05/resource-model.jpg)
\*\*Figure 1 - the DCMI resource model\*\*

The abstract model of DC metadata *descriptions* is as follows:

* A *description set* is a set of one or more *descriptions*, each of which describes a single *resource*.
* A *description* is made up of one or more *statements* (about one, and only one, *described resource*) and zero or one *resource URI* (a *URI* that identifies the *described resource*).
* Each *statement* instantiates a *property-value pair* and is made up of a *property URI* (a *URI* that identifies a *property*), zero or one *value URI* (a *URI* that identifies the *value* associated with the *property*), zero or one *vocabulary encoding scheme URI* (a *URI* that identifies the *vocabulary encoding scheme* of which the *value* is a member), and zero or more *value representations*.
* The *value representation* may take the form of a *value string* or a *rich representation*.
* Each *value string* is a string which represents the *resource*. *Value strings* are intended to be human-readable.
* Each *value string* may have either an associated *syntax encoding scheme URI* that identifies a *syntax encoding scheme* or an associated *value string language* that is an ISO language tag (for example en-GB) but not both.
* Each *rich representation* is a sequence of octets that represents the *value* (a *resource*) - for example, some marked-up text, an image, a video, some audio, or some combination thereof.
* Each *rich representation* must have an associated *media type* (a MIME Media Type).

![Figure 2 - the DCMI description model](/specifications/dublin-core/abstract-model/2007-02-05/description-model.jpg)
\*\*Figure 2 - the DCMI description model\*\*

The abstract model of the vocabularies used in DC metadata *descriptions* is as follows:

* Each *property* may be related to one or more *classes* by a *has domain* relationship. Where it is stated that a *property* has such a relationship with a *class* and a *described resource* is related to a *value* by that *property*, it follows that the *described resource* is an instance of that *class*.
* Each *property* may be related to one or more *classes* by a *has range* relationship. Where it is stated that a *property* has such a relationship with a *class* and a *described resource* is related to a *value* by that *property*, it follows that the *value* is an instance of that *class*.
* Each *resource* may be an *instance of* one or more *classes*.
* Each *resource* may be a *member of* one or more *vocabulary encoding schemes*.
* Each *class* may be related to one or more other *classes* by a *sub-class of* relationship (where the two *classes* are defined such that all *resources* that are instances of the sub-class are also instances of the related *class*).
* Each *property* may be related to one or more other *properties* by a *sub-property of* relationship. Where it is stated that such a relationship exists, the two *properties* are defined such that whenever a *resource* is related to a *value* by the sub-property, it follows that the *resource* is also related to that same *value* by the *property*.
* Each *syntax encoding scheme* is a *class* (of strings).
* A *vocabulary* is a set of one or more *terms*. Each *term* is a member of one or more *vocabularies*.

![Figure 3 - the DCMI vocabulary model](/specifications/dublin-core/abstract-model/2007-02-05/vocabulary-model.jpg)
\*\*Figure 3 - the DCMI vocabulary model\*\*

A number of things about the model are worth noting:

* Each *value* may be the *described resource* in a separate *description* within the same description set - for example, a separate *description* may provide metadata about the person that is the creator of the *described resource*.
* The description model does not provide an explicit mechanism for indicating the *classes* of the *described resource* or the *classes* of any given *value*. *Classes* of the *described resource* can either be indicated explicitly using one or more *statements* in the *description* or be inferred from the *domains* of the *properties* used in the *description*. *Classes* of any given *value* can either be indicated explicitly using one or more *statements* in a separate *description* about that *value* or be inferred from the *range* of the *property*.

## 3. Descriptions, description sets and records

The abstract model presented above indicates that each DC metadata *description* describes one, and only one, *described resource*. This is commonly referred to as the one-to-one principle.

However, real-world metadata applications tend to be based on loosely grouped sets of *descriptions* (where the *described resources* are typically related in some way), known here as *description sets*. For example, a *description set* might comprise *descriptions* of both a painting and the artist. Furthermore, it is often the case that a *description set* will also contain a *description* about the *description set* itself (sometimes referred to as 'admin metadata' or 'meta-metadata').

*Description sets* are instantiated, for the purposes of exchange between software applications, in the form of metadata *records*, according to one of the DCMI encoding guidelines (for example, XHTML meta tags, XML and RDF/XML) [[DCMI-ENCODINGS](/schemas/)].

## 4. Values

A DC metadata *value* is the physical or conceptual entity that is associated with a *property* when a *property-value pair* is used to describe a *resource*. For example, a *value* associated with the Dublin Coreâ¢ Creator *property* is a person, organization or service - a physical entity. A *value* associated with the Dublin Coreâ¢ Date *property* is a point (or range) in time - a conceptual entity. A *value* associated with the Dublin Coreâ¢ Coverage *property* is a geographic region or country - a physical entity. A *value* associated with the Dublin Coreâ¢ Subject *property* is a concept (a conceptual entity) or a physical object or person (a physical entity). Each of these entities is a *resource*.

The *value* may be identified using a *value URI*. The *value* may be represented by one or more *value strings* and/or *rich representations*. The *value* may described by a separate *description*. In each case, the *value* is a *resource*.

## 5. DCMI Abstract Model semantics

Some of the concepts in the DCMI Abstract Model are taken from the Resource Description Framework (RDF) and RDF Schema (RDFS) as follows:

| DCMI Abstract Model | RDF/RDFS |
| --- | --- |
| *resource* | Class: <http://www.w3.org/2000/01/rdf-schema#Resource> |
| *property* or *element* | Class: <http://www.w3.org/1999/02/22-rdf-syntax-ns#Property> |
| *class* | Class: <http://www.w3.org/2000/01/rdf-schema#Class> |
| *syntax encoding scheme* | Class: <http://www.w3.org/2000/01/rdf-schema#Datatype> |
| *has domain* relationship | Property: <http://www.w3.org/2000/01/rdf-schema#domain> |
| *has range* relationship | Property: <http://www.w3.org/2000/01/rdf-schema#range> |
| *sub-property of* relationship | Property: <http://www.w3.org/2000/01/rdf-schema#subPropertyOf> |
| *sub-class of* relationship | Property: <http://www.w3.org/2000/01/rdf-schema#subClassOf> |

**Table 1 - DCMI Abstract Model semantics**

## 6. Encoding guidelines

Particular encoding guidelines (HTML meta tags, XML, RDF/XML, etc.) [[DCMI-ENCODINGS](/schemas/)] do not need to encode all aspects of the abstract model described above. However, they should refer to the DCMI Abstract Model and indicate which parts of the model are encoded and which are not.

Encoding guidelines should indicate how a *value* can be treated as a *described resource* in a separate *description* in those cases where there is no *value URI*.

## 7. Terminology

This document uses the following terms:

*class* (<http://www.w3.org/2000/01/rdf-schema#Class>)
:   A group containing members that have attributes, behaviours, relationships or semantics in common; a kind of category.

*described resource*
:   A *resource* that is described by a *description*.

*described resource URI*
:   A *URI* that identifies the *described resource*.

*description*
:   One or more *statements* about one, and only one, *described resource*.

*description set*
:   A set of one or more *descriptions*.

*element* (<http://www.w3.org/1999/02/22-rdf-syntax-ns#Property>)
:   A synonym for *property*. It should be noted that the word element is also commonly used to refer to a structural markup component within an XML document.

*has domain* (<http://www.w3.org/2000/01/rdf-schema#domain>)
:   A relationship between a *property* and a *class* which indicates that if a *described resource* is related to a *value* by the *property*, then it follows that the *described resource* is an instance of that *class*.

*has range* (<http://www.w3.org/2000/01/rdf-schema#range>)
:   A relationship between a *property* and a *class* which indicates that if a *described resource* is related to a *value* by the *property*, then it follows that the *value* is an instance of that *class*.

*instance of*
:   A relationship between a *resource* and a *class* which indicates a *class* of which the *resource* is an instance.

*media type*
:   A MIME Media Type (as defined by RFC 2045 [[MIME-1](#MIME-1)] and RFC 2046 [[MIME-2](#MIME-2)].

*member of* (*Proposed URI: <http://purl.org/dc/dcam/memberOf>*)
:   A relationship between a *resource* and a *vocabulary encoding scheme* which indicates that the *resource* is a member of a set.

*property* (<http://www.w3.org/1999/02/22-rdf-syntax-ns#Property>)
:   A specific aspect, characteristic, attribute, or relation used to describe *resources*.

*property URI*
:   A *URI* that identifies a single *property*.

*property/value pair*
:   The combination of a *property* and a *value*, used to describe a *resource*.

*record*
:   An instantiation of a *description set*, created according to one of the DCMI encoding guidelines (for example, XHTML meta tags, XML and RDF/XML).

*resource* (<http://www.w3.org/2000/01/rdf-schema#Resource>)
:   Anything that might be identified. Familiar examples include an electronic document, an image, a service (for example, "today's weather report for Los Angeles"), and a collection of other *resources*. Not all *resources* are network "retrievable"; for example, human beings, corporations, concepts and bound books in a library can also be considered *resources*.

*rich representation*
:   A sequence of octets that represents the *value* -- for example, some marked-up text, an image, a video, some audio, or some combination thereof.

*statement*
:   An instantiation of a *property-value pair* made up of a *property URI* (a *URI* that identifies a *property*), zero or one *value URI* (a *URI* that identifies the *value* associated with the *property*), zero or one *vocabulary encoding scheme URI* (a *URI* that identifies the *vocabulary encoding scheme* of which the *value* is a member), and zero or more *value representations* of the *value*.

*sub-class of* (<http://www.w3.org/2000/01/rdf-schema#subClassOf>)
:   A relationship between two *classes* which indicates that the two *classes* are defined such that all *resources* that are instances of the sub-*class* are also instances of the related *class*).

*sub-property of* (<http://www.w3.org/2000/01/rdf-schema#SubPropertyOf>)
:   A relationship between two *properties* which indicates that the two *properties* are defined such that whenever a *resource* is related to a *value* by the sub-*property*, it follows that the *resource* is also related to that same *value* by the *property*.

*syntax encoding scheme* (<http://www.w3.org/2000/01/rdf-schema#Datatype>)
:   A set of strings and an associated set of rules that describe a mapping between that set of strings and a set of *resources*. The mapping rules may define how the string is structured (for example DCMI Box) or they may simply enumerate all the strings and the corresponding resources (for example ISO 3166).

*syntax encoding scheme URI*
:   A *URI* that identifies a *syntax encoding scheme*.

*term*
:   A *property* (*element*), *class*, *vocabulary encoding scheme*, or *syntax encoding scheme*.

*URI*
:   A Uniform Resource Identifier [[URI](#URI)] or Internationalized Resource Identifier [[IRI](#IRI)].

*value*
:   The physical or conceptual entity (a *resource*) that is associated with a *property* when a *property-value pair* is used to describe a *resource*.

*value URI*
:   A *URI* that identifies the *value*.

*value representation*
:   A surrogate for (i.e. a representation of) the *value*.

*value string*
:   A string, optionally associated with either a *syntax encoding scheme URI* or a *value string language*, which represents the *value*.

*value string language*
:   An ISO language tag that indicates the language of the *value string*.

*vocabulary*
:   A set of one or more *terms*.

*vocabulary encoding scheme* (*Proposed URI: <http://purl.org/dc/dcam/VocabularyEncodingScheme>*)
:   An enumerated set of *resources*.

*vocabulary encoding scheme URI*
:   A *URI* that identifies a *vocabulary encoding scheme*.

## Appendix A - Relationship to legacy DCMI Grammatical Principles

The underlying model for Dublin Coreâ¢ metadata has evolved since first formalisms were proposed in the late 1990s. The following table presents rough terminological equivalences between earlier versions of DCMI *grammatical principles* [DCMI-GRAM-PRIN] and the current DCMI Abstract Model.

| DCMI Grammatical Principles | DCMI Abstract Model |
| --- | --- |
| vocabulary term | *resource* |
| element | *property* or *element* |
| element refinement | *property* with *sub-property of* relation |
| encoding scheme | *syntax encoding scheme* or *vocabulary encoding scheme* |
| syntax encoding scheme | *syntax encoding scheme* |
| qualifier | *property* with *sub-property of* relation, *syntax encoding scheme*, or *vocabulary encoding scheme* |
| vocabulary encoding scheme | *vocabulary encoding scheme* |

**Table 2 - DCMI Grammatical Principles and DCMI Abstract Model**

## References

**[DCMI]**  
Dublin Coreâ¢ Metadata Initiative  
< [http://dublincore.org/](/)>

**[DCMI-GRAM-PRIN]**  
DCMI Usage Board. DCMI Grammatical Principles. November 2003.  
< [http://dublincore.org/specifications/dublin-core/grammatical-principles/](/specifications/dublin-core/grammatical-principles/)>

**[DCMI-ENCODINGS]**  
DCMI Encoding Guidelines  
< [http://dublincore.org/schemas/](/schemas/)>

**[IRI]**  
Duerst, M., M. Suignard. RFC 3987: Internationalized Resource Identifiers (IRIs). Internet Engineering Task Force (IETF). January 2005.  
< <http://www.ietf.org/rfc/rfc3987.txt>>

**[MIME-1]**  
Freed, N. and N. Borenstein. RFC 2045: Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies. Internet Engineering Task Force (IETF). November 1996.  
< <http://www.ietf.org/rfc/rfc2045.txt>>

**[MIME-2]**  
Freed, N. and N. Borenstein. RFC 2045: Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types. Internet Engineering Task Force (IETF). November 1996.  
< <http://www.ietf.org/rfc/rfc2046.txt>>

**[RDF]**  
Klyne, Graham and Jeremy Carroll, editors. Resource Description Framework: Concepts and Abstract Syntax. W3C Recommendation. 10 February 2004.  
< <http://www.w3.org/TR/rdf-concepts/>>

**[RDFS]**  
Brickley, Dan and R.V. Guha, editors. RDF Vocabulary Description Language 1.0: RDF Schema. W3C Recommendation. 10 February 2004.  
< <http://www.w3.org/TR/rdf-schema/>>

**[UML]**  
Booch, Grady, James Rumbaugh and Ivar Jacobson. The Unified Modeling Language User Guide. Addison-Wesley, 1998.

**[URI]**  
Berners-Lee, T., R. Fielding, L. Masinter. RFC 3986: Uniform Resource Identifier (URI): Generic Syntax. Internet Engineering Task Force (IETF). January 2005.  
< <http://www.ietf.org/rfc/rfc3986.txt>>

## Acknowledgements

Thanks to Dan Brickley, Rachel Heery, Alistair Miles, Sarah Pulis, the members of the DC Usage Board and the members of the DCMI Architecture Community for their comments on previous versions of this document.

## Footer

![Dublin Core](/images/dcmi_logo_v802.svg)

### Specifications

* [DCMI Metadata Terms](/specifications/dublin-core/dcmi-terms/)
* [DCMI Specifications](/specifications/dublin-core/)
* [Dublin Core Schemas](/schemas/)
* [LRMI](/specifications/lrmi/)
* [BIBO](/specifications/bibo/)

### Outreach

* [Conferences](/conferences/)
* [Webinars](/webinars/)
* [News](/news/)
* [DCMI Blog](/blog/)
* [Resources](/resources/)

### Organisation

* [About DCMI](/about/)
* [Themes](/themes/)
* [DCMI Community](/themes/community/)
* [Members](/members/)
* [Governance](/groups/governing-board/)
* [Usage Board](/groups/usage-board/)

### Website

* [Service Status](https://status.dublincore.org/)
* [Privacy](/about/privacy/)
* [Legal](/about/copyright/)
* [Contact](/about/contact/)

Unless indicated otherwise, DCMI documents are licensed under a
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)
. Please see the
[DCMI Document Notice](/about/copyright/#documentnotice)
for further instructions.

[Copyright](/about/copyright/#copyright)
©
1995-2025
[DCMI](/)
. DCMI
[liability](/about/copyright/#liability)
,
[trademark/service mark](/about/copyright/#trademark)
,
[document use rules](/about/copyright/#documentnotice)
apply. Your interactions with this site are in accordance with our
[privacy](/about/privacy/)
statements.

The Dublin Core Metadata Initiative (DCMI) is a project of
ASIS&T—a U.S. 501(c)(3) nonprofit under the U.S. Internal
Revenue Code. Contributions to DCMI through ASIS&T are
tax-deductible to the full extent of the law in the United States.

Deployed with
[Hugo](https://gohugo.io/)
[v0.145.0](https://github.com/gohugoio/hugo/releases/tag/v0.145.0)
on
05 Jun 25 13:13 UTC
