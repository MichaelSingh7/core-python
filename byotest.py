def test_are_equal(actual, expected):
    
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)    
    
def test_not_equal(a, b):
    
    assert a != b, "Did not expect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):
    
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):

    assert item not in collection, "{0} is not in {1}".format(collection, item)
    
def test_between(upper_limit, lower_limit, actual):
    
    assert lower_limit <= actual <= upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)
    
def test_exception_was_raised(func, args, message):
    
    try:
        func(*args)
        
        assert False, "Exception was not raised"
    except Exception as e:
        
        assert e.args[0] == message, "The message that was provided did not match the message thrown"