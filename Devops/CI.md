# Continuous Integration 
A CI pipeline is the automated workflow that validates codes before they are integrated into the main branch.

### Why CI pipelines are important ?
- Detects bug early 
- Prevents integration conflicts
- Improve code qualtiy
- Reduce manual testing effort
- Enables faster dilevery 

### Popular CI pipeline tools
- Jenkins
- Github action
- Gitlab CI/CD
- CircleCI

### Typical flow of a CI pipeline
1. Code Commit
2. Pipeline Trigger
3. Build Stage
4. Test Stage
5. Code Quality and Security Checks
6. Artifact Storage

### Core Component of a CI pipeline
- Version Control System
- CI Server
- Build tools
- Test Framework
- Artifact Repository
- Notification System

## Hidden details of CI pipelines

### 1. Ephemeral Build Environments
Modern CI System doesn't use the same machine
Each pipeline run:
- Creates a fresh VM or container
- Installs dependencies from the scratch
- Destroys the environment after completion

Note - Tools like GitHub Actions and GitLab CI/CD rely heavily on ephemeral runners.

### 2. Runner Architecture - 
CI pipeline has two major parts:
- Controller(server): Schedule Jos
- Runner/Agent : Execute Jobs

### 3. Code Execution of CI piplines (ymal or Jenkins files)
In Modern CI systems, the pipeline not executed line by line like a normal scripts
Instead, the CI engine analyzes the pipeline definitions and builds an execution graph.
This graph is call **Directed Acyclic Graph**

Properties:
- Directed : Tasks have a specific order or direction of execution.
- Acyclic : No cicular dependencies are allowed.
- Graph : Each job is node and dependencies is edges.

### 4. Test Isolation and Flaky Tests in CI Pipelines
In continuous integration sysyem, tests are executed automatically on clean environment. For CI pipelines to be reliable, text must be deterministic and isolated.
##### What is Test Isolation ?
Test Isolation means each test must run independently without depending on the state created by other tests.
A test should not depends on:
- Another test output
- Shared Memory
- Shared Database state
- Temporary files created by other Tests

Example of bad practice:
```
test_create_user()
test_delete_user()
```
If test_delete_user() assumes the user created in the previous test exists, the pipeline becomes fragile.

Proper design:
```
test_create_user()
test_delete_user_creates_its_own_user()
```
Each test sets up its own environment and cleans up afterward.

##### Why isolation is important in CI ?
CI pipelines usually:
- Run test in parallel
- Run test on different machines
- Run test in fresh environments

Note - Because of this, any hidden dependency between tests can cause random failures.

##### What is Flaky Test ?
A flaky test is a test that:
- Sometime pass
- Sometimes fails
- Without any changes in the code
Example:
```
Run 1 → PASS
Run 2 → FAIL
Run 3 → PASS
```
##### Cause of Flaky Test
cause of flaky test

**1. Race Condition**

Race conditions happen when multiple processes access shared resources simultaneously.

**2. Timing Issues**

Some tests assume operation complete instantly
```
send_request()
check_response()
```
if the service response slow in CI infrastructure, the test fails

Common reason:
- Network latency
- slow containes
- CPU contention

**3. Parallel Execution**
Modern CI systems run many tests simultaneously to reduce build time.
if tests use shared resources like:
- Same Database
- Same files
- Same port

**4. External dependencies**
Tests that are depends on external system are fragile.
Example:
```
call_payment_api()
verify_response()
```
Possible failures:
- API rate limit
- Network failures
- Service downtime


