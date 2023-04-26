Feature: testing drag and drop

  Scenario: run 2 simple tests of "drag and drop" function
     Given we have the website opened
      When we activate "drag and drop" function both end_to_end and by offset
      Then we confirm that the functions work well