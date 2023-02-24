# Building Microservices - Designing Fine-Grained Systems by Sam Newman

## Chapter 1 - What Are Microservices?

* "Microservices are independently releasable services that are modeled around a business domain" (Newman 3.)
* "They are a type of service-oriented architecture" (Newman 3.)
* Microservices are treated as a black box, hosting business functaionlity through connectors (API network etc..)
* Microservcies avoid teh use of shared databases, each microservice has it's own db in most cases 
* They hide information, encapsulate it
* Limiting the use of external interfaces, that allows for less change or breakage given the fact if the external inerfaces
are backward compatible then the interals can change freely.
* The Hexagonal Architecture pattern - the imprtance of keeping the internal implementation separate 
from it's external interfaces.
* Service-Oriented Architecture vs Microservices 
    * "SOA is a design approach in which multiple services collaborate to provide a certian end set of capabilities" (Newman 5.)
    * "A service hear typically means a completely separate os process" (Newman 5.)
    * Things can be service oriented however still coupled. So not microservices, ex: a bunch of services coupled to the same 
    DB
* Independent Deployability - "The idea that we can make a chagne to a microservice, deploy it and release that change to our users,
 without having to deploy any other microservices (Newman 6.)"
* To do this we need very loosely coupled microservices
* 