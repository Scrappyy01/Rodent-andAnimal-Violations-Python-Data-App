from report_window import report
from report_window import timelines
from report_window import date


class Test_TestAccountValidator:
    def test_validator_valid_string():
        
        assert(date("12asdasd"), True)
    
    def test_date2():
        
        assert(date("25/42/1593"), False)

    def test_date2():
        
        assert(date("15-2-2012"), True)

    def test_date3():
       
        assert(date("hello"), True)

    def test_date4():
      
        assert(date("12/12/12"), True)

    def test_date5():
      
        assert(timelines("12/12/12"), True)

    def Timeline_Test1():
      
        assert(timelines(Date1 = "ASED")), True)

    def Timeline_Test2():
      
        assert(timelines(Date2 = 234), True)

    def Timeline_Test3():
      
        assert(timelines(Date2 = 234, Date1 = "6/15/2015"), True)

    

  