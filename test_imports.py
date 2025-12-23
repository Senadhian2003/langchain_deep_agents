#!/usr/bin/env python3
"""
Sample test file to verify that dependencies can be imported and work correctly.
Run this after installing dependencies with: uv add deepagents tavily-python
"""

def test_imports():
    """Test importing the required packages."""
    try:
        print("Testing imports...")
        
        # Test deepagents import
        print("  - Importing deepagents...")
        import deepagents
        print(f"    ✓ deepagents imported successfully (version: {getattr(deepagents, '__version__', 'unknown')})")
        
        # Test tavily-python import
        print("  - Importing tavily...")
        import tavily
        print(f"    ✓ tavily imported successfully (version: {getattr(tavily, '__version__', 'unknown')})")
        
        print("\n✅ All imports successful!")
        return True
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("\nMake sure you've installed dependencies with:")
        print("  uv add deepagents tavily-python")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    test_imports()

