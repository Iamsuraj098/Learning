# GraphQL
GraphQL is a query language for APIs and a runtime for executing those queries. It allows clients to request exactly the data they need and nothing more.

Key principles:
- The client shapes the response.
- There is a single endpoint.
- Strongly typed schema define the contract.
- Resolving logic is modular and pluggable.

---

### Why GraphQL Was Introduced

Traditional REST APIs often face issues:

- Overfetching (fetching more data than needed).
- Underfetching (needing multiple endpoints to complete a single page).
- Difficult schema evolution.
- Mobile clients requiring optimized data payloads.
- GraphQL solves this by letting the client specify fields and relationships in a single structured query.

---

### GraphQL Schema (The Heart of the System)

The GraphQL schema is a strict, typed contract between client and server.

It contains:

- Object types
- Field definitions
- Relationships (nested fields)
- Query type
- Mutation type
- Optional Subscription type (for realtime)

Example conceptual schema:
```
type User {
  id: ID!
  name: String!
  posts: [Post!]
}

type Post {
  id: ID!
  title: String!
  author: User!
}

```
---

### How GraphQL Executes a Query (Internal Mechanics)
Step-by-step:
- Parse: Converts the query string to an abstract syntax tree.
- Validate: Ensures the query matches the schema (types, arguments, field).
- Execute:
	- Start with query root object.
	- For each requested field, call the resolver.
	- if a field returns an object tpes, walk into its field recursively.
- Assemble result in the shape requested by the client.

---

### Single Endpoint Architecture

Unlike REST which uses multiple resources such as:

- GET /users
- GET /users/5/posts
- POST /users

GraphQL uses one endpoint, such as: **POST /graphql**

The request body contains the query.

Advantages:

- Simplifies versioning.
- Reduces the number of network calls.
- Easier to secure, monitor, and log.

---

### When GraphQL is a Good Fit

Use GraphQL when:

- Clients require flexible data shaping.
- There are many frontend apps (web, mobile, dashboards).
- You want to aggregate multiple backend systems.
- Frequent schema changes are expected.

Avoid GraphQL when:

- You need extremely simple CRUD.
- Hard real-time systems.
- Very large or unpredictable queries from clients.
- Strict caching via CDN is essential.

---

### What Strawberry Is

Strawberry is a modern Python library for building GraphQL APIs.

It allows you to define your GraphQL schema using Python classes and type hints, then automatically converts them into a complete GraphQL schema.

---

### How Strawberry Works

Strawberry relies heavily on decorators and Python typing.

You define:

- Object types for output
- **Input** types for mutation arguments
- Queries for fetching data
- **Mutations** for modifying data
- **Resolvers** (async or sync functions)
- Strawberry then produces a GraphQL schema that your server can expose.


---

### Difference between Reat API and Graph API.

1. **Endpoints**

   * REST: Multiple endpoints for different resources.
   * GraphQL: Single endpoint for all operations.

2. **Data Fetching**

   * REST: Fixed response, may return extra or insufficient data.
   * GraphQL: Client selects exactly the fields needed.

3. **Request Structure**

   * REST: Uses HTTP methods like GET, POST, PUT, DELETE.
   * GraphQL: Uses Queries, Mutations, and Subscriptions.

4. **Versioning**

   * REST: Often requires versioning such as v1, v2.
   * GraphQL: Usually no versioning; schema evolves with deprecation.

5. **Performance**

   * REST: Can require multiple calls for related data.
   * GraphQL: Can fetch all related data in one request.

6. **Schema**

   * REST: No strict schema by default.
   * GraphQL: Strongly typed schema that defines all fields and types.

7. **Caching**

   * REST: Easy with URL-based caching.
   * GraphQL: Harder because everything uses the same endpoint.

8. **Error Handling**

   * REST: Uses HTTP status codes.
   * GraphQL: Always returns 200; errors included in the response body.

9. **Use Cases**

   * REST: Simple CRUD operations, static data, easy caching.
   * GraphQL: Complex data needs, multiple nested relationships, flexible client requirements.

10. **Table**

| Aspect             | REST              | GraphQL                |
| ------------------ | ----------------- | ---------------------- |
| Data fetching      | Fixed             | Client-defined         |
| Endpoints          | Multiple          | Single                 |
| Versioning         | Common            | Rare                   |
| Over/underfetching | Common            | Avoided                |
| Schema             | Not enforced      | Strongly typed         |
| Caching            | Simple            | Complex                |
| Performance        | Simple            | Requires batching      |
| Real-time          | Limited           | Built-in subscriptions |
| Error format       | HTTP status codes | Error object           |
