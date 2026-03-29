from utils.logger import get_logger

def test_logger():
    logger = get_logger("test_logger", "logs/test.log")
    
    logger.info("This is a test log message")
    logger.warning("Warning message")
    logger.error("Error message")
    
    assert True