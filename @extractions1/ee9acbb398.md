---
title: http://www.w3.org/1999/02/22-rdf-syntax-ns#
source_url: http://www.w3.org/1999/02/22-rdf-syntax-ns#
date_collected: '2025-06-19'
license: Fair Use
---

@prefix rdf:  .
@prefix rdfs:  .
@prefix owl:  .
@prefix dc:  .
 a owl:Ontology ;
dc:title "The RDF Concepts Vocabulary (RDF)" ;
dc:date "2019-12-16" ;
dc:description "This is the RDF Schema for the RDF vocabulary terms in the RDF Namespace, defined in RDF 1.1 Concepts." .
rdf:HTML a rdfs:Datatype ;
rdfs:subClassOf rdfs:Literal ;
rdfs:isDefinedBy  ;
rdfs:seeAlso  ;
rdfs:label "HTML" ;
rdfs:comment "The datatype of RDF literals storing fragments of HTML content" .
rdf:langString a rdfs:Datatype ;
rdfs:subClassOf rdfs:Literal ;
rdfs:isDefinedBy  ;
rdfs:seeAlso  ;
rdfs:label "langString" ;
rdfs:comment "The datatype of language-tagged string values" .
rdf:PlainLiteral a rdfs:Datatype ;
rdfs:isDefinedBy  ;
rdfs:subClassOf rdfs:Literal ;
rdfs:seeAlso  ;
rdfs:label "PlainLiteral" ;
rdfs:comment "The class of plain (i.e. untyped) literal values, as used in RIF and OWL 2" .
rdf:type a rdf:Property ;
rdfs:isDefinedBy  ;
rdfs:label "type" ;
rdfs:comment "The subject is an instance of a class." ;
rdfs:range rdfs:Class ;
rdfs:domain rdfs:Resource .
rdf:Property a rdfs:Class ;
rdfs:isDefinedBy  ;
rdfs:label "Property" ;
rdfs:comment "The class of RDF properties." ;
rdfs:subClassOf rdfs:Resource .
rdf:Statement a rdfs:Class ;
rdfs:isDefinedBy  ;
rdfs:label "Statement" ;
rdfs:subClassOf rdfs:Resource ;
rdfs:comment "The class of RDF statements." .
rdf:subject a rdf:Property ;
rdfs:isDefinedBy  ;
rdfs:label "subject" ;
rdfs:comment "The subject of the subject RDF statement." ;
rdfs:domain rdf:Statement ;
rdfs:range rdfs:Resource .
rdf:predicate a rdf:Property ;
rdfs:isDefinedBy  ;
rdfs:label "predicate" ;
rdfs:comment "The predicate of the subject RDF statement." ;
rdfs:domain rdf:Statement ;
rdfs:range rdfs:Resource .
rdf:object a rdf:Property ;
rdfs:isDefinedBy  ;
rdfs:label "object" ;
rdfs:comment "The object of the subject RDF statement." ;
rdfs:domain rdf:Statement ;
rdfs:range rdfs:Resource .
rdf:Bag a rdfs:Class ;
rdfs:isDefinedBy  ;
rdfs:label "Bag" ;
rdfs:comment "The class of unordered containers." ;
rdfs:subClassOf rdfs:Container .
rdf:Seq a rdfs:Class ;
rdfs:isDefinedBy  ;
rdfs:label "Seq" ;
rdfs:comment "The class of ordered containers." ;
rdfs:subClassOf rdfs:Container .
rdf:Alt a rdfs:Class ;
rdfs:isDefinedBy  ;
rdfs:label "Alt" ;
rdfs:comment "The class of containers of alternatives." ;
rdfs:subClassOf rdfs:Container .
rdf:value a rdf:Property ;
rdfs:isDefinedBy  ;
rdfs:label "value" ;
rdfs:comment "Idiomatic property used for structured values." ;
rdfs:domain rdfs:Resource ;
rdfs:range rdfs:Resource .
rdf:List a rdfs:Class ;
rdfs:isDefinedBy  ;
rdfs:label "List" ;
rdfs:comment "The class of RDF Lists." ;
rdfs:subClassOf rdfs:Resource .
rdf:nil a rdf:List ;
rdfs:isDefinedBy  ;
rdfs:label "nil" ;
rdfs:comment "The empty list, with no items in it. If the rest of a list is nil then the list has no more items in it." .
rdf:first a rdf:Property ;
rdfs:isDefinedBy  ;
rdfs:label "first" ;
rdfs:comment "The first item in the subject RDF list." ;
rdfs:domain rdf:List ;
rdfs:range rdfs:Resource .
rdf:rest a rdf:Property ;
rdfs:isDefinedBy  ;
rdfs:label "rest" ;
rdfs:comment "The rest of the subject RDF list after the first item." ;
rdfs:domain rdf:List ;
rdfs:range rdf:List .
rdf:XMLLiteral a rdfs:Datatype ;
rdfs:subClassOf rdfs:Literal ;
rdfs:isDefinedBy  ;
rdfs:label "XMLLiteral" ;
rdfs:comment "The datatype of XML literal values." .
rdf:JSON a rdfs:Datatype ;
rdfs:label "JSON" ;
rdfs:comment "The datatype of RDF literals storing JSON content." ;
rdfs:subClassOf rdfs:Literal ;
rdfs:isDefinedBy  ;
rdfs:seeAlso  .
rdf:CompoundLiteral a rdfs:Class ;
rdfs:label "CompoundLiteral" ;
rdfs:comment "A class representing a compound literal." ;
rdfs:subClassOf rdfs:Resource ;
rdfs:isDefinedBy  ;
rdfs:seeAlso  .
rdf:language a rdf:Property ;
rdfs:label "language" ;
rdfs:comment "The language component of a CompoundLiteral." ;
rdfs:domain rdf:CompoundLiteral ;
rdfs:isDefinedBy  ;
rdfs:seeAlso  .
rdf:direction a rdf:Property ;
rdfs:label "direction" ;
rdfs:comment "The base direction component of a CompoundLiteral." ;
rdfs:domain rdf:CompoundLiteral ;
rdfs:isDefinedBy  ;
rdfs:seeAlso  .
