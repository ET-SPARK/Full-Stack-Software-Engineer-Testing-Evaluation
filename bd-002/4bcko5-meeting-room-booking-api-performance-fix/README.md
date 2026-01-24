# Meeting Room Booking API - Performance Optimization

## Docker Commands

### Test Before Version (Unoptimized)
```bash
# Run tests (automatically stops when test completes)
docker-compose up --build --abort-on-container-exit server-before test-before

# Clean up
docker-compose down -v
```

### Test After Version (Optimized)
```bash
# Run tests (automatically stops when test completes)
docker-compose up --build --abort-on-container-exit server-after test-after

# Clean up
docker-compose down -v
```

### Run Full Evaluation
```bash
# Run complete evaluation (automatically stops when evaluation completes)
docker-compose up --build --abort-on-container-exit evaluate

# Clean up
docker-compose down -v
```

### Quick Cleanup
```bash
# Stop all containers and remove volumes
docker-compose down -v
```

## Test Results

- **Before (Unoptimized)**: 8/10 tests passed
  - Missing database indexes
  - N+1 query problems
  
- **After (Optimized)**: 10/10 tests passed ✅
  - All performance requirements met
  - Query optimization with JOINs
  - Proper database indexes added

## Evaluation Reports

Test reports are automatically generated in:
```
evaluation/reports/YYYY-MM-DD/HH-MM-SS/report.json
```

Each report contains:
- Test execution results
- Performance metrics
- Before/After comparison
- Requirements checklist

## Project Structure

```
.
├── repository_before/       # Unoptimized version (baseline)
├── repository_after/        # Optimized version (solution)
├── tests/                   # Comprehensive test suite
├── evaluation/              # Evaluation scripts and reports
├── patches/                 # Diff between before and after
├── trajectory/              # Engineering process documentation
├── instances/               # Task metadata and test mapping
├── docker-compose.yml       # Docker orchestration
└── README.md               # This file
```

## Key Optimizations

1. **Database Indexes**: Added 4 strategic indexes on bookings table
   - Composite index on (room_id, status)
   - Index on user_id
   - Index on start_time
   - Partial index on (room_id, start_time) for active bookings

2. **Query Optimization**: Eliminated N+1 query problems
   - Replaced loops with SQL JOINs
   - Reduced queries from O(n) to O(1)
   - Used subqueries for efficient status checks

3. **Connection Pool**: Optimized database connection usage
   - Use pool.query() for simple queries
   - Reserve client.connect() for transactions only

## Performance Improvements

| Endpoint | Before | After | Improvement |
|----------|--------|-------|-------------|
| GET /api/rooms | 4+ queries | 1 query | 75% reduction |
| GET /api/bookings/mine | 1+N queries | 1 query | >90% reduction |
| GET /api/rooms/:id/bookings | 1+N queries | 1 query | >90% reduction |
| POST /api/bookings | 4 queries | 2 queries | 50% reduction |
