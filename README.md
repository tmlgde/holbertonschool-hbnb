# 📘 HBnB Evolution - Technical Documentation

## 🔍 Introduction

Ce document présente l'architecture technique de l'application **HBnB Evolution**, une version simplifiée d’AirBnB.  
Il regroupe les **diagrammes UML** essentiels et des **explications détaillées** sur les composants principaux du système :

- Les services/API exposés aux utilisateurs
- La logique métier (Business Logic Layer)
- La couche de persistance (Persistence Layer)

Ce document sert de **blueprint technique** pour les phases de développement, de test et de maintenance de l’application.

---

## 🧱 High-Level Architecture (Diagramme de packages UML)

```mermaid
classDiagram

class PresentationLayer {
    <<Interface>>
    +UserService
    +PlaceService
    +ReviewService
    +AmenityService
}

class BusinessLogicLayer {
    +HBnBFacade
    +User
    +Place
    +Review
    +Amenity
}

class PersistenceLayer {
    +UserRepository
    +PlaceRepository
    +ReviewRepository
    +AmenityRepository
}

PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
