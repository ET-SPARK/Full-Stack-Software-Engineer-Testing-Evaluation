# Meeting Room Booking API - Performance Optimization

## Docker Commands

### Test Before Version (Unoptimized)

```bash
# Start before version and run tests
docker-compose up --build server-before test-before
```

### Test After Version (Optimized)

```bash
# Start after version and run tests
docker-compose up --build server-after test-after
```

### Run Full Evaluation

```bash
# Run complete evaluation (tests both versions and generates comparison)
docker-compose up --build evaluate
```

### Clean Up

```bash
# Stop and remove all containers and volumes
docker-compose down -v
```