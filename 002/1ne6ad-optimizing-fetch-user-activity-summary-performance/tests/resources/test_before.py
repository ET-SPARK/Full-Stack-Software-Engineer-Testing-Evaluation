"""Tests for repository_before implementation."""
import sys
import os
import time
import threading
import pytest
import psutil
import importlib.util
from unittest.mock import patch

# Add repository_before to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../repository_before'))

from fetch_user_activity_summary import fetch_user_activity_summary
from db import DB


class TestBeforeImplementation:
    """Test the baseline implementation."""
    
    def setup_method(self):
        """Set up test data before each test."""
        self.db = DB()
        self._seed_test_data()
    
    def teardown_method(self):
        """Clean up after each test."""
        self._cleanup_test_data()
    
    def _seed_test_data(self):
        """Seed the database with test data."""
        with self.db.conn.cursor() as cur:
            # Clear existing data
            cur.execute("DELETE FROM events")
            
            # Insert test data for user 1 (high volume user)
            test_events = []
            for i in range(10000):  # Large dataset to test performance
                event_type = ['click', 'view', 'purchase'][i % 3]
                price = 10.50 if event_type == 'purchase' else None
                metadata = {'price': price} if price else {}
                test_events.append((i, 1, event_type, metadata))
            
            # Insert some duplicate events to test de-duplication
            for i in range(100):
                test_events.append((i, 1, 'click', {}))  # Duplicates of first 100 events
            
            # Insert test data for user 2 (medium volume)
            for i in range(1000):
                event_type = ['click', 'view'][i % 2]
                test_events.append((10000 + i, 2, event_type, {}))
            
            # Insert test data for user 3 (low volume)
            test_events.extend([
                (20000, 3, 'click', {}),
                (20001, 3, 'view', {}),
                (20002, 3, 'purchase', {'price': 25.99})
            ])
            
            # Bulk insert
            cur.executemany(
                "INSERT INTO events (id, user_id, type, metadata) VALUES (%s, %s, %s, %s)",
                test_events
            )
            self.db.conn.commit()
    
    def _cleanup_test_data(self):
        """Clean up test data."""
        with self.db.conn.cursor() as cur:
            cur.execute("DELETE FROM events")
            self.db.conn.commit()
    
    def test_functional_correctness(self):
        """Test that the implementation produces correct results."""
        # Test user 3 (simple case)
        result = fetch_user_activity_summary(3)
        expected = {
            'click': 1,
            'view': 1, 
            'purchase': 1,
            'total_value': 25.99
        }
        assert result == expected, f"Expected {expected}, got {result}"
        
        # Test user 2 (no purchases)
        result = fetch_user_activity_summary(2)
        assert result['purchase'] == 0
        assert result['total_value'] == 0.0
        assert result['click'] + result['view'] == 1000  # Should handle de-duplication
    
    def test_performance_baseline(self):
        """Test performance characteristics of before implementation."""
        # Measure execution time for high-volume user
        start_time = time.time()
        result = fetch_user_activity_summary(1)
        execution_time = time.time() - start_time
        
        # Should complete but may be slow
        assert result is not None
        print(f"Before implementation execution time: {execution_time:.4f}s")
        
        # Verify correctness for user 1
        # Should have ~3333 clicks, ~3333 views, ~3334 purchases (with de-duplication)
        assert result['click'] > 3000
        assert result['view'] > 3000  
        assert result['purchase'] > 3000
        assert result['total_value'] > 30000  # ~3334 * 10.50
    
    def test_memory_usage_baseline(self):
        """Test memory usage of before implementation."""
        process = psutil.Process()
        
        # Measure memory before
        mem_before = process.memory_info().rss
        
        # Execute function
        result = fetch_user_activity_summary(1)
        
        # Measure memory after
        mem_after = process.memory_info().rss
        memory_delta = mem_after - mem_before
        
        print(f"Before implementation memory delta: {memory_delta} bytes")
        
        # Should use some memory (this is the baseline)
        assert result is not None
    
    def test_large_dataset_handling(self):
        """Test how before implementation handles large datasets."""
        # Test with user 1 (10,000+ events)
        result = fetch_user_activity_summary(1)
        
        # Should handle large datasets without crashing
        assert isinstance(result, dict)
        assert all(key in result for key in ['click', 'view', 'purchase', 'total_value'])
        assert all(isinstance(result[key], (int, float)) for key in result.keys())
    
    def test_edge_cases(self):
        """Test edge cases for before implementation."""
        # Test non-existent user
        result = fetch_user_activity_summary(999999)
        expected = {'click': 0, 'view': 0, 'purchase': 0, 'total_value': 0.0}
        assert result == expected
        
        # Test user with no events (after cleanup)
        with self.db.conn.cursor() as cur:
            cur.execute("DELETE FROM events WHERE user_id = 3")
            self.db.conn.commit()
        
        result = fetch_user_activity_summary(3)
        assert result == expected
    
    def test_data_integrity(self):
        """Test data integrity for before implementation."""
        result = fetch_user_activity_summary(1)
        
        # All values should be non-negative
        assert result['click'] >= 0
        assert result['view'] >= 0
        assert result['purchase'] >= 0
        assert result['total_value'] >= 0.0
        
        # Types should be correct
        assert isinstance(result['click'], int)
        assert isinstance(result['view'], int)
        assert isinstance(result['purchase'], int)
        assert isinstance(result['total_value'], float)