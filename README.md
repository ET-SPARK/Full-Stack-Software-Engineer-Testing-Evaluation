# Software Engineering Projects Portfolio

This repository contains 6 fully dockerized software engineering projects demonstrating expertise in performance optimization, testing, bug fixes, and system resilience across multiple technology stacks.

## Projects

### 1. User Activity Summary Performance Optimization
**Directory:** `1ne6ad-optimizing-fetch-user-activity-summary-performance`

Optimizes database queries for user activity summaries, reducing query execution time through efficient SQL optimization and query restructuring.

**Technologies:** Python, PostgreSQL, Docker  
**Focus:** Database query optimization, performance tuning

---

### 2. Audit Logger Test Coverage
**Directory:** `21xfjf-auditlogger-test-coverage`

Improves test coverage for an audit logging system by adding comprehensive unit tests for a Go-based audit logger, ensuring reliability and correctness.

**Technologies:** Go, Docker  
**Focus:** Test coverage, unit testing, audit logging

---

### 3. Attendance System Resilience (Vue 2)
**Directory:** `34za6n-attendanceresiliencevue2`

Enhances a Vue 2 attendance system with resilience patterns including retry logic, error handling, offline support, and graceful degradation for improved user experience.

**Technologies:** Vue 2, Vuex, JavaScript, Docker  
**Focus:** Frontend resilience, error handling, state management

---

### 4. Meeting Room Booking API Performance Fix
**Directory:** `4bcko5-meeting-room-booking-api-performance-fix`

Fixes performance bottlenecks in a meeting room booking API by optimizing database queries, reducing N+1 query problems, and improving response times.

**Technologies:** Node.js, Express.js, SQLite, Docker  
**Focus:** API performance, query optimization, backend optimization

---

### 5. AI Maze Solver Test Suite
**Directory:** `9u6zuo-ai-maze-solver-test-suite`

AI-powered maze solver implementing pathfinding algorithms (BFS, DFS, A*) with a comprehensive test suite validating solver correctness and performance.

**Technologies:** React, JavaScript, Jest, Docker  
**Focus:** Algorithm implementation, pathfinding, comprehensive testing

---

### 6. Investment Portfolio Analytics Dashboard
**Directory:** `emzmuo-investment-portfolio-analytics-dashboard`

Real-time investment portfolio analytics and visualization dashboard featuring market simulation, performance metrics, sector allocation, and historical chart analysis.

**Technologies:** React, Vite, JavaScript/TypeScript, Docker  
**Focus:** Data visualization, real-time analytics, financial calculations

---

## Project Structure

Each project follows a consistent structure:

```
project-name/
├── repository_before/     # Original implementation (with issues)
├── repository_after/      # Improved/fixed implementation
├── tests/                 # Comprehensive test suites
├── evaluation/            # Automated evaluation scripts
├── instances/             # Test instances and scenarios
├── trajectory/            # Development trajectory documentation
├── patches/               # Code patches showing changes
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose orchestration
└── README.md              # Project-specific instructions
```

## Running Projects

All projects are fully dockerized. General workflow:

### 1. Build the Docker Environment
```bash
cd <project-directory>
docker compose build
```

### 2. Test Before Version (Original Implementation)
```bash
docker compose run --rm repository-before
# or
docker compose --profile test run --rm test-before
```

### 3. Test After Version (Improved Implementation)
```bash
docker compose run --rm repository-after
# or
docker compose --profile test run --rm test-after
```

### 4. Run Comprehensive Evaluation
```bash
docker compose run --rm evaluation
# or
docker compose --profile eval run --rm evaluation
```

## Technologies Used

- **Languages:** Python, JavaScript/TypeScript, Go, Node.js
- **Frontend:** React, Vue 2, Vuex, Vite
- **Backend:** Express.js, Node.js
- **Databases:** PostgreSQL, SQLite
- **Testing:** Jest, pytest, Go testing
- **Tools:** Docker, Docker Compose
- **Focus Areas:** Performance optimization, test coverage, resilience patterns, algorithm implementation, data visualization

## Key Features

✅ **Before/After Implementations** - Clear demonstration of improvements  
✅ **Comprehensive Test Suites** - Extensive testing for reliability  
✅ **Dockerized Environments** - Reproducible testing and evaluation  
✅ **Automated Evaluations** - Metrics and performance analysis  
✅ **Multi-Technology Stack** - Diverse technical expertise  
✅ **Real-World Scenarios** - Practical software engineering challenges

---

*This repository showcases practical software engineering skills through real-world problem-solving, demonstrating expertise in optimization, testing, debugging, and system design across multiple technology stacks.*
