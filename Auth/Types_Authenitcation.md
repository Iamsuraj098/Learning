# Authentication Protocol

| Authentication Type              | Purpose                                      | Common Use Case                                      |
| -------------------------------- | -------------------------------------------- | ---------------------------------------------------- |
| OpenID Connect (OIDC)            | Authentication + Identity Layer on OAuth 2.0 | "Login with Google", Single Sign-On (SSO)            |
| OAuth 2.0                        | Authorization (not authentication by itself) | Granting apps access to APIs                         |
| SAML 2.0                         | Enterprise Single Sign-On                    | Corporate applications, Active Directory integration |
| Kerberos                         | Ticket-based authentication                  | Windows domains, intranets                           |
| LDAP Authentication              | User authentication against a directory      | Enterprise user management                           |
| JWT Authentication               | Token-based authentication                   | REST APIs, microservices                             |
| API Key Authentication           | Simple application authentication            | Public/private APIs                                  |
| Basic Authentication             | Username/password in HTTP headers            | Legacy applications                                  |
| Digest Authentication            | More secure version of Basic Auth            | Legacy web systems                                   |
| Certificate-Based Authentication | Identity via digital certificates            | Enterprise VPNs, secure networks                     |
| FIDO2                            | Passwordless authentication                  | Security keys, biometrics                            |
| WebAuthn                         | Browser-based passwordless login             | Passkeys, biometric login                            |
