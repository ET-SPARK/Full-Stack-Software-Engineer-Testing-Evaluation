# Project Repository

This repository contains two main collections of software engineering projects and evaluations.

## Repository Structure

### 📁 001 - Core Projects Collection

Contains 9 projects focused on various software engineering challenges including refactoring, optimization, and bug fixes:

1. **0c1112-Async_Generator** - Async generator implementation and evaluation
2. **351e96-base85-refactor** - Base85 encoding/decoding refactoring project
3. **53bd29-Modular-Express-js-Refactor** - Express.js modular architecture refactoring
4. **899d52-Rate_limiter_optimization** - Rate limiter performance optimization
5. **99cd28-Eliminating_ghost_state_in_asynchronous_react_upload_flow** - React async upload flow state management
6. **b999ca-distributed_dependency_cycle_detection** - Distributed dependency cycle detection system
7. **BD-RL-001-mechanical_refactor_score** - Mechanical refactoring scoring system
8. **c9c8c5-Prisma_Schema_Service_Bug_Fix** - Prisma schema service bug resolution
9. **cfcfd6-Correct_functional_bugs_in_legacy_javascript_code** - Legacy JavaScript code bug fixes

### 📁 002 - Dockerized Test & Evaluation Suite

Contains 6 fully dockerized projects with comprehensive test suites and performance evaluations:

1. **1ne6ad-optimizing-fetch-user-activity-summary-performance** - User activity summary query optimization
2. **21xfjf-auditlogger-test-coverage** - Audit logger test coverage improvements
3. **34za6n-attendanceresiliencevue2** - Vue 2 attendance system resilience enhancements
4. **4bcko5-meeting-room-booking-api-performance-fix** - Meeting room booking API performance optimization
5. **9u6zuo-ai-maze-solver-test-suite** - AI-based maze solver with comprehensive test suite
6. **emzmuo-investment-portfolio-analytics-dashboard** - Investment portfolio analytics dashboard

## Project Structure Pattern

### 001 Projects
Each project typically contains:
- `repository_before/` - Original implementation
- `repository_after/` - Improved/fixed implementation
- `tests/` - Test suites
- `evaluation/` - Evaluation reports and metrics
- `patches/` - Code patches (where applicable)

### 002 Projects
Each project includes:
- `repository_before/` - Original implementation
- `repository_after/` - Improved/fixed implementation
- `tests/` - Test suites
- `evaluation/` - Evaluation reports and metrics
- `instances/` - Test instances
- `trajectory/` - Execution trajectories
- `patches/` - Code patches
- `Dockerfile` - Docker configuration
- `docker-compose.yml` - Docker Compose orchestration
- `README.md` - Project-specific instructions

## Running 002 Projects

All projects in the `002/` folder are fully dockerized. General workflow:

### 1. Build the Docker Environment
```bash
cd 002/<project-name>
docker compose build
```

### 2. Test Before Version (Original Implementation)
```bash
docker compose --profile test run --rm test-before
# or
docker compose run --rm repository-before
```

### 3. Test After Version (Improved Implementation)
```bash
docker compose --profile test run --rm test-after
# or
docker compose run --rm repository-after
```

### 4. Run Comprehensive Evaluation
```bash
docker compose --profile eval run --rm evaluation
# or
docker compose run --rm evaluation
```

## Technologies

The projects span multiple technologies and frameworks:
- **Languages**: Python, JavaScript/TypeScript, Node.js
- **Frameworks**: Express.js, React, Vue 2, Prisma
- **Tools**: Docker, Jest, pytest
- **Focus Areas**: Performance optimization, refactoring, bug fixes, test coverage, resilience

## Evaluation Reports

Evaluation reports are stored in timestamped directories under each project's `evaluation/reports/` folder, containing detailed metrics and analysis in JSON format.

---

*This repository serves as a comprehensive collection of software engineering case studies, demonstrating best practices in refactoring, optimization, testing, and bug resolution.*
